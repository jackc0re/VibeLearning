"""
Hash Tables - Exercises
=======================
"""

print("=" * 50)
print("HASH TABLES - Exercises")
print("=" * 50)

# EXERCISE 1: Implement delete method
# EXERCISE 2: Implement contains method

# SOLUTIONS
print("\n--- Solutions ---")

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
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
    
    def contains(self, key):
        return self.get(key) is not None

ht = HashTable()
ht.set("a", 1)
ht.set("b", 2)
print(f"Contains 'a': {ht.contains('a')}")
print(f"Contains 'x': {ht.contains('x')}")
ht.delete("a")
print(f"After delete, contains 'a': {ht.contains('a')}")

print("\n" + "=" * 50)
print("Congratulations! Module 02 complete!")
print("=" * 50)
