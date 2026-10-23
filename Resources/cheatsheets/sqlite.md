# SQLite Cheatsheet

Quick reference for `sqlite3`: connecting, running queries, CRUD, the one
non-negotiable safety rule, and joins. Everything here is standard library —
no `pip install` needed.

---

## The Copy-Paste Pattern

```python
import sqlite3

# Context-manager form: commits on success, rolls back on exception.
# (Note: `with` does NOT close the connection - close it yourself.)
with sqlite3.connect("my_database.db") as conn:
    conn.row_factory = sqlite3.Row        # Access columns by name
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row["name"], row["email"])
    conn.close()
```

Manual form (fine for quick scripts — just don't forget the two closing steps):

```python
import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# ... your queries ...

conn.commit()   # Save changes to the file
conn.close()    # Release the file
```

---

## Cursor Methods

| Method | What it does | Returns |
|--------|--------------|---------|
| `cursor.execute(sql, params)` | Run one SQL statement | The cursor (chainable) |
| `cursor.executemany(sql, list_of_params)` | Run the SQL once per parameter set | The cursor |
| `cursor.fetchone()` | Next row, or `None` if done | One row |
| `cursor.fetchall()` | All remaining rows | List of rows |
| `cursor.fetchmany(n)` | Up to `n` rows | List of rows |
| `conn.commit()` | Make pending changes permanent | — |
| `conn.rollback()` | Undo changes since last commit | — |

```python
# executemany: one statement, many rows (much faster than a loop)
users = [("Alice", "alice@example.com"), ("Bob", "bob@example.com")]
cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
```

---

## CRUD Snippets

```python
# CREATE (insert)
cursor.execute(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    ("Alice", "alice@example.com"),
)

# READ (select)
cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
row = cursor.fetchone()          # None if no match
rows = cursor.fetchall()         # [] if no match

# UPDATE — always a WHERE, or you update EVERY row
cursor.execute(
    "UPDATE users SET email = ? WHERE name = ?",
    ("new@example.com", "Alice"),
)

# DELETE — same warning: check the WHERE twice
cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))
```

---

## ⚠️ The One Non-Negotiable Rule: Parameterize Every Query

Never build SQL with f-strings or `+`. Values passed as parameters are treated
purely as data and can never change the meaning of your SQL.

```python
# ❌ UNSAFE - string formatting invites SQL injection
username = "alice' OR '1'='1"
cursor.execute(f"SELECT * FROM users WHERE name = '{username}'")
# The query becomes: SELECT * FROM users WHERE name = 'alice' OR '1'='1'
# ...which matches EVERY user. Game over.

# ✅ SAFE - pass a parameter tuple, use ? placeholders
cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
```

Details that trip people up:

- One value still needs a **tuple**: `(username,)` — note the trailing comma.
- `executemany` takes a **list of tuples**: `[(a, b), (c, d)]`.
- Placeholders mark values only — table and column names can't be
  parameterized (build those from code you control, never user input).

---

## Transactions in Two Sentences

SQLite runs your statements inside a transaction: nothing hits the file until
you `conn.commit()`, and `conn.rollback()` undoes everything since the last
commit. The `with sqlite3.connect(...)` form automates this — commit when the
block exits cleanly, rollback if an exception escapes — which is why it's the
recommended pattern for multi-step writes (e.g. transfer money out of one
account and into another: both happen or neither does).

---

## Tiny Schema + Join

```python
import sqlite3

with sqlite3.connect("shop.db") as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id   INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id      INTEGER PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            total   REAL NOT NULL
        )
    """)
    cursor.executemany(
        "INSERT INTO users (name) VALUES (?)",
        [("Alice",), ("Bob",)],
    )

    # JOIN: pair each order with the user who placed it
    cursor.execute("""
        SELECT users.name, orders.total
        FROM orders
        JOIN users ON orders.user_id = users.id
        ORDER BY orders.total DESC
    """)
    for row in cursor.fetchall():
        print(row["name"], row["total"])
```

> A `JOIN` walks the connection between tables: every `orders.user_id` that
> matches a `users.id` produces one combined row.

---

## Quick Reference

| Task | Code |
|------|------|
| Open a database | `sqlite3.connect("file.db")` |
| In-memory scratch DB | `sqlite3.connect(":memory:")` |
| Get a cursor | `cursor = conn.cursor()` |
| Run SQL | `cursor.execute(sql, params)` |
| Many rows in | `cursor.executemany(sql, list)` |
| One row out | `cursor.fetchone()` |
| All rows out | `cursor.fetchall()` |
| Column names as keys | `conn.row_factory = sqlite3.Row` |
| Save changes | `conn.commit()` |
| Undo changes | `conn.rollback()` |

---

**Learn more:** [SQLite basics](../../19_data_processing/01_sqlite_basics/README.md) ·
[SQL fundamentals](../../19_data_processing/02_sql_fundamentals/README.md)

**Back to [Resources](../README.md)**
