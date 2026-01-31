# 📊 JSON & CSV Deep Dive

> **Advanced data serialization techniques**

---

## 🎯 Learning Objectives

By the end of this section, you'll understand:
- Advanced JSON serialization (custom encoders/decoders)
- Working with JSON Lines format
- Advanced CSV reading and writing
- Handling complex data structures

---

## 📦 JSON Module Recap

Basic usage (from File I/O module):

```python
import json

# Reading
data = json.load(open('data.json'))
data = json.loads('{"key": "value"}')

# Writing
json.dump(data, open('output.json', 'w'), indent=2)
json_string = json.dumps(data, indent=2)
```

---

## 🔧 Custom JSON Encoding

### The Problem

```python
import json
from datetime import datetime

# This fails!
data = {'time': datetime.now()}
json.dumps(data)  # TypeError: not JSON serializable
```

### Solution: Custom Encoder

```python
import json
from datetime import datetime
from pathlib import Path

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        # Handle datetime
        if isinstance(obj, datetime):
            return obj.isoformat()
        
        # Handle Path objects
        if isinstance(obj, Path):
            return str(obj)
        
        # Handle sets
        if isinstance(obj, set):
            return list(obj)
        
        # Let the base class handle it or raise error
        return super().default(obj)

# Usage
data = {
    'time': datetime.now(),
    'path': Path('/home/user'),
    'tags': {'python', 'json'}
}

json_str = json.dumps(data, cls=CustomEncoder, indent=2)
```

---

## 🔨 Custom JSON Decoding

```python
import json
from datetime import datetime

def object_hook(obj):
    """Convert dict back to objects."""
    # Detect datetime strings
    if 'timestamp' in obj:
        obj['timestamp'] = datetime.fromisoformat(obj['timestamp'])
    return obj

# Usage
data = json.loads(json_string, object_hook=object_hook)
```

---

## 📄 JSON Lines (JSONL) Format

JSON Lines is a format where each line is a valid JSON object.

```python
import json

# Writing JSON Lines
data = [
    {'name': 'Alice', 'score': 95},
    {'name': 'Bob', 'score': 87},
]

with open('data.jsonl', 'w') as f:
    for item in data:
        f.write(json.dumps(item) + '\n')

# Reading JSON Lines
data = []
with open('data.jsonl') as f:
    for line in f:
        data.append(json.loads(line.strip()))
```

**Use cases:** Logs, streaming data, large datasets that don't fit in memory.

---

## 📑 CSV Module Recap

Basic usage:

```python
import csv

# Reading
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# DictReader
with open('data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['column_name'])
```

---

## 🔧 Advanced CSV

### Custom Dialects

```python
import csv

# Define a custom dialect
csv.register_dialect('myformat',
    delimiter=';',
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    lineterminator='\n'
)

# Use the dialect
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='myformat')
    writer.writerow(['name', 'value'])
```

### Handling Different Encodings

```python
import csv

# UTF-8 with BOM for Excel compatibility
with open('data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Value'])

# Reading with specific encoding
with open('data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
```

### Large CSV Files (Streaming)

```python
import csv

def stream_csv_rows(filename):
    """Stream CSV rows one at a time (memory efficient)."""
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header
        for row in reader:
            yield dict(zip(header, row))

# Process without loading entire file
for row in stream_csv_rows('huge_file.csv'):
    process(row)  # Process one row at a time
```

---

## 🔄 Converting Between Formats

### CSV to JSON

```python
import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
```

### JSON to CSV

```python
import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, encoding='utf-8') as f:
        data = json.load(f)
    
    if not data:
        return
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
```

---

## ⚠️ Common Mistakes

1. **Not specifying encoding** - Always use `encoding='utf-8'`
2. **Forgetting `newline=''`** in CSV mode
3. **Trying to serialize unserializable objects** - Use custom encoder
4. **Loading huge files into memory** - Use streaming for large files

---

## 📝 Quick Reference

```python
import json
import csv

# JSON with custom types
class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

json.dumps(data, cls=Encoder)

# JSON Lines
with open('file.jsonl') as f:
    for line in f:
        data = json.loads(line)

# CSV streaming
with open('file.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        process(row)
```

---

## 🎓 Next Steps

Run `examples.py` to see these in action, then try `exercises.py`!
