"""
Advanced Exercise 7: Data Processing
====================================
Schema validation, an ETL pipeline into SQLite, lazy stream
processing with generators, and batch processing with chunking.
"""

print("=" * 50)
print("EXERCISE 7: Data Processing")
print("=" * 50)


# =============================================================================
# EXERCISE 7.1: Data Validation
# =============================================================================
print("\n--- Exercise 7.1: Data Validation ---")
"""
Validate incoming records against a schema before anything
downstream touches them.

Write validate_record(record, schema) that returns
(clean_record, errors):
- Missing required fields are reported
- Wrong types are reported (use isinstance)
- Values outside min/max are reported
- Unknown keys are reported and dropped from the clean record
"""


# Your code below:
SCHEMA = {
    "name": {"type": str, "required": True},
    "age": {"type": int, "required": True, "min": 0, "max": 130},
    "email": {"type": str, "required": False},
}


def validate_record(record, schema):
    """Return (clean_record, list of error strings)."""
    pass


# Test (uncomment after implementing)
# clean, errors = validate_record({"name": "Ada", "age": 36}, SCHEMA)
# print(clean, errors)


# =============================================================================
# EXERCISE 7.2: ETL Pipeline
# =============================================================================
print("\n--- Exercise 7.2: ETL Pipeline ---")
"""
Extract -> Transform -> Load, with a report at the end:

- extract(): return the raw rows (they look like a sloppy CSV)
- transform(rows): strip names, lowercase emails, parse amounts
  like " 1,250.50 " into floats, DROP rows with an empty name or
  an unparseable amount, and add tier = "high" when amount >= 1000
  else "standard"
- load(rows): create an in-memory SQLite table sales and insert
- report(conn): totals by tier with a GROUP BY query
"""

import sqlite3


# Your code below:
RAW_ROWS = [
    ["  Alice  ", " ALICE@Example.COM ", " 1,250.50 "],
    ["bob", "Bob@Example.com", "340.00"],
    ["  Cara", "cara@example.com", " 2,750.25 "],
    ["", "nobody@example.com", "12.00"],
    ["Dan", "dan@example.com", "not-a-number"],
]


def extract():
    """Return the raw rows (pretend we just read a CSV)."""
    pass


def transform(rows):
    """Clean and enrich rows; drop rows that fail validation."""
    pass


def load(rows):
    """Create an in-memory sales table and insert the rows."""
    pass


def report(conn):
    """Print the aggregate summary."""
    pass


# =============================================================================
# EXERCISE 7.3: Stream Processing
# =============================================================================
print("\n--- Exercise 7.3: Stream Processing ---")
"""
Process records one at a time without building a big list:

- parse_lines(lines): generator yielding {"level", "message"} dicts
- errors_only(records): generator passing through only ERROR lines
- Consume the chained generators with a plain for loop, keeping
  only a running count - nothing is ever materialized
"""


# Your code below:
LOG_LINES = [
    "INFO app started",
    "INFO user logged in",
    "ERROR db timeout",
    "INFO cache warmed",
    "ERROR disk full",
    "WARNING slow query",
] * 3


def parse_lines(lines):
    """Yield one {"level", "message"} dict per line."""
    pass


def errors_only(records):
    """Yield only records whose level is ERROR."""
    pass


# =============================================================================
# EXERCISE 7.4: Batch Processing
# =============================================================================
print("\n--- Exercise 7.4: Batch Processing ---")
"""
Work in fixed-size batches:

- chunked(items, size): generator yielding successive slices
- The solution processes 1000 transactions in batches of 100,
  sums each batch, then combines the batch totals into a grand
  summary (use math.isclose when comparing float totals)
"""

import math


# Your code below:
TRANSACTIONS = [((i * 37) % 200) + 0.99 for i in range(1000)]


def chunked(items, size):
    """Yield successive fixed-size batches."""
    pass


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 7.1
print("\n--- Solution 7.1 ---")


def validate_record(record, schema):
    """Return (clean_record, list of error strings)."""
    clean = {}
    errors = []
    for key, rules in schema.items():
        if key not in record:
            if rules.get("required"):
                errors.append(f"missing required field '{key}'")
            continue
        value = record[key]
        if not isinstance(value, rules["type"]):
            expected = rules["type"].__name__
            errors.append(f"'{key}' must be {expected}, got {type(value).__name__}")
            continue
        if "min" in rules and value < rules["min"]:
            errors.append(f"'{key}' below minimum {rules['min']}")
            continue
        if "max" in rules and value > rules["max"]:
            errors.append(f"'{key}' above maximum {rules['max']}")
            continue
        clean[key] = value
    for key in record:
        if key not in schema:
            errors.append(f"unknown field '{key}'")
    return clean, errors


cases = [
    {"name": "Ada", "age": 36, "email": "ada@example.com"},
    {"age": 999, "admin": True},
    {"name": 7, "age": 30},
]
for record in cases:
    clean, errors = validate_record(record, SCHEMA)
    print(f"Record: {record}")
    print(f"  clean : {clean}")
    print(f"  errors: {errors}")

good_clean, good_errors = validate_record(cases[0], SCHEMA)
print("PASS" if good_clean == cases[0] and good_errors == [] else "FAIL")

# SOLUTION 7.2
print("\n--- Solution 7.2 ---")


def extract():
    """Return the raw rows (pretend we just read a CSV)."""
    return [list(row) for row in RAW_ROWS]


def transform(rows):
    """Clean and enrich rows; drop rows that fail validation."""
    clean_rows = []
    for name, email, amount_text in rows:
        name = name.strip()
        email = email.strip().lower()
        try:
            amount = float(amount_text.strip().replace(",", ""))
        except ValueError:
            continue
        if not name or "@" not in email:
            continue
        tier = "high" if amount >= 1000 else "standard"
        clean_rows.append((name, email, amount, tier))
    return clean_rows


def load(rows):
    """Create an in-memory sales table and insert the rows."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE sales (name TEXT, email TEXT, amount REAL, tier TEXT)")
    conn.executemany("INSERT INTO sales VALUES (?, ?, ?, ?)", rows)
    conn.commit()
    return conn


def report(conn):
    """Print the aggregate summary."""
    total, count = conn.execute("SELECT SUM(amount), COUNT(*) FROM sales").fetchone()
    print(f"Loaded {count} valid rows, total {total:.2f}")
    for tier, tier_total, tier_count in conn.execute(
        "SELECT tier, SUM(amount), COUNT(*) FROM sales GROUP BY tier ORDER BY tier"
    ):
        print(f"  {tier:9s} {tier_count} rows, total {tier_total:.2f}")


clean_rows = transform(extract())
print(f"Transformed {len(RAW_ROWS)} raw rows into {len(clean_rows)} clean rows")
for row in clean_rows:
    print(f"  {row}")

conn = load(clean_rows)
report(conn)
kept = conn.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
print("PASS" if kept == 3 else "FAIL")
conn.close()

# SOLUTION 7.3
print("\n--- Solution 7.3 ---")


def parse_lines(lines):
    """Yield one {"level", "message"} dict per line."""
    for line in lines:
        level, _, message = line.partition(" ")
        yield {"level": level, "message": message}


def errors_only(records):
    """Yield only records whose level is ERROR."""
    for record in records:
        if record["level"] == "ERROR":
            yield record


stream = errors_only(parse_lines(LOG_LINES))
print(f"Pipeline built before consuming: {type(stream).__name__} (nothing ran yet)")
error_count = 0
for record in stream:
    error_count += 1
    print(f"  {record['level']}: {record['message']}")
print(f"Streamed {error_count} errors out of {len(LOG_LINES)} lines without a list")
print("PASS" if error_count == 6 else "FAIL")

# SOLUTION 7.4
print("\n--- Solution 7.4 ---")


def chunked(items, size):
    """Yield successive fixed-size batches."""
    for start in range(0, len(items), size):
        yield items[start : start + size]


grand_total = 0.0
grand_count = 0
batches = 0
for batch_number, batch in enumerate(chunked(TRANSACTIONS, 100), start=1):
    batches += 1
    batch_total = sum(batch)
    grand_total += batch_total
    grand_count += len(batch)
    if batch_number <= 3:
        print(f"  batch {batch_number}: {len(batch)} txns, total {batch_total:.2f}")

print(f"Processed {grand_count} transactions in {batches} batches")
print(f"Grand total: {grand_total:.2f}")
print("PASS" if math.isclose(grand_total, sum(TRANSACTIONS)) and grand_count == 1000 else "FAIL")

print("\n" + "=" * 50)
print("Great job! Move on to 08_security.py")
print("=" * 50)
