# 📊 Generating Reports

> **Prerequisites:** Modules 01-03, 19_data_processing/01-04  
> **Estimated Time:** 1.5-2 hours

Learn to create meaningful reports and summaries from your data.

---

## What is a Report?

A report transforms raw data into actionable insights through:

- **Summaries** - Key metrics and totals
- **Breakdowns** - Data segmented by categories
- **Trends** - Changes over time
- **Comparisons** - Performance vs. benchmarks

**Think of it like this:** Data is ingredients; a report is a meal that nourishes decision-making.

---

## Types of Reports

| Report Type | Purpose | Example |
|-------------|---------|---------|
| **Summary** | Overview of key metrics | Total sales, customer count |
| **Detailed** | Line-by-line information | Transaction history |
| **Trend** | Changes over time | Monthly sales growth |
| **Comparison** | Performance vs. targets | Budget vs. actual |
| **Exception** | Highlighting issues | Low stock alerts |

---

## Report Components

### Header Information

```python
from datetime import datetime

print("=" * 60)
print("SALES REPORT")
print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("=" * 60)
```

### Key Performance Indicators (KPIs)

```python
# Fetch summary metrics
cursor.execute('''
    SELECT 
        COUNT(*) as total_orders,
        SUM(total_amount) as total_revenue,
        AVG(total_amount) as avg_order,
        MAX(total_amount) as largest_order
    FROM orders
    WHERE date >= '2024-01-01'
''')
kpis = cursor.fetchone()

print(f"Total Orders: {kpis[0]:,}")
print(f"Total Revenue: ${kpis[1]:,.2f}")
print(f"Average Order: ${kpis[2]:.2f}")
```

### Tabular Data

```python
# Format data as a table
print(f"{'Product':<20} {'Qty':>8} {'Revenue':>12}")
print("-" * 42)
cursor.execute('SELECT product, quantity, revenue FROM sales')
for product, qty, revenue in cursor.fetchall():
    print(f"{product:<20} {qty:>8,} ${revenue:>11,.2f}")
```

---

## Common Report Patterns

### Executive Summary

High-level overview for decision-makers:

```python
def generate_executive_summary(cursor):
    print("\n📊 EXECUTIVE SUMMARY\n")
    
    # Key metrics
    cursor.execute('SELECT COUNT(*), SUM(revenue) FROM sales')
    count, revenue = cursor.fetchone()
    
    # Growth calculation
    cursor.execute('''
        SELECT SUM(revenue) FROM sales 
        WHERE date >= date('now', '-30 days')
    ''')
    recent = cursor.fetchone()[0] or 0
    
    print(f"Total Customers: {count:,}")
    print(f"Total Revenue: ${revenue:,.2f}")
    print(f"Recent Activity (30 days): ${recent:,.2f}")
```

### Trend Analysis

```python
def generate_trend_report(cursor):
    print("\n📈 MONTHLY TRENDS\n")
    
    cursor.execute('''
        SELECT 
            strftime('%Y-%m', date) as month,
            COUNT(*) as orders,
            SUM(amount) as revenue
        FROM sales
        GROUP BY month
        ORDER BY month
    ''')
    
    prev_revenue = None
    for month, orders, revenue in cursor.fetchall():
        if prev_revenue:
            change = ((revenue - prev_revenue) / prev_revenue) * 100
            trend = "📈" if change > 0 else "📉"
            print(f"{month}: ${revenue:>10,.2f} ({trend} {change:+.1f}%)")
        else:
            print(f"{month}: ${revenue:>10,.2f}")
        prev_revenue = revenue
```

### Top N Report

```python
def generate_top_products(cursor, n=5):
    print(f"\n🏆 TOP {n} PRODUCTS\n")
    
    cursor.execute('''
        SELECT product, SUM(quantity) as qty, SUM(revenue) as rev
        FROM sales
        GROUP BY product
        ORDER BY rev DESC
        LIMIT ?
    ''', (n,))
    
    for i, (product, qty, rev) in enumerate(cursor.fetchall(), 1):
        medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, f"{i}.")
        print(f"{medal} {product:<20} Qty: {qty:>4}  Rev: ${rev:>10,.2f}")
```

---

## Exporting Reports

### Text/Console Output

```python
def export_to_console(data, title):
    print(f"\n{'='*50}")
    print(title.center(50))
    print('='*50)
    for row in data:
        print(f"  {row[0]}: {row[1]}")
```

### CSV Export

```python
import csv

def export_to_csv(cursor, filename, query):
    cursor.execute(query)
    rows = cursor.fetchall()
    headers = [description[0] for description in cursor.description]
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Exported {len(rows)} rows to {filename}")
```

### Markdown Report

```python
def export_to_markdown(cursor, filename):
    cursor.execute('SELECT * FROM sales_summary')
    rows = cursor.fetchall()
    headers = [d[0] for d in cursor.description]
    
    with open(filename, 'w') as f:
        # Header
        f.write('| ' + ' | '.join(headers) + ' |\n')
        f.write('|' + '|'.join(['---' for _ in headers]) + '|\n')
        
        # Data
        for row in rows:
            f.write('| ' + ' | '.join(str(c) for c in row) + ' |\n')
```

---

## Report Best Practices

1. **Know your audience** - Executives want summaries; analysts want details
2. **Highlight exceptions** - Make problems stand out
3. **Include context** - Compare to previous periods or targets
4. **Be consistent** - Same format, same time periods
5. **Automate** - Generate reports on schedule

---

## Report Automation

```python
def generate_daily_report():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    
    today = datetime.now().strftime('%Y-%m-%d')
    filename = f"daily_report_{today}.txt"
    
    with open(filename, 'w') as f:
        # Redirect print to file
        import sys
        old_stdout = sys.stdout
        sys.stdout = f
        
        generate_executive_summary(cursor)
        generate_trend_report(cursor)
        generate_top_products(cursor)
        
        sys.stdout = old_stdout
    
    conn.close()
    print(f"Report saved: {filename}")

# Run daily (would use a scheduler in production)
# generate_daily_report()
```

---

## Common Mistakes

1. **Too much data** - Overwhelming instead of informing
2. **No context** - Numbers without comparison are meaningless
3. **Inconsistent formatting** - Hard to read and compare
4. **Stale data** - Old reports lead to bad decisions
5. **No action items** - Reports should drive decisions

---

## ✅ Before You Continue

1. What are the key components of a good report?
2. When would you use a trend report vs. a summary report?
3. How can you make reports more actionable?
4. What formats are best for sharing reports?

---

## Next Steps

- Run `examples.py` to see report generation in action
- Practice with `exercises.py`
- Try creating your own reports from real data!
