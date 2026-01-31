"""
Data Cleaning - Examples
========================
Learn techniques for handling messy data in Python and SQLite.
"""

import sqlite3
import os
import re
from datetime import datetime

DB_NAME = "cleaning_examples.db"

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("=" * 70)
print("DATA CLEANING - Examples")
print("=" * 70)

# Create database with intentionally messy data
conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row  # Enable dictionary access
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE raw_customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT,
        birth_date TEXT,
        age TEXT,  -- String to demonstrate type issues
        city TEXT,
        country TEXT,
        registration_date TEXT
    )
''')

# Insert messy data
messy_data = [
    (1, '  John Doe  ', 'john@email.com', '(555) 123-4567', '1990-05-15', '33', 'New York', 'USA', '2023-01-15'),
    (2, 'Jane Smith', 'JANE@EMAIL.COM', '555.987.6543', '1985/08/22', '38', 'Los Angeles', 'usa', '2023-02-20'),
    (3, 'Bob Johnson', 'bob@email.com', '555-456-7890', '15-03-1978', 'fourty-five', 'Chicago', 'USA', '2023-03-10'),
    (4, '  Alice Brown  ', 'alice@email.com', '(555) 111-2222', None, None, 'Houston', 'US', '2023-01-15'),
    (5, 'John Doe', 'john@email.com', '5551234567', '1990-05-15', '33', 'New York', 'USA', '2023-04-05'),  # Duplicate
    (6, 'Carol White', 'invalid-email', '555-abc-defg', '2020-13-45', '150', 'Miami', 'United States', '2023-05-12'),
    (7, None, 'dave@email.com', '555.333.4444', '1992-11-30', '31', 'Seattle', None, '2023-06-18'),
    (8, 'Eve Davis', None, '(555) 777-8888', '1988-04-10', '35', 'Boston', 'usa', '2023-07-22'),
]

cursor.executemany('''
    INSERT INTO raw_customers VALUES (?,?,?,?,?,?,?,?,?)
''', messy_data)
conn.commit()

print("\n--- Original Messy Data ---\n")
cursor.execute('SELECT * FROM raw_customers')
for row in cursor.fetchall():
    print(f"ID {row['id']}: {dict(row)}")

# =============================================================================
# SECTION 1: PROFILE THE DATA
# =============================================================================
print("\n--- 1. Data Profiling ---\n")

# Count total rows
cursor.execute('SELECT COUNT(*) FROM raw_customers')
total = cursor.fetchone()[0]
print(f"Total rows: {total}")

# Check for NULL values in each column
cursor.execute('''
    SELECT 
        COUNT(*) - COUNT(name) as missing_name,
        COUNT(*) - COUNT(email) as missing_email,
        COUNT(*) - COUNT(phone) as missing_phone,
        COUNT(*) - COUNT(birth_date) as missing_birth_date,
        COUNT(*) - COUNT(age) as missing_age,
        COUNT(*) - COUNT(country) as missing_country
    FROM raw_customers
''')
nulls = cursor.fetchone()
print("\nMissing values per column:")
for col, count in zip(nulls.keys(), nulls):
    print(f"  {col}: {count}")

# Find duplicate emails
cursor.execute('''
    SELECT email, COUNT(*) as count
    FROM raw_customers
    WHERE email IS NOT NULL
    GROUP BY email
    HAVING COUNT(*) > 1
''')
dups = cursor.fetchall()
print(f"\nDuplicate emails found: {len(dups)}")
for row in dups:
    print(f"  {row['email']}: {row['count']} occurrences")

# =============================================================================
# SECTION 2: CLEANING FUNCTIONS
# =============================================================================
print("\n--- 2. Creating Cleaning Functions ---\n")

def clean_name(name):
    """Trim whitespace and capitalize properly."""
    if name is None:
        return None
    return name.strip().title()

def clean_email(email):
    """Normalize email to lowercase."""
    if email is None:
        return None
    return email.strip().lower()

def validate_email(email):
    """Basic email validation."""
    if email is None:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def clean_phone(phone):
    """Standardize phone format to digits only."""
    if phone is None:
        return None
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return None  # Invalid phone

def parse_date(date_str):
    """Try multiple date formats and return ISO format."""
    if date_str is None:
        return None
    formats = ['%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y', '%m/%d/%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    return None  # Invalid date

def clean_age(age_str):
    """Convert age to integer with validation."""
    if age_str is None:
        return None
    try:
        age = int(age_str)
        if 0 <= age <= 120:
            return age
    except ValueError:
        pass
    return None  # Invalid age

def clean_country(country):
    """Standardize country names."""
    if country is None:
        return None
    country = country.strip().upper()
    mappings = {
        'USA': 'United States',
        'US': 'United States',
        'UNITED STATES': 'United States',
        'UK': 'United Kingdom',
        'U.K.': 'United Kingdom',
    }
    return mappings.get(country, country.title())

print("Cleaning functions defined:")
print("  - clean_name(): Trim and title case")
print("  - clean_email(): Lowercase and validate")
print("  - clean_phone(): Standardize format")
print("  - parse_date(): Parse various formats")
print("  - clean_age(): Validate and convert")
print("  - clean_country(): Standardize country names")

# =============================================================================
# SECTION 3: APPLY CLEANING
# =============================================================================
print("\n--- 3. Applying Data Cleaning ---\n")

# Create clean table
cursor.execute('''
    CREATE TABLE clean_customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        email_valid BOOLEAN,
        phone TEXT,
        birth_date TEXT,
        age INTEGER,
        city TEXT,
        country TEXT,
        registration_date TEXT,
        data_quality_score REAL
    )
''')

# Fetch and clean each row
cursor.execute('SELECT * FROM raw_customers')
changes_made = []

for row in cursor.fetchall():
    row_id = row['id']
    
    # Apply cleaning functions
    name = clean_name(row['name'])
    email = clean_email(row['email'])
    email_valid = validate_email(email)
    phone = clean_phone(row['phone'])
    birth_date = parse_date(row['birth_date'])
    age = clean_age(row['age'])
    city = clean_name(row['city'])
    country = clean_country(row['country'])
    reg_date = parse_date(row['registration_date'])
    
    # Calculate data quality score (percentage of valid fields)
    fields = [name, email, phone, birth_date, age, country]
    valid_count = sum(1 for f in fields if f is not None)
    quality_score = valid_count / len(fields)
    
    # Track changes
    if name != row['name']:
        changes_made.append(f"ID {row_id}: Trimmed name '{row['name']}' -> '{name}'")
    if email != row['email']:
        changes_made.append(f"ID {row_id}: Normalized email '{row['email']}' -> '{email}'")
    if phone != row['phone']:
        changes_made.append(f"ID {row_id}: Reformatted phone '{row['phone']}' -> '{phone}'")
    if birth_date != row['birth_date'] and birth_date is not None:
        changes_made.append(f"ID {row_id}: Parsed date '{row['birth_date']}' -> '{birth_date}'")
    
    cursor.execute('''
        INSERT INTO clean_customers 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (row_id, name, email, email_valid, phone, birth_date, age, city, country, reg_date, quality_score))

conn.commit()

print("Sample of changes made:")
for change in changes_made[:10]:
    print(f"  {change}")
if len(changes_made) > 10:
    print(f"  ... and {len(changes_made) - 10} more changes")

# =============================================================================
# SECTION 4: REMOVE DUPLICATES
# =============================================================================
print("\n--- 4. Removing Duplicates ---\n")

# Before deduplication
cursor.execute('SELECT COUNT(*) FROM clean_customers')
count_before = cursor.fetchone()[0]
print(f"Rows before deduplication: {count_before}")

# Find duplicates based on email
cursor.execute('''
    SELECT email, COUNT(*) as count, GROUP_CONCAT(id) as ids
    FROM clean_customers
    WHERE email IS NOT NULL
    GROUP BY email
    HAVING COUNT(*) > 1
''')
duplicates = cursor.fetchall()

print("\nDuplicate records found:")
ids_to_delete = []
for row in duplicates:
    ids = [int(x) for x in row['ids'].split(',')]
    keep = min(ids)  # Keep the lowest ID
    delete = ids[1:]  # Delete the rest
    ids_to_delete.extend(delete)
    print(f"  Email '{row['email']}': IDs {ids}, keeping ID {keep}, deleting {delete}")

# Delete duplicates
if ids_to_delete:
    placeholders = ','.join('?' * len(ids_to_delete))
    cursor.execute(f'DELETE FROM clean_customers WHERE id IN ({placeholders})', ids_to_delete)
    conn.commit()

cursor.execute('SELECT COUNT(*) FROM clean_customers')
count_after = cursor.fetchone()[0]
print(f"\nRows after deduplication: {count_after}")
print(f"Removed {count_before - count_after} duplicate(s)")

# =============================================================================
# SECTION 5: HANDLE MISSING VALUES
# =============================================================================
print("\n--- 5. Handling Missing Values ---\n")

# Strategy 1: Fill country with 'Unknown'
cursor.execute('''
    UPDATE clean_customers 
    SET country = 'Unknown' 
    WHERE country IS NULL
''')
print(f"Filled {cursor.rowcount} missing country values with 'Unknown'")

# Strategy 2: Calculate age from birth_date where age is missing
cursor.execute('''
    UPDATE clean_customers 
    SET age = CAST((julianday('now') - julianday(birth_date)) / 365.25 AS INTEGER)
    WHERE age IS NULL AND birth_date IS NOT NULL
''')
print(f"Calculated age for {cursor.rowcount} records from birth date")

# Strategy 3: Fill missing names with "Anonymous"
cursor.execute('''
    UPDATE clean_customers 
    SET name = 'Anonymous' 
    WHERE name IS NULL
''')
print(f"Filled {cursor.rowcount} missing name(s) with 'Anonymous'")

conn.commit()

# =============================================================================
# SECTION 6: OUTLIER DETECTION
# =============================================================================
print("\n--- 6. Outlier Detection ---\n")

# Find outliers in age using standard deviation
cursor.execute('''
    SELECT AVG(age), AVG(age*age) 
    FROM clean_customers 
    WHERE age IS NOT NULL
''')
avg, avg_sq = cursor.fetchone()
std_dev = (avg_sq - avg**2) ** 0.5
lower = avg - 2 * std_dev
upper = avg + 2 * std_dev

print(f"Age statistics:")
print(f"  Mean: {avg:.1f}")
print(f"  Std Dev: {std_dev:.1f}")
print(f"  Normal range: {lower:.1f} - {upper:.1f}")

cursor.execute('''
    SELECT id, name, age 
    FROM clean_customers 
    WHERE age < ? OR age > ?
''', (lower, upper))
outliers = cursor.fetchall()

print(f"\nPotential outliers (outside 2 std dev): {len(outliers)}")
for row in outliers:
    print(f"  ID {row['id']}: {row['name']} - Age {row['age']}")

# =============================================================================
# SECTION 7: FINAL CLEAN DATA
# =============================================================================
print("\n--- 7. Final Clean Data ---\n")

cursor.execute('SELECT * FROM clean_customers ORDER BY id')
print(f"{'ID':<4} {'Name':<18} {'Email':<20} {'Phone':<16} {'Age':<4} {'Country':<15} {'Quality':<8}")
print("-" * 90)
for row in cursor.fetchall():
    email = (row['email'][:17] + '...') if row['email'] and len(row['email']) > 20 else (row['email'] or 'N/A')
    print(f"{row['id']:<4} {row['name'] or 'N/A':<18} {email:<20} {row['phone'] or 'N/A':<16} {row['age'] or 'N/A':<4} {row['country'] or 'N/A':<15} {row['data_quality_score']:.0%}")

# Summary statistics
cursor.execute('''
    SELECT 
        COUNT(*) as total,
        AVG(data_quality_score) as avg_quality,
        SUM(CASE WHEN email_valid THEN 1 ELSE 0 END) as valid_emails
    FROM clean_customers
''')
summary = cursor.fetchone()

print("\n" + "=" * 70)
print("CLEANING SUMMARY")
print("=" * 70)
print(f"Total records: {summary['total']}")
print(f"Duplicates removed: {count_before - count_after}")
print(f"Valid emails: {summary['valid_emails']}/{summary['total']}")
print(f"Average data quality score: {summary['avg_quality']:.1%}")

conn.close()

# Clean up
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

print("\n" + "=" * 70)
print("Examples complete!")
print("=" * 70)
