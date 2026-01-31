# Data Structures Cheatsheet

Quick reference for Python's built-in data structures: lists, tuples, dictionaries, sets, and their methods.

---

## Lists (Mutable, Ordered)

### Creating Lists
```python
# Empty list
my_list = []
my_list = list()

# With values
my_list = [1, 2, 3, 4, 5]
my_list = ["a", "b", "c"]
my_list = [1, "hello", 3.14, True]  # Mixed types

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

### List Methods (In-Place)
```python
my_list = [1, 2, 3]

# Add elements
my_list.append(4)        # [1, 2, 3, 4] - Add to end
my_list.insert(1, 5)    # [1, 5, 2, 3, 4] - Insert at index
my_list.extend([6, 7])   # [1, 5, 2, 3, 4, 6, 7] - Add iterable

# Remove elements
my_list.remove(2)        # Remove first occurrence of value
popped = my_list.pop()   # Remove and return last element
del my_list[0]           # Remove by index
my_list.clear()          # Remove all elements: []

# Modify elements
my_list[0] = 10          # [10, 5, 3, 4, 6]
my_list.sort()           # Sort in place: [3, 4, 5, 6, 10]
my_list.reverse()        # Reverse in place
```

### List Operations
```python
my_list = [1, 2, 3, 4, 5]

# Access (zero-indexed)
my_list[0]              # 1
my_list[-1]             # 5 (last element)
my_list[1:4]            # [2, 3, 4] (slice)
my_list[::2]            # [1, 3, 5] (every 2nd)
my_list[::-1]           # [5, 4, 3, 2, 1] (reverse)

# Length
len(my_list)            # 5

# Check membership
3 in my_list            # True
10 in my_list           # False

# Count and index
my_list.count(2)        # 1
my_list.index(3)        # 2

# Sort (returns new list)
sorted([3, 1, 2])       # [1, 2, 3]

# Concatenation
[1, 2] + [3, 4]        # [1, 2, 3, 4]
[1] * 3                 # [1, 1, 1]
```

---

## Tuples (Immutable, Ordered)

### Creating Tuples
```python
# Empty tuple
my_tuple = ()
my_tuple = tuple()

# With values
my_tuple = (1, 2, 3)
my_tuple = 1, 2, 3      # Parentheses optional

# Single element (need comma)
my_tuple = (1,)         # Correct
my_tuple = (1)          # This is just int 1

# From list
my_tuple = tuple([1, 2, 3])

# Tuple comprehension (using generator)
my_tuple = tuple(x for x in range(5))  # (0, 1, 2, 3, 4)
```

### Tuple Operations
```python
my_tuple = (1, 2, 3, 4, 5)

# Access (same as list)
my_tuple[0]             # 1
my_tuple[1:4]           # (2, 3, 4)
my_tuple[::-1]          # (5, 4, 3, 2, 1)

# Length
len(my_tuple)           # 5

# Count and index
my_tuple.count(2)       # 1
my_tuple.index(3)       # 2

# Check membership
3 in my_tuple          # True

# Concatenation
(1, 2) + (3, 4)        # (1, 2, 3, 4)
(1,) * 3                # (1, 1, 1)

# Unpacking
a, b, c = (1, 2, 3)    # a=1, b=2, c=3
first, *rest = (1, 2, 3, 4)  # first=1, rest=[2, 3, 4]

# Named tuples (from collections)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)         # p.x=1, p.y=2
```

---

## Dictionaries (Mutable, Key-Value)

### Creating Dictionaries
```python
# Empty dict
my_dict = {}
my_dict = dict()

# With key-value pairs
my_dict = {"name": "Alice", "age": 25, "city": "NYC"}
my_dict = {1: "one", 2: "two", 3: "three"}

# From key-value pairs
my_dict = dict([("name", "Bob"), ("age", 30)])

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Default values (from collections)
from collections import defaultdict
dd = defaultdict(int)
dd["key"] += 1        # No KeyError, starts at 0
```

### Dictionary Methods
```python
my_dict = {"name": "Alice", "age": 25}

# Access values
my_dict["name"]              # "Alice" (KeyError if not found)
my_dict.get("name")         # "Alice" (None if not found)
my_dict.get("city", "NYC")  # "NYC" (default if not found)

# Add/Update
my_dict["city"] = "NYC"     # Add or update
my_dict.update({"age": 26, "job": "Engineer"})

# Remove
del my_dict["age"]          # Remove by key (KeyError if not found)
my_dict.pop("age", None)    # Remove and return (None if not found)
my_dict.popitem()           # Remove and return last inserted (Python 3.7+)
my_dict.clear()             # Remove all items: {}

# Keys, values, items
my_dict.keys()              # View of keys: dict_keys(['name', 'city'])
my_dict.values()            # View of values: dict_values(['Alice', 'NYC'])
my_dict.items()             # View of key-value pairs: dict_items([...])

# Check membership
"name" in my_dict           # True
"Alice" in my_dict          # False (checks keys, not values)

# Length
len(my_dict)                # 2

# Iterate
for key in my_dict:
    pass                    # Iterate over keys
for key, value in my_dict.items():
    pass                    # Iterate over key-value pairs
```

---

## Sets (Mutable, Unique, Unordered)

### Creating Sets
```python
# Empty set
my_set = set()            # Note: {} creates empty dict

# With values
my_set = {1, 2, 3, 4, 5}
my_set = {"a", "b", "c"}  # Order not guaranteed

# From list (removes duplicates)
my_set = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Set comprehension
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
```

### Set Methods
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Add/Remove
set1.add(5)               # {1, 2, 3, 4, 5}
set1.update([6, 7])       # {1, 2, 3, 4, 5, 6, 7}
set1.remove(1)            # Remove element (KeyError if not found)
set1.discard(1)           # Remove element (no error if not found)
set1.pop()                # Remove and return arbitrary element
set1.clear()              # Remove all elements: set()

# Length
len(set1)                 # 7

# Check membership
3 in set1                 # True

# Set operations (return new sets)
set1 | set2               # Union: {1, 2, 3, 4, 5, 6}
set1 & set2               # Intersection: {3, 4}
set1 - set2               # Difference: {1, 2}
set1 ^ set2               # Symmetric difference: {1, 2, 5, 6}

# In-place operations
set1 |= set2              # set1 = set1 | set2
set1 &= set2              # set1 = set1 & set2
set1 -= set2              # set1 = set1 - set2
set1 ^= set2              # set1 = set1 ^ set2

# Comparisons
set1 <= set2              # True if set1 is subset of set2
set1 < set2               # True if set1 is proper subset
set1 >= set2              # True if set1 is superset of set2
set1 > set2               # True if set1 is proper superset
set1.isdisjoint(set2)     # True if no common elements
```

---

## Frozensets (Immutable Sets)

```python
# Create
my_frozenset = frozenset([1, 2, 3, 4])

# Operations (same as set, but no methods that modify)
my_frozenset & {2, 3, 5}  # frozenset({2, 3})
len(my_frozenset)         # 4
1 in my_frozenset         # True

# No add/remove/update methods (immutable)
```

---

## Comparison Table

| Feature | List | Tuple | Dict | Set |
|---------|------|-------|------|-----|
| **Mutable?** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Ordered?** | ✅ Yes | ✅ Yes | ✅ Yes (3.7+) | ❌ No |
| **Dups?** | ✅ Yes | ✅ Yes | ✅ Keys only | ❌ No |
| **Index?** | ✅ Yes | ✅ Yes | ❌ No (by key) | ❌ No |
| **Syntax** | `[1, 2]` | `(1, 2)` | `{"k": v}` | `{1, 2}` |
| **Empty** | `[]` | `()` | `{}` | `set()` |

---

## Common Patterns

### Stack (LIFO)
```python
stack = []

# Push
stack.append(1)
stack.append(2)     # [1, 2]

# Pop
item = stack.pop()  # Returns 2, stack = [1]
```

### Queue (FIFO)
```python
from collections import deque

queue = deque()

# Enqueue
queue.append(1)
queue.append(2)     # deque([1, 2])

# Dequeue
item = queue.popleft()  # Returns 1, deque([2])
```

### Counter (Frequency)
```python
from collections import Counter

counts = Counter([1, 1, 2, 2, 2, 3])
# Counter({2: 3, 1: 2, 3: 1})

counts.most_common(2)   # [(2, 3), (1, 2)]
```

### Default Dictionary
```python
from collections import defaultdict

dd = defaultdict(list)
dd["key"].append(1)
dd["key"].append(2)     # {"key": [1, 2]}
```

### Group by Key
```python
from collections import defaultdict

items = [("a", 1), ("b", 2), ("a", 3)]
grouped = defaultdict(list)

for key, value in items:
    grouped[key].append(value)
# {"a": [1, 3], "b": [2]}
```

---

## Performance Reference

| Operation | List | Tuple | Dict | Set |
|-----------|------|-------|------|-----|
| **Access by index** | O(1) | O(1) | - | - |
| **Access by key** | - | - | O(1) | - |
| **Search** | O(n) | O(n) | - | O(1) |
| **Append/Insert** | O(1)* | - | O(1) | O(1) |
| **Delete** | O(n)* | - | O(1) | O(1) |

*List append is O(1), but insert/pop(0) is O(n)

---

## Quick Reference

### List Methods
- `append(x)`, `extend(iter)`, `insert(i, x)`
- `remove(x)`, `pop(i)`, `clear()`
- `index(x)`, `count(x)`, `sort()`, `reverse()`

### Tuple Methods
- `index(x)`, `count(x)`

### Dict Methods
- `get(k, d)`, `keys()`, `values()`, `items()`
- `pop(k, d)`, `popitem()`, `clear()`
- `update(other)`

### Set Methods
- `add(x)`, `remove(x)`, `discard(x)`
- `union()`, `intersection()`, `difference()`
- `issubset()`, `issuperset()`, `isdisjoint()`

---

**Back to [Resources](../README.md)**
