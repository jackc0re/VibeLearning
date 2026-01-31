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
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        raise KeyError(key)
```

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

## Next Steps

Practice with [examples.py](examples.py)!
