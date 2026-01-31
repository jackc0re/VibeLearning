# 🧹 Data Cleaning

> **Prerequisites:** Modules 01-03, 19_data_processing/01-02  
> **Estimated Time:** 1.5-2 hours

Learn techniques for handling messy, incomplete, and inconsistent data.

---

## Why Data Cleaning Matters

Real-world data is messy:
- Missing values
- Duplicate records
- Inconsistent formatting
- Invalid data types
- Typos and errors

**Garbage in, garbage out** - Clean data is essential for accurate analysis!

---

## Common Data Quality Issues

| Issue | Example | Solution |
|-------|---------|----------|
| **Missing values** | `age: None` | Imputation, deletion |
| **Duplicates** | Same record twice | Deduplication |
| **Inconsistent formats** | `"2024-01-01"` vs `"01/01/2024"` | Standardization |
| **Typos** | `"Englsh"` vs `"English"` | Validation, correction |
| **Outliers** | Age: 150 | Detection, handling |
| **Type mismatches** | `"123"` instead of `123` | Type conversion |

---

## Handling Missing Values

### Detect Missing Values

```python
import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Count NULL values per column
cursor.execute('''
    SELECT 
        COUNT(*) - COUNT(age) as missing_age,
        COUNT(*) - COUNT(email) as missing_email
    FROM users
''')
```

### Strategies for Missing Data

```python
# 1. Delete rows with missing values
# Use when: Missing data is rare and random
cursor.execute('DELETE FROM users WHERE email IS NULL')

# 2. Fill with default value
# Use when: There's a sensible default
cursor.execute('UPDATE users SET country = ? WHERE country IS NULL', ('Unknown',))

# 3. Fill with statistical value (mean, median)
# Use when: Data is numeric and missing at random
cursor.execute('SELECT AVG(age) FROM users WHERE age IS NOT NULL')
avg_age = cursor.fetchone()[0]
cursor.execute('UPDATE users SET age = ? WHERE age IS NULL', (avg_age,))

# 4. Forward fill (use previous value)
# Use when: Data is ordered (time series)
```

---

## Removing Duplicates

### Find Duplicates

```python
# Find duplicate emails
cursor.execute('''
    SELECT email, COUNT(*) as count
    FROM users
    GROUP BY email
    HAVING COUNT(*) > 1
''')
```

### Remove Duplicates

```python
# Keep only the first occurrence
cursor.execute('''
    DELETE FROM users
    WHERE id NOT IN (
        SELECT MIN(id)
        FROM users
        GROUP BY email
    )
''')
```

---

## Standardizing Data

### String Standardization

```python
# Trim whitespace
cursor.execute("UPDATE users SET name = TRIM(name)")

# Convert to consistent case
cursor.execute("UPDATE users SET email = LOWER(email)")
cursor.execute("UPDATE products SET category = UPPER(category)")

# Standardize formats
cursor.execute('''
    UPDATE users 
    SET phone = REPLACE(REPLACE(phone, '(', ''), ')', '')
''')  # Remove parentheses from phone numbers
```

### Date Standardization

```python
from datetime import datetime

# Convert various date formats to ISO format
def standardize_date(date_str):
    formats = ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    return None  # Invalid date
```

---

## Data Validation

### Check Constraints

```python
# Validate email format (basic check)
cursor.execute('''
    SELECT * FROM users 
    WHERE email NOT LIKE '%@%.%'
''')
invalid_emails = cursor.fetchall()

# Validate age is reasonable
cursor.execute('SELECT * FROM users WHERE age < 0 OR age > 120')
invalid_ages = cursor.fetchall()

# Check for negative prices
cursor.execute('SELECT * FROM products WHERE price < 0')
invalid_prices = cursor.fetchall()
```

### Data Type Conversion

```python
# Convert string numbers to integers
def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Convert and validate
cursor.execute('SELECT id, age FROM users')
for row_id, age_str in cursor.fetchall():
    age = safe_int(age_str)
    if age < 0 or age > 120:
        age = None  # Mark as invalid
    cursor.execute('UPDATE users SET age = ? WHERE id = ?', (age, row_id))
```

---

## Outlier Detection

### Statistical Methods

```python
# Using standard deviation
cursor.execute('SELECT AVG(price), AVG(price*price) FROM products')
avg, avg_sq = cursor.fetchone()
std_dev = (avg_sq - avg**2) ** 0.5

# Find outliers (beyond 3 standard deviations)
lower = avg - 3 * std_dev
upper = avg + 3 * std_dev
cursor.execute('''
    SELECT * FROM products 
    WHERE price < ? OR price > ?
''', (lower, upper))
outliers = cursor.fetchall()
```

### IQR Method (Interquartile Range)

```python
# More robust to extreme outliers
# Q1 = 25th percentile, Q3 = 75th percentile
# IQR = Q3 - Q1
# Outliers are < Q1 - 1.5*IQR or > Q3 + 1.5*IQR
```

---

## Data Cleaning Workflow

```
┌─────────────────┐
│  1. Profile     │  → Understand data structure, identify issues
│     Data        │
└────────┬────────┘
         ↓
┌─────────────────┐
│  2. Handle      │  → Remove or fill missing values
│  Missing Data   │
└────────┬────────┘
         ↓
┌─────────────────┐
│  3. Remove      │  → Delete duplicate records
│   Duplicates    │
└────────┬────────┘
         ↓
┌─────────────────┐
│  4. Standardize │  → Consistent formats, units, casing
│     Formats     │
└────────┬────────┘
         ↓
┌─────────────────┐
│  5. Validate    │  → Check ranges, formats, constraints
│     & Fix       │
└────────┬────────┘
         ↓
┌─────────────────┐
│  6. Document    │  → Record what was changed
│   Changes       │
└─────────────────┘
```

---

## Best Practices

1. **Always work on a copy** - Never clean original data directly
2. **Document everything** - Track what was changed and why
3. **Be conservative** - Don't remove data unless necessary
4. **Validate results** - Check your cleaning didn't introduce errors
5. **Automate** - Create reusable cleaning functions

---

## Common Mistakes

1. **Deleting too aggressively** - Losing valuable data
2. **Filling missing values blindly** - Using inappropriate defaults
3. **Not checking for duplicates** - Inflating counts
4. **Ignoring outliers** - They might be errors or interesting cases
5. **No documentation** - Can't reproduce or explain changes

---

## ✅ Before You Continue

1. What are 3 different ways to handle missing data?
2. When should you delete duplicates vs. keep them?
3. Why is it important to standardize text casing?
4. What's the difference between an outlier and an error?

---

## Next Steps

- Run `examples.py` to see data cleaning in action
- Practice with `exercises.py`
- Learn data transformation techniques next!
