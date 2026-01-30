# 🔍 SQL Fundamentals

> **Prerequisites:** 19_data_processing/01_sqlite_basics  
> **Estimated Time:** 2-2.5 hours

Master the essential SQL commands for querying and manipulating data.

---

## What is SQL?

**SQL (Structured Query Language)** is the standard language for interacting with relational databases. It allows you to:

- Query data with `SELECT`
- Insert data with `INSERT`
- Update data with `UPDATE`
- Delete data with `DELETE`

**Think of it like this:** If the database is a filing cabinet, SQL is the language you use to ask the librarian for specific files.

---

## The SELECT Statement

The most commonly used SQL command. It retrieves data from one or more tables.

### Basic Syntax

```sql
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name;  -- All columns
```

### Filtering with WHERE

```sql
SELECT * FROM employees WHERE department = 'Sales';
SELECT * FROM products WHERE price > 100;
SELECT * FROM users WHERE age BETWEEN 18 AND 65;
```

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `=` | Equal to |
| `!=` or `<>` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |
| `BETWEEN` | Within a range |
| `IN` | Match any in a list |
| `LIKE` | Pattern matching |
| `IS NULL` | Is NULL value |

### Logical Operators

```sql
-- AND: Both conditions must be true
SELECT * FROM products WHERE price > 50 AND stock > 0;

-- OR: At least one condition must be true
SELECT * FROM employees WHERE department = 'Sales' OR department = 'Marketing';

-- NOT: Negates a condition
SELECT * FROM products WHERE NOT category = 'Electronics';

-- Combining them
SELECT * FROM employees 
WHERE (department = 'Sales' OR department = 'Marketing') 
  AND salary > 50000;
```

---

## Sorting and Limiting Results

### ORDER BY

```sql
-- Ascending (default)
SELECT * FROM products ORDER BY price;

-- Descending
SELECT * FROM products ORDER BY price DESC;

-- Multiple columns
SELECT * FROM employees ORDER BY department ASC, salary DESC;
```

### LIMIT

```sql
-- Top 10 most expensive products
SELECT * FROM products ORDER BY price DESC LIMIT 10;

-- Skip first 20, get next 10 (pagination)
SELECT * FROM products LIMIT 10 OFFSET 20;
```

---

## Aggregation Functions

Aggregate functions perform calculations on a set of values.

```sql
-- Count rows
SELECT COUNT(*) FROM employees;
SELECT COUNT(DISTINCT department) FROM employees;

-- Sum values
SELECT SUM(salary) FROM employees;

-- Average
SELECT AVG(price) FROM products;

-- Minimum and Maximum
SELECT MIN(price), MAX(price) FROM products;
```

### GROUP BY

Group rows that have the same values into summary rows.

```sql
-- Employees per department
SELECT department, COUNT(*) as employee_count
FROM employees
GROUP BY department;

-- Average salary by department
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
```

### HAVING Clause

Filter groups (used instead of WHERE for aggregate conditions):

```sql
-- Departments with more than 5 employees
SELECT department, COUNT(*) as count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

> **WHERE vs HAVING:** `WHERE` filters rows before grouping, `HAVING` filters groups after aggregation.

---

## Pattern Matching with LIKE

```sql
-- Names starting with 'J'
SELECT * FROM employees WHERE name LIKE 'J%';

-- Emails ending with '@company.com'
SELECT * FROM users WHERE email LIKE '%@company.com';

-- Titles containing 'Manager'
SELECT * FROM jobs WHERE title LIKE '%Manager%';

-- Single character wildcard
SELECT * FROM products WHERE code LIKE 'A__';  -- A followed by 2 chars
```

| Wildcard | Meaning |
|----------|---------|
| `%` | Zero or more characters |
| `_` | Exactly one character |

---

## Joining Tables

Combine rows from two or more tables based on related columns.

### INNER JOIN

Returns only matching rows from both tables.

```sql
SELECT employees.name, departments.name as dept_name
FROM employees
INNER JOIN departments ON employees.dept_id = departments.id;
```

### LEFT JOIN

Returns all rows from the left table, and matching rows from the right.

```sql
-- All employees, even those without a department
SELECT employees.name, departments.name as dept_name
FROM employees
LEFT JOIN departments ON employees.dept_id = departments.id;
```

### Join Types Visual

```
INNER JOIN:     LEFT JOIN:      RIGHT JOIN:     FULL JOIN:
  A     B        A     B        A     B        A     B
  ◆====◆         ◆====◆              ◆====◆     ◆====◆
  ◆====◆         ◆====◆              ◆====◆     ◆    ◆
       ◆         ◆                  ◆====◆     ◆====◆
```

---

## Subqueries

A query within another query.

```sql
-- Employees earning above average salary
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Products in the same category as 'Laptop'
SELECT name FROM products
WHERE category = (SELECT category FROM products WHERE name = 'Laptop');
```

---

## SQL Command Quick Reference

| Task | SQL |
|------|-----|
| Select all columns | `SELECT * FROM table` |
| Select specific columns | `SELECT col1, col2 FROM table` |
| Filter rows | `SELECT * FROM table WHERE condition` |
| Sort results | `SELECT * FROM table ORDER BY col ASC/DESC` |
| Limit results | `SELECT * FROM table LIMIT n` |
| Count rows | `SELECT COUNT(*) FROM table` |
| Sum column | `SELECT SUM(col) FROM table` |
| Average | `SELECT AVG(col) FROM table` |
| Group by | `SELECT col, COUNT(*) FROM table GROUP BY col` |
| Join tables | `SELECT * FROM t1 JOIN t2 ON t1.id = t2.id` |

---

## Common Mistakes

1. **Forgetting GROUP BY** - Must include all non-aggregated columns in GROUP BY
2. **Using WHERE with aggregates** - Use HAVING instead of WHERE for aggregate conditions
3. **Case sensitivity** - SQL keywords are not case-sensitive, but string comparisons might be
4. **Missing quotes** - String literals need single quotes: `'value'` not `value`
5. **Ambiguous column names** - Specify table name when joining: `table.column`

---

## ✅ Before You Continue

1. What's the difference between WHERE and HAVING?
2. When would you use a LEFT JOIN instead of an INNER JOIN?
3. How do you find duplicate values in a table?
4. What's the difference between COUNT(*) and COUNT(column)?

---

## Next Steps

- Run `examples.py` to see SQL queries in action
- Practice with `exercises.py`
- Learn data cleaning techniques next!
