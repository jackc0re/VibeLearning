"""
JSON & CSV Deep Dive - Examples
===============================
Advanced data serialization techniques.
"""

print("=" * 60)
print("JSON & CSV DEEP DIVE - Examples")
print("=" * 60)

import json
import csv
import tempfile
from datetime import datetime, date
from pathlib import Path

# =============================================================================
# CUSTOM JSON ENCODER
# =============================================================================
print("\n--- Custom JSON Encoder ---\n")

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        # Handle datetime
        if isinstance(obj, datetime):
            return {
                '__type__': 'datetime',
                'value': obj.isoformat()
            }

        # Handle date
        if isinstance(obj, date):
            return {
                '__type__': 'date',
                'value': obj.isoformat()
            }

        # Handle Path
        if isinstance(obj, Path):
            return {
                '__type__': 'Path',
                'value': str(obj)
            }

        # Handle set
        if isinstance(obj, set):
            return {
                '__type__': 'set',
                'value': list(obj)
            }

        # Handle bytes
        if isinstance(obj, bytes):
            return {
                '__type__': 'bytes',
                'value': obj.decode('utf-8', errors='replace')
            }

        return super().default(obj)

# Test custom encoder
data = {
    'name': 'Project',
    'created': datetime.now(),
    'start_date': date.today(),
    'files': {Path('file1.txt'), Path('file2.txt')},
    'tags': {'python', 'json', 'data'},
    'raw': b'binary data',
}

json_str = json.dumps(data, cls=CustomEncoder, indent=2)
print("Encoded with custom encoder:")
print(json_str[:500] + "...")

# =============================================================================
# CUSTOM JSON DECODER
# =============================================================================
print("\n--- Custom JSON Decoder ---\n")

def object_hook(obj):
    """Decode custom objects."""
    if '__type__' in obj:
        type_name = obj['__type__']
        value = obj['value']

        if type_name == 'datetime':
            return datetime.fromisoformat(value)
        elif type_name == 'date':
            return date.fromisoformat(value)
        elif type_name == 'Path':
            return Path(value)
        elif type_name == 'set':
            return set(value)
        elif type_name == 'bytes':
            return value.encode('utf-8')

    return obj

# Decode
decoded = json.loads(json_str, object_hook=object_hook)
print("Decoded data types:")
for key, value in decoded.items():
    print(f"  {key}: {type(value).__name__} = {repr(value)[:50]}...")

# =============================================================================
# JSON LINES FORMAT
# =============================================================================
print("\n--- JSON Lines Format ---\n")

with tempfile.TemporaryDirectory() as tmpdir:
    jsonl_file = Path(tmpdir) / 'data.jsonl'

    # Write JSON Lines
    records = [
        {'id': 1, 'event': 'login', 'timestamp': '2024-01-15T10:00:00'},
        {'id': 2, 'event': 'logout', 'timestamp': '2024-01-15T12:00:00'},
        {'id': 3, 'event': 'purchase', 'timestamp': '2024-01-15T14:30:00', 'amount': 99.99},
    ]

    with open(jsonl_file, 'w') as f:
        for record in records:
            f.write(json.dumps(record) + '\n')

    print(f"Written {len(records)} records to JSON Lines")

    # Read JSON Lines
    loaded_records = []
    with open(jsonl_file) as f:
        for line_num, line in enumerate(f, 1):
            if line.strip():
                loaded_records.append(json.loads(line.strip()))

    print(f"Read {len(loaded_records)} records:")
    for rec in loaded_records:
        print(f"  {rec}")

# =============================================================================
# ADVANCED CSV
# =============================================================================
print("\n--- Advanced CSV ---\n")

with tempfile.TemporaryDirectory() as tmpdir:
    csv_file = Path(tmpdir) / 'data.csv'

    # Writing with custom dialect
    csv.register_dialect('semicolon',
        delimiter=';',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL,
        lineterminator='\n'
    )

    data = [
        {'name': 'Alice', 'city': 'New York', 'score': '95'},
        {'name': 'Bob', 'city': 'Los Angeles', 'score': '87'},
        {'name': 'Carol;Special', 'city': 'Chicago', 'score': '92'},  # Has semicolon!
    ]

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'city', 'score'], dialect='semicolon')
        writer.writeheader()
        writer.writerows(data)

    print("CSV with semicolon delimiter:")
    print(csv_file.read_text())

    # Reading back
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, dialect='semicolon')
        print("\nRead back:")
        for row in reader:
            print(f"  {row}")

# =============================================================================
# STREAMING LARGE FILES
# =============================================================================
print("\n--- Streaming Large Files ---\n")

def stream_csv_rows(filename):
    """Stream CSV rows one at a time."""
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def stream_jsonl(filename):
    """Stream JSON Lines one at a time."""
    with open(filename) as f:
        for line in f:
            if line.strip():
                yield json.loads(line.strip())

# Create test files
with tempfile.TemporaryDirectory() as tmpdir:
    # CSV
    csv_file = Path(tmpdir) / 'test.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'value'])
        for i in range(100):
            writer.writerow([i, f'value_{i}'])

    # Stream and process
    count = 0
    for row in stream_csv_rows(csv_file):
        count += 1
        if count <= 3:
            print(f"  CSV row {count}: {row}")
    print(f"  ... (total {count} rows)")

    # JSONL
    jsonl_file = Path(tmpdir) / 'test.jsonl'
    with open(jsonl_file, 'w') as f:
        for i in range(100):
            json.dump({'id': i, 'data': f'item_{i}'}, f)
            f.write('\n')

    count = 0
    for obj in stream_jsonl(jsonl_file):
        count += 1
        if count <= 3:
            print(f"  JSONL row {count}: {obj}")
    print(f"  ... (total {count} rows)")

# =============================================================================
# FORMAT CONVERSION
# =============================================================================
print("\n--- Format Conversion ---\n")

def csv_to_json(csv_file, json_file):
    """Convert CSV to JSON."""
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Convert numeric strings to numbers where possible
    for row in data:
        for key, value in row.items():
            try:
                if '.' in value:
                    row[key] = float(value)
                else:
                    row[key] = int(value)
            except ValueError:
                pass  # Keep as string

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    return len(data)

def json_to_csv(json_file, csv_file):
    """Convert JSON to CSV."""
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)

    if not data:
        return 0

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return len(data)

# Test conversion
with tempfile.TemporaryDirectory() as tmpdir:
    base = Path(tmpdir)

    # Create CSV
    csv_path = base / 'data.csv'
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'age', 'score'])
        writer.writerow(['Alice', '30', '95.5'])
        writer.writerow(['Bob', '25', '87.0'])

    # Convert to JSON
    json_path = base / 'data.json'
    count = csv_to_json(csv_path, json_path)
    print(f"Converted {count} rows to JSON:")
    print(json_path.read_text())

    # Convert back to CSV
    csv_path2 = base / 'data2.csv'
    count = json_to_csv(json_path, csv_path2)
    print(f"\nConverted back to CSV:")
    print(csv_path2.read_text())

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
