# 📦 Tuples

Tuples are **immutable** sequences — like lists that can't be changed after creation.

---

## What is a Tuple?

Think of a tuple as a **sealed container**: once packed, you can look inside but can't add, remove, or change items.

```python
# A tuple is defined with parentheses
coordinates = (10, 20)
point = (3, 4, 5)

# The parentheses are optional (but recommended for clarity)
rgb = 255, 128, 0
```

---

## Creating Tuples

```python
# Empty tuple
empty = ()
empty = tuple()

# Single element (note the comma!)
single = (42,)      # ✅ Tuple with one element
not_tuple = (42)    # ❌ Just an integer in parentheses!

# Multiple elements
colors = ("red", "green", "blue")
mixed = (1, "hello", 3.14, True)

# From other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
```

> ⚠️ **Important:** A single-element tuple needs a trailing comma: `(42,)` not `(42)`.

---

## Accessing Elements

```python
point = (10, 20, 30, 40, 50)

# Indexing (same as lists)
print(point[0])    # 10
print(point[-1])   # 50

# Slicing
print(point[1:3])  # (20, 30)
print(point[::-1]) # (50, 40, 30, 20, 10)
```

---

## Tuple Unpacking

One of Python's most useful features:

```python
# Basic unpacking
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")  # x=10, y=20

# Unpacking with *rest
first, *middle, last = (1, 2, 3, 4, 5)
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Swap variables
a, b = 1, 2
a, b = b, a    # a=2, b=1

# Return multiple values from function
def get_dimensions():
    return (100, 200)  # Returns a tuple

width, height = get_dimensions()
```

---

## Tuple Methods

Tuples have only two methods (they're immutable!):

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - how many times value appears
numbers.count(2)  # 3

# index() - position of first occurrence
numbers.index(4)  # 4
```

---

## Tuples vs Lists

| Feature | Tuple | List |
|---------|-------|------|
| Mutable | ❌ No | ✅ Yes |
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Methods | 2 | Many |
| Hashable | ✅ Yes | ❌ No |
| Speed | Slightly faster | Slightly slower |
| Memory | Less | More |

### When to Use Tuples

1. **Fixed data** that shouldn't change (coordinates, RGB colors)
2. **Dictionary keys** (lists can't be keys!)
3. **Multiple return values** from functions
4. **Data integrity** when you want to prevent modification

```python
# Tuple as dictionary key
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

# This won't work with lists!
# locations = {[40.7128, -74.0060]: "New York"}  # ❌ TypeError
```

---

## Named Tuples

For more readable tuples with named fields:

```python
from collections import namedtuple

# Define a named tuple type
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p = Point(10, 20)
print(p.x)     # 10
print(p.y)     # 20
print(p[0])    # 10 (still works like regular tuple)

# Unpack like regular tuple
x, y = p

# More examples
Person = namedtuple('Person', ['name', 'age', 'city'])
alice = Person('Alice', 25, 'NYC')
print(f"{alice.name} is {alice.age} years old")
```

---

## Tuple Operations

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
combined = t1 + t2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = t1 * 3   # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership
2 in t1     # True
7 in t1     # False

# Comparison
(1, 2) < (1, 3)   # True (compares element by element)
(1, 2) == (1, 2)  # True
```

---

## Immutability Gotchas

```python
# Can't modify tuple elements
t = (1, 2, 3)
t[0] = 99  # ❌ TypeError!

# BUT: if tuple contains mutable objects, they can change!
t = ([1, 2], [3, 4])
t[0].append(3)  # ✅ Works!
print(t)  # ([1, 2, 3], [3, 4])

# The tuple itself didn't change (still same references)
# But the list inside did
```

---

## Common Patterns

### Multiple return values
```python
def min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_max([3, 1, 4, 1, 5, 9])
```

### Enumerate with tuples
```python
for index, value in enumerate(['a', 'b', 'c']):
    print(f"{index}: {value}")
```

### Zip creates tuples
```python
names = ['Alice', 'Bob']
ages = [25, 30]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### Sorting by tuple element
```python
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
students.sort(key=lambda x: x[1])  # Sort by grade
```

---

## Quick Reference

```python
# Create
t = ()            # Empty
t = (1,)          # Single element (comma!)
t = (1, 2, 3)     # Multiple elements
t = 1, 2, 3       # Without parentheses

# Access
t[0]              # First element
t[-1]             # Last element
t[1:3]            # Slice

# Methods
t.count(value)    # Count occurrences
t.index(value)    # Find position

# Operations
t1 + t2           # Concatenate
t * 3             # Repeat
x, y = t          # Unpack
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
