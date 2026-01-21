"""
Lists and Arrays - Examples
===========================
Run this file to see lists in action!
"""

print("=" * 50)
print("LISTS AND ARRAYS - Examples")
print("=" * 50)

# =============================================================================
# CREATING LISTS
# =============================================================================
print("\n--- Creating Lists ---\n")

# Different ways to create lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, None]

print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed types: {mixed}")

# From other iterables
letters = list("Python")
range_list = list(range(1, 6))
print(f"\nFrom string 'Python': {letters}")
print(f"From range(1, 6): {range_list}")

# =============================================================================
# ACCESSING ELEMENTS
# =============================================================================
print("\n--- Accessing Elements ---\n")

colors = ["red", "orange", "yellow", "green", "blue"]
print(f"List: {colors}")

# Positive indexing
print(f"\nPositive indexing:")
print(f"  colors[0] = {colors[0]} (first)")
print(f"  colors[2] = {colors[2]} (third)")

# Negative indexing
print(f"\nNegative indexing:")
print(f"  colors[-1] = {colors[-1]} (last)")
print(f"  colors[-2] = {colors[-2]} (second to last)")

# Slicing
print(f"\nSlicing:")
print(f"  colors[1:3] = {colors[1:3]} (index 1 to 2)")
print(f"  colors[:3] = {colors[:3]} (first 3)")
print(f"  colors[2:] = {colors[2:]} (from index 2)")
print(f"  colors[::2] = {colors[::2]} (every 2nd)")
print(f"  colors[::-1] = {colors[::-1]} (reversed)")

# =============================================================================
# MODIFYING LISTS
# =============================================================================
print("\n--- Modifying Lists ---\n")

# Changing elements
animals = ["cat", "dog", "bird"]
print(f"Original: {animals}")
animals[1] = "hamster"
print(f"After animals[1] = 'hamster': {animals}")

# Adding elements
print(f"\nAdding elements:")
nums = [1, 2, 3]
print(f"Original: {nums}")

nums.append(4)
print(f"After append(4): {nums}")

nums.insert(0, 0)
print(f"After insert(0, 0): {nums}")

nums.extend([5, 6, 7])
print(f"After extend([5, 6, 7]): {nums}")

# Removing elements
print(f"\nRemoving elements:")
letters = ['a', 'b', 'c', 'd', 'e']
print(f"Original: {letters}")

removed = letters.pop()
print(f"After pop(): {letters}, removed '{removed}'")

removed = letters.pop(0)
print(f"After pop(0): {letters}, removed '{removed}'")

letters.remove('c')
print(f"After remove('c'): {letters}")

# =============================================================================
# LIST METHODS
# =============================================================================
print("\n--- List Methods ---\n")

# Sorting
scores = [85, 92, 78, 95, 88]
print(f"Original scores: {scores}")

scores.sort()
print(f"After sort(): {scores}")

scores.sort(reverse=True)
print(f"After sort(reverse=True): {scores}")

# Reversing
items = [1, 2, 3, 4, 5]
print(f"\nOriginal: {items}")
items.reverse()
print(f"After reverse(): {items}")

# Finding elements
fruits = ["apple", "banana", "cherry", "banana"]
print(f"\nList: {fruits}")
print(f"Index of 'banana': {fruits.index('banana')}")
print(f"Count of 'banana': {fruits.count('banana')}")

# =============================================================================
# LIST COMPREHENSIONS
# =============================================================================
print("\n--- List Comprehensions ---\n")

# Basic comprehension
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers 0-9: {evens}")

# Transform elements
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(f"Original: {words}")
print(f"Uppercase: {upper_words}")

# With if-else
nums = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in nums]
print(f"Numbers: {nums}")
print(f"Labels: {labels}")

# =============================================================================
# NESTED LISTS (2D)
# =============================================================================
print("\n--- Nested Lists (2D) ---\n")

# Create a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Accessing elements
print(f"\nmatrix[0][0] = {matrix[0][0]} (top-left)")
print(f"matrix[1][2] = {matrix[1][2]} (row 1, col 2)")
print(f"matrix[2][1] = {matrix[2][1]} (row 2, col 1)")

# Get a column
column_1 = [row[1] for row in matrix]
print(f"\nColumn 1: {column_1}")

# Flatten a matrix
flat = [item for row in matrix for item in row]
print(f"Flattened: {flat}")

# =============================================================================
# COMMON PATTERNS
# =============================================================================
print("\n--- Common Patterns ---\n")

# Min, max, sum
numbers = [23, 45, 12, 67, 34, 89, 21]
print(f"Numbers: {numbers}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

# Membership testing
fruits = ["apple", "banana", "cherry"]
print(f"\nFruits: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")

# Enumerate for index + value
print(f"\nEnumerate:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# Zip to combine lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print(f"\nZip example:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# =============================================================================
# COPYING LISTS
# =============================================================================
print("\n--- Copying Lists ---\n")

original = [1, 2, 3]

# These create references, not copies!
same_list = original
same_list.append(4)
print(f"After modifying 'same_list', original is: {original}")

# Reset
original = [1, 2, 3]

# Creating actual copies
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

copy1.append(4)
print(f"After modifying copy, original is: {original}")
print(f"Copy is: {copy1}")

# =============================================================================
# LIST AS STACK (LIFO)
# =============================================================================
print("\n--- List as Stack (LIFO) ---\n")

stack = []
print("Push 'a', 'b', 'c':")
stack.append('a')
stack.append('b')
stack.append('c')
print(f"Stack: {stack}")

print("\nPop items:")
while stack:
    item = stack.pop()
    print(f"  Popped: {item}, Stack now: {stack}")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
