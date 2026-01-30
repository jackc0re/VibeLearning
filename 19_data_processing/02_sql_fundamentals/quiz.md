# 🔍 SQL Fundamentals - Quiz

Test your SQL knowledge!

---

## Question 1
**Which clause is used to filter rows before grouping?**

A) `HAVING`  
B) `WHERE`  
C) `GROUP BY`  
D) `FILTER`

---

## Question 2
**What does `SELECT COUNT(DISTINCT department) FROM employees` return?**

A) Total number of employees  
B) Number of unique departments  
C) Employees with distinct names  
D) All departments with counts

---

## Question 3
**Which SQL statement correctly finds employees earning between 50000 and 70000?**

A) `SELECT * FROM employees WHERE salary = 50000 AND 70000`  
B) `SELECT * FROM employees WHERE salary BETWEEN 50000 AND 70000`  
C) `SELECT * FROM employees WHERE salary IN (50000, 70000)`  
D) `SELECT * FROM employees WHERE salary RANGE 50000 TO 70000`

---

## Question 4
**What is the result of `SELECT * FROM products LIMIT 5 OFFSET 10`?**

A) First 5 rows  
B) Rows 11-15  
C) Rows 10-15  
D) Last 5 rows

---

## Question 5
**Which join returns all rows from the left table and matching rows from the right?**

A) `INNER JOIN`  
B) `RIGHT JOIN`  
C) `LEFT JOIN`  
D) `FULL JOIN`

---

## Question 6
**What does the `%` wildcard match in a LIKE clause?**

A) Exactly one character  
B) Zero or more characters  
C) Exactly one number  
D) A percentage sign

---

## Question 7
**Which query finds the department with the highest average salary?**

A) `SELECT department, MAX(AVG(salary)) FROM employees GROUP BY department`  
B) `SELECT department, AVG(salary) FROM employees GROUP BY department ORDER BY AVG(salary) DESC LIMIT 1`  
C) `SELECT department, AVG(salary) as max FROM employees`  
D) `SELECT TOP 1 department, AVG(salary) FROM employees GROUP BY department`

---

## Question 8
**What is a subquery?**

A) A query that runs faster than the main query  
B) A query nested inside another query  
C) A query that only returns one row  
D) A query without a WHERE clause

---

## Question 9
**What does `COALESCE(column, 0)` do?**

A) Converts column to uppercase  
B) Returns 0 if column is NULL  
C) Counts non-NULL values  
D) Concatenates column with 0

---

## Question 10
**Which statement is TRUE about NULL values?**

A) `NULL = NULL` returns TRUE  
B) `NULL != NULL` returns TRUE  
C) `NULL IS NULL` returns TRUE  
D) `NULL = 0` returns TRUE

---

# Answers

<details>
<summary>Click to reveal answers</summary>

1. **B** - `WHERE` filters rows before grouping; `HAVING` filters groups after aggregation.
2. **B** - `COUNT(DISTINCT column)` counts unique values in that column.
3. **B** - `BETWEEN` is inclusive and checks if value is within range.
4. **B** - OFFSET skips first 10 rows, LIMIT returns next 5 (rows 11-15).
5. **C** - `LEFT JOIN` returns all rows from left table and matching rows from right.
6. **B** - `%` matches zero or more characters; `_` matches exactly one character.
7. **B** - Group by department, order by average salary descending, take first result.
8. **B** - A subquery is a query nested inside another query (in SELECT, FROM, or WHERE).
9. **B** - `COALESCE` returns the first non-NULL value from its arguments.
10. **C** - NULL is not equal to anything, not even NULL. Use `IS NULL` to check for NULL.

</details>
