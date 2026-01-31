"""
JSON & CSV Deep Dive - Exercises
================================
Practice problems for advanced JSON and CSV handling.
"""

print("=" * 60)
print("JSON & CSV DEEP DIVE - Exercises")
print("=" * 60)

import json
import csv
import tempfile
from datetime import datetime, date
from pathlib import Path

# =============================================================================
# EXERCISE 1: JSON Enum Encoder
# =============================================================================
print("\n--- Exercise 1: JSON Enum Encoder ---\n")
"""
Create a custom JSON encoder that handles Python enums.

from enum import Enum

class Status(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"

Your encoder should serialize Status.ACTIVE to "active".
"""

from enum import Enum

class Status(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        # Your code here
        pass  # TODO: Implement

# Test
# data = {'status': Status.ACTIVE, 'user': 'Alice'}
# print(json.dumps(data, cls=EnumEncoder))

# =============================================================================
# EXERCISE 2: CSV Normalizer
# =============================================================================
print("\n--- Exercise 2: CSV Normalizer ---\n")
"""
Write a function that reads a CSV file and normalizes it:
- Strip whitespace from all values
- Convert 'true'/'false' strings to booleans
- Convert numeric strings to int/float
- Skip empty rows
"""

def normalize_csv(input_file, output_file):
    """
    Read CSV, normalize data, write to new CSV.
    """
    # Your code here
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 3: JSON Schema Validator (Simple)
# =============================================================================
print("\n--- Exercise 3: Simple JSON Validator ---\n")
"""
Write a function that validates JSON data against a simple schema.
Schema defines required fields and their types.

Example schema:
{
    'name': str,
    'age': int,
    'email': str,
    'score': float
}
"""

def validate_json(data, schema):
    """
    Validate data against schema.
    Return (is_valid, list_of_errors).
    """
    # Your code here
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 4: Merge JSONL Files
# =============================================================================
print("\n--- Exercise 4: Merge JSONL Files ---\n")
"""
Write a function that merges multiple JSONL files.
Handle duplicate IDs (keep last occurrence).

Assume each record has an 'id' field.
"""

def merge_jsonl_files(input_files, output_file, id_field='id'):
    """
    Merge multiple JSONL files, removing duplicates by id_field.
    Keep the last occurrence of each ID.
    """
    # Your code here
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 5: CSV Pivot Table
# =============================================================================
print("\n--- Exercise 5: CSV Pivot Table ---\n")
"""
Write a function that creates a pivot table from CSV data.

Input: CSV with columns [date, category, amount]
Output: CSV with dates as rows, categories as columns, sum of amounts as values
"""

def pivot_csv(input_file, output_file, row_field, col_field, value_field):
    """
    Create pivot table from CSV.
    """
    # Your code here
    pass  # TODO: Implement

# =============================================================================
# EXERCISE 6: Streaming JSON Processor
# =============================================================================
print("\n--- Exercise 6: Streaming JSON Processor ---\n")
"""
Write a function that processes a large JSON Lines file.
Filter records based on a condition and write matching records to output.
Process in streaming fashion (don't load all into memory).
"""

def filter_jsonl(input_file, output_file, condition_func):
    """
    Filter JSONL records by condition function.
    condition_func receives a record and returns True/False.
    """
    # Your code here
    pass  # TODO: Implement

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# =============================================================================
# SOLUTION 1: JSON Enum Encoder
# =============================================================================
print("\n--- Solution 1: JSON Enum Encoder ---\n")

class EnumEncoderSolution(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        return super().default(obj)

data = {'status': Status.ACTIVE, 'user': 'Alice'}
print(json.dumps(data, cls=EnumEncoderSolution))

# =============================================================================
# SOLUTION 2: CSV Normalizer
# =============================================================================
print("\n--- Solution 2: CSV Normalizer ---\n")

def normalize_value(value):
    """Normalize a single value."""
    value = value.strip()

    # Boolean
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False

    # Integer
    try:
        return int(value)
    except ValueError:
        pass

    # Float
    try:
        return float(value)
    except ValueError:
        pass

    return value

def normalize_csv_solution(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)

        rows = []
        for row in reader:
            # Skip empty rows
            if not any(cell.strip() for cell in row):
                continue
            # Normalize each cell
            normalized = [normalize_value(cell) for cell in row]
            rows.append(normalized)

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

with tempfile.TemporaryDirectory() as tmpdir:
    input_csv = Path(tmpdir) / 'input.csv'
    output_csv = Path(tmpdir) / 'output.csv'

    with open(input_csv, 'w', newline='', encoding='utf-8') as f:
        f.write("name,active,score\n")
        f.write("  Alice  , true , 95.5\n")
        f.write("Bob,false, 87\n")
        f.write("\n")  # Empty row
        f.write("Carol,TRUE,92\n")

    normalize_csv_solution(input_csv, output_csv)
    print("Normalized CSV:")
    print(output_csv.read_text())

# =============================================================================
# SOLUTION 3: JSON Validator
# =============================================================================
print("\n--- Solution 3: JSON Validator ---\n")

def validate_json_solution(data, schema):
    errors = []

    for field, expected_type in schema.items():
        if field not in data:
            errors.append(f"Missing required field: {field}")
            continue

        value = data[field]
        if not isinstance(value, expected_type):
            errors.append(f"Field '{field}': expected {expected_type.__name__}, got {type(value).__name__}")

    return (len(errors) == 0, errors)

schema = {'name': str, 'age': int, 'score': float}

valid_data = {'name': 'Alice', 'age': 30, 'score': 95.5}
invalid_data = {'name': 'Bob', 'age': '25', 'score': 87.0}

print(f"Valid data: {validate_json_solution(valid_data, schema)}")
print(f"Invalid data: {validate_json_solution(invalid_data, schema)}")

# =============================================================================
# SOLUTION 4: Merge JSONL
# =============================================================================
print("\n--- Solution 4: Merge JSONL ---\n")

def merge_jsonl_files_solution(input_files, output_file, id_field='id'):
    seen = {}

    # First pass: collect all records (last wins)
    for input_file in input_files:
        with open(input_file) as f:
            for line in f:
                if line.strip():
                    record = json.loads(line)
                    record_id = record.get(id_field)
                    if record_id is not None:
                        seen[record_id] = record

    # Write merged
    with open(output_file, 'w') as f:
        for record in seen.values():
            f.write(json.dumps(record) + '\n')

    return len(seen)

with tempfile.TemporaryDirectory() as tmpdir:
    file1 = Path(tmpdir) / '1.jsonl'
    file2 = Path(tmpdir) / '2.jsonl'
    output = Path(tmpdir) / 'merged.jsonl'

    file1.write_text('{"id": 1, "name": "Alice"}\n{"id": 2, "name": "Bob"}\n')
    file2.write_text('{"id": 2, "name": "Bob Updated"}\n{"id": 3, "name": "Carol"}\n')

    count = merge_jsonl_files_solution([file1, file2], output)
    print(f"Merged {count} unique records:")
    print(output.read_text())

# =============================================================================
# SOLUTION 5: CSV Pivot
# =============================================================================
print("\n--- Solution 5: CSV Pivot ---\n")

def pivot_csv_solution(input_file, output_file, row_field, col_field, value_field):
    # Read data
    with open(input_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Build pivot
    pivot = {}
    columns = set()

    for row in data:
        row_key = row[row_field]
        col_key = row[col_field]
        value = float(row[value_field])

        columns.add(col_key)

        if row_key not in pivot:
            pivot[row_key] = {}

        pivot[row_key][col_key] = pivot[row_key].get(col_key, 0) + value

    # Write output
    sorted_cols = sorted(columns)
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([row_field] + sorted_cols)

        for row_key in sorted(pivot.keys()):
            row = [row_key] + [pivot[row_key].get(col, 0) for col in sorted_cols]
            writer.writerow(row)

with tempfile.TemporaryDirectory() as tmpdir:
    input_csv = Path(tmpdir) / 'input.csv'
    output_csv = Path(tmpdir) / 'pivot.csv'

    with open(input_csv, 'w', newline='', encoding='utf-8') as f:
        f.write("date,category,amount\n")
        f.write("2024-01,A,100\n")
        f.write("2024-01,B,200\n")
        f.write("2024-02,A,150\n")
        f.write("2024-02,B,250\n")
        f.write("2024-01,A,50\n")  # Duplicate date/category

    pivot_csv_solution(input_csv, output_csv, 'date', 'category', 'amount')
    print("Pivot table:")
    print(output_csv.read_text())

# =============================================================================
# SOLUTION 6: Streaming Filter
# =============================================================================
print("\n--- Solution 6: Streaming Filter ---\n")

def filter_jsonl_solution(input_file, output_file, condition_func):
    matched = 0
    total = 0

    with open(input_file) as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if not line.strip():
                continue

            total += 1
            record = json.loads(line)

            if condition_func(record):
                outfile.write(json.dumps(record) + '\n')
                matched += 1

    return matched, total

with tempfile.TemporaryDirectory() as tmpdir:
    input_file = Path(tmpdir) / 'input.jsonl'
    output_file = Path(tmpdir) / 'filtered.jsonl'

    with open(input_file, 'w') as f:
        for i in range(100):
            json.dump({'id': i, 'score': i * 10}, f)
            f.write('\n')

    # Filter for score >= 500
    matched, total = filter_jsonl_solution(
        input_file,
        output_file,
        lambda r: r['score'] >= 500
    )

    print(f"Filtered {matched}/{total} records (score >= 500)")
    print("First 3 results:")
    lines = output_file.read_text().strip().split('\n')
    for line in lines[:3]:
        print(f"  {line}")

print("\n" + "=" * 60)
print("Exercises complete!")
print("=" * 60)
