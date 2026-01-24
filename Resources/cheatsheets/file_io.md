# File I/O Cheatsheet

Quick reference for file operations in Python: reading/writing files, JSON, CSV, and path manipulation.

---

## Basic File Operations

### Opening Files
```python
# Best practice: context manager (automatically closes file)
with open("file.txt", "r") as file:
    content = file.read()

# Alternative (must manually close)
file = open("file.txt", "r")
content = file.read()
file.close()
```

### File Modes

| Mode | Description | Creates? | Pointer |
|------|-------------|-----------|---------|
| `"r"` | Read | ❌ No | Start |
| `"r+"` | Read + Write | ❌ No | Start |
| `"w"` | Write (overwrite) | ✅ Yes | Start |
| `"w+"` | Read + Write (overwrite) | ✅ Yes | Start |
| `"a"` | Append | ✅ Yes | End |
| `"a+"` | Read + Append | ✅ Yes | End |
| `"x"` | Exclusive creation | ✅ Yes | Start |

```python
# Read mode (default)
with open("file.txt", "r") as f:
    pass

# Write mode (overwrites existing)
with open("file.txt", "w") as f:
    f.write("Hello")

# Append mode (adds to end)
with open("file.txt", "a") as f:
    f.write("World")

# Binary mode for non-text files
with open("image.png", "rb") as f:
    data = f.read()

# Text mode with encoding
with open("file.txt", "r", encoding="utf-8") as f:
    pass
```

---

## Reading Files

### Read Entire File
```python
# Read all content as string
with open("file.txt", "r") as file:
    content = file.read()

# Read lines as list (preserves newlines)
with open("file.txt", "r") as file:
    lines = file.readlines()

# Read lines (strips newlines)
with open("file.txt", "r") as file:
    lines = [line.strip() for line in file]
```

### Read Line by Line
```python
# Memory efficient for large files
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read one line at a time
with open("file.txt", "r") as file:
    line = file.readline()      # First line
    while line:
        print(line.strip())
        line = file.readline()  # Next line
```

### File Methods
```python
with open("file.txt", "r") as file:
    file.read()           # Read all
    file.readline()       # Read one line
    file.readlines()      # Read all lines
    file.tell()           # Current position
    file.seek(0)          # Move to position
    file.seek(0, 2)       # Move to end (0=from start, 1=current, 2=end)
```

---

## Writing Files

### Write Text
```python
# Write string (overwrites)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line\n")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### Append to File
```python
# Add to existing file
with open("log.txt", "a") as file:
    file.write("New log entry\n")
```

### Write Binary
```python
# Write binary data
data = b'\x48\x65\x6c\x6c\x6f'  # "Hello" in bytes
with open("binary.dat", "wb") as file:
    file.write(data)
```

---

## Working with Directories

### os Module
```python
import os

# Check path exists
os.path.exists("file.txt")          # True/False
os.path.isfile("file.txt")          # True if file
os.path.isdir("folder")            # True if directory

# Get current directory
os.getcwd()                         # Current path

# Change directory
os.chdir("/path/to/directory")

# Create directory
os.mkdir("new_folder")              # Create single directory
os.makedirs("a/b/c")                # Create nested directories

# Remove directory
os.rmdir("folder")                  # Remove empty folder
os.removedirs("a/b/c")              # Remove nested empty folders

# List directory contents
os.listdir(".")                     # List files and folders

# Path operations
os.path.join("folder", "file.txt")  # "folder/file.txt"
os.path.basename("/path/to/file.txt") # "file.txt"
os.path.dirname("/path/to/file.txt")  # "/path/to"
os.path.splitext("file.txt")        # ("file", ".txt")
os.path.abspath("file.txt")         # Absolute path

# File info
os.path.getsize("file.txt")         # File size in bytes
os.path.getmtime("file.txt")        # Last modified timestamp
```

### pathlib Module (Python 3.4+)
```python
from pathlib import Path

# Create path
path = Path("folder/file.txt")

# Check path exists
path.exists()                       # True/False
path.is_file()                      # True if file
path.is_dir()                       # True if directory

# Path operations
path.parent                        # Parent directory
path.name                          # Filename
path.stem                          # Name without extension
path.suffix                        # Extension
path.with_suffix(".csv")            # Change extension

# Read/Write
path.read_text()                   # Read as string
path.write_text("Hello")            # Write string
path.read_bytes()                   # Read as bytes
path.write_bytes(b"Hello")          # Write bytes

# Create directories
path.mkdir()                        # Create directory
path.mkdir(parents=True)            # Create parent directories if needed

# List directory
list(Path(".").iterdir())           # List all files/folders

# Find files
list(Path(".").glob("*.txt"))      # Find all .txt files
list(Path(".").rglob("*.py"))      # Recursive search
```

---

## Working with JSON

### Reading JSON
```python
import json

# Read from file
with open("data.json", "r") as file:
    data = json.load(file)

# Parse JSON string
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
print(data["name"])  # "Alice"
```

### Writing JSON
```python
import json

# Write to file (pretty printed)
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

# Convert to JSON string
json_string = json.dumps(data, indent=2)
```

### JSON Options
```python
data = {"name": "Alice", "age": 25}

# Pretty print
json.dumps(data, indent=2)
"""
{
  "name": "Alice",
  "age": 25
}
"""

# Sort keys
json.dumps(data, sort_keys=True)

# Handle non-serializable types
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json()
        return super().default(obj)

json.dumps(data, cls=CustomEncoder)
```

---

## Working with CSV

### Reading CSV
```python
import csv

# Read all rows as list
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list

# Read as dictionary (header row used as keys)
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["column_name"])  # Access by column name
```

### Writing CSV
```python
import csv

# Write from list of lists
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "NYC"],
    ["Bob", 30, "LA"]
]
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Write from list of dictionaries
data = [
    {"Name": "Alice", "Age": 25, "City": "NYC"},
    {"Name": "Bob", "Age": 30, "City": "LA"}
]
with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
    writer.writeheader()
    writer.writerows(data)
```

### CSV Options
```python
# Custom delimiter and quote character
with open("data.csv", "r") as file:
    reader = csv.reader(file, delimiter=';', quotechar="'")

# Handle quoting
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)  # Quote all fields
```

---

## Error Handling

### Common File Errors
```python
try:
    with open("file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except IsADirectoryError:
    print("Path is a directory, not a file!")
except IOError as e:
    print(f"IO Error: {e}")
```

### Safe File Creation
```python
import os

# Check if file exists before overwriting
filename = "output.txt"
if os.path.exists(filename):
    print(f"Warning: {filename} will be overwritten")

# Create backup before writing
if os.path.exists(filename):
    backup = filename + ".bak"
    os.replace(filename, backup)

with open(filename, "w") as file:
    file.write("New content")
```

---

## Common Patterns

### Copy File
```python
# Method 1: Read and write
with open("source.txt", "rb") as src, open("dest.txt", "wb") as dst:
    dst.write(src.read())

# Method 2: With shutil (larger files)
import shutil
shutil.copy("source.txt", "dest.txt")
```

### Rename/Move File
```python
import os

os.rename("old_name.txt", "new_name.txt")
os.replace("old.txt", "new.txt")  # Overwrites if exists
```

### Delete File
```python
import os

os.remove("file.txt")  # Raises error if file doesn't exist

# Safe delete
if os.path.exists("file.txt"):
    os.remove("file.txt")
```

### Count Lines
```python
# Method 1 (reads entire file)
with open("file.txt", "r") as file:
    line_count = len(file.readlines())

# Method 2 (memory efficient)
line_count = 0
with open("file.txt", "r") as file:
    for line in file:
        line_count += 1
```

### Find Files by Pattern
```python
import glob

# Find all .txt files in directory
txt_files = glob.glob("*.txt")

# Find all .py files recursively
py_files = glob.glob("**/*.py", recursive=True)
```

---

## Temporary Files

```python
import tempfile

# Create temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
    tmp.write("Temporary content")
    tmp_path = tmp.name

# File exists while context is active
print(f"Temp file: {tmp_path}")

# Use the file
with open(tmp_path, "r") as f:
    print(f.read())

# File deleted automatically after context (if delete=True)
```

---

## File Encoding

```python
# Specify encoding when opening
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Common encodings
encoding = "utf-8"      # Most common, universal
encoding = "latin-1"    # Western European languages
encoding = "ascii"       # Only ASCII characters
encoding = "utf-16"      # Variable length, supports all characters

# Detect encoding (requires chardet library)
import chardet
with open("file.txt", "rb") as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    print(result["encoding"])  # Detected encoding
```

---

## Quick Reference

| Operation | Code | Description |
|-----------|------|-------------|
| **Open** | `open("file.txt", "r")` | Open file |
| **Read all** | `file.read()` | Read entire file |
| **Read line** | `file.readline()` | Read single line |
| **Read lines** | `file.readlines()` | Read all lines |
| **Write** | `file.write(text)` | Write string |
| **Write lines** | `file.writelines(list)` | Write list of strings |
| **Close** | `file.close()` | Close file |
| **JSON load** | `json.load(file)` | Parse JSON from file |
| **JSON dump** | `json.dump(data, file)` | Write JSON to file |
| **CSV reader** | `csv.reader(file)` | Read CSV |
| **CSV writer** | `csv.writer(file)` | Write CSV |

---

**Back to [Resources](../README.md)**
