# Python Basics Cheatsheet

Quick reference for Python fundamentals: variables, operators, control flow, functions, and exceptions.

---

## Variables & Data Types

### Basic Types
```python
# Numbers
x = 42              # int
y = 3.14            # float
z = 1 + 2j          # complex

# Strings
name = "Alice"
greeting = f"Hello, {name}"  # f-string

# Boolean
is_active = True
is_done = False

# None
result = None
```

### Type Conversion
```python
# Explicit conversion
int("42")           # 42
float("3.14")       # 3.14
str(123)            # "123"
bool(1)             # True
bool(0)             # False

# Check type
type(x) == int      # True
isinstance(x, int)  # True
```

---

## Operators

### Arithmetic Operators
```python
a + b    # Addition
a - b    # Subtraction
a * b    # Multiplication
a / b    # Division (float)
a // b   # Floor division (int)
a % b    # Modulus (remainder)
a ** b   # Exponentiation

# Examples
7 / 2     # 3.5
7 // 2    # 3
7 % 2     # 1
2 ** 3    # 8
```

### Comparison Operators
```python
a == b   # Equal
a != b   # Not equal
a > b    # Greater than
a < b    # Less than
a >= b   # Greater or equal
a <= b   # Less or equal

# Chaining
10 < x < 20  # x between 10 and 20
```

### Logical Operators
```python
a and b   # Both must be True
a or b    # At least one True
not a     # Negate

# Short-circuit evaluation
a and b   # b not evaluated if a is False
a or b    # b not evaluated if a is True
```

### Membership Operators
```python
item in sequence       # True if item in sequence
item not in sequence   # True if item NOT in sequence

# Examples
"x" in "hello"          # False
2 in [1, 2, 3]         # True
"key" in {"key": 1}     # True
```

### Identity Operators
```python
a is b       # True if same object
a is not b   # True if different objects

# Examples
x = [1, 2]
y = [1, 2]
x is y       # False (different objects)
x == y       # True (same values)

x = None
x is None    # True (None is singleton)
```

### Assignment Operators
```python
x = 5       # Assignment
x += 3      # x = x + 3  → 8
x -= 2      # x = x - 2  → 6
x *= 4      # x = x * 4  → 24
x /= 2      # x = x / 2  → 12.0
x //= 3     # x = x // 3 → 4
x %= 3      # x = x % 3  → 1
x **= 2     # x = x ** 2 → 1
```

---

## Control Flow

### If-Elif-Else
```python
if condition:
    # Code to execute if True
elif another_condition:
    # Code to execute if True
else:
    # Code to execute if all False

# Ternary operator
value = "yes" if condition else "no"

# Multiple conditions
if x > 0 and x < 10:
    pass
```

### While Loop
```python
while condition:
    # Code to repeat
    break     # Exit loop
    continue  # Skip to next iteration

# Example
count = 0
while count < 5:
    print(count)
    count += 1
```

### For Loop
```python
for item in sequence:
    # Code to execute for each item
    break     # Exit loop
    continue  # Skip to next iteration

# Range
for i in range(5):         # 0, 1, 2, 3, 4
    pass

for i in range(2, 5):      # 2, 3, 4
    pass

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    pass

# Enumerate - get index and value
for i, item in enumerate(items):
    print(f"{i}: {item}")

# Zip - iterate multiple sequences
for a, b in zip(list1, list2):
    pass
```

### Match-Case (Python 3.10+)
```python
match value:
    case 1:
        print("one")
    case 2 | 3:
        print("two or three")
    case _:
        print("other")
```

---

## Functions

### Basic Functions
```python
def greet(name):
    """Docstring describing function."""
    return f"Hello, {name}!"

# Call
result = greet("Alice")
```

### Parameters
```python
# Positional parameters
def func(a, b, c):
    pass
func(1, 2, 3)

# Default parameters
def func(a, b=5, c="hello"):
    pass
func(1)           # a=1, b=5, c="hello"
func(1, 10)        # a=1, b=10, c="hello"

# Keyword arguments
func(b=2, a=1, c="test")

# Arbitrary positional args (*args)
def func(*args):
    for arg in args:
        print(arg)
func(1, 2, 3)      # args = (1, 2, 3)

# Arbitrary keyword args (**kwargs)
def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
func(name="Alice", age=25)  # kwargs = {'name': 'Alice', 'age': 25}
```

### Return Values
```python
def calculate(x, y):
    return x + y, x - y  # Return tuple

# Unpack
sum_result, diff_result = calculate(10, 5)

# Return None (default)
def process():
    pass  # Implicitly returns None
```

### Scope & Global
```python
x = 10  # Global

def outer():
    y = 5  # Enclosing

    def inner():
        z = 3  # Local
        nonlocal y  # Modify enclosing variable
        global x   # Modify global variable
        x = 20
        y = 10
        return x + y + z
```

---

## String Manipulation

### Basic Operations
```python
s = "Hello, World!"

# Length
len(s)              # 13

# Access (zero-indexed)
s[0]                # 'H'
s[-1]               # '!'

# Slicing [start:end:step]
s[0:5]              # 'Hello'
s[7:]               # 'World!'
s[::2]              # 'Hlo ol!'
s[::-1]             # '!dlroW ,olleH' (reverse)

# Concatenation
s1 = "Hello"
s2 = "World"
s1 + " " + s2       # 'Hello World'

# Repetition
"ha" * 3            # 'hahaha'
```

### String Methods
```python
# Case
s.lower()           # 'hello, world!'
s.upper()           # 'HELLO, WORLD!'
s.title()           # 'Hello, World!'
s.capitalize()       # 'Hello, world!'
s.swapcase()        # 'hELLO, wORLD!'

# Search & Check
s.find("World")     # 7 (returns -1 if not found)
s.index("World")    # 7 (raises ValueError if not found)
s.startswith("Hello")  # True
s.endswith("!")     # True
"ello" in s         # True

# Replace
s.replace("World", "Python")  # 'Hello, Python!'

# Strip whitespace
s = "  hello  "
s.strip()           # 'hello'
s.lstrip()          # 'hello  '
s.rstrip()          # '  hello'

# Split & Join
s.split(",")        # ['Hello', ' World!']
" ".join(['a', 'b', 'c'])  # 'a b c'

# Format
f"{name} is {age}"  # f-string (Python 3.6+)
"{} is {}".format(name, age)
"%s is %d" % (name, age)

# Other
s.count("l")        # 3
s.isdigit()         # Check if all digits
s.isalpha()         # Check if all letters
s.isalnum()         # Check if alphanumeric
```

---

## Exception Handling

### Try-Except-Finally
```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle specific exception
    print(f"Error: {e}")
except ValueError:
    # Handle another exception
    print("Invalid value")
except Exception as e:
    # Catch all exceptions
    print(f"Unexpected error: {e}")
else:
    # Execute if no exception occurred
    print("Success!")
finally:
    # Always execute (cleanup)
    print("Cleanup code")
```

### Common Exceptions
```python
# Raising exceptions
raise ValueError("Invalid input")
raise TypeError("Expected int")
raise Exception("Custom error")

# Built-in exceptions
ZeroDivisionError   # Division by zero
NameError          # Undefined variable
TypeError          # Operation on wrong type
ValueError         # Invalid value
IndexError         # Index out of range
KeyError           # Key not found in dict
AttributeError     # Attribute doesn't exist
FileNotFoundError  # File doesn't exist
ImportError        # Module import failed
```

### Custom Exceptions
```python
class CustomError(Exception):
    """Custom exception class."""
    pass

# Raise custom exception
raise CustomError("Something went wrong!")
```

---

## Input & Output

### Input
```python
# Get user input (always returns string)
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to int
```

### Output
```python
# Basic print
print("Hello")
print("Hello", "World")  # Hello World

# Separator and end
print("a", "b", "c", sep="-", end="!\n")  # a-b-c!

# Formatted output
print(f"Name: {name}, Age: {age}")

# Print with flush (for real-time output)
print("Loading...", end="", flush=True)
```

---

## Useful Built-in Functions

```python
# Type conversions
int(x)        # Convert to integer
float(x)      # Convert to float
str(x)        # Convert to string
bool(x)       # Convert to boolean
list(x)       # Convert to list
tuple(x)      # Convert to tuple
set(x)        # Convert to set

# Math
abs(x)        # Absolute value
round(x, n)   # Round to n decimals
min(seq)      # Minimum value
max(seq)      # Maximum value
sum(seq)      # Sum of values

# Sequences
len(seq)      # Length
sorted(seq)   # Return sorted list
reversed(seq) # Return reversed iterator
enumerate(seq)# Return (index, value) pairs
zip(*iterables)# Combine sequences

# Type checking
type(x)       # Return type
isinstance(x, type)  # Check if instance of type
hasattr(obj, attr)   # Check if object has attribute

# Others
help(obj)     # Show help documentation
dir(obj)      # List object attributes
id(obj)       # Return object's unique id
```

---

## Quick Reference Table

| Category | Command | Example |
|----------|---------|---------|
| Variable | `x = 5` | Assign value |
| Print | `print(x)` | Display value |
| Input | `input()` | Get user input |
| If | `if x > 0:` | Conditional |
| Loop | `for i in range(5):` | Repeat |
| Function | `def func():` | Define function |
| Return | `return x` | Return value |
| String | `s.upper()` | Uppercase |
| Exception | `try/except` | Handle errors |

---

**Back to [Resources](../README.md)**
