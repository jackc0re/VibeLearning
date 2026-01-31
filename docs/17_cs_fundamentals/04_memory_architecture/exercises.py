"""
Memory Architecture - Exercises
===============================
Practice understanding memory, references, and efficiency.
"""

import sys

print("=" * 60)
print("MEMORY ARCHITECTURE - Exercises")
print("=" * 60)

# =============================================================================
# EXERCISE 1: Memory Size Explorer
# =============================================================================
print("\n--- Exercise 1: Memory Size Explorer ---")
print("""
Write a function that takes any Python object and returns a detailed
memory report including:
- Size of the object itself
- Size of any contained objects (for lists, dicts, etc.)
- Total estimated memory usage
""")

def memory_report(obj):
    """
    Generate a memory report for an object.

    Args:
        obj: Any Python object

    Returns:
        Dictionary with memory information
    """
    # Your code here:
    pass

# Test with various objects
# report = memory_report([1, 2, 3, 4, 5])
# print(report)

# =============================================================================
# EXERCISE 2: Reference Chain Tracker
# =============================================================================
print("\n--- Exercise 2: Reference Chain Tracker ---")
print("""
Write a function that traces how many references exist to an object
through different variables.

Example:
a = [1, 2, 3]
b = a
c = b
d = a

The function should report that there are 4 references to the list.
""")

def count_references(obj):
    """
    Count how many references point to an object.

    Args:
        obj: Any Python object

    Returns:
        Integer count of references
    """
    # Your code here:
    # Hint: Use sys.getrefcount() - 1 (getrefcount adds a temporary reference)
    pass

# Test
# a = [1, 2, 3]
# print(f"References to a: {count_references(a)}")
# b = a
# print(f"References after b = a: {count_references(a)}")
# c = b
# print(f"References after c = b: {count_references(a)}")

# =============================================================================
# EXERCISE 3: Shallow vs Deep Copy Detector
# =============================================================================
print("\n--- Exercise 3: Shallow vs Deep Copy Detector ---")
print("""
Write a function that determines if a copy is shallow or deep by
modifying nested objects and checking if the original changes.
""")

def is_shallow_copy(original, copy_obj):
    """
    Determine if copy_obj is a shallow copy of original.

    Args:
        original: The original object (with nested mutable objects)
        copy_obj: The copied object

    Returns:
        True if shallow copy, False if deep copy
    """
    # Your code here:
    pass

# Test
# original = [[1], [2], [3]]
# shallow = original.copy()
# deep = copy.deepcopy(original)
#
# print(f"shallow is shallow? {is_shallow_copy(original, shallow)}")  # True
# print(f"deep is shallow? {is_shallow_copy(original, deep)}")        # False

# =============================================================================
# EXERCISE 4: Memory-Efficient Data Structure
# =============================================================================
print("\n--- Exercise 4: Memory-Efficient Data Structure ---")
print("""
Create a simple data structure that stores student grades.
Make it memory-efficient by using __slots__ to prevent creation
of __dict__ for each instance.

Compare memory usage with and without __slots__.
""")

class StudentWithDict:
    """Regular class with __dict__."""
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class StudentWithSlots:
    """Class with __slots__ for memory efficiency."""
    # Your code here:
    # __slots__ = [...]

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Compare memory usage
# students_dict = [StudentWithDict(f"Student{i}", i) for i in range(1000)]
# students_slots = [StudentWithSlots(f"Student{i}", i) for i in range(1000)]
#
# size_dict = sum(sys.getsizeof(s) for s in students_dict)
# size_slots = sum(sys.getsizeof(s) for s in students_slots)
#
# print(f"Memory with __dict__: {size_dict} bytes")
# print(f"Memory with __slots__: {size_slots} bytes")
# print(f"Savings: {size_dict - size_slots} bytes")

# =============================================================================
# EXERCISE 5: Reference Cycle Detector
# =============================================================================
print("\n--- Exercise 5: Reference Cycle Detector ---")
print("""
Write a function that detects if a circular reference exists
in a dictionary (a key's value references back to the dict).
""")

def has_cycle(obj, seen=None):
    """
    Detect circular references in a data structure.

    Args:
        obj: Dictionary or list to check
        seen: Set of already-seen object ids (for recursion)

    Returns:
        True if a cycle is detected, False otherwise
    """
    # Your code here:
    pass

# Test
# a = {"name": "a"}
# b = {"name": "b", "ref": a}
# a["ref"] = b  # Creates cycle
#
# print(f"Has cycle: {has_cycle(a)}")  # True

# no_cycle = {"a": 1, "b": {"c": 2}}
# print(f"Has cycle: {has_cycle(no_cycle)}")  # False

# =============================================================================
# EXERCISE 6: Immutable vs Mutable Parameter Passing
# =============================================================================
print("\n--- Exercise 6: Immutable vs Mutable Parameter Passing ---")
print("""
Predict and verify what happens in each of these function calls:
""")

def mystery_function_1(x):
    x = x + 1
    return x

def mystery_function_2(lst):
    lst = lst + [4]
    return lst

def mystery_function_3(lst):
    lst += [4]
    return lst

def mystery_function_4(lst):
    lst.append(4)
    return lst

# Predict what these will print, then test:
# a = 5
# print(f"Before: a = {a}")
# result = mystery_function_1(a)
# print(f"After: a = {a}, result = {result}")

# b = [1, 2, 3]
# print(f"\nBefore: b = {b}")
# result = mystery_function_2(b)
# print(f"After: b = {b}, result = {result}")

# c = [1, 2, 3]
# print(f"\nBefore: c = {c}")
# result = mystery_function_3(c)
# print(f"After: c = {c}, result = {result}")

# d = [1, 2, 3]
# print(f"\nBefore: d = {d}")
# result = mystery_function_4(d)
# print(f"After: d = {d}, result = {result}")

# =============================================================================
# EXERCISE 7: Memory-Efficient String Builder
# =============================================================================
print("\n--- Exercise 7: Memory-Efficient String Builder ---")
print("""
Create a StringBuilder class that efficiently concatenates strings
without creating many intermediate objects.

It should:
- Collect strings in a list
- Join them only when requested
- Support append() and __str__() methods

Compare performance with naive string concatenation.
""")

class StringBuilder:
    """Efficient string building."""

    def __init__(self):
        # Your code here:
        pass

    def append(self, s):
        """Add a string to the builder."""
        # Your code here:
        pass

    def __str__(self):
        """Return the final string."""
        # Your code here:
        pass

# Compare performance
# import time
#
# # Naive
# start = time.time()
# result = ""
# for i in range(100000):
#     result += str(i)
# naive_time = time.time() - start
#
# # StringBuilder
# start = time.time()
# sb = StringBuilder()
# for i in range(100000):
#     sb.append(str(i))
# result = str(sb)
# builder_time = time.time() - start
#
# print(f"Naive time: {naive_time:.4f}s")
# print(f"StringBuilder time: {builder_time:.4f}s")
# print(f"Speedup: {naive_time / builder_time:.1f}x")

# =============================================================================
# EXERCISE 8: Stack Depth Calculator
# =============================================================================
print("\n--- Exercise 8: Stack Depth Calculator ---")
print("""
Write a recursive function that calculates and returns the current
stack depth (how many function calls deep we are).

Hint: Use a default parameter that tracks depth.
""")

def get_stack_depth(depth=0):
    """
    Return the current call stack depth.

    Args:
        depth: Current depth (used for recursion)

    Returns:
        Maximum depth reached
    """
    # Your code here:
    pass

# Test
# print(f"Stack depth from main: {get_stack_depth()}")

# def wrapper():
#     return get_stack_depth()
# print(f"Stack depth from wrapper: {wrapper()}")

# def outer():
#     def middle():
#         def inner():
#             return get_stack_depth()
#         return inner()
#     return middle()
# print(f"Stack depth from nested: {outer()}")

print("\n" + "=" * 60)
print("Exercises complete! Check your answers below.")
print("=" * 60)

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

print("\n--- Exercise 1: Memory Size Explorer (Solution) ---")
solution_1 = '''
import sys

def memory_report(obj):
    """Generate a memory report for an object."""
    size = sys.getsizeof(obj)
    contained = 0

    # For containers, add sizes of contents
    if isinstance(obj, (list, tuple, set)):
        for item in obj:
            contained += sys.getsizeof(item)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            contained += sys.getsizeof(k) + sys.getsizeof(v)

    return {
        "object_size": size,
        "contained_size": contained,
        "total_size": size + contained,
        "id": id(obj),
        "type": type(obj).__name__
    }
'''
print(solution_1)

print("\n--- Exercise 2: Reference Chain Tracker (Solution) ---")
solution_2 = '''
import sys

def count_references(obj):
    """Count references to an object."""
    # sys.getrefcount adds 1 for the temporary reference
    return sys.getrefcount(obj) - 1
'''
print(solution_2)

print("\n--- Exercise 3: Shallow vs Deep Copy Detector (Solution) ---")
solution_3 = '''
import copy

def is_shallow_copy(original, copy_obj):
    """Check if copy_obj is a shallow copy of original."""
    if original is copy_obj:
        return False  # Same object, not a copy

    # For lists/tuples with nested mutable objects
    if isinstance(original, (list, tuple)) and len(original) > 0:
        # Check if first nested mutable object is shared
        if isinstance(original[0], (list, dict)):
            return original[0] is copy_obj[0]

    return False  # Assume deep if we can't detect shallow
'''
print(solution_3)

print("\n--- Exercise 4: Memory-Efficient Data Structure (Solution) ---")
solution_4 = '''
class StudentWithSlots:
    """Class with __slots__ for memory efficiency."""
    __slots__ = ['name', 'grade']

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# __slots__ prevents creation of __dict__, saving memory
# Also prevents adding new attributes dynamically
'''
print(solution_4)

print("\n--- Exercise 5: Reference Cycle Detector (Solution) ---")
solution_5 = '''
def has_cycle(obj, seen=None):
    """Detect circular references."""
    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return True

    seen.add(obj_id)

    if isinstance(obj, dict):
        for v in obj.values():
            if isinstance(v, (dict, list)) and has_cycle(v, seen.copy()):
                return True
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)) and has_cycle(item, seen.copy()):
                return True

    return False
'''
print(solution_5)

print("\n--- Exercise 6: Immutable vs Mutable Parameter Passing (Solution) ---")
print("""
mystery_function_1: a = 5 (unchanged) - integers are immutable
mystery_function_2: b = [1, 2, 3] (unchanged) - + creates new list
mystery_function_3: c = [1, 2, 3, 4] (MODIFIED!) - += modifies in place
mystery_function_4: d = [1, 2, 3, 4] (MODIFIED!) - append modifies in place

Key insight: += and append() modify the object; + creates a new one
""")

print("\n--- Exercise 7: Memory-Efficient String Builder (Solution) ---")
solution_7 = '''
class StringBuilder:
    def __init__(self):
        self.parts = []

    def append(self, s):
        self.parts.append(s)

    def __str__(self):
        return "".join(self.parts)
'''
print(solution_7)

print("\n--- Exercise 8: Stack Depth Calculator (Solution) ---")
solution_8 = '''
def get_stack_depth(depth=0):
    """Return current call stack depth."""
    try:
        1 / 0  # Force exception to get stack trace
    except ZeroDivisionError:
        import traceback
        stack = traceback.extract_stack()
        return len(stack) - 1  # Subtract 1 for current frame

# Alternative recursive approach:
def get_stack_depth_recursive(depth=0):
    try:
        return get_stack_depth_recursive(depth + 1)
    except RecursionError:
        return depth
'''
print(solution_8)

print("\n" + "=" * 60)
print("All solutions provided. Keep practicing!")
print("=" * 60)
