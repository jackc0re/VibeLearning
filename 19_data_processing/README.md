# 🗃️ Module 19: Data Processing & Databases

> **Difficulty:** ⭐⭐⭐ Intermediate  
> **Estimated Time:** 8-10 hours  
> **Prerequisites:** Modules 01-03 (Foundations), Module 10 (File I/O)

Learn to store, query, clean, transform, and report on data using SQLite and Python.

---

## Module Overview

Data is the lifeblood of modern applications. This module teaches you practical skills for working with structured data—from storing it in databases to generating meaningful reports.

### What You'll Learn

- ✅ Create and manage SQLite databases
- ✅ Write SQL queries for data retrieval and manipulation
- ✅ Clean messy real-world data
- ✅ Transform data for analysis
- ✅ Generate professional reports

---

## Topics

### [01_sqlite_basics](01_sqlite_basics/) - SQLite Basics
Learn to create databases, tables, and perform CRUD operations.

**Key Concepts:**
- Connecting to SQLite databases
- Creating tables with constraints
- INSERT, SELECT, UPDATE, DELETE operations
- Using parameterized queries

**Files:** `README.md`, `examples.py`, `exercises.py`, `quiz.md`

---

### [02_sql_fundamentals](02_sql_fundamentals/) - SQL Fundamentals
Master SQL for querying and analyzing data.

**Key Concepts:**
- SELECT statements with filtering (WHERE)
- Sorting (ORDER BY) and limiting results
- Aggregation functions (COUNT, SUM, AVG, MIN, MAX)
- GROUP BY and HAVING clauses
- JOINing multiple tables
- Subqueries

**Files:** `README.md`, `examples.py`, `exercises.py`, `quiz.md`

---

### [03_data_cleaning](03_data_cleaning/) - Data Cleaning
Handle messy, incomplete, and inconsistent data.

**Key Concepts:**
- Identifying data quality issues
- Handling missing values (NULLs)
- Removing duplicates
- Standardizing formats
- Data validation
- Outlier detection

**Files:** `README.md`, `examples.py`, `exercises.py`, `quiz.md`

---

### [04_data_transformation](04_data_transformation/) - Data Transformation
Transform raw data into useful formats for analysis.

**Key Concepts:**
- Filtering and selecting data
- Sorting and ranking
- Creating calculated fields
- Aggregation and grouping
- Pivoting data (rows to columns)
- Date and string transformations

**Files:** `README.md`, `examples.py`, `exercises.py`, `quiz.md`

---

### [05_generating_reports](05_generating_reports/) - Generating Reports
Create meaningful reports and summaries from your data.

**Key Concepts:**
- Report types (summary, trend, comparison)
- Key Performance Indicators (KPIs)
- Formatting tabular data
- Exporting to CSV and text files
- Report automation

**Files:** `README.md`, `examples.py`, `exercises.py`, `quiz.md`

---

## Learning Path

```
┌─────────────────────────────────────────────────────────────────┐
│                    DATA PROCESSING & DATABASES                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Week 1: Foundations                                             │
│  ┌──────────────┐    ┌──────────────┐                           │
│  │ SQLite Basics │ -> │ SQL Fundam.  │                           │
│  └──────────────┘    └──────────────┘                           │
│         │                   │                                    │
│         ▼                   ▼                                    │
│  ┌──────────────┐    ┌──────────────┐                           │
│  │ CRUD ops     │    │ Queries      │                           │
│  │ Tables       │    │ Joins        │                           │
│  │ Constraints  │    │ Aggregation  │                           │
│  └──────────────┘    └──────────────┘                           │
│                                                                  │
│  Week 2: Practical Skills                                        │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │ Data Cleaning │ -> │ Data Xform   │ -> │ Reports      │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
│         │                   │                   │               │
│         ▼                   ▼                   ▼               │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │ Missing data │    │ Filtering    │    │ KPIs         │       │
│  │ Duplicates   │    │ Pivoting     │    │ Export       │       │
│  │ Validation   │    │ Calculations │    │ Formatting   │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Module Project Ideas

Apply your skills with these projects:

### 📝 Personal Expense Tracker
- Track expenses with categories
- Monthly spending reports
- Budget vs. actual analysis

### 📚 Book/Library Manager
- Catalog books with metadata
- Track borrowing/returning
- Generate reading statistics

### 🏋️ Workout Logger
- Log exercises with sets/reps
- Track progress over time
- Personal records report

---

## Key Takeaways

By the end of this module, you will:

1. **Understand databases** - Know when and why to use SQLite
2. **Write SQL** - Query, filter, aggregate, and join data
3. **Clean data** - Handle real-world data quality issues
4. **Transform data** - Prepare data for analysis
5. **Create reports** - Generate actionable insights

---

## Common Use Cases

| Use Case | Tools/Techniques |
|----------|-----------------|
| Store application data | SQLite + Python sqlite3 |
| Analyze sales data | SQL aggregation + GROUP BY |
| Clean survey responses | Data validation + standardization |
| Generate monthly reports | SQL queries + CSV export |
| Track inventory | Tables + constraints + reports |

---

## SQLite Quick Reference

```python
import sqlite3

# Connect
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
''')

# Insert
cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Alice', 'a@b.com'))

# Query
cursor.execute('SELECT * FROM users WHERE name = ?', ('Alice',))
rows = cursor.fetchall()

# Commit and close
conn.commit()
conn.close()
```

---

## Next Steps

After completing this module, you'll be ready for:
- **Module 20: Web Basics** - Build web interfaces for your data
- **Projects** - Apply database skills to real-world projects
- **Advanced SQL** - Explore window functions, CTEs, and optimization

---

## Resources

- [SQLite Documentation](https://sqlite.org/docs.html)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [Python sqlite3 Module](https://docs.python.org/3/library/sqlite3.html)

---

**Happy Learning! 🚀**
