"""
Loops - Examples
================
Run this file to see loops in action!
"""

print("=" * 50)
print("LOOPS - Examples")
print("=" * 50)

# =============================================================================
# BASIC FOR LOOP
# =============================================================================
print("\n--- Basic For Loop ---\n")

print("Counting from 0 to 4:")
for i in range(5):
    print(f"  i = {i}")

print("\nCounting from 2 to 5:")
for i in range(2, 6):
    print(f"  i = {i}")

print("\nCounting by 2s:")
for i in range(0, 10, 2):
    print(f"  i = {i}")

print("\nCountdown:")
for i in range(5, 0, -1):
    print(f"  {i}...")
print("  Liftoff! 🚀")

# =============================================================================
# ITERATING OVER COLLECTIONS
# =============================================================================
print("\n--- Iterating Over Collections ---\n")

# List
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# String
print("\nCharacters in 'Hello':")
for char in "Hello":
    print(f"  '{char}'")

# Dictionary
person = {"name": "Alice", "age": 25, "city": "NYC"}
print("\nPerson details:")
for key, value in person.items():
    print(f"  {key}: {value}")

# =============================================================================
# ENUMERATE
# =============================================================================
print("\n--- Enumerate ---\n")

colors = ["red", "green", "blue"]

print("With index (starting at 0):")
for i, color in enumerate(colors):
    print(f"  {i}: {color}")

print("\nWith index (starting at 1):")
for i, color in enumerate(colors, start=1):
    print(f"  {i}. {color}")

# =============================================================================
# WHILE LOOP
# =============================================================================
print("\n--- While Loop ---\n")

# Basic counting
print("Counting with while:")
count = 0
while count < 5:
    print(f"  count = {count}")
    count += 1

# Decreasing
print("\nDecreasing:")
value = 5
while value > 0:
    print(f"  value = {value}")
    value -= 1

# =============================================================================
# BREAK AND CONTINUE
# =============================================================================
print("\n--- Break and Continue ---\n")

# Break - exit loop early
print("Break example (stop at 5):")
for i in range(10):
    if i == 5:
        print("  Found 5! Breaking...")
        break
    print(f"  {i}")

# Continue - skip iteration
print("\nContinue example (skip even numbers):")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}")

# =============================================================================
# FOR-ELSE
# =============================================================================
print("\n--- For-Else ---\n")

# When item is found (break executed)
print("Searching for 4 in [1, 2, 3, 4, 5]:")
for num in [1, 2, 3, 4, 5]:
    if num == 4:
        print("  Found 4! ✓")
        break
else:
    print("  4 not found")

# When item is not found (else executes)
print("\nSearching for 10 in [1, 2, 3, 4, 5]:")
for num in [1, 2, 3, 4, 5]:
    if num == 10:
        print("  Found 10!")
        break
else:
    print("  10 not found ✗")

# =============================================================================
# NESTED LOOPS
# =============================================================================
print("\n--- Nested Loops ---\n")

# Multiplication table (partial)
print("Multiplication Table (1-3):")
for i in range(1, 4):
    row = ""
    for j in range(1, 4):
        row += f"  {i}×{j}={i*j:2}"
    print(row)

# Grid pattern
print("\nGrid pattern:")
for row in range(3):
    for col in range(4):
        print("■ ", end="")
    print()  # New line after each row

# =============================================================================
# COMMON PATTERNS
# =============================================================================
print("\n--- Common Patterns ---\n")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Numbers: {numbers}")

# Sum/Accumulator
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")

# Counter
count = 0
for num in numbers:
    if num > 4:
        count += 1
print(f"Numbers > 4: {count}")

# Maximum
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f"Maximum: {max_val}")

# Build new list
doubled = []
for num in numbers:
    doubled.append(num * 2)
print(f"Doubled: {doubled}")

# =============================================================================
# LIST COMPREHENSION
# =============================================================================
print("\n--- List Comprehension ---\n")

# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares (for loop): {squares}")

# List comprehension
squares = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares}")

# With condition
evens = [i for i in range(10) if i % 2 == 0]
print(f"Even numbers: {evens}")

# With transformation
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(f"Uppercased: {upper}")

# =============================================================================
# ZIP - ITERATE MULTIPLE LISTS
# =============================================================================
print("\n--- Zip ---\n")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

print("People:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}, lives in {city}")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
