# 🎯 Sets

Sets are unordered collections of **unique** elements — perfect for removing duplicates and mathematical set operations.

---

## What is a Set?

Think of a set like a **bag of unique marbles**: you can add items, but duplicates are automatically ignored.

```python
# Duplicates are removed automatically
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}
```

---

## Creating Sets

```python
# Empty set (NOT {} - that's an empty dict!)
empty = set()

# With initial values
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

# From other iterables
letters = set("hello")  # {'h', 'e', 'l', 'o'} - duplicates removed!
from_list = set([1, 2, 2, 3])  # {1, 2, 3}

# Set comprehension
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
```

> ⚠️ **Important:** `{}` creates an empty **dictionary**, not a set. Use `set()` for empty sets.

---

## Set Operations

### Mathematical Set Operations
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all elements from both)
a | b          # {1, 2, 3, 4, 5, 6}
a.union(b)     # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
a & b          # {3, 4}
a.intersection(b)

# Difference (in a but not b)
a - b          # {1, 2}
a.difference(b)

# Symmetric difference (in one but not both)
a ^ b          # {1, 2, 5, 6}
a.symmetric_difference(b)
```

### Visual Representation
```
Set A: {1, 2, 3, 4}
Set B: {3, 4, 5, 6}

Union (A | B):        {1, 2, 3, 4, 5, 6}  ← Everything
Intersection (A & B): {3, 4}              ← Only overlap
Difference (A - B):   {1, 2}              ← Only in A
Symmetric (A ^ B):    {1, 2, 5, 6}        ← Not in overlap
```

---

## Modifying Sets

```python
s = {1, 2, 3}

# Add single element
s.add(4)           # {1, 2, 3, 4}

# Add multiple elements
s.update([5, 6])   # {1, 2, 3, 4, 5, 6}

# Remove (raises error if not found)
s.remove(6)        # {1, 2, 3, 4, 5}
s.remove(99)       # ❌ KeyError!

# Discard (no error if not found)
s.discard(99)      # No error

# Pop (remove and return arbitrary element)
item = s.pop()

# Clear all
s.clear()          # set()
```

---

## Checking Membership

```python
fruits = {"apple", "banana", "cherry"}

# Check if element exists (very fast!)
"apple" in fruits      # True
"grape" in fruits      # False
"grape" not in fruits  # True

# Subset/Superset checks
a = {1, 2}
b = {1, 2, 3, 4}

a.issubset(b)      # True (a ⊆ b)
b.issuperset(a)    # True (b ⊇ a)
a < b              # True (proper subset)

# Disjoint (no common elements)
{1, 2}.isdisjoint({3, 4})  # True
{1, 2}.isdisjoint({2, 3})  # False
```

---

## Common Use Cases

### Remove Duplicates (Keep Order)
```python
items = [1, 3, 2, 3, 1, 4, 2]

# Using set (loses order)
unique_unordered = list(set(items))  # [1, 2, 3, 4] (order may vary)

# Keep original order (Python 3.7+)
unique_ordered = list(dict.fromkeys(items))  # [1, 3, 2, 4]
```

### Find Common Elements
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = set(list1) & set(list2)  # {4, 5}
```

### Check for Duplicates
```python
items = [1, 2, 3, 2]
has_duplicates = len(items) != len(set(items))  # True
```

### Filter List by Allowed Values
```python
allowed = {"admin", "user", "guest"}
roles = ["admin", "hacker", "user", "root"]

valid = [r for r in roles if r in allowed]  # ["admin", "user"]
```

---

## Frozen Sets (Immutable Sets)

```python
# Regular sets are mutable
s = {1, 2, 3}
s.add(4)  # Works

# Frozen sets are immutable
fs = frozenset([1, 2, 3])
fs.add(4)  # ❌ AttributeError

# Useful as dictionary keys or set elements
nested = {frozenset([1, 2]), frozenset([3, 4])}
```

---

## Performance

Sets use hash tables for O(1) average operations:

| Operation | Time Complexity |
|-----------|-----------------|
| Add | O(1) |
| Remove | O(1) |
| Check membership | O(1) |
| Union/Intersection | O(min(len(a), len(b))) |

This makes `in` checks much faster than lists:
```python
# For large collections:
my_list = list(range(10000))
my_set = set(range(10000))

9999 in my_list  # Slow: O(n)
9999 in my_set   # Fast: O(1)
```

---

## Common Mistakes

### 1. Empty set syntax
```python
empty = {}      # ❌ This is a dict!
empty = set()   # ✅ This is a set
```

### 2. Sets are unordered
```python
s = {3, 1, 2}
print(s)  # Order not guaranteed!

# If you need order, use a list
```

### 3. Mutable elements not allowed
```python
s = {[1, 2], [3, 4]}  # ❌ TypeError: list is unhashable

# Use tuples instead
s = {(1, 2), (3, 4)}  # ✅ Works
```

---

## Quick Reference

```python
# Create
s = set()
s = {1, 2, 3}
s = set([1, 2, 3])

# Add/Remove
s.add(item)
s.update([items])
s.remove(item)    # Error if missing
s.discard(item)   # No error

# Operations
a | b   # Union
a & b   # Intersection
a - b   # Difference
a ^ b   # Symmetric difference

# Checks
item in s
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
