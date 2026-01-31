"""
Tuples - Exercises
==================
Solutions at the bottom of this file.
"""

print("=" * 50)
print("TUPLES - Exercises")
print("=" * 50)

# EXERCISE 1: Tuple Unpacking
print("\n--- Exercise 1: Tuple Unpacking ---\n")
"""
Unpack data = ("John", "Doe", 25, "NYC", "Engineer") 
and print: "John Doe, 25, is an Engineer in NYC"
"""
data = ("John", "Doe", 25, "NYC", "Engineer")
# Your code here

# EXERCISE 2: Split First/Middle/Last
print("\n--- Exercise 2: Split Tuple ---\n")
"""
Write split_tuple((1,2,3,4,5)) -> (1, [2,3,4], 5)
"""
def split_tuple(t):
    pass  # Your code

# EXERCISE 3: Sort by Multiple Keys
print("\n--- Exercise 3: Sort Students ---\n")
"""
Sort by: score (desc), age (asc), name (asc)
"""
students = [("Alice", 25, 85), ("Bob", 22, 90), ("Charlie", 22, 90)]
# Your code here

# EXERCISE 4: Distance
print("\n--- Exercise 4: Distance ---\n")
"""
Calculate distance between two points.
distance((0,0), (3,4)) -> 5.0
"""
def distance(p1, p2):
    pass  # Your code

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# Solution 1
print("\n--- Solution 1 ---")
first, last, age, city, job = data
print(f"{first} {last}, {age}, is an {job} in {city}")

# Solution 2
print("\n--- Solution 2 ---")
def split_tuple(t):
    if len(t) < 2:
        return (t[0] if t else None, [], t[0] if t else None)
    first, *middle, last = t
    return (first, middle, last)
print(f"Result: {split_tuple((1, 2, 3, 4, 5))}")

# Solution 3
print("\n--- Solution 3 ---")
sorted_students = sorted(students, key=lambda x: (-x[2], x[1], x[0]))
for s in sorted_students:
    print(f"  {s}")

# Solution 4
print("\n--- Solution 4 ---")
import math
def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
print(f"distance((0,0), (3,4)): {distance((0,0), (3,4))}")

print("\n" + "=" * 50)
print("Great job! Move on to 06_stacks_queues next.")
print("=" * 50)
