"""
Generating Reports - Examples
=============================
Learn to create meaningful reports from your data.
"""

import sqlite3
import os
from datetime import datetime
import csv

DB_NAME = "reports_examples.db"
REPORT_FILE = "sample_report.txt"

# Clean up
for f in [DB_NAME, REPORT_FILE, "sales_report.csv"]:
    if os.path.exists(f):
        os.remove(f)

print("=" * 70)
print("GENERATING REPORTS - Examples")
print("=" * 70)

# Setup database with sample sales data
conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.executescript('''
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY,
        date TEXT,
        customer TEXT,
        product TEXT,
        category TEXT,
        region TEXT,
        quantity INTEGER,
        unit_price REAL
    );
    
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        stock_level INTEGER,
        reorder_point INTEGER
    );
''')

# Generate sample sales data for 3 months
import random
products = [
    ('Laptop Pro', 'Electronics', 1200),
    ('Wireless Mouse', 'Electronics', 25),
    ('USB-C Hub', 'Electronics', 80),
    ('Office Chair', 'Furniture', 250),
    ('Standing Desk', 'Furniture', 600),
    ('Monitor 27"', 'Electronics', 350),
    ('Notebook Set', 'Office Supplies', 15),
    ('Desk Lamp', 'Furniture', 45),
]
customers = ['Acme Corp', 'Beta Inc', 'Gamma LLC', 'Delta Co', 'Epsilon Ltd']
regions = ['North', 'South', 'East', 'West']

sales_data = []
sale_id = 1
for month in [1, 2, 3]:
    for day in range(1, 29, 3):  # Every 3 days
        for _ in range(random.randint(2, 5)):  # 2-5 sales per day
            date = f"2024-{month:02d}-{day:02d}"
            prod_name, category, price = random.choice(products)
            qty = random.randint(1, 5)
            sales_data.append((
                sale_id, date, random.choice(customers), prod_name, category,
                random.choice(regions), qty, price
            ))
            sale_id += 1

cursor.executemany('INSERT INTO sales VALUES (?,?,?,?,?,?,?,?)', sales_data)

# Insert product inventory
cursor.executemany('''
    INSERT INTO products (name, category, stock_level, reorder_point)
    VALUES (?, ?, ?, ?)
''', [
    ('Laptop Pro', 'Electronics', 15, 5),
    ('Wireless Mouse', 'Electronics', 150, 50),
    ('USB-C Hub', 'Electronics', 45, 20),
    ('Office Chair', 'Furniture', 25, 10),
    ('Standing Desk', 'Furniture', 12, 5),
    ('Monitor 27"', 'Electronics', 30, 15),
    ('Notebook Set', 'Office Supplies', 200, 100),
    ('Desk Lamp', 'Furniture', 60, 30),
])
conn.commit()

# =============================================================================
# SECTION 1: EXECUTIVE SUMMARY
# =============================================================================
print("\n" + "=" * 70)
print("📊 EXECUTIVE SUMMARY")
print("=" * 70)
print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Data Source: {DB_NAME}")
print()

# Key metrics
cursor.execute('''
    SELECT 
        COUNT(*) as total_transactions,
        COUNT(DISTINCT customer) as unique_customers,
        SUM(quantity * unit_price) as total_revenue,
        AVG(quantity * unit_price) as avg_transaction,
        SUM(quantity) as total_units
    FROM sales
''')
kpis = cursor.fetchone()

print("KEY PERFORMANCE INDICATORS")
print("-" * 40)
print(f"  Total Transactions:  {kpis['total_transactions']:,}")
print(f"  Unique Customers:    {kpis['unique_customers']}")
print(f"  Total Revenue:       ${kpis['total_revenue']:,.2f}")
print(f"  Average Transaction: ${kpis['avg_transaction']:,.2f}")
print(f"  Total Units Sold:    {kpis['total_units']:,}")

# =============================================================================
# SECTION 2: MONTHLY BREAKDOWN
# =============================================================================
print("\n" + "=" * 70)
print("📅 MONTHLY PERFORMANCE")
print("=" * 70)

cursor.execute('''
    SELECT 
        CASE strftime('%m', date)
            WHEN '01' THEN 'January'
            WHEN '02' THEN 'February'
            WHEN '03' THEN 'March'
        END as month,
        COUNT(*) as transactions,
        SUM(quantity * unit_price) as revenue,
        AVG(quantity * unit_price) as avg_sale
    FROM sales
    GROUP BY strftime('%m', date)
    ORDER BY strftime('%m', date)
''')

print(f"  {'Month':<12} {'Orders':>8} {'Revenue':>15} {'Avg Sale':>12}")
print("  " + "-" * 50)
prev_revenue = None
for row in cursor.fetchall():
    change_str = ""
    if prev_revenue:
        change = ((row['revenue'] - prev_revenue) / prev_revenue) * 100
        trend = "📈" if change > 0 else "📉"
        change_str = f"{trend} {change:+.1f}%"
    print(f"  {row['month']:<12} {row['transactions']:>8,} ${row['revenue']:>14,.2f} ${row['avg_sale']:>11,.2f} {change_str}")
    prev_revenue = row['revenue']

# =============================================================================
# SECTION 3: CATEGORY ANALYSIS
# =============================================================================
print("\n" + "=" * 70)
print("📦 SALES BY CATEGORY")
print("=" * 70)

cursor.execute('''
    SELECT 
        category,
        COUNT(*) as transactions,
        SUM(quantity) as units,
        SUM(quantity * unit_price) as revenue,
        ROUND(100.0 * SUM(quantity * unit_price) / (SELECT SUM(quantity * unit_price) FROM sales), 1) as pct
    FROM sales
    GROUP BY category
    ORDER BY revenue DESC
''')

print(f"  {'Category':<15} {'Orders':>8} {'Units':>8} {'Revenue':>15} {'Share':>8}")
print("  " + "-" * 60)
total_rev = 0
for row in cursor.fetchall():
    bar = "█" * int(row['pct'] / 5)  # Simple bar chart
    print(f"  {row['category']:<15} {row['transactions']:>8,} {row['units']:>8,} ${row['revenue']:>14,.2f} {row['pct']:>6}% {bar}")

# =============================================================================
# SECTION 4: REGIONAL PERFORMANCE
# =============================================================================
print("\n" + "=" * 70)
print("🌍 REGIONAL PERFORMANCE")
print("=" * 70)

cursor.execute('''
    SELECT 
        region,
        COUNT(*) as transactions,
        SUM(quantity * unit_price) as revenue,
        COUNT(DISTINCT customer) as customers
    FROM sales
    GROUP BY region
    ORDER BY revenue DESC
''')

print(f"  {'Region':<10} {'Orders':>8} {'Customers':>10} {'Revenue':>15}")
print("  " + "-" * 48)
for row in cursor.fetchall():
    print(f"  {row['region']:<10} {row['transactions']:>8,} {row['customers']:>10} ${row['revenue']:>14,.2f}")

# =============================================================================
# SECTION 5: TOP CUSTOMERS
# =============================================================================
print("\n" + "=" * 70)
print("🏆 TOP 5 CUSTOMERS")
print("=" * 70)

cursor.execute('''
    SELECT 
        customer,
        COUNT(*) as orders,
        SUM(quantity * unit_price) as total_spent,
        AVG(quantity * unit_price) as avg_order
    FROM sales
    GROUP BY customer
    ORDER BY total_spent DESC
    LIMIT 5
''')

print(f"  {'Rank':<6} {'Customer':<15} {'Orders':>8} {'Total Spent':>15} {'Avg Order':>12}")
print("  " + "-" * 60)
for i, row in enumerate(cursor.fetchall(), 1):
    medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"  {i}.")
    print(f"  {medal:<6} {row['customer']:<15} {row['orders']:>8,} ${row['total_spent']:>14,.2f} ${row['avg_order']:>11,.2f}")

# =============================================================================
# SECTION 6: TOP PRODUCTS
# =============================================================================
print("\n" + "=" * 70)
print("📈 TOP 5 PRODUCTS BY REVENUE")
print("=" * 70)

cursor.execute('''
    SELECT 
        product,
        category,
        SUM(quantity) as units_sold,
        SUM(quantity * unit_price) as revenue,
        COUNT(*) as orders
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC
    LIMIT 5
''')

print(f"  {'#':<4} {'Product':<20} {'Category':<12} {'Units':>8} {'Revenue':>12}")
print("  " + "-" * 60)
for i, row in enumerate(cursor.fetchall(), 1):
    print(f"  {i:<4} {row['product']:<20} {row['category']:<12} {row['units_sold']:>8,} ${row['revenue']:>11,.2f}")

# =============================================================================
# SECTION 7: INVENTORY ALERT
# =============================================================================
print("\n" + "=" * 70)
print("⚠️  LOW STOCK ALERT")
print("=" * 70)

cursor.execute('''
    SELECT name, category, stock_level, reorder_point
    FROM products
    WHERE stock_level <= reorder_point
    ORDER BY (stock_level * 1.0 / reorder_point)
''')

alerts = cursor.fetchall()
if alerts:
    print(f"  {'Product':<20} {'Category':<12} {'Stock':>8} {'Reorder At':>12} {'Status':>10}")
    print("  " + "-" * 65)
    for row in alerts:
        status = "🔴 CRITICAL" if row['stock_level'] < row['reorder_point'] / 2 else "🟡 LOW"
        print(f"  {row['name']:<20} {row['category']:<12} {row['stock_level']:>8} {row['reorder_point']:>12} {status:>10}")
else:
    print("  ✅ All stock levels are healthy!")

# =============================================================================
# SECTION 8: EXPORT TO CSV
# =============================================================================
print("\n" + "=" * 70)
print("💾 EXPORTING REPORT DATA")
print("=" * 70)

# Export detailed sales data
cursor.execute('''
    SELECT 
        date,
        customer,
        product,
        category,
        region,
        quantity,
        unit_price,
        quantity * unit_price as total
    FROM sales
    ORDER BY date
''')

rows = cursor.fetchall()
headers = ['Date', 'Customer', 'Product', 'Category', 'Region', 'Qty', 'Price', 'Total']

with open('sales_report.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

print(f"  Exported {len(rows)} records to 'sales_report.csv'")

# =============================================================================
# SECTION 9: SAVE FULL REPORT TO FILE
# =============================================================================
print("\n" + "=" * 70)
print("📝 SAVING COMPLETE REPORT")
print("=" * 70)

def generate_full_report(conn, filename):
    """Generate a complete report saved to a text file."""
    cursor = conn.cursor()
    
    with open(filename, 'w') as f:
        f.write("=" * 70 + "\n")
        f.write("SALES PERFORMANCE REPORT".center(70) + "\n")
        f.write("=" * 70 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Executive Summary
        f.write("EXECUTIVE SUMMARY\n")
        f.write("-" * 40 + "\n")
        cursor.execute('SELECT COUNT(*), SUM(quantity * unit_price) FROM sales')
        count, revenue = cursor.fetchone()
        f.write(f"Total Transactions: {count:,}\n")
        f.write(f"Total Revenue: ${revenue:,.2f}\n\n")
        
        # Category Breakdown
        f.write("SALES BY CATEGORY\n")
        f.write("-" * 40 + "\n")
        cursor.execute('''
            SELECT category, SUM(quantity * unit_price) as rev
            FROM sales GROUP BY category ORDER BY rev DESC
        ''')
        for cat, rev in cursor.fetchall():
            f.write(f"  {cat}: ${rev:,.2f}\n")
        
        f.write("\n" + "=" * 70 + "\n")
        f.write("END OF REPORT\n")
    
    return filename

report_file = generate_full_report(conn, REPORT_FILE)
print(f"  Full report saved to: {report_file}")

conn.close()

print("\n" + "=" * 70)
print("Examples complete!")
print("=" * 70)

# Cleanup (optional - comment out to keep files)
# for f in [DB_NAME, REPORT_FILE, "sales_report.csv"]:
#     if os.path.exists(f):
#         os.remove(f)
