"""
Sets - Examples
===============
Run this file to see sets in action!
"""

print("=" * 50)
print("SETS - Examples")
print("=" * 50)

# =============================================================================
# CREATING SETS
# =============================================================================
print("\n--- Creating Sets ---\n")

# Empty set
empty = set()  # NOT {} which creates a dict!
print(f"Empty set: {empty}")

# Set with values
fruits = {"apple", "banana", "cherry"}
print(f"Fruits: {fruits}")

# Duplicates are removed
duplicates = {1, 2, 2, 3, 3, 3}
print(f"Set with duplicates removed: {duplicates}")

# From string (each character is an element)
letters = set("mississippi")
print(f"Letters in 'mississippi': {letters}")

# From list
numbers = set([1, 2, 3, 4, 5])
print(f"From list: {numbers}")

# Set comprehension
squares = {x**2 for x in range(1, 6)}
print(f"Squares 1-5: {squares}")

# =============================================================================
# SET OPERATIONS
# =============================================================================
print("\n--- Set Operations ---\n")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"Set A: {a}")
print(f"Set B: {b}")

# Union
print(f"\nUnion (A | B): {a | b}")
print(f"Union (A.union(B)): {a.union(b)}")

# Intersection
print(f"\nIntersection (A & B): {a & b}")
print(f"Intersection (A.intersection(B)): {a.intersection(b)}")

# Difference
print(f"\nDifference (A - B): {a - b}")
print(f"Difference (B - A): {b - a}")

# Symmetric difference
print(f"\nSymmetric difference (A ^ B): {a ^ b}")

# =============================================================================
# MODIFYING SETS
# =============================================================================
print("\n--- Modifying Sets ---\n")

s = {1, 2, 3}
print(f"Original: {s}")

# Add single element
s.add(4)
print(f"After add(4): {s}")

# Adding duplicate has no effect
s.add(4)
print(f"After add(4) again: {s}")

# Add multiple elements
s.update([5, 6, 7])
print(f"After update([5, 6, 7]): {s}")

# Remove element
s.remove(7)
print(f"After remove(7): {s}")

# Discard (no error if not found)
s.discard(99)
print(f"After discard(99): {s}")

# Pop (removes and returns arbitrary element)
popped = s.pop()
print(f"Popped {popped}, set now: {s}")

# =============================================================================
# CHECKING MEMBERSHIP
# =============================================================================
print("\n--- Checking Membership ---\n")

fruits = {"apple", "banana", "cherry"}

print(f"Set: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")

# Subset/Superset
small = {1, 2}
large = {1, 2, 3, 4}

print(f"\nsmall = {small}")
print(f"large = {large}")
print(f"small.issubset(large): {small.issubset(large)}")
print(f"large.issuperset(small): {large.issuperset(small)}")
print(f"small < large (proper subset): {small < large}")

# Disjoint
x = {1, 2}
y = {3, 4}
z = {2, 3}

print(f"\nx = {x}, y = {y}, z = {z}")
print(f"x.isdisjoint(y): {x.isdisjoint(y)}")  # No common elements
print(f"x.isdisjoint(z): {x.isdisjoint(z)}")  # Has common element 2

# =============================================================================
# COMMON USE CASES
# =============================================================================
print("\n--- Common Use Cases ---\n")

# Remove duplicates
items = [1, 3, 2, 3, 1, 4, 2, 5]
unique = list(set(items))
print(f"Original list: {items}")
print(f"Unique (via set): {unique}")

# Keep order while removing duplicates
unique_ordered = list(dict.fromkeys(items))
print(f"Unique (keeping order): {unique_ordered}")

# Find common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"\nCommon elements: {common}")

# Find unique to each list
only_in_list1 = set(list1) - set(list2)
only_in_list2 = set(list2) - set(list1)
print(f"Only in list1: {only_in_list1}")
print(f"Only in list2: {only_in_list2}")

# Check for duplicates
def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(f"\n[1, 2, 3, 2] has duplicates: {has_duplicates([1, 2, 3, 2])}")
print(f"[1, 2, 3, 4] has duplicates: {has_duplicates([1, 2, 3, 4])}")

# =============================================================================
# FROZEN SETS
# =============================================================================
print("\n--- Frozen Sets ---\n")

# Frozen set is immutable
fs = frozenset([1, 2, 3])
print(f"Frozen set: {fs}")

# Can use frozen sets as dictionary keys
cache = {
    frozenset(["a", "b"]): "value1",
    frozenset(["c", "d"]): "value2"
}
print(f"Cache with frozenset keys: {cache}")

# Can have frozen sets inside regular sets
nested = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozensets: {nested}")

# =============================================================================
# PERFORMANCE COMPARISON
# =============================================================================
print("\n--- Performance Comparison ---\n")

import time

# Create large list and set
size = 100000
large_list = list(range(size))
large_set = set(range(size))

# Time list lookup
start = time.time()
for _ in range(1000):
    size - 1 in large_list
list_time = time.time() - start

# Time set lookup
start = time.time()
for _ in range(1000):
    size - 1 in large_set
set_time = time.time() - start

print(f"1000 lookups in list of {size:,} items: {list_time:.4f}s")
print(f"1000 lookups in set of {size:,} items: {set_time:.4f}s")
print(f"Set is {list_time/set_time:.0f}x faster!")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
