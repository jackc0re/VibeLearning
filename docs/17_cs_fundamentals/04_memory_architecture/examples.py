"""
Memory Architecture - Examples
==============================
Exploring stack vs heap, references, and memory management.
"""

import sys

print("=" * 60)
print("MEMORY ARCHITECTURE - Examples")
print("=" * 60)

# =============================================================================
# MEMORY SIZES
# =============================================================================
print("\n--- Memory Sizes ---\n")

sizes = [
    ("1 Byte", 1),
    ("1 Kilobyte (KB)", 1024),
    ("1 Megabyte (MB)", 1024 ** 2),
    ("1 Gigabyte (GB)", 1024 ** 3),
]

for name, size in sizes:
    print(f"{name:20s} = {size:,} bytes")

# =============================================================================
# OBJECT IDS AND MEMORY ADDRESSES
# =============================================================================
print("\n" + "=" * 60)
print("OBJECT IDs AND MEMORY ADDRESSES")
print("=" * 60)

# Every object has a unique id (memory address in CPython)
x = 42
y = 42
z = x

print(f"\nx = 42, id(x) = {id(x)}")
print(f"y = 42, id(y) = {id(y)}")
print(f"z = x,  id(z) = {id(z)}")

# Python caches small integers!
print(f"\nx and y have same id? {id(x) == id(y)} (Python caches -5 to 256)")
print(f"x and z have same id? {id(x) == id(z)} (z references x)")

# Larger integers may have different ids
a = 1000
b = 1000
print(f"\nFor large integers (1000):")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"Same id? {id(a) == id(b)} (implementation dependent)")

# =============================================================================
# IS VS ==
# =============================================================================
print("\n" + "=" * 60)
print("IS VS ==")
print("=" * 60)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # Same reference

print(f"\nlist1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")

print(f"\nlist1 == list2: {list1 == list2}  (same values)")
print(f"list1 is list2: {list1 is list2}  (different objects)")
print(f"list1 is list3: {list1 is list3}  (same object)")

print(f"\nid(list1): {id(list1)}")
print(f"id(list2): {id(list2)}")
print(f"id(list3): {id(list3)}")

# =============================================================================
# MUTABLE VS IMMUTABLE
# =============================================================================
print("\n" + "=" * 60)
print("MUTABLE VS IMMUTABLE OBJECTS")
print("=" * 60)

print("\n--- Immutable: Integers ---")
x = 10
print(f"x = {x}, id = {id(x)}")
x = x + 1  # Creates a NEW integer!
print(f"x = {x}, id = {id(x)} (new object)")

print("\n--- Immutable: Strings ---")
s = "hello"
print(f"s = '{s}', id = {id(s)}")
s = s + " world"  # Creates a NEW string!
print(f"s = '{s}', id = {id(s)} (new object)")

print("\n--- Mutable: Lists ---")
lst = [1, 2, 3]
print(f"lst = {lst}, id = {id(lst)}")
lst.append(4)  # Modifies in place!
print(f"lst = {lst}, id = {id(lst)} (same object, modified)")

print("\n--- Mutable: Dictionaries ---")
d = {"a": 1}
print(f"d = {d}, id = {id(d)}")
d["b"] = 2  # Modifies in place!
print(f"d = {d}, id = {id(d)} (same object, modified)")

# =============================================================================
# OBJECT SIZES WITH SYS.GETSIZEOF
# =============================================================================
print("\n" + "=" * 60)
print("OBJECT SIZES")
print("=" * 60)

objects = [
    ("Integer 0", 0),
    ("Integer 42", 42),
    ("Integer 10**100", 10**100),
    ("Empty string", ""),
    ("String 'hello'", "hello"),
    ("Empty list", []),
    ("List [1, 2, 3]", [1, 2, 3]),
    ("Empty tuple", ()),
    ("Tuple (1, 2, 3)", (1, 2, 3)),
    ("Empty dict", {}),
    ("Dict {'a': 1}", {"a": 1}),
    ("Boolean True", True),
    ("None", None),
]

print(f"\n{'Object':<25s} {'Size (bytes)':<15s}")
print("-" * 40)
for name, obj in objects:
    size = sys.getsizeof(obj)
    print(f"{name:<25s} {size:<15d}")

# =============================================================================
# REFERENCE COUNTING
# =============================================================================
print("\n" + "=" * 60)
print("REFERENCE COUNTING")
print("=" * 60)

import ctypes

def ref_count(address):
    """Get the reference count of an object at given address."""
    return ctypes.c_long.from_address(address).value

# Create an object
my_list = [1, 2, 3]
list_id = id(my_list)

print(f"\nCreated my_list = [1, 2, 3]")
print(f"Reference count: {ref_count(list_id)}")

# Create another reference
another_ref = my_list
print(f"\nCreated another_ref = my_list")
print(f"Reference count: {ref_count(list_id)}")

# And another
yet_another = my_list
print(f"Created yet_another = my_list")
print(f"Reference count: {ref_count(list_id)}")

# Remove a reference
del another_ref
print(f"\nDeleted another_ref")
print(f"Reference count: {ref_count(list_id)}")

# Rebind
yet_another = None
print(f"Rebound yet_another to None")
print(f"Reference count: {ref_count(list_id)}")

print("\nNote: Reference count is for demonstration only.")
print("Python's memory management is automatic!")

# =============================================================================
# THE CALL STACK
# =============================================================================
print("\n" + "=" * 60)
print("THE CALL STACK")
print("=" * 60)

call_depth = 0

def function_a():
    global call_depth
    call_depth += 1
    print(f"  {'  ' * call_depth}→ Entering function_a (depth: {call_depth})")
    local_var_a = "I'm in A"
    print(f"  {'  ' * call_depth}  Local variable: {local_var_a}")
    function_b()
    print(f"  {'  ' * call_depth}← Leaving function_a (depth: {call_depth})")
    call_depth -= 1

def function_b():
    global call_depth
    call_depth += 1
    print(f"  {'  ' * call_depth}→ Entering function_b (depth: {call_depth})")
    local_var_b = "I'm in B"
    print(f"  {'  ' * call_depth}  Local variable: {local_var_b}")
    function_c()
    print(f"  {'  ' * call_depth}← Leaving function_b (depth: {call_depth})")
    call_depth -= 1

def function_c():
    global call_depth
    call_depth += 1
    print(f"  {'  ' * call_depth}→ Entering function_c (depth: {call_depth})")
    local_var_c = "I'm in C"
    print(f"  {'  ' * call_depth}  Local variable: {local_var_c}")
    print(f"  {'  ' * call_depth}  (C does its work)")
    print(f"  {'  ' * call_depth}← Leaving function_c (depth: {call_depth})")
    call_depth -= 1

print("\nFunction call trace:")
print("(Each level represents a stack frame)")
function_a()

# =============================================================================
# STACK OVERFLOW DEMONSTRATION (CAREFUL!)
# =============================================================================
print("\n" + "=" * 60)
print("RECURSION AND STACK")
print("=" * 60)

def count_down(n, limit=10):
    """A safe recursive function."""
    if n <= 0 or limit <= 0:
        return "Done!"
    print(f"  count_down({n}), remaining depth: {limit}")
    return count_down(n - 1, limit - 1)

print("\nSafe recursion (depth limited):")
result = count_down(5)
print(f"Result: {result}")

print("\nNote: Python has a default recursion limit (usually 1000)")
print("to prevent accidental stack overflows.")

# =============================================================================
# PASS BY REFERENCE DEMONSTRATION
# =============================================================================
print("\n" + "=" * 60)
print("PASS BY OBJECT REFERENCE")
print("=" * 60)

def demonstrate_mutable(lst):
    """Demonstrates mutable object modification."""
    print(f"  Inside function, before append:")
    print(f"    lst = {lst}, id = {id(lst)}")
    lst.append(4)
    print(f"  Inside function, after append:")
    print(f"    lst = {lst}, id = {id(lst)}")

def demonstrate_immutable(x):
    """Demonstrates immutable object rebinding."""
    print(f"  Inside function, before change:")
    print(f"    x = {x}, id = {id(x)}")
    x = x + 1
    print(f"  Inside function, after change:")
    print(f"    x = {x}, id = {id(x)}")

def demonstrate_rebinding(lst):
    """Demonstrates rebinding a variable."""
    print(f"  Inside function, before rebind:")
    print(f"    lst = {lst}, id = {id(lst)}")
    lst = [4, 5, 6]  # Creates a NEW list!
    print(f"  Inside function, after rebind:")
    print(f"    lst = {lst}, id = {id(lst)}")

print("\n--- Mutable Object (List) ---")
my_list = [1, 2, 3]
print(f"Before function: my_list = {my_list}, id = {id(my_list)}")
demonstrate_mutable(my_list)
print(f"After function: my_list = {my_list}")
print("  → Original was modified!")

print("\n--- Immutable Object (Integer) ---")
my_int = 5
print(f"Before function: my_int = {my_int}, id = {id(my_int)}")
demonstrate_immutable(my_int)
print(f"After function: my_int = {my_int}")
print("  → Original was NOT modified (immutable)")

print("\n--- Rebinding (List) ---")
my_list2 = [1, 2, 3]
print(f"Before function: my_list2 = {my_list2}, id = {id(my_list2)}")
demonstrate_rebinding(my_list2)
print(f"After function: my_list2 = {my_list2}")
print("  → Original unchanged (variable was rebound to new object)")

# =============================================================================
# SHALLOW VS DEEP COPY
# =============================================================================
print("\n" + "=" * 60)
print("SHALLOW VS DEEP COPY")
print("=" * 60)

import copy

# Original list with nested list
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow = original.copy()
# Or: shallow = original[:]
# Or: shallow = list(original)

# Deep copy
deep = copy.deepcopy(original)

print(f"\nOriginal: {original}")
print(f"Shallow:  {shallow}")
print(f"Deep:     {deep}")

print(f"\nModifying original[0][0] = 999")
original[0][0] = 999

print(f"\nOriginal: {original}")
print(f"Shallow:  {shallow}  (nested object modified!)")
print(f"Deep:     {deep}     (completely independent)")

print("\nWhy? Shallow copy copies references to nested objects.")
print("     Deep copy creates new copies of everything.")

# =============================================================================
# MEMORY EFFICIENCY TIPS
# =============================================================================
print("\n" + "=" * 60)
print("MEMORY EFFICIENCY COMPARISON")
print("=" * 60)

import time

print("\n--- List Concatenation vs Join ---")

# Method 1: String concatenation (bad)
start = time.time()
result = ""
for i in range(10000):
    result += str(i)
time_concat = time.time() - start

# Method 2: List join (good)
start = time.time()
parts = []
for i in range(10000):
    parts.append(str(i))
result = "".join(parts)
time_join = time.time() - start

# Method 3: Generator expression (best)
start = time.time()
result = "".join(str(i) for i in range(10000))
time_gen = time.time() - start

print(f"String concatenation: {time_concat:.4f} seconds")
print(f"List append + join:   {time_join:.4f} seconds")
print(f"Generator + join:     {time_gen:.4f} seconds")

print("\n--- List vs Generator ---")

# List comprehension (stores all in memory)
start = time.time()
total = sum([x**2 for x in range(1000000)])
time_list = time.time() - start

# Generator expression (processes one at a time)
start = time.time()
total = sum(x**2 for x in range(1000000))
time_generator = time.time() - start

print(f"List comprehension: {time_list:.4f} seconds")
print(f"Generator:          {time_generator:.4f} seconds")
print(f"Sum: {total}")

print("\n" + "=" * 60)
print("Examples complete! Try the exercises next.")
print("=" * 60)
