# 📋 Lists and Arrays

Lists are Python's most versatile data structure — ordered, mutable collections that can hold any type of data.

---

## What is a List?

Think of a list as a **numbered container** where you can store multiple items in order.

```python
# Creating a list is like making a shopping list
shopping = ["milk", "eggs", "bread"]
#              0       1       2      <- index positions
```

---

## Creating Lists

```python
# Empty list
empty = []
empty = list()

# List with items
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "hello", 3.14, True]  # Different types OK!

# List from other iterables
letters = list("hello")  # ['h', 'e', 'l', 'l', 'o']
nums = list(range(5))    # [0, 1, 2, 3, 4]
```

---

## Accessing Elements

### Indexing (Single Element)
```python
fruits = ["apple", "banana", "cherry", "date"]

# Positive indexing (from start)
print(fruits[0])   # "apple" (first)
print(fruits[1])   # "banana" (second)

# Negative indexing (from end)
print(fruits[-1])  # "date" (last)
print(fruits[-2])  # "cherry" (second to last)
```

### Slicing (Multiple Elements)
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# [start:end] - end is exclusive!
print(fruits[1:3])   # ["banana", "cherry"]
print(fruits[:3])    # ["apple", "banana", "cherry"]
print(fruits[2:])    # ["cherry", "date", "elderberry"]
print(fruits[::2])   # ["apple", "cherry", "elderberry"] (every 2nd)
print(fruits[::-1])  # Reversed list
```

---

## Modifying Lists

### Changing Elements
```python
colors = ["red", "green", "blue"]
colors[1] = "yellow"  # ["red", "yellow", "blue"]
```

### Adding Elements
```python
nums = [1, 2, 3]

nums.append(4)        # [1, 2, 3, 4] - add to end
nums.insert(0, 0)     # [0, 1, 2, 3, 4] - insert at index
nums.extend([5, 6])   # [0, 1, 2, 3, 4, 5, 6] - add multiple
```

### Removing Elements
```python
letters = ['a', 'b', 'c', 'd', 'e']

letters.pop()         # Removes and returns 'e'
letters.pop(0)        # Removes and returns 'a'
letters.remove('c')   # Removes first 'c' found
del letters[0]        # Delete by index
letters.clear()       # Remove all: []
```

---

## Common List Methods

| Method | Description | Example |
|--------|-------------|---------|
| `append(x)` | Add to end | `[1,2].append(3)` → `[1,2,3]` |
| `insert(i, x)` | Insert at index | `[1,3].insert(1, 2)` → `[1,2,3]` |
| `extend(list)` | Add multiple | `[1].extend([2,3])` → `[1,2,3]` |
| `pop(i)` | Remove & return | `[1,2,3].pop()` → `3` |
| `remove(x)` | Remove first x | `[1,2,2].remove(2)` → `[1,2]` |
| `index(x)` | Find position | `[1,2,3].index(2)` → `1` |
| `count(x)` | Count occurrences | `[1,1,2].count(1)` → `2` |
| `sort()` | Sort in place | `[3,1,2].sort()` → `[1,2,3]` |
| `reverse()` | Reverse in place | `[1,2,3].reverse()` → `[3,2,1]` |
| `copy()` | Shallow copy | `new = old.copy()` |

---

## List Comprehensions

A concise way to create lists:

```python
# Traditional way
squares = []
for x in range(5):
    squares.append(x ** 2)
# [0, 1, 4, 9, 16]

# List comprehension
squares = [x ** 2 for x in range(5)]
# [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transform strings
words = ["hello", "world"]
upper = [w.upper() for w in words]
# ["HELLO", "WORLD"]
```

---

## Nested Lists (2D Arrays)

```python
# Matrix / grid
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access: matrix[row][column]
print(matrix[0][0])  # 1 (top-left)
print(matrix[1][2])  # 6 (row 1, column 2)

# Loop through all elements
for row in matrix:
    for item in row:
        print(item, end=" ")
# 1 2 3 4 5 6 7 8 9
```

---

## Common Patterns

### Find min/max
```python
nums = [5, 2, 8, 1, 9]
print(min(nums))  # 1
print(max(nums))  # 9
print(sum(nums))  # 25
```

### Check membership
```python
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)     # True
print("grape" not in fruits) # True
```

### Iterate with index
```python
colors = ["red", "green", "blue"]
for i, color in enumerate(colors):
    print(f"{i}: {color}")
# 0: red
# 1: green
# 2: blue
```

---

## Common Mistakes

### 1. Index out of range
```python
items = [1, 2, 3]
print(items[3])  # ❌ IndexError! (valid: 0, 1, 2)
```

### 2. Modifying while iterating
```python
nums = [1, 2, 3, 4, 5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)  # ❌ Dangerous! Skips elements

# ✅ Better: create new list
odds = [n for n in nums if n % 2 != 0]
```

### 3. Shallow vs deep copy
```python
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(original[0][0])  # 99! Inner list is shared

# ✅ Deep copy for nested structures
import copy
deep = copy.deepcopy(original)
```

---

## Lists vs Arrays

| Feature | Python List | Array (NumPy) |
|---------|-------------|---------------|
| Types | Mixed allowed | Single type only |
| Speed | Slower | Very fast |
| Memory | More | Less |
| Use case | General purpose | Math/science |

> 💡 **Note:** For everyday programming, Python lists are perfect. Use NumPy arrays when doing heavy numerical computing.

---

## Quick Reference

```python
# Create
my_list = [1, 2, 3]
empty = []

# Access
first = my_list[0]
last = my_list[-1]
subset = my_list[1:3]

# Modify
my_list.append(4)
my_list.insert(0, 0)
my_list.pop()
my_list.remove(2)

# Query
len(my_list)
2 in my_list
my_list.index(1)
my_list.count(1)

# Transform
my_list.sort()
my_list.reverse()
sorted_copy = sorted(my_list)
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
