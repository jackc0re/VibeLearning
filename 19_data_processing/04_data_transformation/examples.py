"""
Data Transformation - Examples
==============================
Learn to transform data for analysis using SQL and Python.
"""

import sqlite3
import os

DB_NAME = "transformation_examples.db"

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("=" * 70)
print("DATA TRANSFORMATION - Examples")
print("=" * 70)

# Setup database
conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Create tables
cursor.executescript('''
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY,
        date TEXT,
        product TEXT,
        category TEXT,
        region TEXT,
        quantity INTEGER,
        unit_price REAL
    );
    
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary REAL,
        hire_date TEXT,
        manager_id INTEGER
    );
''')

# Insert sales data
sales_data = [
    ('2024-01-15', 'Laptop', 'Electronics', 'North', 5, 999.99),
    ('2024-01-16', 'Mouse', 'Electronics', 'North', 20, 29.99),
    ('2024-01-17', 'Laptop', 'Electronics', 'South', 3, 999.99),
    ('2024-02-10', 'Desk', 'Furniture', 'North', 2, 449.99),
    ('2024-02-15', 'Chair', 'Furniture', 'South', 5, 199.99),
    ('2024-02-20', 'Laptop', 'Electronics', 'East', 4, 999.99),
    ('2024-03-05', 'Monitor', 'Electronics', 'North', 10, 299.99),
    ('2024-03-10', 'Desk', 'Furniture', 'East', 3, 449.99),
    ('2024-03-15', 'Mouse', 'Electronics', 'West', 15, 29.99),
    ('2024-03-20', 'Chair', 'Furniture', 'North', 8, 199.99),
]
cursor.executemany('INSERT INTO sales (date, product, category, region, quantity, unit_price) VALUES (?,?,?,?,?,?)', sales_data)

# Insert employee data
employees = [
    (1, 'Alice', 'Engineering', 95000, '2020-01-15', None),
    (2, 'Bob', 'Engineering', 85000, '2021-03-20', 1),
    (3, 'Carol', 'Sales', 75000, '2019-06-10', None),
    (4, 'David', 'Sales', 65000, '2022-01-05', 3),
    (5, 'Eve', 'Sales', 72000, '2021-08-15', 3),
    (6, 'Frank', 'Marketing', 70000, '2020-11-01', None),
]
cursor.executemany('INSERT INTO employees VALUES (?,?,?,?,?,?)', employees)
conn.commit()

# =============================================================================
# SECTION 1: BASIC FILTERING AND SELECTION
# =============================================================================
print("\n--- 1. Filtering and Selection ---\n")

print("Electronics sales only:")
cursor.execute("SELECT date, product, quantity FROM sales WHERE category = 'Electronics'")
for row in cursor.fetchall():
    print(f"  {row['date']}: {row['product']} x{row['quantity']}")

print("\nHigh-value sales (total > $2000):")
cursor.execute('''
    SELECT date, product, quantity * unit_price as total
    FROM sales
    WHERE quantity * unit_price > 2000
''')
for row in cursor.fetchall():
    print(f"  {row['date']}: {row['product']} = ${row['total']:.2f}")

# =============================================================================
# SECTION 2: SORTING
# =============================================================================
print("\n--- 2. Sorting Data ---\n")

print("Sales by total value (highest first):")
cursor.execute('''
    SELECT product, quantity, unit_price, quantity * unit_price as total
    FROM sales
    ORDER BY total DESC
''')
print(f"  {'Product':<12} {'Qty':>4} {'Price':>10} {'Total':>10}")
for row in cursor.fetchall():
    print(f"  {row['product']:<12} {row['quantity']:>4} ${row['unit_price']:>9.2f} ${row['total']:>9.2f}")

print("\nEmployees by department, then salary:")
cursor.execute('SELECT name, department, salary FROM employees ORDER BY department, salary DESC')
for row in cursor.fetchall():
    print(f"  {row['department']:<12} | {row['name']:<10} | ${row['salary']:,.0f}")

# =============================================================================
# SECTION 3: CALCULATED FIELDS
# =============================================================================
print("\n--- 3. Creating Calculated Fields ---\n")

print("Sales with calculated totals and discounts:")
cursor.execute('''
    SELECT 
        product,
        quantity,
        unit_price,
        quantity * unit_price as gross_total,
        quantity * unit_price * 0.9 as discounted_total,
        quantity * unit_price * 0.1 as potential_discount
    FROM sales
    LIMIT 5
''')
print(f"  {'Product':<10} {'Gross':>10} {'With 10% Off':>12} {'You Save':>10}")
for row in cursor.fetchall():
    print(f"  {row['product']:<10} ${row['gross_total']:>9.2f} ${row['discounted_total']:>11.2f} ${row['potential_discount']:>9.2f}")

print("\nEmployee tenure calculation:")
cursor.execute('''
    SELECT 
        name,
        hire_date,
        ROUND((julianday('now') - julianday(hire_date)) / 365.25, 1) as years_employed
    FROM employees
    ORDER BY years_employed DESC
''')
for row in cursor.fetchall():
    print(f"  {row['name']:<10} | Hired: {row['hire_date']} | {row['years_employed']} years")

# =============================================================================
# SECTION 4: CONDITIONAL LOGIC (CASE)
# =============================================================================
print("\n--- 4. Conditional Logic with CASE ---\n")

print("Sales categorized by value:")
cursor.execute('''
    SELECT 
        product,
        quantity * unit_price as total,
        CASE 
            WHEN quantity * unit_price >= 3000 THEN 'Large'
            WHEN quantity * unit_price >= 1000 THEN 'Medium'
            ELSE 'Small'
        END as order_size
    FROM sales
    ORDER BY total DESC
''')
print(f"  {'Product':<12} {'Total':>10} {'Category':>10}")
for row in cursor.fetchall():
    print(f"  {row['product']:<12} ${row['total']:>9.2f} {row['order_size']:>10}")

print("\nEmployee salary grades:")
cursor.execute('''
    SELECT 
        name,
        department,
        salary,
        CASE 
            WHEN salary >= 90000 THEN 'A'
            WHEN salary >= 75000 THEN 'B'
            WHEN salary >= 60000 THEN 'C'
            ELSE 'D'
        END as grade
    FROM employees
    ORDER BY salary DESC
''')
for row in cursor.fetchall():
    print(f"  {row['name']:<10} ({row['department']:<12}) | ${row['salary']:>7,.0f} | Grade {row['grade']}")

# =============================================================================
# SECTION 5: AGGREGATION AND GROUPING
# =============================================================================
print("\n--- 5. Aggregation and Grouping ---\n")

print("Sales by category:")
cursor.execute('''
    SELECT 
        category,
        COUNT(*) as transactions,
        SUM(quantity) as units_sold,
        SUM(quantity * unit_price) as revenue,
        AVG(quantity * unit_price) as avg_order
    FROM sales
    GROUP BY category
''')
print(f"  {'Category':<12} {'Orders':>6} {'Units':>6} {'Revenue':>12} {'Avg Order':>10}")
for row in cursor.fetchall():
    print(f"  {row['category']:<12} {row['transactions']:>6} {row['units_sold']:>6} ${row['revenue']:>11,.2f} ${row['avg_order']:>9.2f}")

print("\nSales by region and category:")
cursor.execute('''
    SELECT 
        region,
        category,
        COUNT(*) as orders,
        SUM(quantity * unit_price) as revenue
    FROM sales
    GROUP BY region, category
    ORDER BY region, revenue DESC
''')
print(f"  {'Region':<8} {'Category':<12} {'Orders':>6} {'Revenue':>12}")
for row in cursor.fetchall():
    print(f"  {row['region']:<8} {row['category']:<12} {row['orders']:>6} ${row['revenue']:>11,.2f}")

# =============================================================================
# SECTION 6: STRING TRANSFORMATIONS
# =============================================================================
print("\n--- 6. String Transformations ---\n")

print("Product name transformations:")
cursor.execute('''
    SELECT 
        product as original,
        UPPER(product) as uppercase,
        LOWER(product) as lowercase,
        LENGTH(product) as length,
        product || ' (' || category || ')' as full_name
    FROM sales
    GROUP BY product
''')
for row in cursor.fetchall():
    print(f"  {row['original']:<10} | {row['uppercase']:<12} | {row['lowercase']:<12} | len={row['length']} | {row['full_name']}")

# =============================================================================
# SECTION 7: PIVOTING DATA
# =============================================================================
print("\n--- 7. Pivoting Data (Sales by Region) ---\n")

print("Revenue by category and region (pivot):")
cursor.execute('''
    SELECT 
        category,
        SUM(CASE WHEN region = 'North' THEN quantity * unit_price ELSE 0 END) as north,
        SUM(CASE WHEN region = 'South' THEN quantity * unit_price ELSE 0 END) as south,
        SUM(CASE WHEN region = 'East' THEN quantity * unit_price ELSE 0 END) as east,
        SUM(CASE WHEN region = 'West' THEN quantity * unit_price ELSE 0 END) as west,
        SUM(quantity * unit_price) as total
    FROM sales
    GROUP BY category
''')
print(f"  {'Category':<12} {'North':>10} {'South':>10} {'East':>10} {'West':>10} {'Total':>10}")
print("  " + "-" * 62)
for row in cursor.fetchall():
    print(f"  {row['category']:<12} ${row['north']:>9,.0f} ${row['south']:>9,.0f} ${row['east']:>9,.0f} ${row['west']:>9,.0f} ${row['total']:>9,.0f}")

# =============================================================================
# SECTION 8: DATE TRANSFORMATIONS
# =============================================================================
print("\n--- 8. Date Transformations ---\n")

print("Sales by month:")
cursor.execute('''
    SELECT 
        SUBSTR(date, 1, 7) as month,
        COUNT(*) as orders,
        SUM(quantity * unit_price) as revenue
    FROM sales
    GROUP BY month
    ORDER BY month
''')
print(f"  {'Month':<10} {'Orders':>6} {'Revenue':>12}")
for row in cursor.fetchall():
    print(f"  {row['month']:<10} {row['orders']:>6} ${row['revenue']:>11,.2f}")

print("\nSales by day of week:")
cursor.execute('''
    SELECT 
        CASE CAST(strftime('%w', date) AS INTEGER)
            WHEN 0 THEN 'Sunday'
            WHEN 1 THEN 'Monday'
            WHEN 2 THEN 'Tuesday'
            WHEN 3 THEN 'Wednesday'
            WHEN 4 THEN 'Thursday'
            WHEN 5 THEN 'Friday'
            WHEN 6 THEN 'Saturday'
        END as day_of_week,
        COUNT(*) as orders
    FROM sales
    GROUP BY day_of_week
    ORDER BY strftime('%w', date)
''')
for row in cursor.fetchall():
    print(f"  {row['day_of_week']:<10}: {row['orders']} orders")

# =============================================================================
# SECTION 9: ADVANCED TRANSFORMATIONS
# =============================================================================
print("\n--- 9. Advanced: Running Totals ---\n")

print("Running total of sales by date:")
cursor.execute('''
    SELECT 
        date,
        product,
        quantity * unit_price as daily_sale,
        (SELECT SUM(s2.quantity * s2.unit_price) 
         FROM sales s2 
         WHERE s2.date <= s1.date) as running_total
    FROM sales s1
    ORDER BY date
''')
print(f"  {'Date':<12} {'Product':<10} {'Daily':>10} {'Running Total':>14}")
for row in cursor.fetchall():
    print(f"  {row['date']:<12} {row['product']:<10} ${row['daily_sale']:>9,.2f} ${row['running_total']:>13,.2f}")

conn.close()

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("\n" + "=" * 70)
print("Examples complete!")
print("=" * 70)
