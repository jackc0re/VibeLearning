# 🔄 Data Transformation

> **Prerequisites:** Modules 01-03, 19_data_processing/01-03  
> **Estimated Time:** 1.5-2 hours

Learn to transform raw data into useful formats for analysis and reporting.

---

## What is Data Transformation?

Data transformation is the process of converting data from one format or structure to another. It includes:

- **Filtering** - Selecting relevant rows
- **Sorting** - Ordering data meaningfully
- **Aggregating** - Summarizing data
- **Pivoting** - Rotating data (rows to columns)
- **Calculated fields** - Creating new columns from existing ones

**Think of it like this:** Raw data is like crude oil; transformation refines it into useful fuel.

---

## Filtering and Selection

### Selecting Specific Columns

```python
# Only get what you need
cursor.execute('''
    SELECT customer_id, order_date, total_amount 
    FROM orders
''')
```

### Row Filtering

```python
# Multiple conditions
cursor.execute('''
    SELECT * FROM sales 
    WHERE date >= '2024-01-01' 
      AND amount > 100
      AND region IN ('North', 'South')
''')
```

---

## Sorting and Ranking

### Basic Sorting

```python
# Single column
cursor.execute('SELECT * FROM products ORDER BY price DESC')

# Multiple columns
cursor.execute('''
    SELECT * FROM employees 
    ORDER BY department ASC, salary DESC
''')
```

### Ranking with Window Functions (SQLite 3.25+)

```python
# Rank employees by salary within each department
cursor.execute('''
    SELECT 
        name,
        department,
        salary,
        RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rank
    FROM employees
''')
```

---

## Aggregation and Grouping

### Common Aggregations

```python
# Summarize by category
cursor.execute('''
    SELECT 
        category,
        COUNT(*) as product_count,
        AVG(price) as avg_price,
        MIN(price) as min_price,
        MAX(price) as max_price,
        SUM(units_sold) as total_sold
    FROM products
    GROUP BY category
''')
```

### Grouping Sets (Multiple Grouping Levels)

```python
# Total and by category in one query
# (Simulated with UNION in basic SQLite)
cursor.execute('''
    SELECT category, COUNT(*) as count FROM products GROUP BY category
    UNION ALL
    SELECT 'TOTAL' as category, COUNT(*) FROM products
''')
```

---

## Pivoting Data

Pivoting transforms rows into columns (like a spreadsheet pivot table).

### Example: Sales by Month

```python
# Before pivot:
# month    | sales
# ---------|-------
# January  | 1000
# February | 1500
# March    | 1200

# After pivot:
# jan_sales | feb_sales | mar_sales
# ----------|-----------|----------
# 1000      | 1500      | 1200

# Using CASE statements for pivot
cursor.execute('''
    SELECT 
        product_id,
        SUM(CASE WHEN month = 'Jan' THEN sales ELSE 0 END) as jan_sales,
        SUM(CASE WHEN month = 'Feb' THEN sales ELSE 0 END) as feb_sales,
        SUM(CASE WHEN month = 'Mar' THEN sales ELSE 0 END) as mar_sales
    FROM monthly_sales
    GROUP BY product_id
''')
```

---

## Creating Calculated Fields

### Simple Calculations

```python
cursor.execute('''
    SELECT 
        product_name,
        price,
        quantity,
        price * quantity as total_value,
        price * 0.9 as discounted_price
    FROM inventory
''')
```

### Conditional Logic

```python
cursor.execute('''
    SELECT 
        customer_name,
        order_total,
        CASE 
            WHEN order_total >= 1000 THEN 'VIP'
            WHEN order_total >= 500 THEN 'Premium'
            ELSE 'Standard'
        END as customer_tier
    FROM orders
''')
```

### Date Calculations

```python
cursor.execute('''
    SELECT 
        order_date,
        julianday('now') - julianday(order_date) as days_ago,
        date(order_date, '+30 days') as due_date
    FROM orders
''')
```

---

## String Transformations

### Concatenation

```python
cursor.execute('''
    SELECT 
        first_name || ' ' || last_name as full_name,
        city || ', ' || country as location
    FROM customers
''')
```

### String Functions

```python
cursor.execute('''
    SELECT 
        UPPER(name) as uppercase_name,
        LOWER(email) as lowercase_email,
        SUBSTR(phone, 1, 3) as area_code,
        LENGTH(description) as desc_length,
        REPLACE(status, 'active', 'live') as new_status
    FROM users
''')
```

---

## Data Normalization and Denormalization

### Normalization (Reduce Redundancy)

Split one table into many:

```
# Before: orders(customer, address, product, price, ...)
# After:  customers(id, name, address)
#         products(id, name, price)
#         orders(id, customer_id, product_id, quantity)
```

### Denormalization (Improve Read Performance)

Join tables for reporting:

```python
cursor.execute('''
    SELECT 
        c.name as customer,
        p.name as product,
        o.quantity,
        p.price * o.quantity as total
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN products p ON o.product_id = p.id
''')
```

---

## Common Transformation Patterns

| Pattern | SQL Technique |
|---------|---------------|
| Filter rows | `WHERE` clause |
| Select columns | Column list in `SELECT` |
| Sort data | `ORDER BY` |
| Summarize | `GROUP BY` with aggregates |
| Add calculated fields | Expressions in `SELECT` |
| Conditional values | `CASE` statements |
| Pivot data | `CASE` with aggregates |
| Join tables | `JOIN` clauses |

---

## Best Practices

1. **Transform incrementally** - Apply one transformation at a time
2. **Validate results** - Check row counts and sample data
3. **Use views** - Save complex transformations as database views
4. **Document logic** - Comment why transformations are needed
5. **Keep originals** - Don't overwrite source data

---

## Common Mistakes

1. **Forgetting GROUP BY** - All non-aggregated columns must be in GROUP BY
2. **Null handling** - `NULL + anything = NULL`; use `COALESCE`
3. **Type mismatches** - Can't concatenate numbers and strings directly
4. **Losing data** - Inner joins exclude non-matching rows unintentionally
5. **Over-pivoting** - Creating too many columns makes data unwieldy

---

## ✅ Before You Continue

1. When would you pivot data vs. keep it in row format?
2. What's the difference between WHERE and HAVING in aggregation queries?
3. How do you handle NULL values in calculations?
4. When should you normalize vs. denormalize data?

---

## Next Steps

- Run `examples.py` to see transformations in action
- Practice with `exercises.py`
- Learn report generation next!
