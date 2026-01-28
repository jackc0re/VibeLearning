# 📁 Pathlib Module

> **Object-oriented filesystem paths**

---

## 🎯 Learning Objectives

By the end of this section, you'll understand:
- Why `pathlib` is preferred over `os.path`
- How to create and manipulate Path objects
- How to navigate directories and find files
- How to read and write files with Path objects

---

## 🔄 Pathlib vs os.path

| Task | os.path | pathlib |
|------|---------|---------|
| Join paths | `os.path.join(a, b)` | `Path(a) / b` |
| Get filename | `os.path.basename(p)` | `Path(p).name` |
| Get directory | `os.path.dirname(p)` | `Path(p).parent` |
| Get extension | `os.path.splitext(p)` | `Path(p).suffix` |
| Check exists | `os.path.exists(p)` | `Path(p).exists()` |
| Check is file | `os.path.isfile(p)` | `Path(p).is_file()` |

### Why Pathlib?

1. **More intuitive** - Uses `/` operator for path joining
2. **Object-oriented** - Methods on Path objects
3. **Cross-platform** - Handles Windows vs Unix paths automatically
4. **More features** - Built-in glob, pattern matching, etc.

---

## 🛤️ Creating Paths

```python
from pathlib import Path

# Current directory
cwd = Path.cwd()

# Home directory
home = Path.home()

# From string
config = Path('/etc/config.txt')  # Absolute
readme = Path('README.md')        # Relative

# Building paths with /
data_dir = Path('project') / 'data' / 'users.json'
# Windows: project\data\users.json
# Unix: project/data/users.json
```

---

## 📂 Path Components

```python
from pathlib import Path

p = Path('/home/user/documents/file.txt')

print(p.name)       # 'file.txt'
print(p.stem)       # 'file'
print(p.suffix)     # '.txt'
print(p.suffixes)   # ['.txt']
print(p.parent)     # Path('/home/user/documents')
print(p.parents[0]) # Path('/home/user/documents')
print(p.parents[1]) # Path('/home/user')
print(p.parts)      # ('/', 'home', 'user', 'documents', 'file.txt')
print(p.anchor)     # '/' (Unix) or 'C:\\' (Windows)
```

---

## 🔍 Checking Paths

```python
from pathlib import Path

p = Path('example.txt')

# Existence and type
p.exists()      # Does it exist?
p.is_file()     # Is it a file?
p.is_dir()      # Is it a directory?
p.is_symlink()  # Is it a symbolic link?
p.is_absolute() # Is it an absolute path?

# File properties
if p.exists():
    print(p.stat())           # File stats
    print(p.stat().st_size)   # File size in bytes
```

---

## 📖 Reading and Writing Files

### Reading

```python
from pathlib import Path

# Read entire file as text
content = Path('file.txt').read_text(encoding='utf-8')

# Read as bytes
data = Path('image.png').read_bytes()

# Read lines
lines = Path('file.txt').read_text().splitlines()
```

### Writing

```python
from pathlib import Path

# Write text
Path('output.txt').write_text('Hello, World!', encoding='utf-8')

# Write bytes
Path('output.bin').write_bytes(b'\x00\x01\x02\x03')

# Append (read, modify, write)
p = Path('log.txt')
p.write_text(p.read_text() + '\nNew line')
```

---

## 🔎 Finding Files

### Glob Patterns

```python
from pathlib import Path

# Current directory
p = Path('.')

# All Python files
list(p.glob('*.py'))

# Recursive search
list(p.rglob('*.py'))  # All .py files in subdirectories

# Multiple patterns
list(p.glob('**/*.txt'))  # All .txt files recursively
```

### Pattern Matching

```python
from pathlib import Path

p = Path('document.txt')

p.match('*.txt')        # True
p.match('doc*.txt')     # True
p.match('*.py')         # False
```

---

## 📁 Directory Operations

```python
from pathlib import Path

# Create directory
dir_path = Path('new_folder')
dir_path.mkdir()          # Fails if exists
dir_path.mkdir(exist_ok=True)  # OK if exists
dir_path.mkdir(parents=True, exist_ok=True)  # Create parents too

# Create nested structure
Path('a/b/c').mkdir(parents=True, exist_ok=True)

# Rename
Path('old.txt').rename('new.txt')

# Delete
Path('file.txt').unlink()       # Delete file
Path('empty_dir').rmdir()       # Delete empty directory

# Iterate directory
for item in Path('.').iterdir():
    print(item)
```

---

## ⚠️ Common Mistakes

1. **Forgetting Path() wrapper** - Can't use `/` with strings directly
2. **Not handling exceptions** - Path operations can fail
3. **Using `+` instead of `/`** - `+` concatenates strings, `/` joins paths
4. **Forgetting `parents=True`** - `mkdir()` fails if parent doesn't exist
5. **Not specifying encoding** - Always use `encoding='utf-8'` for text

---

## 📝 Quick Reference

```python
from pathlib import Path

# Creating
p = Path('folder') / 'file.txt'

# Components
p.name, p.stem, p.suffix, p.parent

# Checking
p.exists(), p.is_file(), p.is_dir()

# Reading/Writing
p.read_text(), p.write_text('content')
p.read_bytes(), p.write_bytes(b'data')

# Finding
list(Path('.').glob('*.py'))
list(Path('.').rglob('**/*.txt'))

# Directories
Path('new').mkdir(parents=True, exist_ok=True)
```

---

## 🎓 Next Steps

Run `examples.py` to see pathlib in action, then try `exercises.py`!
