"""
SQL Fundamentals - Examples
===========================
Comprehensive SQL query examples using SQLite.
"""

import sqlite3
import os

DB_NAME = "sql_examples.db"

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("=" * 70)
print("SQL FUNDAMENTALS - Examples")
print("=" * 70)

# Setup database with sample data
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create tables
cursor.executescript('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        salary INTEGER,
        hire_date TEXT,
        manager_id INTEGER
    );
    
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        location TEXT,
        budget INTEGER
    );
    
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY,
        employee_id INTEGER,
        product TEXT,
        amount REAL,
        sale_date TEXT
    );
''')

# Insert employees
employees = [
    (1, 'Alice Johnson', 'Engineering', 95000, '2020-03-15', None),
    (2, 'Bob Smith', 'Engineering', 85000, '2021-06-01', 1),
    (3, 'Carol White', 'Sales', 75000, '2019-11-20', None),
    (4, 'David Brown', 'Sales', 65000, '2022-01-10', 3),
    (5, 'Eve Davis', 'Marketing', 70000, '2020-08-15', None),
    (6, 'Frank Miller', 'Engineering', 90000, '2020-05-20', 1),
    (7, 'Grace Wilson', 'Sales', 72000, '2021-03-01', 3),
    (8, 'Henry Taylor', 'HR', 55000, '2022-09-01', None),
    (9, 'Ivy Anderson', 'Engineering', 88000, '2021-12-15', 1),
    (10, 'Jack Thomas', 'Marketing', 68000, '2022-04-10', 5),
]
cursor.executemany('INSERT INTO employees VALUES (?,?,?,?,?,?)', employees)

# Insert departments
departments = [
    (1, 'Engineering', 'Building A', 500000),
    (2, 'Sales', 'Building B', 300000),
    (3, 'Marketing', 'Building A', 200000),
    (4, 'HR', 'Building C', 100000),
]
cursor.executemany('INSERT INTO departments VALUES (?,?,?,?)', departments)

# Insert sales data
sales = [
    (1, 3, 'Widget Pro', 5000, '2024-01-15'),
    (2, 4, 'Widget Basic', 1200, '2024-01-16'),
    (3, 7, 'Widget Pro', 5000, '2024-01-17'),
    (4, 3, 'Widget Premium', 10000, '2024-01-18'),
    (5, 4, 'Widget Basic', 1200, '2024-01-19'),
    (6, 7, 'Widget Basic', 1200, '2024-01-20'),
    (7, 3, 'Widget Pro', 5000, '2024-01-21'),
]
cursor.executemany('INSERT INTO sales VALUES (?,?,?,?,?)', sales)

conn.commit()

# =============================================================================
# SECTION 1: BASIC SELECT
# =============================================================================
print("\n--- 1. Basic SELECT Queries ---\n")

print("All employees:")
cursor.execute('SELECT name, department, salary FROM employees')
for row in cursor.fetchall():
    print(f"  {row[0]:20} | {row[1]:12} | ${row[2]:,}")

# =============================================================================
# SECTION 2: WHERE CLAUSE
# =============================================================================
print("\n--- 2. Filtering with WHERE ---\n")

print("Engineering employees:")
cursor.execute("SELECT name, salary FROM employees WHERE department = 'Engineering'")
for name, salary in cursor.fetchall():
    print(f"  {name}: ${salary:,}")

print("\nHigh earners (salary > 80000):")
cursor.execute('SELECT name, salary FROM employees WHERE salary > 80000')
for name, salary in cursor.fetchall():
    print(f"  {name}: ${salary:,}")

print("\nHired in 2021:")
cursor.execute("SELECT name, hire_date FROM employees WHERE hire_date LIKE '2021-%'")
for name, date in cursor.fetchall():
    print(f"  {name}: {date}")

# =============================================================================
# SECTION 3: COMPARISON AND LOGICAL OPERATORS
# =============================================================================
print("\n--- 3. Comparison and Logical Operators ---\n")

print("Sales or Marketing staff:")
cursor.execute("""
    SELECT name, department, salary FROM employees 
    WHERE department = 'Sales' OR department = 'Marketing'
""")
for name, dept, salary in cursor.fetchall():
    print(f"  {name} ({dept}): ${salary:,}")

print("\nEngineering staff earning over 85000:")
cursor.execute("""
    SELECT name, salary FROM employees 
    WHERE department = 'Engineering' AND salary > 85000
""")
for name, salary in cursor.fetchall():
    print(f"  {name}: ${salary:,}")

print("\nEmployees NOT in Engineering:")
cursor.execute("SELECT name, department FROM employees WHERE department != 'Engineering'")
for name, dept in cursor.fetchall():
    print(f"  {name}: {dept}")

# =============================================================================
# SECTION 4: ORDER BY
# =============================================================================
print("\n--- 4. Sorting Results ---\n")

print("Employees by salary (highest first):")
cursor.execute('SELECT name, salary FROM employees ORDER BY salary DESC')
for name, salary in cursor.fetchall():
    print(f"  ${salary:>7,} - {name}")

print("\nEmployees by department, then by name:")
cursor.execute('SELECT department, name FROM employees ORDER BY department, name')
for dept, name in cursor.fetchall():
    print(f"  {dept:12} | {name}")

# =============================================================================
# SECTION 5: LIMIT AND OFFSET
# =============================================================================
print("\n--- 5. Limiting Results ---\n")

print("Top 3 highest paid employees:")
cursor.execute('SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 3')
for i, (name, salary) in enumerate(cursor.fetchall(), 1):
    print(f"  {i}. {name}: ${salary:,}")

print("\n3rd and 4th highest paid (pagination example):")
cursor.execute('SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 2 OFFSET 2')
for name, salary in cursor.fetchall():
    print(f"  {name}: ${salary:,}")

# =============================================================================
# SECTION 6: AGGREGATION FUNCTIONS
# =============================================================================
print("\n--- 6. Aggregation Functions ---\n")

cursor.execute('SELECT COUNT(*) FROM employees')
print(f"Total employees: {cursor.fetchone()[0]}")

cursor.execute('SELECT COUNT(DISTINCT department) FROM employees')
print(f"Unique departments: {cursor.fetchone()[0]}")

cursor.execute('SELECT SUM(salary) FROM employees')
print(f"Total payroll: ${cursor.fetchone()[0]:,}")

cursor.execute('SELECT AVG(salary) FROM employees')
avg_salary = cursor.fetchone()[0]
print(f"Average salary: ${avg_salary:,.2f}")

cursor.execute('SELECT MIN(salary), MAX(salary) FROM employees')
min_sal, max_sal = cursor.fetchone()
print(f"Salary range: ${min_sal:,} - ${max_sal:,}")

# =============================================================================
# SECTION 7: GROUP BY
# =============================================================================
print("\n--- 7. Grouping Data ---\n")

print("Employee count by department:")
cursor.execute('''
    SELECT department, COUNT(*) as count, AVG(salary) as avg_sal
    FROM employees
    GROUP BY department
    ORDER BY count DESC
''')
print(f"  {'Department':<15} | {'Count':>5} | {'Avg Salary':>12}")
print("  " + "-" * 40)
for dept, count, avg in cursor.fetchall():
    print(f"  {dept:<15} | {count:>5} | ${avg:>10,.0f}")

# =============================================================================
# SECTION 8: HAVING CLAUSE
# =============================================================================
print("\n--- 8. Filtering Groups with HAVING ---\n")

print("Departments with 2+ employees:")
cursor.execute('''
    SELECT department, COUNT(*) as count
    FROM employees
    GROUP BY department
    HAVING COUNT(*) >= 2
''')
for dept, count in cursor.fetchall():
    print(f"  {dept}: {count} employees")

print("\nDepartments with average salary over 75000:")
cursor.execute('''
    SELECT department, AVG(salary) as avg_sal
    FROM employees
    GROUP BY department
    HAVING AVG(salary) > 75000
''')
for dept, avg in cursor.fetchall():
    print(f"  {dept}: ${avg:,.2f} average")

# =============================================================================
# SECTION 9: LIKE PATTERN MATCHING
# =============================================================================
print("\n--- 9. Pattern Matching with LIKE ---\n")

print("Names starting with 'A':")
cursor.execute("SELECT name FROM employees WHERE name LIKE 'A%'")
for row in cursor.fetchall():
    print(f"  - {row[0]}")

print("\nNames containing 'son':")
cursor.execute("SELECT name FROM employees WHERE name LIKE '%son%'")
for row in cursor.fetchall():
    print(f"  - {row[0]}")

print("\nNames ending with 'son':")
cursor.execute("SELECT name FROM employees WHERE name LIKE '%son'")
for row in cursor.fetchall():
    print(f"  - {row[0]}")

# =============================================================================
# SECTION 10: JOINS
# =============================================================================
print("\n--- 10. Joining Tables ---\n")

print("INNER JOIN - Employees and their sales:")
cursor.execute('''
    SELECT e.name, s.product, s.amount
    FROM employees e
    INNER JOIN sales s ON e.id = s.employee_id
    ORDER BY e.name
''')
for name, product, amount in cursor.fetchall():
    print(f"  {name:20} | {product:15} | ${amount:,.0f}")

print("\nTotal sales by employee:")
cursor.execute('''
    SELECT e.name, SUM(s.amount) as total_sales
    FROM employees e
    INNER JOIN sales s ON e.id = s.employee_id
    GROUP BY e.id
    ORDER BY total_sales DESC
''')
for name, total in cursor.fetchall():
    print(f"  {name}: ${total:,.0f}")

# =============================================================================
# SECTION 11: SUBQUERIES
# =============================================================================
print("\n--- 11. Subqueries ---\n")

print("Employees earning above average:")
cursor.execute('''
    SELECT name, salary
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
    ORDER BY salary DESC
''')
for name, salary in cursor.fetchall():
    print(f"  {name}: ${salary:,} (avg: ${avg_salary:,.0f})")

print("\nHighest paid employee in each department:")
cursor.execute('''
    SELECT e.department, e.name, e.salary
    FROM employees e
    INNER JOIN (
        SELECT department, MAX(salary) as max_sal
        FROM employees
        GROUP BY department
    ) m ON e.department = m.department AND e.salary = m.max_sal
''')
for dept, name, salary in cursor.fetchall():
    print(f"  {dept}: {name} (${salary:,})")

# =============================================================================
# SECTION 12: COMPLEX QUERIES
# =============================================================================
print("\n--- 12. Complex Query Example ---\n")

print("Sales performance report:")
cursor.execute('''
    SELECT 
        e.department,
        COUNT(DISTINCT e.id) as employee_count,
        COUNT(s.id) as total_transactions,
        COALESCE(SUM(s.amount), 0) as total_revenue,
        COALESCE(AVG(s.amount), 0) as avg_sale
    FROM employees e
    LEFT JOIN sales s ON e.id = s.employee_id
    GROUP BY e.department
    ORDER BY total_revenue DESC
''')
print(f"  {'Department':<12} | {'Employees':>9} | {'Sales':>5} | {'Revenue':>10} | {'Avg Sale':>9}")
print("  " + "-" * 65)
for dept, emp_count, sales_count, revenue, avg_sale in cursor.fetchall():
    print(f"  {dept:<12} | {emp_count:>9} | {sales_count:>5} | ${revenue:>9,.0f} | ${avg_sale:>8,.0f}")

conn.close()

print("\n" + "=" * 70)
print("Examples complete!")
print("=" * 70)

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
