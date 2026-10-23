# 🗄️ SQLite Basics

> **Prerequisites:** Modules 01-03, 10 (File I/O)  
> **Estimated Time:** 1.5-2 hours

Learn to use SQLite, a lightweight database engine that's built into Python. No server setup required!

---

## What is SQLite?

SQLite is a **self-contained, serverless database** that stores all data in a single file. It's perfect for:

- Desktop applications
- Small to medium websites
- Data analysis projects
- Prototyping before moving to larger databases

**Think of it like this:** A regular database (MySQL, PostgreSQL) is like a library with librarians—you need to ask for books. SQLite is like having the entire library in your backpack.

---

## Why SQLite?

| Feature | Benefit |
|---------|---------|
| **Zero Configuration** | No server to install or configure |
| **Single File** | Entire database is one `.db` file |
| **Built-in Python** | Comes with Python via `sqlite3` module |
| **Portable** | Move the file anywhere |
| **Reliable** | Used by billions of devices worldwide |

---

## Basic Workflow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Connect to DB  │ --> │  Execute SQL    │ --> │   Close conn    │
│  (or create)    │     │  (CRUD ops)     │     │   (save data)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## Connecting to a Database

```python
import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = conn.cursor()

# ... do database operations ...

# Save changes and close
conn.commit()
conn.close()
```

**Best Practice:** Use the `with` statement so a failed block rolls back and a successful one commits:

```python
import sqlite3

with sqlite3.connect('my_database.db') as conn:
    cursor = conn.cursor()
    # ... operations ...
    # Committed automatically when the block exits without an error,
    # rolled back if an exception escapes the block.
    # Careful: `with` does NOT close the connection - call conn.close() too.
```

---

## Creating Tables

```python
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
```

### Common Data Types

| Type | Description | Example |
|------|-------------|---------|
| `INTEGER` | Whole numbers | `42`, `-7` |
| `REAL` | Floating point | `3.14`, `-0.5` |
| `TEXT` | Strings | `'Hello'` |
| `BLOB` | Binary data | Images, files |
| `NUMERIC` | Numbers/dates stored as numbers when possible | `3.14`, `'2025-01-01'` |
| `NULL` | Missing value | `None` in Python |

> SQLite has no separate boolean type - `True`/`False` are stored as `1`/`0` in an `INTEGER` column.

### Constraints

| Constraint | Purpose |
|------------|---------|
| `PRIMARY KEY` | Unique identifier for each row |
| `AUTOINCREMENT` | Automatically generate IDs |
| `NOT NULL` | Column must have a value |
| `UNIQUE` | No duplicate values allowed |
| `DEFAULT` | Default value if none provided |
| `FOREIGN KEY` | Links to another table |

---

## CRUD Operations

### Create (INSERT)

```python
# Insert single row
cursor.execute('''
    INSERT INTO users (name, email, age) 
    VALUES (?, ?, ?)
''', ('Alice', 'alice@example.com', 30))

# Insert multiple rows
users = [
    ('Bob', 'bob@example.com', 25),
    ('Carol', 'carol@example.com', 35),
    ('David', 'david@example.com', 28)
]
cursor.executemany('''
    INSERT INTO users (name, email, age) 
    VALUES (?, ?, ?)
''', users)
```

> **Note:** Always use `?` placeholders to prevent SQL injection attacks! If
> user input like `bob' OR '1'='1` is pasted into SQL with an f-string, the query
> becomes `... WHERE name = 'bob' OR '1'='1'` and returns **every** row; with a
> `?` placeholder the same input is just a literal value and matches nothing.
> `examples.py` section 9 runs this attack and the safe version side by side.

### Read (SELECT)

```python
# Fetch all rows
cursor.execute('SELECT * FROM users')
all_users = cursor.fetchall()  # Returns list of tuples

# Fetch one row
cursor.execute('SELECT * FROM users WHERE id = ?', (1,))
user = cursor.fetchone()  # Returns tuple or None

# Fetch many rows
cursor.execute('SELECT * FROM users')
some_users = cursor.fetchmany(5)  # First 5 rows
```

### Update

```python
cursor.execute('''
    UPDATE users 
    SET age = ? 
    WHERE name = ?
''', (31, 'Alice'))
```

### Delete

```python
cursor.execute('DELETE FROM users WHERE id = ?', (5,))
```

---

## Row Factory (Dictionary-style Access)

By default, rows are returned as tuples. For clearer code:

```python
# Access by column name instead of index
conn.row_factory = sqlite3.Row

cursor.execute('SELECT * FROM users')
row = cursor.fetchone()

print(row['name'])   # Instead of row[1]
print(row['email'])  # Instead of row[2]
```

---

## Transactions

SQLite supports transactions for data integrity:

```python
try:
    cursor.execute('INSERT INTO accounts (user_id, balance) VALUES (?, ?)', (1, 100))
    cursor.execute('UPDATE accounts SET balance = balance - ? WHERE user_id = ?', (50, 1))
    cursor.execute('UPDATE accounts SET balance = balance + ? WHERE user_id = ?', (50, 2))
    conn.commit()  # All or nothing
except sqlite3.Error as e:
    conn.rollback()  # Undo all changes
    print(f"Transaction failed: {e}")
```

---

## Common Mistakes

1. **Forgetting to commit()** - Changes are lost!
2. **Not closing connections** - Can lead to locked databases
3. **String formatting instead of placeholders** - SQL injection risk
4. **Not checking if table exists** - "table already exists" errors

---

## Quick Reference

| Task | Code |
|------|------|
| Connect | `conn = sqlite3.connect('file.db')` |
| Create cursor | `cursor = conn.cursor()` |
| Execute SQL | `cursor.execute(sql, params)` |
| Execute many | `cursor.executemany(sql, list)` |
| Fetch all | `cursor.fetchall()` |
| Fetch one | `cursor.fetchone()` |
| Commit | `conn.commit()` |
| Close | `conn.close()` |

---

## ✅ Before You Continue

1. How do you create a new SQLite database?
2. What's the difference between `fetchone()`, `fetchall()`, and `fetchmany()`?
3. Why should you use `?` placeholders instead of string formatting?
4. When would you use `conn.rollback()`?

---

## Next Steps

- Run `examples.py` to see SQLite in action
- Practice with `exercises.py`
- Learn SQL queries in the next topic!

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
