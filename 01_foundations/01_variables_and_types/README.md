# 📦 Variables and Types

Variables are containers for storing data. Types define what kind of data you're storing.

---

## What is a Variable?

Think of a variable as a **labeled box** where you can store something.

```python
# Creating a variable is like putting something in a labeled box
message = "Hello, World!"
#  ↑          ↑
# label    contents
```

The `=` sign is the **assignment operator** — it puts the value on the right into the variable on the left.

---

## Naming Rules

### ✅ Valid variable names:
```python
name = "Alice"
age = 25
user_name = "bob123"
firstName = "John"
_private = "hidden"
counter2 = 0
```

### ❌ Invalid variable names:
```python
2nd_place = "silver"    # Can't start with a number
user-name = "bob"       # No hyphens allowed
my name = "Alice"       # No spaces allowed
class = "Python"        # Can't use reserved words
```

### 💡 Naming Conventions:
```python
# Python style (snake_case) - RECOMMENDED
user_name = "alice"
total_count = 42
is_valid = True

# Other styles you'll see (less common in Python)
userName = "alice"      # camelCase
UserName = "alice"      # PascalCase
```

---

## Basic Data Types

Python has several built-in types:

### 1. Strings (str) — Text
```python
name = "Alice"
greeting = 'Hello!'  # Single or double quotes work
long_text = """This is a
multiline string"""

# String operations
full_name = "Alice" + " " + "Smith"  # Concatenation
repeated = "Ha" * 3  # "HaHaHa"
length = len(name)   # 5
```

### 2. Integers (int) — Whole Numbers
```python
age = 25
temperature = -10
population = 1_000_000  # Underscores for readability

# Integer operations
total = 10 + 5    # 15
diff = 10 - 5     # 5
product = 10 * 5  # 50
```

### 3. Floats (float) — Decimal Numbers
```python
height = 1.75
pi = 3.14159
temperature = -40.0

# Float operations
half = 10 / 4     # 2.5 (always returns float)
result = 3.14 * 2 # 6.28
```

### 4. Booleans (bool) — True/False
```python
is_student = True
has_license = False

# Boolean operations
can_drive = has_license and age >= 16
is_teenager = age >= 13 and age <= 19
```

### 5. None — Absence of Value
```python
result = None  # No value assigned yet

# Check for None
if result is None:
    print("No result yet")
```

---

## Type Checking and Conversion

### Check type with `type()`:
```python
name = "Alice"
age = 25
height = 1.75
is_student = True

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student)) # <class 'bool'>
```

### Convert between types:
```python
# String to integer
age_str = "25"
age = int(age_str)  # 25 (now an integer)

# Integer to string
count = 42
count_str = str(count)  # "42"

# String to float
price_str = "19.99"
price = float(price_str)  # 19.99

# Float to integer (truncates!)
pi = 3.14159
whole = int(pi)  # 3 (not rounded, just truncated)
```

---

## Dynamic Typing

Python is **dynamically typed** — variables can change type:

```python
x = 10        # x is an integer
print(type(x))  # <class 'int'>

x = "hello"   # Now x is a string!
print(type(x))  # <class 'str'>

x = [1, 2, 3] # Now x is a list!
print(type(x))  # <class 'list'>
```

> ⚠️ **Note:** Just because you *can* change types doesn't mean you *should*. It can make code confusing.

---

## Common Mistakes

### 1. Using before assigning:
```python
print(username)  # ❌ NameError: 'username' is not defined
username = "alice"
```

### 2. Wrong type operations:
```python
age = "25"
next_year = age + 1  # ❌ TypeError: can't add string and int
next_year = int(age) + 1  # ✅ Convert first
```

### 3. Case sensitivity:
```python
Name = "Alice"
print(name)  # ❌ NameError: 'name' is not defined
print(Name)  # ✅ Correct
```

---

## Real-World Analogy

| Concept | Real-World | Python |
|---------|------------|--------|
| Variable | A labeled jar | `cookies = 10` |
| String | A name tag | `name = "Alice"` |
| Integer | Counting on fingers | `age = 25` |
| Float | A thermometer reading | `temp = 98.6` |
| Boolean | A light switch (on/off) | `is_on = True` |
| None | Empty box | `result = None` |

---

## Quick Reference

```python
# Creating variables
name = "Alice"           # String
age = 25                 # Integer
height = 1.75            # Float
is_student = True        # Boolean
data = None              # None

# Checking type
type(variable)           # Returns the type

# Converting types
str(25)                  # "25"
int("25")               # 25
float("3.14")           # 3.14
bool(1)                 # True
bool(0)                 # False
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
