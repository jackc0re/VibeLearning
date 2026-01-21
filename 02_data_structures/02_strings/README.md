# 🔤 Strings Deep Dive

Strings are sequences of characters — the way we work with text in Python. This module covers advanced string manipulation beyond the basics.

---

## What is a String?

A string is an **immutable sequence** of characters.

```python
text = "Hello, World!"
# Strings are indexed like lists
#  H  e  l  l  o  ,     W  o  r  l  d  !
#  0  1  2  3  4  5  6  7  8  9 10 11 12
```

> 💡 **Immutable** means once created, a string cannot be changed. Operations return new strings.

---

## Creating Strings

```python
# Single or double quotes
name = 'Alice'
message = "Hello, World!"

# Multiline strings
poem = """Roses are red,
Violets are blue,
Python is great,
And so are you."""

# Raw strings (ignore escape sequences)
path = r"C:\Users\name\folder"  # backslashes treated literally

# F-strings (formatted strings)
name = "Alice"
greeting = f"Hello, {name}!"
```

---

## String Indexing & Slicing

```python
text = "Python"

# Indexing
print(text[0])    # 'P'
print(text[-1])   # 'n'

# Slicing [start:end:step]
print(text[0:3])   # 'Pyt'
print(text[::2])   # 'Pto' (every 2nd character)
print(text[::-1])  # 'nohtyP' (reversed)

# Strings are immutable!
text[0] = 'J'  # ❌ TypeError!
text = 'J' + text[1:]  # ✅ Create new string
```

---

## Essential String Methods

### Case Conversion
```python
text = "Hello World"

text.upper()      # "HELLO WORLD"
text.lower()      # "hello world"
text.title()      # "Hello World"
text.capitalize() # "Hello world"
text.swapcase()   # "hELLO wORLD"
```

### Searching
```python
text = "Hello, World!"

text.find("World")     # 7 (index where found)
text.find("Python")    # -1 (not found)
text.index("World")    # 7 (raises ValueError if not found)
text.count("l")        # 3
text.startswith("He")  # True
text.endswith("!")     # True
"World" in text        # True
```

### Modifying
```python
text = "Hello, World!"

text.replace("World", "Python")  # "Hello, Python!"
text.replace("l", "L", 1)        # "HeLlo, World!" (replace first only)

"  spaces  ".strip()    # "spaces"
"  spaces  ".lstrip()   # "spaces  "
"  spaces  ".rstrip()   # "  spaces"
"xxHelloxx".strip("x")  # "Hello"
```

### Splitting & Joining
```python
# Split into list
text = "apple,banana,cherry"
text.split(",")  # ["apple", "banana", "cherry"]

"Hello World".split()  # ["Hello", "World"] (splits on whitespace)

lines = "line1\nline2\nline3"
lines.splitlines()  # ["line1", "line2", "line3"]

# Join list into string
fruits = ["apple", "banana", "cherry"]
", ".join(fruits)  # "apple, banana, cherry"
"-".join(fruits)   # "apple-banana-cherry"
```

### Checking Content
```python
"hello".isalpha()    # True (only letters)
"12345".isdigit()    # True (only digits)
"hello123".isalnum() # True (letters and/or digits)
"   ".isspace()      # True (only whitespace)
"Hello".isupper()    # False
"HELLO".isupper()    # True
"hello".islower()    # True
```

---

## String Formatting

### F-Strings (Recommended)
```python
name = "Alice"
age = 25
score = 95.5

# Basic interpolation
print(f"Name: {name}, Age: {age}")

# Expressions inside braces
print(f"Next year: {age + 1}")

# Width and alignment
print(f"{'left':<10}|{'center':^10}|{'right':>10}")
# left      |  center  |     right

# Number formatting
print(f"Score: {score:.1f}")    # One decimal: 95.5
print(f"Score: {score:08.2f}")  # Pad with zeros: 00095.50
print(f"Large: {1000000:,}")    # Thousands separator: 1,000,000
print(f"Percent: {0.756:.1%}")  # Percentage: 75.6%
```

### Format Method
```python
# Positional
"{} and {}".format("a", "b")  # "a and b"

# Named
"{name} is {age}".format(name="Alice", age=25)

# Indexed
"{0} {1} {0}".format("hello", "world")  # "hello world hello"
```

---

## Common Patterns

### Reverse a string
```python
text = "Hello"
reversed_text = text[::-1]  # "olleH"
```

### Check palindrome
```python
def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]

is_palindrome("A man a plan a canal Panama")  # True
```

### Count words
```python
text = "Hello World, how are you?"
word_count = len(text.split())  # 5
```

### Find all occurrences
```python
text = "banana"
char = "a"
indices = [i for i, c in enumerate(text) if c == char]
# [1, 3, 5]
```

### Remove punctuation
```python
import string

text = "Hello, World!"
clean = text.translate(str.maketrans("", "", string.punctuation))
# "Hello World"
```

---

## Common Mistakes

### 1. Strings are immutable
```python
s = "hello"
s[0] = "H"  # ❌ TypeError

# ✅ Create a new string
s = "H" + s[1:]
```

### 2. Split returns a list
```python
"a,b,c".split(",")  # Returns ['a', 'b', 'c'], not a string!
```

### 3. Case-sensitive comparisons
```python
"Hello" == "hello"  # False!
"Hello".lower() == "hello".lower()  # True
```

---

## Quick Reference

```python
# Creation
s = "hello"
s = 'hello'
s = """multiline"""
s = f"formatted {var}"

# Access
s[0]       # First character
s[-1]      # Last character
s[1:3]     # Slice

# Methods
s.upper(), s.lower(), s.title()
s.strip(), s.lstrip(), s.rstrip()
s.split(), s.join()
s.find(), s.index(), s.count()
s.replace(), s.startswith(), s.endswith()
s.isalpha(), s.isdigit(), s.isalnum()

# Operators
s + " world"   # Concatenation
s * 3          # Repetition
"x" in s       # Membership
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
