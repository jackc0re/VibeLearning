# 🗄️ SQLite Basics - Quiz

Test your understanding of SQLite fundamentals.

---

## Question 1
**Which Python module provides SQLite functionality?**

A) `sqlite`  
B) `sqlite3`  
C) `db.sqlite`  
D) `pysqlite`

---

## Question 2
**What does `cursor.fetchone()` return if no rows match the query?**

A) An empty list `[]`  
B) An empty tuple `()`  
C) `None`  
D) Raises an exception

---

## Question 3
**What is the correct way to safely insert user-provided data?**

A) `cursor.execute(f"INSERT INTO users VALUES ('{name}')")`  
B) `cursor.execute("INSERT INTO users VALUES (?)", (name,))`  
C) `cursor.execute("INSERT INTO users VALUES ('" + name + "')")`  
D) Both A and C

---

## Question 4
**Which constraint ensures a column cannot have NULL values?**

A) `UNIQUE`  
B) `PRIMARY KEY`  
C) `NOT NULL`  
D) `CHECK`

---

## Question 5
**What happens if you forget to call `conn.commit()`?**

A) The program crashes  
B) Changes are automatically saved  
C) Changes are lost when connection closes  
D) Nothing, it's optional

---

## Question 6
**Which method is best for inserting multiple rows at once?**

A) Multiple `execute()` calls in a loop  
B) `executemany()`  
C) `executeall()`  
D) `batch_insert()`

---

## Question 7
**What is the purpose of `conn.row_factory = sqlite3.Row`?**

A) Makes rows immutable  
B) Allows accessing columns by name instead of index  
C) Creates a factory pattern for rows  
D) Improves query performance

---

## Question 8
**Which SQLite data type is best for storing monetary values?**

A) `INTEGER` (store cents)  
B) `REAL`  
C) `TEXT`  
D) `BLOB`

---

## Question 9
**What does `AUTOINCREMENT` do?**

A) Automatically commits transactions  
B) Automatically generates unique integer IDs  
C) Automatically increments numeric columns  
D) Automatically creates indexes

---

## Question 10
**In the context manager pattern (`with sqlite3.connect() as conn:`), when is the transaction committed?**

A) Immediately after each execute  
B) When the `with` block exits successfully  
C) You still need to call `commit()` manually  
D) Never, changes are lost

---

# Answers

<details>
<summary>Click to reveal answers</summary>

1. **B** - The module is `sqlite3` and it's built into Python.
2. **C** - `fetchone()` returns `None` when no rows match.
3. **B** - Always use parameterized queries with `?` placeholders to prevent SQL injection.
4. **C** - `NOT NULL` ensures a column must have a value.
5. **C** - Without `commit()`, all changes are rolled back when the connection closes.
6. **B** - `executemany()` is more efficient for inserting multiple rows.
7. **B** - It allows dictionary-style access like `row['column_name']`.
8. **A** - Best practice is to store monetary values as INTEGER (cents) to avoid floating-point errors. `REAL` can also work but has precision issues.
9. **B** - `AUTOINCREMENT` automatically generates unique integer IDs for new rows.
10. **B** - The context manager automatically commits when exiting the block (if no exception occurred).

</details>
