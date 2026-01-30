"""
Data Transformation - Exercises
===============================
Practice transforming data for analysis.
"""

import sqlite3
import os

DB_NAME = "transformation_exercises.db"

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("=" * 70)
print("DATA TRANSFORMATION - Exercises")
print("=" * 70)

# Setup database
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        customer TEXT,
        product TEXT,
        category TEXT,
        order_date TEXT,
        quantity INTEGER,
        unit_price REAL,
        shipping_cost REAL
    )
''')

orders = [
    (1, 'Acme Corp', 'Widget A', 'Widgets', '2024-01-10', 100, 5.99, 25.00),
    (2, 'Beta Inc', 'Widget B', 'Widgets', '2024-01-15', 50, 7.99, 15.00),
    (3, 'Acme Corp', 'Gadget X', 'Gadgets', '2024-01-20', 25, 49.99, 30.00),
    (4, 'Gamma LLC', 'Widget A', 'Widgets', '2024-02-05', 200, 5.99, 40.00),
    (5, 'Beta Inc', 'Gadget Y', 'Gadgets', '2024-02-10', 10, 99.99, 20.00),
    (6, 'Delta Co', 'Widget B', 'Widgets', '2024-02-15', 75, 7.99, 20.00),
    (7, 'Acme Corp', 'Widget A', 'Widgets', '2024-03-01', 150, 5.99, 35.00),
    (8, 'Gamma LLC', 'Gadget X', 'Gadgets', '2024-03-10', 30, 49.99, 35.00),
]
cursor.executemany('INSERT INTO orders VALUES (?,?,?,?,?,?,?,?)', orders)
conn.commit()

# =============================================================================
# EXERCISE 1: Basic Calculations
# =============================================================================
print("\n--- Exercise 1: Calculate Order Totals ---\n")
"""
Write a query to calculate for each order:
- subtotal (quantity * unit_price)
- total_cost (subtotal + shipping_cost)
- avg_price_per_unit (total_cost / quantity)

Display: customer, product, quantity, subtotal, total_cost
"""
# Your code here:
# cursor.execute('''
#     SELECT 
#         customer,
#         product,
#         quantity,
#         ... as subtotal,
#         ... as total_cost
#     FROM orders
# ''')

# =============================================================================
# EXERCISE 2: Aggregation
# =============================================================================
print("\n--- Exercise 2: Customer Summary ---\n")
"""
Create a summary showing for each customer:
- total number of orders
- total quantity ordered
- total revenue (sum of subtotals)
- average order value

Sort by total revenue (descending).
"""
# Your code here:

# =============================================================================
# EXERCISE 3: Conditional Logic
# =============================================================================
print("\n--- Exercise 3: Order Size Categories ---\n")
"""
Categorize each order based on total_cost:
- total_cost >= 1000: 'Large'
- total_cost >= 500: 'Medium'
- total_cost < 500: 'Small'

Count how many orders fall into each category.
"""
# Your code here:
# Use CASE statement

# =============================================================================
# EXERCISE 4: Date Transformations
# =============================================================================
print("\n--- Exercise 4: Monthly Sales Analysis ---\n")
"""
Group orders by month (extract month from order_date).
For each month, calculate:
- number of orders
- total revenue
- average order value

Sort by month.
"""
# Your code here:
# Hint: Use SUBSTR(order_date, 1, 7) to get YYYY-MM

# =============================================================================
# EXERCISE 5: Pivot Table
# =============================================================================
print("\n--- Exercise 5: Revenue by Customer and Category ---\n")
"""
Create a pivot table showing revenue by customer (rows) and category (columns).
The output should look like:
  Customer    | Widgets | Gadgets | Total
  Acme Corp   | $...    | $...    | $...
  Beta Inc    | $...    | $...    | $...
  ...
"""
# Your code here:
# Use CASE statements to pivot

# =============================================================================
# EXERCISE 6: Top Performers
# =============================================================================
print("\n--- Exercise 6: Top 3 Products by Revenue ---\n")
"""
Find the top 3 products by total revenue.
Display: product name, total quantity sold, total revenue
"""
# Your code here:
# Use GROUP BY, ORDER BY, LIMIT

# =============================================================================
# EXERCISE 7: Customer Segmentation
# =============================================================================
print("\n--- Exercise 7: Customer Value Tiers ---\n")
"""
Classify customers into tiers based on their total spending:
- total >= 1500: 'Gold'
- total >= 800: 'Silver'
- total < 800: 'Bronze'

Count customers in each tier.
"""
# Your code here:
# Use a subquery or CTE to first calculate customer totals

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

# Exercise 1: Basic Calculations
cursor.execute('''
    SELECT 
        customer,
        product,
        quantity,
        quantity * unit_price as subtotal,
        quantity * unit_price + shipping_cost as total_cost
    FROM orders
''')

# Exercise 2: Customer Summary
cursor.execute('''
    SELECT 
        customer,
        COUNT(*) as num_orders,
        SUM(quantity) as total_qty,
        SUM(quantity * unit_price) as total_revenue,
        AVG(quantity * unit_price) as avg_order
    FROM orders
    GROUP BY customer
    ORDER BY total_revenue DESC
''')

# Exercise 3: Order Size Categories
cursor.execute('''
    SELECT 
        CASE 
            WHEN quantity * unit_price + shipping_cost >= 1000 THEN 'Large'
            WHEN quantity * unit_price + shipping_cost >= 500 THEN 'Medium'
            ELSE 'Small'
        END as order_size,
        COUNT(*) as count
    FROM orders
    GROUP BY order_size
''')

# Exercise 4: Monthly Sales Analysis
cursor.execute('''
    SELECT 
        SUBSTR(order_date, 1, 7) as month,
        COUNT(*) as orders,
        SUM(quantity * unit_price) as revenue,
        AVG(quantity * unit_price) as avg_order
    FROM orders
    GROUP BY month
    ORDER BY month
''')

# Exercise 5: Pivot Table
cursor.execute('''
    SELECT 
        customer,
        SUM(CASE WHEN category = 'Widgets' THEN quantity * unit_price ELSE 0 END) as widgets,
        SUM(CASE WHEN category = 'Gadgets' THEN quantity * unit_price ELSE 0 END) as gadgets,
        SUM(quantity * unit_price) as total
    FROM orders
    GROUP BY customer
''')

# Exercise 6: Top 3 Products
cursor.execute('''
    SELECT 
        product,
        SUM(quantity) as total_qty,
        SUM(quantity * unit_price) as total_revenue
    FROM orders
    GROUP BY product
    ORDER BY total_revenue DESC
    LIMIT 3
''')

# Exercise 7: Customer Value Tiers
cursor.execute('''
    SELECT 
        tier,
        COUNT(*) as customer_count
    FROM (
        SELECT 
            customer,
            CASE 
                WHEN SUM(quantity * unit_price) >= 1500 THEN 'Gold'
                WHEN SUM(quantity * unit_price) >= 800 THEN 'Silver'
                ELSE 'Bronze'
            END as tier
        FROM orders
        GROUP BY customer
    )
    GROUP BY tier
''')
""")

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
