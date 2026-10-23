"""
Tuples - Exercises
==================
Try to solve each exercise before looking at the solution!
Solutions are provided at the bottom of this file.
"""

print("=" * 50)
print("TUPLES - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: Swap Two Values
# =============================================================================
print("\n--- Exercise 1: Swap Two Values ---\n")
"""
Swap the values of a and b in ONE line, using tuple unpacking.

Start:  a = "left", b = "right"
Result: a = "right", b = "left"
"""

a = "left"
b = "right"

# Your code here:
# a, b = ...


# =============================================================================
# EXERCISE 2: Days of the Week
# =============================================================================
print("\n--- Exercise 2: Days of the Week ---\n")
"""
The days of the week never change, so a tuple is a better fit than a list.

1. Create DAYS holding the 7 day names, Monday first.
2. Print the first and the last day using indexing.
3. Try to append "Funday" and catch the error it raises.
4. Print how many days there are.

Expected: the append fails with AttributeError, and the count is 7.
"""

# Your code here:
# DAYS = (...)


# =============================================================================
# EXERCISE 3: Tuple Unpacking
# =============================================================================
print("\n--- Exercise 3: Tuple Unpacking ---\n")
"""
Unpack data = ("John", "Doe", 25, "NYC", "Engineer")
and print: "John Doe, 25, is an Engineer in NYC"
"""
data = ("John", "Doe", 25, "NYC", "Engineer")

# Your code here


# =============================================================================
# EXERCISE 4: Split First/Middle/Last
# =============================================================================
print("\n--- Exercise 4: Split Tuple ---\n")
"""
Write split_tuple((1, 2, 3, 4, 5)) -> (1, [2, 3, 4], 5)

Return the first item, the middle items as a list, and the last item.
"""


def split_tuple(t):
    pass  # Your code


# Test:
# print(split_tuple((1, 2, 3, 4, 5)))


# =============================================================================
# EXERCISE 5: Sort Students
# =============================================================================
print("\n--- Exercise 5: Sort Students ---\n")
"""
Each student is a (name, age, score) tuple. Sort them by:
1. score, highest first
2. age, lowest first
3. name, alphabetically

Expected: [('Bob', 22, 90), ('Charlie', 22, 90), ('Alice', 25, 85)]
"""
students = [("Alice", 25, 85), ("Bob", 22, 90), ("Charlie", 22, 90)]

# Your code here
# sorted_students = ...


# =============================================================================
# EXERCISE 6: Distance
# =============================================================================
print("\n--- Exercise 6: Distance ---\n")
"""
Calculate the distance between two points, given as (x, y) tuples.
distance((0, 0), (3, 4)) -> 5.0
"""


def distance(p1, p2):
    pass  # Your code


# Test:
# print(distance((0, 0), (3, 4)))


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# Solution 1
print("\n--- Solution 1 ---")
a = "left"
b = "right"
print(f"Before: a={a}, b={b}")
a, b = b, a
print(f"After:  a={a}, b={b}")

# Solution 2
print("\n--- Solution 2 ---")
DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(f"DAYS = {DAYS}")
print(f"First day: {DAYS[0]}")
print(f"Last day: {DAYS[-1]}")
try:
    DAYS.append("Funday")
except AttributeError:
    print("DAYS.append('Funday') -> AttributeError: tuples cannot be changed")
print(f"Number of days: {len(DAYS)}")

# Solution 3
print("\n--- Solution 3 ---")
first, last, age, city, job = data
print(f"{first} {last}, {age}, is an {job} in {city}")

# Solution 4
print("\n--- Solution 4 ---")
def split_tuple(t):
    if len(t) < 2:
        return (t[0] if t else None, [], t[0] if t else None)
    first, *middle, last = t
    return (first, middle, last)
print(f"Result: {split_tuple((1, 2, 3, 4, 5))}")

# Solution 5
print("\n--- Solution 5 ---")
# lambda = tiny unnamed function ("given a student tuple x, use -x[2]"), full treatment in Module 05
sorted_students = sorted(students, key=lambda x: (-x[2], x[1], x[0]))
for s in sorted_students:
    print(f"  {s}")

# Solution 6
print("\n--- Solution 6 ---")
import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

print(f"distance((0, 0), (3, 4)): {distance((0, 0), (3, 4))}")

print("\n" + "=" * 50)
print("Great job! Move on to 06_stacks_queues next.")
print("=" * 50)
