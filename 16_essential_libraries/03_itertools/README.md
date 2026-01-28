# 🔄 Itertools Module

> **Iterator tools for efficient looping and combinatorics**

---

## 🎯 Learning Objectives

By the end of this section, you'll understand:
- How to create infinite iterators
- How to combine multiple iterables efficiently
- How to filter and slice iterators
- Combinatoric generators for permutations and combinations

---

## 🔁 Infinite Iterators

These iterators never stop - use with `islice` or a break condition!

### count() - Counting indefinitely

```python
from itertools import count

# Start at 10, step by 2
for i in count(10, 2):
    if i > 20:
        break
    print(i)  # 10, 12, 14, 16, 18, 20
```

### cycle() - Repeating a sequence

```python
from itertools import cycle

colors = cycle(['red', 'green', 'blue'])
for _ in range(5):
    print(next(colors))  # red, green, blue, red, green
```

### repeat() - Repeat a value

```python
from itertools import repeat

# Repeat 'hello' 3 times
list(repeat('hello', 3))  # ['hello', 'hello', 'hello']
```

---

## 🔀 Combinatoric Iterators

### permutations() - All possible orderings

```python
from itertools import permutations

# All 2-item permutations
list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

### combinations() - All unique combinations

```python
from itertools import combinations

# All 2-item combinations (order doesn't matter)
list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]
```

### product() - Cartesian product

```python
from itertools import product

# All combinations from multiple iterables
list(product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

---

## ⛓️ Combining Iterators

### chain() - Concatenate iterables

```python
from itertools import chain

# Flatten multiple lists
list(chain([1, 2], [3, 4], [5, 6]))
# [1, 2, 3, 4, 5, 6]

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
list(chain.from_iterable(nested))
# [1, 2, 3, 4, 5, 6]
```

### zip_longest() - Zip with fill value

```python
from itertools import zip_longest

names = ['Alice', 'Bob']
scores = [95, 87, 92]

# Regular zip stops at shortest
list(zip(names, scores))  # [('Alice', 95), ('Bob', 87)]

# zip_longest fills the rest
list(zip_longest(names, scores, fillvalue='N/A'))
# [('Alice', 95), ('Bob', 87), ('N/A', 92)]
```

---

## ✂️ Filtering and Slicing

### islice() - Slice an iterator

```python
from itertools import islice

# Get first 5 items from an infinite iterator
from itertools import count
first_five = list(islice(count(10), 5))
# [10, 11, 12, 13, 14]

# Get items 3-7
list(islice(range(20), 3, 8))
# [3, 4, 5, 6, 7]
```

### compress() - Filter using a selector

```python
from itertools import compress

data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, True, False, True]

list(compress(data, selectors))
# ['a', 'c', 'e']
```

### takewhile() and dropwhile()

```python
from itertools import takewhile, dropwhile

numbers = [1, 2, 3, 4, 5, 1, 2]

# Take while condition is true
list(takewhile(lambda x: x < 4, numbers))
# [1, 2, 3]

# Drop while condition is true, then take rest
list(dropwhile(lambda x: x < 4, numbers))
# [4, 5, 1, 2]
```

---

## 🗂️ Grouping

### groupby() - Group consecutive equal elements

```python
from itertools import groupby

# Note: Input must be sorted for meaningful groups!
data = ['A', 'A', 'B', 'B', 'B', 'A', 'C']

for key, group in groupby(data):
    print(f"{key}: {list(group)}")
# A: ['A', 'A']
# B: ['B', 'B', 'B']
# A: ['A']
# C: ['C']
```

With a key function:
```python
data = [('Alice', 25), ('Bob', 25), ('Carol', 30)]
data.sort(key=lambda x: x[1])  # Sort by age

for age, group in groupby(data, key=lambda x: x[1]):
    print(f"Age {age}: {[name for name, _ in group]}")
```

---

## ⚠️ Common Mistakes

1. **Forgetting to sort before groupby** - `groupby` only groups consecutive items
2. **Infinite loops with infinite iterators** - Always use `islice` or break
3. **Consuming iterators** - Remember, most itertools return iterators, not lists
4. **Modifying while iterating** - Don't change the source during iteration

---

## 📝 Quick Reference

```python
from itertools import (
    count, cycle, repeat,           # Infinite
    permutations, combinations,     # Combinatoric
    product, chain, zip_longest,    # Combining
    islice, compress,               # Filtering
    takewhile, dropwhile, groupby   # Conditional
)

# Most common patterns
list(islice(count(1), 10))                    # First 10 numbers
list(chain(*nested_lists))                    # Flatten
list(zip_longest(a, b, fillvalue=0))          # Unequal lengths
list(combinations(items, 2))                  # Pairs
```

---

## 🎓 Next Steps

Run `examples.py` to see itertools in action, then try `exercises.py`!
