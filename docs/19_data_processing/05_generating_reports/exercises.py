"""
Generating Reports - Exercises
==============================
Practice creating reports from data.
"""

import sqlite3
import os
from datetime import datetime

DB_NAME = "reports_exercises.db"

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("=" * 70)
print("GENERATING REPORTS - Exercises")
print("=" * 70)

# Setup database
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        order_date TEXT,
        customer TEXT,
        product TEXT,
        category TEXT,
        quantity INTEGER,
        price REAL
    )
''')

orders = [
    ('2024-01-05', 'TechCorp', 'Server', 'Hardware', 2, 5000),
    ('2024-01-12', 'DevStudio', 'Laptop', 'Hardware', 5, 1200),
    ('2024-01-18', 'TechCorp', 'Monitor', 'Hardware', 10, 300),
    ('2024-02-03', 'StartUp Inc', 'Software License', 'Software', 20, 99),
    ('2024-02-15', 'DevStudio', 'Keyboard', 'Hardware', 15, 80),
    ('2024-02-28', 'TechCorp', 'Mouse', 'Hardware', 20, 25),
    ('2024-03-05', 'StartUp Inc', 'Server', 'Hardware', 1, 5000),
    ('2024-03-10', 'DevStudio', 'Software License', 'Software', 10, 99),
    ('2024-03-22', 'Freelancer', 'Laptop', 'Hardware', 1, 1200),
]
cursor.executemany('INSERT INTO orders VALUES (NULL,?,?,?,?,?,?)', orders)
conn.commit()

# =============================================================================
# EXERCISE 1: Basic Summary Report
# =============================================================================
print("\n--- Exercise 1: Order Summary ---\n")
"""
Create a summary report showing:
- Total number of orders
- Total revenue (sum of quantity * price)
- Average order value
- Number of unique customers

Format it nicely with headers and separators.
"""
# Your code here:
# cursor.execute('SELECT ...')
# Print formatted results

# =============================================================================
# EXERCISE 2: Monthly Report
# =============================================================================
print("\n--- Exercise 2: Monthly Breakdown ---\n")
"""
Create a monthly report showing:
- Month name (January, February, March)
- Number of orders that month
- Total revenue that month
- Percentage of total revenue

Calculate the percentage manually: (month_revenue / total_revenue) * 100
"""
# Your code here:

# =============================================================================
# EXERCISE 3: Category Comparison
# =============================================================================
print("\n--- Exercise 3: Category Performance ---\n")
"""
Compare Hardware vs Software sales:
- Total revenue for each category
- Total units sold for each category
- Average price per unit (revenue / units)

Display as a comparison table.
"""
# Your code here:

# =============================================================================
# EXERCISE 4: Customer Ranking
# =============================================================================
print("\n--- Exercise 4: Top Customers ---\n")
"""
Rank customers by total spending:
- Customer name
- Number of orders
- Total amount spent
- Rank (1st, 2nd, 3rd, etc.)

Sort by total spent (descending) and assign ranks.
"""
# Your code here:

# =============================================================================
# EXERCISE 5: Product Performance
# =============================================================================
print("\n--- Exercise 5: Product Analysis ---\n")
"""
Analyze each product's performance:
- Product name
- Total quantity sold
- Total revenue
- Number of unique customers who bought it

Hint: Use COUNT(DISTINCT customer) for unique customers.
"""
# Your code here:

# =============================================================================
# EXERCISE 6: Export Report
# =============================================================================
print("\n--- Exercise 6: Export to File ---\n")
"""
Export a summary report to a text file named 'order_summary.txt'.
Include:
- Report title and generation date
- All the metrics from Exercise 1
- The monthly breakdown from Exercise 2

Format it as a professional-looking text report.
"""
# Your code here:
# with open('order_summary.txt', 'w') as f:
#     f.write(...)

conn.close()

print("\n" + "=" * 70)
print("Exercises complete! Check solutions at the bottom.")
print("=" * 70)

# =============================================================================
# SOLUTIONS
# =============================================================================
print("""
# SOLUTIONS
# =========

# Exercise 1: Basic Summary Report
print("\\n" + "=" * 50)
print("ORDER SUMMARY")
print("=" * 50)
cursor.execute('''
    SELECT 
        COUNT(*) as total_orders,
        SUM(quantity * price) as total_revenue,
        AVG(quantity * price) as avg_order,
        COUNT(DISTINCT customer) as unique_customers
    FROM orders
''')
row = cursor.fetchone()
print(f"Total Orders:       {row[0]}")
print(f"Total Revenue:      ${row[1]:,.2f}")
print(f"Average Order:      ${row[2]:,.2f}")
print(f"Unique Customers:   {row[3]}")

# Exercise 2: Monthly Report
cursor.execute('SELECT SUM(quantity * price) FROM orders')
total_revenue = cursor.fetchone()[0]

cursor.execute('''
    SELECT 
        CASE strftime('%m', order_date)
            WHEN '01' THEN 'January'
            WHEN '02' THEN 'February'
            WHEN '03' THEN 'March'
        END as month,
        COUNT(*) as orders,
        SUM(quantity * price) as revenue
    FROM orders
    GROUP BY strftime('%m', order_date)
''')

print(f"\\n{'Month':<12} {'Orders':>8} {'Revenue':>12} {'Share':>8}")
print("-" * 45)
for month, orders, revenue in cursor.fetchall():
    pct = (revenue / total_revenue) * 100
    print(f"{month:<12} {orders:>8} ${revenue:>10,.0f} {pct:>7.1f}%")

# Exercise 3: Category Comparison
cursor.execute('''
    SELECT 
        category,
        SUM(quantity * price) as revenue,
        SUM(quantity) as units,
        1.0 * SUM(quantity * price) / SUM(quantity) as avg_price
    FROM orders
    GROUP BY category
''')
print("\\nCATEGORY COMPARISON")
print("-" * 45)
print(f"{'Category':<15} {'Revenue':>12} {'Units':>8} {'Avg Price':>10}")
for cat, rev, units, avg in cursor.fetchall():
    print(f"{cat:<15} ${rev:>10,.0f} {units:>8} ${avg:>9,.0f}")

# Exercise 4: Customer Ranking
cursor.execute('''
    SELECT 
        customer,
        COUNT(*) as orders,
        SUM(quantity * price) as total_spent
    FROM orders
    GROUP BY customer
    ORDER BY total_spent DESC
''')
print("\\nCUSTOMER RANKING")
print("-" * 50)
print(f"{'Rank':<6} {'Customer':<15} {'Orders':>8} {'Spent':>12}")
rank = 1
for customer, orders, spent in cursor.fetchall():
    suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(rank, 'th')
    print(f"{rank}{suffix:<5} {customer:<15} {orders:>8} ${spent:>10,.0f}")
    rank += 1

# Exercise 5: Product Performance
cursor.execute('''
    SELECT 
        product,
        SUM(quantity) as total_qty,
        SUM(quantity * price) as revenue,
        COUNT(DISTINCT customer) as unique_customers
    FROM orders
    GROUP BY product
    ORDER BY revenue DESC
''')
print("\\nPRODUCT PERFORMANCE")
print("-" * 60)
print(f"{'Product':<20} {'Qty':>8} {'Revenue':>12} {'Customers':>10}")
for prod, qty, rev, cust in cursor.fetchall():
    print(f"{prod:<20} {qty:>8} ${rev:>10,.0f} {cust:>10}")

# Exercise 6: Export to File
with open('order_summary.txt', 'w') as f:
    f.write("=" * 60 + "\\n")
    f.write("ORDER SUMMARY REPORT\\n")
    f.write("=" * 60 + "\\n")
    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\\n\\n")
    
    cursor.execute('SELECT SUM(quantity * price), COUNT(*) FROM orders')
    total, count = cursor.fetchone()
    f.write(f"Total Orders: {count}\\n")
    f.write(f"Total Revenue: ${total:,.2f}\\n\\n")
    
    f.write("Monthly Breakdown\\n")
    f.write("-" * 30 + "\\n")
    cursor.execute('''
        SELECT strftime('%m', order_date) as m, SUM(quantity * price)
        FROM orders GROUP BY m ORDER BY m
    ''')
    for month, rev in cursor.fetchall():
        month_name = ['', 'Jan', 'Feb', 'Mar'][int(month)]
        f.write(f"{month_name}: ${rev:,.2f}\\n")
    
    f.write("\\n" + "=" * 60 + "\\n")
    f.write("END OF REPORT\\n")

print("\\nReport exported to 'order_summary.txt'")
""")

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
if os.path.exists('order_summary.txt'):
    os.remove('order_summary.txt')
