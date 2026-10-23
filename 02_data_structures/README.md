# 📊 Module 02: Data Structures

Learn how to organize and store data efficiently. From Python's built-in collections to classic computer science structures.

---

## What's in This Module

| Topic | Description |
|-------|-------------|
| [01_lists_arrays](01_lists_arrays/README.md) | Ordered, mutable collections |
| [02_strings](02_strings/README.md) | Text manipulation deep-dive |
| [03_dictionaries_maps](03_dictionaries_maps/README.md) | Key-value data storage |
| [04_sets](04_sets/README.md) | Unique, unordered collections |
| [05_tuples](05_tuples/README.md) | Immutable sequences |
| [06_stacks_queues](06_stacks_queues/README.md) | LIFO and FIFO structures |
| [07_linked_lists](07_linked_lists/README.md) | Node-based linear structures |
| [08_trees](08_trees/README.md) | Hierarchical data organization |
| [09_graphs](09_graphs/README.md) | Network-like connections |
| [10_hash_tables](10_hash_tables/README.md) | Fast key lookups explained |

---

## Learning Objectives

By the end of this module, you will:

- ✅ Master Python's built-in data structures (lists, dicts, sets, tuples)
- ✅ Understand when to use each data structure
- ✅ Implement classic structures from scratch (linked lists, trees)
- ✅ Analyze time complexity of common operations
- ✅ Choose the right structure for different problems

---

## Time Estimate

⏱️ **12-15 hours** total for this module

| Topic | Time |
|-------|------|
| Lists & Arrays | 1-2 hours |
| Strings | 1 hour |
| Dictionaries | 1-2 hours |
| Sets | 1 hour |
| Tuples | 30 min |
| Stacks & Queues | 1-2 hours |
| Linked Lists | 2 hours |
| Trees | 2-3 hours |
| Graphs | 2-3 hours |
| Hash Tables | 1-2 hours |

---

## Prerequisites

- Complete [01_foundations](../01_foundations/README.md)
- Comfortable with variables, loops, and functions

---

## Key Concepts Preview

### Lists — Ordered, Mutable
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")      # Add to end
fruits[0] = "apricot"      # Modify by index
```

### Dictionaries — Key-Value Pairs
```python
person = {"name": "Alice", "age": 25}
person["city"] = "NYC"     # Add new key
print(person["name"])      # Access by key
```

### Sets — Unique Elements
```python
unique = {1, 2, 3, 3, 3}   # {1, 2, 3}
a = {1, 2}
b = {2, 3}
print(a | b)               # Union: {1, 2, 3}
```

### Choosing the Right Structure

| Need | Use |
|------|-----|
| Ordered collection, duplicates OK | `list` |
| Fast key lookups | `dict` |
| Unique elements only | `set` |
| Immutable sequence | `tuple` |
| Last-in-first-out | Stack (list) |
| First-in-first-out | Queue (deque) |

---

## Start Learning!

Begin with **[01_lists_arrays](01_lists_arrays/README.md)** — the most versatile built-in structure.
