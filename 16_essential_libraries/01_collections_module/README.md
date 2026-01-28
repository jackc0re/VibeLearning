# 📊 Collections Module

> **Specialized container datatypes for every need**

---

## 🎯 Learning Objectives

By the end of this section, you'll understand:
- What `Counter` is and how to count elements efficiently
- How `defaultdict` eliminates KeyError checks
- When to use `namedtuple` for readable, lightweight objects
- Why `deque` is superior for queue operations

---

## 🔢 Counter - Counting Made Easy

Think of `Counter` as a smart dictionary that automatically counts things for you.

### Real-World Analogy

Imagine you're tallying votes. Instead of checking "have I seen this candidate before?" every time, `Counter` just handles it:

```python
from collections import Counter

# Count letters in a word
letters = Counter("banana")
print(letters)  # Counter({'a': 3, 'n': 2, 'b': 1})

# Most common elements
print(letters.most_common(2))  # [('a', 3), ('n', 2)]
```

### Key Features

| Method | Description |
|--------|-------------|
| `Counter(iterable)` | Create a counter from any iterable |
| `.most_common(n)` | Get the n most common elements |
| `.elements()` | Expand back to individual elements |
| `+`, `-` | Combine counters with arithmetic |

---

## 🗝️ defaultdict - Never Get KeyError Again

A `defaultdict` automatically creates a default value for missing keys.

### Real-World Analogy

It's like having a vending machine that dispenses an empty box if you press a button for something that doesn't exist — instead of crashing.

```python
from collections import defaultdict

# Group words by length
words = ["cat", "dog", "elephant", "bird", "fish"]
by_length = defaultdict(list)

for word in words:
    by_length[len(word)].append(word)

print(dict(by_length))
# {3: ['cat', 'dog'], 8: ['elephant'], 4: ['bird'], 4: ['fish']}
```

### Common Default Factory Functions

```python
defaultdict(int)      # Starts at 0
defaultdict(list)     # Starts with []
defaultdict(set)      # Starts with set()
defaultdict(dict)     # Starts with {}
```

---

## 🏷️ namedtuple - Self-Documenting Tuples

`namedtuple` creates tuple-like objects with named fields.

### Real-World Analogy

A regular tuple is like a row in a spreadsheet with no headers. A namedtuple adds the headers so you know what each column means.

```python
from collections import namedtuple

# Define a Point class
Point = namedtuple('Point', ['x', 'y'])

p = Point(3, 4)
print(p.x, p.y)      # 3 4
print(p[0], p[1])    # 3 4 (also works as tuple)
```

### Benefits

- **Immutable** - Like regular tuples
- **Named access** - `p.x` instead of `p[0]`
- **Unpackable** - `x, y = p`
- **Memory efficient** - Faster than regular classes

---

## 🔄 deque - Double-Ended Queue

`deque` (pronounced "deck") is a list optimized for operations at both ends.

### Real-World Analogy

Imagine a line of people where you can efficiently add or remove people from either the front OR the back. With a regular list, adding/removing from the front is slow.

```python
from collections import deque

# Create a deque
d = deque([1, 2, 3])

# Fast operations at both ends
d.appendleft(0)      # [0, 1, 2, 3]
d.append(4)          # [0, 1, 2, 3, 4]
d.popleft()          # Returns 0
```

### Performance Comparison

| Operation | List | Deque |
|-----------|------|-------|
| Append right | O(1) | O(1) |
| Append left | O(n) | O(1) |
| Pop right | O(1) | O(1) |
| Pop left | O(n) | O(1) |

Use `deque` for:
- Queues (FIFO)
- Stacks (LIFO)
- Sliding window algorithms
- Maintaining recent history

---

## ⚠️ Common Mistakes

1. **Modifying Counter directly** - Use `update()` for adding counts
2. **Forgetting to import** - These are in `collections`, not built-in
3. **Using list as default** - Use `list` function, not `[]`
4. **Mutable defaults in namedtuple** - Fields should be immutable

---

## 📝 Quick Reference

```python
from collections import Counter, defaultdict, namedtuple, deque

# Counter
c = Counter(['a', 'b', 'a', 'c', 'a'])
c.most_common(1)  # [('a', 3)]

# defaultdict
d = defaultdict(list)
d['missing']  # Returns [], no KeyError

# namedtuple
Person = namedtuple('Person', 'name age')
p = Person('Alice', 30)

# deque
dq = deque(maxlen=3)  # Fixed size, auto-discards old items
dq.extend([1, 2, 3, 4])  # Only keeps [2, 3, 4]
```

---

## 🎓 Next Steps

Run `examples.py` to see these in action, then try `exercises.py`!
