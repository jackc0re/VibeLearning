# 🔄 Data Transformation - Quiz

Test your data transformation knowledge!

---

## Question 1
**What SQL clause is used to create conditional calculated fields?**

A) `IF`  
B) `WHEN`  
C) `CASE`  
D) `CONDITION`

---

## Question 2
**How do you concatenate two columns in SQLite?**

A) `CONCAT(first_name, last_name)`  
B) `first_name + last_name`  
C) `first_name || last_name`  
D) `JOIN(first_name, last_name)`

---

## Question 3
**What is "pivoting" in data transformation?**

A) Sorting data by multiple columns  
B) Converting rows into columns  
C) Aggregating data by groups  
D) Filtering data by conditions

---

## Question 4
**Which expression correctly calculates a 15% discount?**

A) `price - 15`  
B) `price * 0.15`  
C) `price * 0.85`  
D) `price / 1.15`

---

## Question 5
**How do you extract the month from a date '2024-03-15' in SQLite?**

A) `MONTH(date)`  
B) `EXTRACT(MONTH FROM date)`  
C) `SUBSTR(date, 6, 2)`  
D) `strftime('%m', date)`

---

## Question 6
**What does `COALESCE(value, 0)` do?**

A) Rounds value to 0 decimal places  
B) Returns 0 if value is NULL  
C) Checks if value equals 0  
D) Converts value to integer

---

## Question 7
**In a pivot query using CASE statements, why do we use SUM?**

A) To add up all the CASE results  
B) To collapse multiple rows into one  
C) Because CASE returns multiple values  
D) To calculate totals automatically

---

## Question 8
**What happens if you divide by NULL in SQL?**

A) Returns 0  
B) Returns NULL  
C) Raises an error  
D) Returns infinity

---

## Question 9
**Which is the correct syntax for categorizing sales?**

A) `IF amount > 1000 THEN 'Large' ELSE 'Small'`  
B) `CASE WHEN amount > 1000 THEN 'Large' ELSE 'Small' END`  
C) `WHEN amount > 1000 THEN 'Large' ELSE 'Small'`  
D) `CATEGORY('Large' IF amount > 1000 ELSE 'Small')`

---

## Question 10
**What is the purpose of GROUP BY in aggregation queries?**

A) To sort results  
B) To filter rows  
C) To group rows with same values for summarization  
D) To join tables

---

# Answers

<details>
<summary>Click to reveal answers</summary>

1. **C** - `CASE` is used for conditional logic in SQL.
2. **C** - SQLite uses `||` for string concatenation.
3. **B** - Pivoting transforms row-based data into column-based format.
4. **C** - `price * 0.85` gives the price after 15% discount.
5. **D** - `strftime('%m', date)` extracts the month from a date.
6. **B** - `COALESCE` returns the first non-NULL value from its arguments.
7. **B** - SUM with CASE collapses rows, keeping only matching values.
8. **B** - Any operation with NULL returns NULL (except IS NULL).
9. **B** - `CASE WHEN condition THEN value ELSE value END` is correct syntax.
10. **C** - GROUP BY groups rows with the same values in specified columns.

</details>
