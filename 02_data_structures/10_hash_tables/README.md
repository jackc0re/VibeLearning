# 🗄️ Hash Tables

The data structure behind Python dictionaries — enabling **O(1) average** lookups.

---

## How Hash Tables Work

1. **Hash Function**: Converts key → integer (hash code)
2. **Index Calculation**: hash code % table_size = bucket index
3. **Storage**: Value stored at calculated index

```
key "apple" → hash() → 12345 → 12345 % 10 = 5 → store at index 5
```

---

## Collision Handling

When two keys hash to same index:

### Chaining
Each bucket holds a list of key-value pairs.
```
Index 5: [("apple", 1), ("orange", 2)]
```

### Open Addressing
Find next empty slot (linear/quadratic probing).

---

## Simple Implementation

> 💡 **First time seeing `class`?** Start with the [10-line primer in Stacks and Queues](../06_stacks_queues/README.md#stack-class-implementation) - a class is a blueprint, `__init__` sets it up, `self` is the instance. Full treatment in [Module 04](../../04_oop_concepts/01_classes_and_objects/README.md).

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def set(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def get(self, key):
        """Return the value stored under key, or None if the key is missing."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
```

> 💡 **The `get()` contract:** a missing key returns `None` in this implementation -
> it does not raise. `exercises.py` uses the same contract, so the two files behave
> identically. It is a design decision worth making on purpose: a `None` return reads
> easily (`if value is None:`) but cannot tell "not stored" from "stored as None". Python's
> own `dict` does both - `d[key]` raises `KeyError`, `d.get(key)` returns `None`.

---

## Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Lookup | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case when all keys collide (rare with good hash function).

---

## Python's dict

Python dictionaries ARE hash tables!

```python
d = {"key": "value"}  # Hash table behind the scenes
d["key"]              # O(1) lookup
```

---

## Common Mistakes

### 1. Using a mutable key
```python
table = {}
table[[1, 2]] = "pair"     # ❌ TypeError: unhashable type: 'list'

# ✅ Keys must be hashable: str, int, tuple of immutables
table[(1, 2)] = "pair"
```
A key's hash must never change - if it did, the value would be filed under an index nobody
looks at again. Lists and dicts are mutable, so they cannot be keys.

### 2. Assuming the entries come out in a particular order
```python
d = {"b": 1, "a": 2, "c": 3}
for key in d:
    print(key)             # ❌ do not rely on this being sorted

# ✅ Sort when order matters
for key in sorted(d):
    print(key)             # a, b, c
```
Python dicts keep *insertion* order (3.7+), not sorted order, and a hand-written hash table
does not even promise that - two keys that collide sit in the same bucket in whatever order
they were inserted.

### 3. Forgetting how `get()` reports a missing key
```python
table = HashTable()
table.get("missing")       # None - no exception (see the contract note above)

# ✅ Check the result before using it
value = table.get("missing")
if value is None:
    print("not stored")
```

---

## Quick Reference

```python
# Python's dict is a hash table
d = {"apple": 1}
d["apple"]             # O(1) average lookup
d.get("pear")          # None instead of KeyError
d.get("pear", 0)       # 0 - your own default

d["cherry"] = 3        # insert or update
"apple" in d           # O(1) membership test
del d["apple"]

# Keys must be hashable (immutable)
hash("apple")          # an int
hash((1, 2))           # a tuple of immutables is fine
hash([1, 2])           # ❌ TypeError: lists are mutable
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
