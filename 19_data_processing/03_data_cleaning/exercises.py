"""
Data Cleaning - Exercises
=========================
Practice data cleaning techniques.
"""

import sqlite3
import os
import re

DB_NAME = "cleaning_exercises.db"

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("=" * 70)
print("DATA CLEANING - Exercises")
print("=" * 70)

# Setup database with messy product data
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        price TEXT,  -- String to simulate type issues
        quantity TEXT,
        supplier_email TEXT,
        last_updated TEXT
    )
''')

products = [
    (1, '  Wireless Mouse  ', 'Electronics', '29.99', '50', 'supplier1@email.com', '2024-01-15'),
    (2, 'USB-C Cable', 'electronics', '12.50', '200', 'SUPPLIER2@EMAIL.COM', '2024/02/20'),
    (3, 'Mechanical Keyboard', 'Electronics', '89.99', 'out of stock', 'invalid-email', '15-03-2024'),
    (4, '  Wireless Mouse  ', 'Electronics', '29.99', '50', 'supplier1@email.com', '2024-01-15'),  # Duplicate
    (5, 'Webcam HD', 'electronics', 'free', '-5', 'supplier3@email.com', '2024-04-10'),
    (6, 'Monitor 27"', None, '299.99', '25', None, '2024-05-22'),
    (7, 'Desk Lamp', 'Furniture', '45.00', '100', 'supplier4@email.com', '2024-06-01'),
    (8, 'Laptop Stand', 'FURNITURE', '35.99', '75', 'supplier5@email.com', 'invalid-date'),
]

cursor.executemany('INSERT INTO products VALUES (?,?,?,?,?,?,?)', products)
conn.commit()

print("\n--- Original Data ---\n")
cursor.execute('SELECT * FROM products')
for row in cursor.fetchall():
    print(row)

# =============================================================================
# EXERCISE 1: Profile the Data
# =============================================================================
print("\n--- Exercise 1: Data Profiling ---\n")
"""
Write queries to:
1. Count total products
2. Count NULL values in each column
3. Find products with duplicate names
"""
# Your code here:
# cursor.execute('SELECT COUNT(*) FROM products')
# total = cursor.fetchone()[0]
# print(f"Total products: {total}")

# =============================================================================
# EXERCISE 2: Standardize Text Data
# =============================================================================
print("\n--- Exercise 2: Standardize Categories ---\n")
"""
The 'category' column has inconsistent casing: 'Electronics', 'electronics', 'FURNITURE'
Write an UPDATE query to standardize all categories to Title Case.
Also trim whitespace from product names.
"""
# Your code here:
# cursor.execute("UPDATE products SET category = ...")
# cursor.execute("UPDATE products SET name = ...")
# conn.commit()

# =============================================================================
# EXERCISE 3: Validate and Clean Prices
# =============================================================================
print("\n--- Exercise 3: Clean Prices ---\n")
"""
The 'price' column has issues:
- Some are strings that can't convert to numbers ('free')
- Need to convert valid prices to REAL numbers

Create a new table 'products_clean' with proper types:
- id INTEGER PRIMARY KEY
- name TEXT
- category TEXT
- price REAL  -- proper numeric type
- quantity INTEGER  -- proper numeric type
- supplier_email TEXT
- email_valid BOOLEAN
- last_updated TEXT

Then insert cleaned data, setting price to NULL for invalid values.
"""
# Your code here:
# cursor.execute('CREATE TABLE products_clean ...')
# def clean_price(price_str):
#     try:
#         return float(price_str)
#     except (ValueError, TypeError):
#         return None
# ... rest of cleaning logic

# =============================================================================
# EXERCISE 4: Validate Emails
# =============================================================================
print("\n--- Exercise 4: Email Validation ---\n")
"""
Write a function to validate email addresses using a regex pattern.
Update the products_clean table to set email_valid based on validation.
Pattern: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

Print a list of invalid emails found.
"""
# Your code here:
# def validate_email(email):
#     pattern = r'...'
#     return bool(re.match(pattern, email)) if email else False

# =============================================================================
# EXERCISE 5: Remove Duplicates
# =============================================================================
print("\n--- Exercise 5: Remove Duplicates ---\n")
"""
Remove duplicate products from products_clean based on name and price.
Keep the record with the lowest ID for each duplicate group.

Print how many duplicates were removed.
"""
# Your code here:
# cursor.execute('''
#     DELETE FROM products_clean
#     WHERE id NOT IN (
#         SELECT MIN(id) FROM products_clean GROUP BY name, price
#     )
# ''')

# =============================================================================
# EXERCISE 6: Handle Missing Data
# =============================================================================
print("\n--- Exercise 6: Handle Missing Categories ---\n")
"""
For products with NULL category, set it to 'Uncategorized'.
Then count how many products are in each category.
"""
# Your code here:

# =============================================================================
# EXERCISE 7: Standardize Dates
# =============================================================================
print("\n--- Exercise 7: Standardize Dates ---\n")
"""
Write a function to parse dates in various formats ('2024-01-15', '2024/02/20', '15-03-2024')
and convert them to ISO format 'YYYY-MM-DD'.

Invalid dates should be set to NULL.
Update the products_clean table with standardized dates.
"""
from datetime import datetime

# Your code here:
# def parse_date(date_str):
#     formats = ['%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y']
#     ...

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

# Exercise 1: Data Profiling
cursor.execute('SELECT COUNT(*) FROM products')
print(f"Total: {cursor.fetchone()[0]}")

cursor.execute('''
    SELECT 
        COUNT(*) - COUNT(name) as missing_name,
        COUNT(*) - COUNT(category) as missing_category,
        COUNT(*) - COUNT(price) as missing_price
    FROM products
''')
nulls = cursor.fetchone()
print(f"Missing values: {dict(nulls)}")

cursor.execute('''
    SELECT name, COUNT(*) FROM products GROUP BY name HAVING COUNT(*) > 1
''')
print("Duplicates:", cursor.fetchall())

# Exercise 2: Standardize Categories
cursor.execute('UPDATE products SET category = UPPER(SUBSTR(category, 1, 1)) || LOWER(SUBSTR(category, 2)) WHERE category IS NOT NULL')
cursor.execute("UPDATE products SET name = TRIM(name)")
conn.commit()

# Exercise 3: Clean Prices
cursor.execute('''
    CREATE TABLE products_clean (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER,
        supplier_email TEXT,
        email_valid BOOLEAN,
        last_updated TEXT
    )
''')

def clean_price(p):
    try:
        p = float(p)
        return p if p >= 0 else None
    except:
        return None

def clean_quantity(q):
    try:
        return int(q)
    except:
        return 0

cursor.execute('SELECT * FROM products')
for row in cursor.fetchall():
    price = clean_price(row[3])
    qty = clean_quantity(row[4])
    cursor.execute('INSERT INTO products_clean VALUES (?,?,?,?,?,?,?,?)',
                   (row[0], row[1], row[2], price, qty, row[5], None, row[6]))
conn.commit()

# Exercise 4: Email Validation
def validate_email(email):
    if not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

cursor.execute('SELECT id, supplier_email FROM products_clean')
for pid, email in cursor.fetchall():
    is_valid = validate_email(email)
    cursor.execute('UPDATE products_clean SET email_valid = ? WHERE id = ?', (is_valid, pid))
conn.commit()

# Exercise 5: Remove Duplicates
cursor.execute('SELECT COUNT(*) FROM products_clean')
before = cursor.fetchone()[0]

cursor.execute('''
    DELETE FROM products_clean
    WHERE id NOT IN (
        SELECT MIN(id) FROM products_clean GROUP BY TRIM(name), price
    )
''')
conn.commit()

cursor.execute('SELECT COUNT(*) FROM products_clean')
after = cursor.fetchone()[0]
print(f"Removed {before - after} duplicates")

# Exercise 6: Handle Missing Categories
cursor.execute("UPDATE products_clean SET category = 'Uncategorized' WHERE category IS NULL")
conn.commit()

cursor.execute('SELECT category, COUNT(*) FROM products_clean GROUP BY category')
print("Category counts:", cursor.fetchall())

# Exercise 7: Standardize Dates
def parse_date(date_str):
    if not date_str:
        return None
    formats = ['%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except:
            continue
    return None

cursor.execute('SELECT id, last_updated FROM products_clean')
for pid, date_str in cursor.fetchall():
    clean_date = parse_date(date_str)
    cursor.execute('UPDATE products_clean SET last_updated = ? WHERE id = ?', (clean_date, pid))
conn.commit()
""")

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
