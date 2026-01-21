"""
Hash Tables - Examples
======================
"""

print("=" * 50)
print("HASH TABLES - Examples")
print("=" * 50)

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
    
    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"  [{i}]: {bucket}")

print("\n--- Custom Hash Table ---")
ht = HashTable(5)
ht.set("apple", 1)
ht.set("banana", 2)
ht.set("cherry", 3)
ht.set("date", 4)

print("Hash table contents:")
ht.display()

print(f"\nGet 'apple': {ht.get('apple')}")
print(f"Get 'cherry': {ht.get('cherry')}")

print("\n--- Python Dict (Hash Table) ---")
d = {"a": 1, "b": 2, "c": 3}
print(f"d['a']: {d['a']}  # O(1) lookup")

print("\n" + "=" * 50)
print("Examples complete!")
print("=" * 50)
