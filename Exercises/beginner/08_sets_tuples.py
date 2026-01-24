"""
Beginner Exercise 8: Sets and Tuples
====================================
Practice working with immutable data structures and sets.
"""

print("=" * 50)
print("EXERCISE 8: Sets and Tuples")
print("=" * 50)


# =============================================================================
# EXERCISE 8.1: Tuple Basics
# =============================================================================
print("\n--- Exercise 8.1: Tuple Basics ---")
"""
Given a tuple:
1. Access elements by index
2. Get length
3. Count occurrences of a value
4. Find index of a value
"""

point = (3, 4, 5)

# Your code below:
first =  # First element
last =  # Last element
length =  # Length
count_4 =  # Count occurrences of 4
index_5 =  # Index of 5

print(f"Tuple: {point}")
print(f"First: {first}")
print(f"Last: {last}")
print(f"Length: {length}")
print(f"Count of 4: {count_4}")
print(f"Index of 5: {index_5}")


# =============================================================================
# EXERCISE 8.2: Tuple Unpacking
# =============================================================================
print("\n--- Exercise 8.2: Tuple Unpacking ---"""
"""
Unpack a tuple into variables.
"""

person = ("Alice", 25, "NYC", "Engineer")

# Your code below:
# Unpack into name, age, city, job

print(f"Name: {name}, Age: {age}, City: {city}, Job: {job}")


# =============================================================================
# EXERCISE 8.3: Tuple Immutability
# =============================================================================
print("\n--- Exercise 8.3: Tuple Immutability ---"""
"""
Demonstrate tuple immutability.
Try to modify a tuple and explain why it fails/works.
"""

point = (1, 2, 3)

# Your code below:
# Try to modify point
# Explain result


# =============================================================================
# EXERCISE 8.4: Named Tuple
# =============================================================================
print("\n--- Exercise 8.4: Named Tuple ---"""
"""
Use collections.namedtuple for better readability.
"""

from collections import namedtuple

# Your code below:
Point =  # Define a named tuple
p =  # Create an instance

print(f"Point: ({p.x}, {p.y})")


# =============================================================================
# EXERCISE 8.5: Set Basics
# =============================================================================
print("\n--- Exercise 8.5: Set Basics ---"""
"""
Given two sets:
1. Union (all elements from both)
2. Intersection (common elements)
3. Difference (elements in A but not in B)
4. Symmetric difference (elements in either but not both)
"""

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Your code below:
union =  # Union
intersection =  # Intersection
difference =  # Difference (A - B)
symmetric_diff =  # Symmetric difference

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference (A-B): {difference}")
print(f"Symmetric difference: {symmetric_diff}")


# =============================================================================
# EXERCISE 8.6: Set Operations
# =============================================================================
print("\n--- Exercise 8.6: Set Operations ---"""
"""
Perform set membership and modification operations.
"""

numbers = {1, 2, 3, 4, 5}

# Your code below:
# Add element
# Remove element
# Check membership
# Get length

print(f"Modified set: {numbers}")


# =============================================================================
# EXERCISE 8.7: Set from List
# =============================================================================
print("\n--- Exercise 8.7: Remove Duplicates ---"""
"""
Remove duplicates from a list using a set.
Preserve order (optional challenge).
"""

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 7, 7]

# Your code below:
unique =  # Remove duplicates using set
unique_ordered =  # Remove duplicates and preserve order

print(f"Original: {numbers}")
print(f"Unique (unordered): {unique}")
print(f"Unique (ordered): {unique_ordered}")


# =============================================================================
# EXERCISE 8.8: Find Unique Elements
# =============================================================================
print("\n--- Exercise 8.8: Find Unique Elements ---"""
"""
Find elements that appear in exactly one of two lists.
"""

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Your code below:
unique =  # Elements in exactly one list

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Unique to one list: {unique}")


# =============================================================================
# EXERCISE 8.9: Frozen Set
# =============================================================================
print("\n--- Exercise 8.9: Frozen Set ---"""
"""
Use frozenset (immutable set) for hashable collections.
"""

# Your code below:
fs =  # Create a frozenset
# Try to modify it
# Explain result


# =============================================================================
# EXERCISE 8.10: Set Comprehension
# =============================================================================
print("\n--- Exercise 8.10: Set Comprehension ---"""
"""
Create a set using comprehension:
- Squares of even numbers from 1-20
"""

# Your code below:
even_squares =  # Set comprehension
print(f"Even squares: {even_squares}")


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 8.1
print("\n--- Solution 8.1 ---")
point = (3, 4, 5)
first = point[0]
last = point[-1]
length = len(point)
count_4 = point.count(4)
index_5 = point.index(5)
print(f"Tuple: {point}")
print(f"First: {first}")
print(f"Last: {last}")
print(f"Length: {length}")
print(f"Count of 4: {count_4}")
print(f"Index of 5: {index_5}")

# SOLUTION 8.2
print("\n--- Solution 8.2 ---")
person = ("Alice", 25, "NYC", "Engineer")
name, age, city, job = person
print(f"Name: {name}, Age: {age}, City: {city}, Job: {job}")

# SOLUTION 8.3
print("\n--- Solution 8.3 ---")
point = (1, 2, 3)
try:
    point[0] = 99
except TypeError as e:
    print(f"Error: {e}")
    print("Tuples are immutable - cannot modify elements after creation")

# SOLUTION 8.4
print("\n--- Solution 8.4 ---")
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"Point: ({p.x}, {p.y})")

# SOLUTION 8.5
print("\n--- Solution 8.5 ---")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union = set_a | set_b
intersection = set_a & set_b
difference = set_a - set_b
symmetric_diff = set_a ^ set_b
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference (A-B): {difference}")
print(f"Symmetric difference: {symmetric_diff}")

# SOLUTION 8.6
print("\n--- Solution 8.6 ---")
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.remove(1)
has_3 = 3 in numbers
has_10 = 10 in numbers
length = len(numbers)
print(f"Modified set: {numbers}")
print(f"Has 3: {has_3}")
print(f"Has 10: {has_10}")
print(f"Length: {length}")

# SOLUTION 8.7
print("\n--- Solution 8.7 ---")
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 7, 7]
unique = list(set(numbers))
unique_ordered = list(dict.fromkeys(numbers))
print(f"Original: {numbers}")
print(f"Unique (unordered): {unique}")
print(f"Unique (ordered): {unique_ordered}")

# SOLUTION 8.8
print("\n--- Solution 8.8 ---")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
unique = list(set(list1) ^ set(list2))
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Unique to one list: {unique}")

# SOLUTION 8.9
print("\n--- Solution 8.9 ---")
fs = frozenset([1, 2, 3, 4, 5])
try:
    fs.add(6)
except AttributeError as e:
    print(f"Error: {e}")
    print("Frozensets are immutable - cannot add or remove elements")

# SOLUTION 8.10
print("\n--- Solution 8.10 ---")
even_squares = {i ** 2 for i in range(1, 21) if i % 2 == 0}
print(f"Even squares: {even_squares}")

print("\n" + "=" * 50)
print("Great job! You've completed all beginner exercises!")
print("Move on to Intermediate exercises.")
print("=" * 50)
