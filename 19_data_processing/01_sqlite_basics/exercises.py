"""
SQLite Basics - Exercises
=========================
Practice your SQLite skills with these exercises.
Try to solve each one before looking at the solutions!
"""

import sqlite3
import os

DB_NAME = "exercises.db"

# Clean up any existing database
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("=" * 60)
print("SQLITE BASICS - Exercises")
print("=" * 60)

# Set up the database
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price REAL,
        quantity INTEGER
    )
''')

# Insert sample data
products = [
    ("Laptop", "Electronics", 999.99, 10),
    ("Mouse", "Electronics", 29.99, 50),
    ("Keyboard", "Electronics", 79.99, 30),
    ("Desk Chair", "Furniture", 199.99, 15),
    ("Desk", "Furniture", 449.99, 8),
    ("Notebook", "Office Supplies", 5.99, 100),
    ("Pen Set", "Office Supplies", 12.99, 200),
    ("Monitor", "Electronics", 299.99, 20),
]
cursor.executemany('INSERT INTO products (name, category, price, quantity) VALUES (?, ?, ?, ?)', products)
conn.commit()

# =============================================================================
# EXERCISE 1: Basic SELECT
# =============================================================================
print("\n--- Exercise 1: Select All Products ---\n")
"""
Write a query to select all columns from the products table.
Print each product's name and price.
"""
# Your code here:
# cursor.execute(...)
# results = cursor.fetchall()
# for row in results:
#     print(...)

# =============================================================================
# EXERCISE 2: Conditional SELECT
# =============================================================================
print("\n--- Exercise 2: Electronics Only ---\n")
"""
Write a query to select only products in the 'Electronics' category.
Print the name and price of each electronics product.
"""
# Your code here:

# =============================================================================
# EXERCISE 3: Price Filter
# =============================================================================
print("\n--- Exercise 3: Products Under $100 ---\n")
"""
Select all products with a price less than $100.
Print the name, category, and price.
"""
# Your code here:

# =============================================================================
# EXERCISE 4: UPDATE
# =============================================================================
print("\n--- Exercise 4: Update Quantity ---\n")
"""
The laptop stock needs to be updated. Change the quantity of 'Laptop' to 15.
Then, verify the update by selecting that row.
"""
# Your code here:
# 1. Update the quantity
# 2. Select and print to verify

# =============================================================================
# EXERCISE 5: DELETE
# =============================================================================
print("\n--- Exercise 5: Delete Product ---\n")
"""
Delete the 'Pen Set' product from the database.
Then, count how many products remain.
"""
# Your code here:
# 1. Delete the product
# 2. Count remaining products

# =============================================================================
# EXERCISE 6: Aggregation
# =============================================================================
print("\n--- Exercise 6: Average Price by Category ---\n")
"""
Calculate the average price for each category.
Print: category name and average price (formatted to 2 decimal places).
Hint: Use GROUP BY
"""
# Your code here:

# =============================================================================
# EXERCISE 7: Create New Table
# =============================================================================
print("\n--- Exercise 7: Create Customers Table ---\n")
"""
Create a new table called 'customers' with these columns:
- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- name (TEXT NOT NULL)
- email (TEXT UNIQUE)
- city (TEXT)

Then insert at least 3 sample customers.
"""
# Your code here:
# 1. CREATE TABLE
# 2. INSERT sample data

# =============================================================================
# EXERCISE 8: Low Stock Alert
# =============================================================================
print("\n--- Exercise 8: Low Stock Products ---\n")
"""
Find all products with quantity less than 20.
These are "low stock" items that need reordering.
Print: name, quantity, and a message saying "REORDER NEEDED"
"""
# Your code here:

conn.close()

print("\n" + "=" * 60)
print("Exercises complete! Check your answers below.")
print("=" * 60)

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("""
# Exercise 1: Basic SELECT
cursor.execute('SELECT * FROM products')
results = cursor.fetchall()
for row in results:
    print(f"  {row[1]}: ${row[3]}")

# Exercise 2: Electronics Only
cursor.execute('SELECT name, price FROM products WHERE category = ?', ('Electronics',))
for name, price in cursor.fetchall():
    print(f"  {name}: ${price}")

# Exercise 3: Products Under $100
cursor.execute('SELECT name, category, price FROM products WHERE price < ?', (100,))
for name, category, price in cursor.fetchall():
    print(f"  {name} ({category}): ${price}")

# Exercise 4: Update Quantity
cursor.execute('UPDATE products SET quantity = ? WHERE name = ?', (15, 'Laptop'))
conn.commit()
cursor.execute('SELECT name, quantity FROM products WHERE name = ?', ('Laptop',))
row = cursor.fetchone()
print(f"  {row[0]} quantity is now {row[1]}")

# Exercise 5: Delete Product
cursor.execute('DELETE FROM products WHERE name = ?', ('Pen Set',))
conn.commit()
cursor.execute('SELECT COUNT(*) FROM products')
print(f"  Remaining products: {cursor.fetchone()[0]}")

# Exercise 6: Average Price by Category
cursor.execute('''
    SELECT category, AVG(price) as avg_price 
    FROM products 
    GROUP BY category
''')
for category, avg in cursor.fetchall():
    print(f"  {category}: ${avg:.2f}")

# Exercise 7: Create Customers Table
cursor.execute('''
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        city TEXT
    )
''')
customers = [
    ('Alice Johnson', 'alice@example.com', 'New York'),
    ('Bob Smith', 'bob@example.com', 'Los Angeles'),
    ('Carol White', 'carol@example.com', 'Chicago')
]
cursor.executemany('INSERT INTO customers (name, email, city) VALUES (?, ?, ?)', customers)
conn.commit()
print("  Created customers table and inserted 3 customers")

# Exercise 8: Low Stock Products
cursor.execute('SELECT name, quantity FROM products WHERE quantity < ?', (20,))
for name, qty in cursor.fetchall():
    print(f"  {name}: {qty} in stock - REORDER NEEDED")
""")

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
