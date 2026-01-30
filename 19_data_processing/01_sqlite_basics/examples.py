"""
SQLite Basics - Examples
=======================
Introduction to SQLite database operations with Python.
"""

import sqlite3
import os

# Clean up any existing database
DB_NAME = "example_library.db"
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("=" * 60)
print("SQLITE BASICS - Examples")
print("=" * 60)

# =============================================================================
# SECTION 1: CONNECTING AND CREATING TABLES
# =============================================================================
print("\n--- 1. Connecting to Database and Creating Tables ---\n")

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()
print(f"Connected to database: {DB_NAME}")

# Create a books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        genre TEXT,
        rating REAL DEFAULT 0.0
    )
''')
print("Created 'books' table")

# Create an authors table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        country TEXT,
        birth_year INTEGER
    )
''')
print("Created 'authors' table")

conn.commit()

# =============================================================================
# SECTION 2: INSERTING DATA
# =============================================================================
print("\n--- 2. Inserting Data ---\n")

# Insert single row
cursor.execute('''
    INSERT INTO books (title, author, year, genre, rating)
    VALUES (?, ?, ?, ?, ?)
''', ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 4.8))
print("Inserted: The Hobbit")

# Insert multiple rows using executemany
books = [
    ("1984", "George Orwell", 1949, "Dystopian", 4.7),
    ("Pride and Prejudice", "Jane Austen", 1813, "Romance", 4.6),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 4.4),
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Classic", 4.9),
    ("Dune", "Frank Herbert", 1965, "Sci-Fi", 4.8),
]

cursor.executemany('''
    INSERT INTO books (title, author, year, genre, rating)
    VALUES (?, ?, ?, ?, ?)
''', books)
print(f"Inserted {len(books)} more books")

# Insert authors
authors = [
    ("J.R.R. Tolkien", "UK", 1892),
    ("George Orwell", "UK", 1903),
    ("Jane Austen", "UK", 1775),
    ("F. Scott Fitzgerald", "USA", 1896),
    ("Harper Lee", "USA", 1926),
    ("Frank Herbert", "USA", 1920),
]

cursor.executemany('''
    INSERT INTO authors (name, country, birth_year)
    VALUES (?, ?, ?)
''', authors)
print(f"Inserted {len(authors)} authors")

conn.commit()

# =============================================================================
# SECTION 3: QUERYING DATA
# =============================================================================
print("\n--- 3. Querying Data ---\n")

# Fetch all books
print("All books:")
cursor.execute('SELECT * FROM books')
all_books = cursor.fetchall()
for book in all_books:
    print(f"  {book[0]}. {book[1]} by {book[2]} ({book[3]}) - {book[4]}")

# Fetch with condition
print("\nBooks published after 1950:")
cursor.execute('SELECT title, year FROM books WHERE year > ?', (1950,))
recent_books = cursor.fetchall()
for title, year in recent_books:
    print(f"  - {title} ({year})")

# Fetch one row
print("\nFirst book in database:")
cursor.execute('SELECT * FROM books WHERE id = ?', (1,))
first_book = cursor.fetchone()
if first_book:
    print(f"  Title: {first_book[1]}")
    print(f"  Author: {first_book[2]}")
    print(f"  Rating: {first_book[5]}/5.0")

# =============================================================================
# SECTION 4: UPDATING DATA
# =============================================================================
print("\n--- 4. Updating Data ---\n")

# Update a book's rating
cursor.execute('''
    UPDATE books SET rating = ? WHERE title = ?
''', (5.0, "The Great Gatsby"))
print("Updated 'The Great Gatsby' rating to 5.0")

# Verify update
cursor.execute('SELECT title, rating FROM books WHERE title = ?', ("The Great Gatsby",))
result = cursor.fetchone()
print(f"New rating: {result[1]}")

conn.commit()

# =============================================================================
# SECTION 5: DELETING DATA
# =============================================================================
print("\n--- 5. Deleting Data ---\n")

# Count before delete
cursor.execute('SELECT COUNT(*) FROM books')
count_before = cursor.fetchone()[0]
print(f"Books before delete: {count_before}")

# Delete a book
cursor.execute('DELETE FROM books WHERE title = ?', ("The Hobbit",))
print("Deleted 'The Hobbit'")

# Count after delete
cursor.execute('SELECT COUNT(*) FROM books')
count_after = cursor.fetchone()[0]
print(f"Books after delete: {count_after}")

conn.commit()

# =============================================================================
# SECTION 6: USING ROW FACTORY (DICTIONARY ACCESS)
# =============================================================================
print("\n--- 6. Using Row Factory ---\n")

# Enable dictionary-style access
conn.row_factory = sqlite3.Row

cursor = conn.cursor()
cursor.execute('SELECT * FROM books WHERE genre = ?', ("Classic",))

print("Classic books (using column names):")
for row in cursor.fetchall():
    print(f"  - {row['title']} ({row['year']}) - Rating: {row['rating']}")

# Reset row factory
conn.row_factory = None
cursor = conn.cursor()

# =============================================================================
# SECTION 7: AGGREGATION QUERIES
# =============================================================================
print("\n--- 7. Aggregation Queries ---\n")

# Count books
cursor.execute('SELECT COUNT(*) FROM books')
total_books = cursor.fetchone()[0]
print(f"Total books: {total_books}")

# Average rating
cursor.execute('SELECT AVG(rating) FROM books')
avg_rating = cursor.fetchone()[0]
print(f"Average rating: {avg_rating:.2f}")

# Books by genre
cursor.execute('''
    SELECT genre, COUNT(*) as count 
    FROM books 
    GROUP BY genre 
    ORDER BY count DESC
''')
print("\nBooks by genre:")
for genre, count in cursor.fetchall():
    print(f"  - {genre}: {count}")

# =============================================================================
# SECTION 8: CONTEXT MANAGER (WITH STATEMENT)
# =============================================================================
print("\n--- 8. Using Context Manager ---\n")

# The 'with' statement automatically commits or rolls back
with sqlite3.connect(DB_NAME) as conn2:
    cursor2 = conn2.cursor()
    cursor2.execute('''
        INSERT INTO books (title, author, year, genre, rating)
        VALUES (?, ?, ?, ?, ?)
    ''', ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 4.8))
    print("Inserted 'The Hobbit' using context manager")
    # Automatically commits when exiting the 'with' block

# =============================================================================
# CLEANUP
# =============================================================================
conn.close()
print("\n" + "=" * 60)
print("Examples complete!")
print(f"Database saved to: {DB_NAME}")
print("=" * 60)
