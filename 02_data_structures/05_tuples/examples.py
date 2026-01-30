"""
Tuples - Examples
=================
Run this file to see tuples in action!
"""

print("=" * 50)
print("TUPLES - Examples")
print("=" * 50)

# =============================================================================
# CREATING TUPLES
# =============================================================================
print("\n--- Creating Tuples ---\n")

# Empty tuple
empty = ()
print(f"Empty tuple: {empty}")

# Single element (note the comma!)
single = (42,)
not_tuple = (42)
print(f"Single element tuple: {single}, type: {type(single)}")
print(f"Not a tuple: {not_tuple}, type: {type(not_tuple)}")

# Multiple elements
coordinates = (10, 20, 30)
print(f"Coordinates: {coordinates}")

# Without parentheses (packing)
rgb = 255, 128, 0
print(f"RGB: {rgb}")

# From other iterables
from_list = tuple([1, 2, 3, 4, 5])
from_string = tuple("hello")
print(f"From list: {from_list}")
print(f"From string: {from_string}")

# =============================================================================
# ACCESSING ELEMENTS
# =============================================================================
print("\n--- Accessing Elements ---\n")

point = (10, 20, 30, 40, 50)
print(f"Tuple: {point}")

print(f"\nIndexing:")
print(f"  point[0] = {point[0]}")
print(f"  point[-1] = {point[-1]}")
print(f"  point[2] = {point[2]}")

print(f"\nSlicing:")
print(f"  point[1:3] = {point[1:3]}")
print(f"  point[:3] = {point[:3]}")
print(f"  point[::2] = {point[::2]}")

# =============================================================================
# TUPLE UNPACKING
# =============================================================================
print("\n--- Tuple Unpacking ---\n")

# Basic unpacking
point = (10, 20)
x, y = point
print(f"point = {point}")
print(f"x, y = point -> x={x}, y={y}")

# Unpacking with rest
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"\nnumbers = {numbers}")
print(f"first, *middle, last = numbers")
print(f"  first = {first}")
print(f"  middle = {middle}")
print(f"  last = {last}")

# Swap variables
a, b = 1, 2
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Ignore values with underscore
data = (1, 2, 3, 4, 5)
first, _, _, _, last = data
print(f"\ndata = {data}")
print(f"Extracting first and last: {first}, {last}")

# =============================================================================
# TUPLES AS RETURN VALUES
# =============================================================================
print("\n--- Tuples as Return Values ---\n")

def get_stats(numbers):
    """Return multiple statistics as a tuple."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [4, 2, 7, 1, 9, 3]
minimum, maximum, average = get_stats(data)
print(f"Data: {data}")
print(f"Min: {minimum}, Max: {maximum}, Avg: {average:.2f}")

def divide_with_remainder(a, b):
    """Return quotient and remainder."""
    return a // b, a % b

quotient, remainder = divide_with_remainder(17, 5)
print(f"\n17 / 5 = {quotient} remainder {remainder}")

# =============================================================================
# TUPLE METHODS
# =============================================================================
print("\n--- Tuple Methods ---\n")

numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {numbers}")

print(f"\ncount(2): {numbers.count(2)}")
print(f"count(5): {numbers.count(5)}")
print(f"index(4): {numbers.index(4)}")
print(f"index(2): {numbers.index(2)}")  # First occurrence

# =============================================================================
# TUPLES AS DICT KEYS
# =============================================================================
print("\n--- Tuples as Dictionary Keys ---\n")

# Coordinates as keys
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}

print("Location lookup:")
for coords, city in locations.items():
    print(f"  {coords} -> {city}")

# Access by tuple key
nyc_coords = (40.7128, -74.0060)
print(f"\nLooking up {nyc_coords}: {locations[nyc_coords]}")

# =============================================================================
# NAMED TUPLES
# =============================================================================
print("\n--- Named Tuples ---\n")

from collections import namedtuple

# Define a named tuple type
Point = namedtuple('Point', ['x', 'y', 'z'])

# Create instances
p1 = Point(10, 20, 30)
p2 = Point(x=5, y=10, z=15)

print(f"Point 1: {p1}")
print(f"  Access by name: x={p1.x}, y={p1.y}, z={p1.z}")
print(f"  Access by index: x={p1[0]}, y={p1[1]}, z={p1[2]}")

# Named tuple for Person
Person = namedtuple('Person', ['name', 'age', 'city'])
alice = Person('Alice', 25, 'NYC')
bob = Person('Bob', 30, 'LA')

print(f"\n{alice.name} is {alice.age} years old, lives in {alice.city}")
print(f"{bob.name} is {bob.age} years old, lives in {bob.city}")

# Convert to dictionary
print(f"\nAs dict: {alice._asdict()}")

# =============================================================================
# TUPLE OPERATIONS
# =============================================================================
print("\n--- Tuple Operations ---\n")

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
print(f"{t1} + {t2} = {t1 + t2}")

# Repetition
print(f"{t1} * 3 = {t1 * 3}")

# Membership
print(f"\n2 in {t1}: {2 in t1}")
print(f"7 in {t1}: {7 in t1}")

# Comparison
print(f"\n(1, 2) < (1, 3): {(1, 2) < (1, 3)}")
print(f"(1, 2) < (2, 1): {(1, 2) < (2, 1)}")
print(f"(1, 2, 3) == tuple([1, 2, 3]): {(1, 2, 3) == tuple([1, 2, 3])}")

# =============================================================================
# IMMUTABILITY
# =============================================================================
print("\n--- Immutability ---\n")

t = (1, 2, 3)
print(f"Tuple: {t}")
print("Trying t[0] = 99 would raise TypeError!")

# But mutable objects inside can change
t = ([1, 2], [3, 4])
print(f"\nTuple with lists: {t}")
t[0].append(999)
print(f"After t[0].append(999): {t}")
print("The tuple didn't change (same references), but the list inside did!")

# =============================================================================
# COMMON PATTERNS
# =============================================================================
print("\n--- Common Patterns ---\n")

# Enumerate
print("Enumerate:")
for i, letter in enumerate(['a', 'b', 'c']):
    print(f"  {i}: {letter}")

# Zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
print("\nZip:")
for name, age in zip(names, ages):
    print(f"  {name} is {age}")

# Sorting by tuple element
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
print(f"\nOriginal: {students}")
sorted_by_grade = sorted(students, key=lambda x: x[1])
print(f"By grade: {sorted_by_grade}")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
