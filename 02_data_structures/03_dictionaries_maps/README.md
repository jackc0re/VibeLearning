# 📖 Dictionaries and Maps

Dictionaries are Python's key-value data structure — perfect for looking up values by a unique identifier.

---

## What is a Dictionary?

Think of a dictionary like a **phone book**: you look up a name (key) to find a phone number (value).

```python
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
# Key: "Alice" -> Value: "555-1234"
```

---

## Creating Dictionaries

```python
# Empty dictionary
empty = {}
empty = dict()

# With initial values
person = {"name": "Alice", "age": 25, "city": "NYC"}

# From list of tuples
items = dict([("a", 1), ("b", 2), ("c", 3)])

# From keyword arguments
config = dict(debug=True, version="1.0", max_size=100)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## Accessing Values

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Bracket notation
print(person["name"])  # "Alice"
print(person["age"])   # 25

# Get method (safer - returns None if missing)
print(person.get("name"))      # "Alice"
print(person.get("country"))   # None
print(person.get("country", "Unknown"))  # "Unknown" (default)

# Bracket notation raises KeyError if missing!
print(person["country"])  # ❌ KeyError: 'country'
```

---

## Modifying Dictionaries

### Adding/Updating Values
```python
person = {"name": "Alice"}

person["age"] = 25           # Add new key
person["name"] = "Alicia"    # Update existing key
person.update({"city": "NYC", "age": 26})  # Update multiple

print(person)  # {"name": "Alicia", "age": 26, "city": "NYC"}
```

### Removing Values
```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

age = person.pop("age")      # Remove and return value
print(age)  # 25

del person["city"]           # Just delete (no return)

person.clear()               # Remove all items
```

---

## Common Dictionary Methods

| Method | Description | Example |
|--------|-------------|---------|
| `get(key, default)` | Get value or default | `d.get('x', 0)` |
| `keys()` | All keys | `list(d.keys())` |
| `values()` | All values | `list(d.values())` |
| `items()` | Key-value pairs | `list(d.items())` |
| `pop(key)` | Remove and return | `d.pop('x')` |
| `update(dict2)` | Merge/update | `d.update({'a': 1})` |
| `setdefault(key, default)` | Get or set default | `d.setdefault('x', [])` |
| `copy()` | Shallow copy | `d2 = d.copy()` |

---

## Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Iterate over keys (default)
for key in person:
    print(key)  # name, age, city

# Iterate over values
for value in person.values():
    print(value)  # Alice, 25, NYC

# Iterate over both
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Dictionary Comprehensions

```python
# Basic
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
# {"a": 1, "b": 2, "c": 3}

# Invert a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

---

## Nested Dictionaries

```python
# Nested structure
users = {
    "alice": {
        "email": "alice@example.com",
        "age": 25,
        "hobbies": ["reading", "coding"]
    },
    "bob": {
        "email": "bob@example.com",
        "age": 30,
        "hobbies": ["gaming", "music"]
    }
}

# Access nested values
print(users["alice"]["email"])       # alice@example.com
print(users["bob"]["hobbies"][0])    # gaming

# Safe nested access
alice_age = users.get("alice", {}).get("age", "Unknown")
```

---

## Checking Keys

```python
person = {"name": "Alice", "age": 25}

# Check if key exists
"name" in person      # True
"country" in person   # False

# Check if key doesn't exist
"country" not in person  # True
```

---

## Common Patterns

### Count occurrences
```python
text = "hello"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Or use Counter
from collections import Counter
counts = Counter(text)
```

### Group items
```python
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
by_letter = {}
for word in words:
    first = word[0]
    if first not in by_letter:
        by_letter[first] = []
    by_letter[first].append(word)
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

### Merge dictionaries
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Python 3.9+
merged = d1 | d2  # {"a": 1, "b": 3, "c": 4}

# Python 3.5+
merged = {**d1, **d2}
```

---

## Common Mistakes

### 1. Modifying while iterating
```python
d = {"a": 1, "b": 2, "c": 3}

# ❌ RuntimeError
for key in d:
    if d[key] < 2:
        del d[key]

# ✅ Create list of keys first
for key in list(d.keys()):
    if d[key] < 2:
        del d[key]
```

### 2. Using mutable keys
```python
# ❌ Lists can't be keys (not hashable)
d = {[1, 2]: "value"}  # TypeError

# ✅ Use tuples instead
d = {(1, 2): "value"}
```

### 3. Missing key errors
```python
d = {"a": 1}
print(d["b"])  # ❌ KeyError

# ✅ Use get() method
print(d.get("b", 0))
```

---

## Quick Reference

```python
# Create
d = {}
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)

# Access
d["key"]           # Raises KeyError if missing
d.get("key")       # Returns None if missing
d.get("key", 0)    # Returns default if missing

# Modify
d["key"] = value   # Add or update
d.update({...})    # Merge another dict
d.pop("key")       # Remove and return
del d["key"]       # Just remove

# Iterate
for key in d: ...
for value in d.values(): ...
for key, value in d.items(): ...

# Check
"key" in d
"key" not in d
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
