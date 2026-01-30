"""
SQL Fundamentals - Exercises
============================
Practice SQL queries with these exercises.
"""

import sqlite3
import os

DB_NAME = "sql_exercises.db"

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("=" * 70)
print("SQL FUNDAMENTALS - Exercises")
print("=" * 70)

# Setup database
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Create tables and insert data
cursor.executescript('''
    CREATE TABLE movies (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        genre TEXT,
        year INTEGER,
        rating REAL,
        box_office INTEGER
    );
    
    CREATE TABLE actors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        birth_year INTEGER,
        nationality TEXT
    );
    
    CREATE TABLE movie_cast (
        movie_id INTEGER,
        actor_id INTEGER,
        role TEXT,
        PRIMARY KEY (movie_id, actor_id)
    );
''')

# Insert movies
movies = [
    (1, 'The Shawshank Redemption', 'Drama', 1994, 9.3, 58300000),
    (2, 'The Godfather', 'Crime', 1972, 9.2, 246000000),
    (3, 'The Dark Knight', 'Action', 2008, 9.0, 1005000000),
    (4, 'Pulp Fiction', 'Crime', 1994, 8.9, 213000000),
    (5, 'Inception', 'Sci-Fi', 2010, 8.8, 836000000),
    (6, 'Forrest Gump', 'Drama', 1994, 8.8, 678000000),
    (7, 'The Matrix', 'Sci-Fi', 1999, 8.7, 463000000),
    (8, 'Goodfellas', 'Crime', 1990, 8.7, 47000000),
    (9, 'Interstellar', 'Sci-Fi', 2014, 8.6, 677000000),
    (10, 'Parasite', 'Thriller', 2019, 8.5, 258000000),
]
cursor.executemany('INSERT INTO movies VALUES (?,?,?,?,?,?)', movies)

# Insert actors
actors = [
    (1, 'Tim Robbins', 1958, 'American'),
    (2, 'Morgan Freeman', 1937, 'American'),
    (3, 'Marlon Brando', 1924, 'American'),
    (4, 'Al Pacino', 1940, 'American'),
    (5, 'Christian Bale', 1974, 'British'),
    (6, 'Heath Ledger', 1979, 'Australian'),
    (7, 'John Travolta', 1954, 'American'),
    (8, 'Samuel L. Jackson', 1948, 'American'),
    (9, 'Leonardo DiCaprio', 1974, 'American'),
    (10, 'Tom Hanks', 1956, 'American'),
]
cursor.executemany('INSERT INTO actors VALUES (?,?,?,?)', actors)

# Insert cast relationships
cast = [
    (1, 1, 'Andy Dufresne'),
    (1, 2, 'Ellis Boyd Redding'),
    (2, 3, 'Don Vito Corleone'),
    (2, 4, 'Michael Corleone'),
    (3, 5, 'Bruce Wayne'),
    (3, 6, 'The Joker'),
    (4, 7, 'Vincent Vega'),
    (4, 8, 'Jules Winnfield'),
    (5, 9, 'Cobb'),
    (6, 10, 'Forrest Gump'),
]
cursor.executemany('INSERT INTO movie_cast VALUES (?,?,?)', cast)

conn.commit()

# =============================================================================
# EXERCISE 1: Basic SELECT
# =============================================================================
print("\n--- Exercise 1: Select All Movies ---\n")
"""
Write a query to select the title, year, and rating of all movies.
Print each movie in the format: "Title (Year) - Rating/10"
"""
# Your code here:
# cursor.execute(...)
# for row in cursor.fetchall():
#     print(...)

# =============================================================================
# EXERCISE 2: WHERE Clause
# =============================================================================
print("\n--- Exercise 2: Sci-Fi Movies ---\n")
"""
Select all Sci-Fi movies released after 2000.
Print: title and year.
"""
# Your code here:

# =============================================================================
# EXERCISE 3: Sorting
# =============================================================================
print("\n--- Exercise 3: Top Rated Movies ---\n")
"""
Get the top 5 highest-rated movies.
Print: title and rating (descending order).
"""
# Your code here:

# =============================================================================
# EXERCISE 4: Aggregation
# =============================================================================
print("\n--- Exercise 4: Average Rating by Genre ---\n")
"""
Calculate the average rating for each genre.
Only include genres with 2+ movies.
Print: genre and average rating (sorted by avg rating descending).
"""
# Your code here:
# Hint: Use GROUP BY and HAVING

# =============================================================================
# EXERCISE 5: Pattern Matching
# =============================================================================
print("\n--- Exercise 5: Movies Starting with 'The' ---\n")
"""
Find all movies with titles starting with 'The'.
Print: title and year.
"""
# Your code here:

# =============================================================================
# EXERCISE 6: Box Office Analysis
# =============================================================================
print("\n--- Exercise 6: Highest Grossing Movies ---\n")
"""
Find movies with box office over $500 million.
Sort by box office (highest first) and show top 3.
Print: title and box office in millions (e.g., "1005M")
"""
# Your code here:

# =============================================================================
# EXERCISE 7: JOIN - Actors in Movies
# =============================================================================
print("\n--- Exercise 7: Movie Cast ---\n")
"""
List all actors and the movies they appeared in.
Use a JOIN between movies, actors, and movie_cast tables.
Print: actor name, movie title, and their role.
"""
# Your code here:
# Hint: You'll need to JOIN all three tables

# =============================================================================
# EXERCISE 8: Subquery
# =============================================================================
print("\n--- Exercise 8: Actors in High-Rated Movies ---\n")
"""
Find all actors who appeared in movies with rating >= 9.0.
Use a subquery to first find the high-rated movie IDs.
Print: actor names (without duplicates).
"""
# Your code here:

# =============================================================================
# EXERCISE 9: Complex Filter
# =============================================================================
print("\n--- Exercise 9: Drama or Crime from 1990s ---\n")
"""
Find all Drama or Crime movies released between 1990 and 1999.
Sort by rating (highest first).
Print: title, genre, year, and rating.
"""
# Your code here:

# =============================================================================
# EXERCISE 10: Total Box Office by Genre
# =============================================================================
print("\n--- Exercise 10: Genre Revenue ---\n")
"""
Calculate total box office revenue for each genre.
Print: genre and total revenue in billions (e.g., "1.005B").
Sort by total revenue (highest first).
"""
# Your code here:

conn.close()

print("\n" + "=" * 70)
print("Exercises complete! Check solutions at the bottom.")
print("=" * 70)

# =============================================================================
# SOLUTIONS
# =============================================================================
print("""
# SOLUTIONS
# =========

# Exercise 1: Basic SELECT
cursor.execute('SELECT title, year, rating FROM movies')
for title, year, rating in cursor.fetchall():
    print(f"  {title} ({year}) - {rating}/10")

# Exercise 2: WHERE Clause
cursor.execute("SELECT title, year FROM movies WHERE genre = 'Sci-Fi' AND year > 2000")
for title, year in cursor.fetchall():
    print(f"  {title} ({year})")

# Exercise 3: Sorting
cursor.execute('SELECT title, rating FROM movies ORDER BY rating DESC LIMIT 5')
for title, rating in cursor.fetchall():
    print(f"  {title}: {rating}")

# Exercise 4: Aggregation
cursor.execute('''
    SELECT genre, AVG(rating) as avg_rating, COUNT(*) as count
    FROM movies
    GROUP BY genre
    HAVING COUNT(*) >= 2
    ORDER BY avg_rating DESC
''')
for genre, avg, count in cursor.fetchall():
    print(f"  {genre}: {avg:.2f} ({count} movies)")

# Exercise 5: Pattern Matching
cursor.execute("SELECT title, year FROM movies WHERE title LIKE 'The%'")
for title, year in cursor.fetchall():
    print(f"  {title} ({year})")

# Exercise 6: Box Office
cursor.execute('''
    SELECT title, box_office 
    FROM movies 
    WHERE box_office > 500000000
    ORDER BY box_office DESC
    LIMIT 3
''')
for title, box in cursor.fetchall():
    print(f"  {title}: {box/1000000:.0f}M")

# Exercise 7: JOIN
cursor.execute('''
    SELECT a.name, m.title, mc.role
    FROM actors a
    JOIN movie_cast mc ON a.id = mc.actor_id
    JOIN movies m ON mc.movie_id = m.id
''')
for actor, movie, role in cursor.fetchall():
    print(f"  {actor} played {role} in {movie}")

# Exercise 8: Subquery
cursor.execute('''
    SELECT DISTINCT a.name
    FROM actors a
    JOIN movie_cast mc ON a.id = mc.actor_id
    WHERE mc.movie_id IN (
        SELECT id FROM movies WHERE rating >= 9.0
    )
''')
for row in cursor.fetchall():
    print(f"  {row[0]}")

# Exercise 9: Complex Filter
cursor.execute('''
    SELECT title, genre, year, rating
    FROM movies
    WHERE (genre = 'Drama' OR genre = 'Crime')
      AND year BETWEEN 1990 AND 1999
    ORDER BY rating DESC
''')
for title, genre, year, rating in cursor.fetchall():
    print(f"  {title} ({genre}, {year}): {rating}")

# Exercise 10: Total Box Office
cursor.execute('''
    SELECT genre, SUM(box_office) as total
    FROM movies
    GROUP BY genre
    ORDER BY total DESC
''')
for genre, total in cursor.fetchall():
    print(f"  {genre}: {total/1000000000:.3f}B")
""")

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)
