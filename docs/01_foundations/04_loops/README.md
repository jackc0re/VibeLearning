# 🔁 Loops

Loops let you repeat code. Instead of writing the same thing many times, write it once and loop.

---

## Why Loops?

Without loops:
```python
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
```

With loops:
```python
for i in range(5):
    print("Hello!")
```

---

## For Loops

Use `for` when you know **how many times** to repeat, or when iterating over a collection.

### Basic Syntax:
```python
for item in iterable:
    # do something with item
```

### Iterating Over Range:
```python
# range(5) = 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# range(start, stop) = start to stop-1
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Counting backwards
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

### Iterating Over Collections:
```python
# List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# String (character by character)
for char in "Hello":
    print(char)

# Dictionary
person = {"name": "Alice", "age": 25}
for key in person:
    print(f"{key}: {person[key]}")

# Dictionary with items()
for key, value in person.items():
    print(f"{key}: {value}")
```

### `enumerate()` - Get Index Too:
```python
fruits = ["apple", "banana", "cherry"]

# Without enumerate
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (cleaner!)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start from different index
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")  # 1, 2, 3
```

---

## While Loops

Use `while` when you **don't know** how many iterations needed, or until a condition becomes false.

### Basic Syntax:
```python
while condition:
    # do something
    # (make sure condition eventually becomes False!)
```

### Examples:
```python
# Count to 5
count = 0
while count < 5:
    print(count)
    count += 1

# User input loop
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Game loop pattern
running = True
while running:
    action = input("Enter action (q to quit): ")
    if action == "q":
        running = False
```

### ⚠️ Infinite Loops:
```python
# This never stops! (Ctrl+C to break)
while True:
    print("Forever...")

# Accidental infinite loop (forgot to update condition)
x = 0
while x < 5:
    print(x)
    # Forgot: x += 1
```

---

## Loop Control: `break` and `continue`

### `break` - Exit the Loop Immediately:
```python
# Find first even number
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even: {num}")
        break  # Exit the loop
```

### `continue` - Skip to Next Iteration:
```python
# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Only odd numbers print
```

### `else` Clause (runs if loop completes normally):
```python
# Search for a value
for num in [1, 3, 5, 7]:
    if num == 4:
        print("Found 4!")
        break
else:
    print("4 not found")  # This runs because no break occurred
```

---

## Nested Loops

Loops inside loops:

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print("---")

# Output:
# 1 × 1 = 1
# 1 × 2 = 2
# 1 × 3 = 3
# ---
# 2 × 1 = 2
# ...
```

### Breaking Out of Nested Loops:
```python
# break only exits the innermost loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop
        print(f"i={i}, j={j}")

# To break outer loop, use a flag
found = False
for i in range(3):
    for j in range(3):
        if some_condition:
            found = True
            break
    if found:
        break
```

---

## Common Loop Patterns

### Sum/Accumulator:
```python
total = 0
for num in [1, 2, 3, 4, 5]:
    total += num
print(f"Sum: {total}")  # 15
```

### Counter:
```python
count = 0
for char in "hello world":
    if char == "l":
        count += 1
print(f"Found 'l' {count} times")  # 3
```

### Building a List:
```python
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # [1, 4, 9, 16, 25]
```

### Finding Max/Min:
```python
numbers = [3, 1, 4, 1, 5, 9, 2]

max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f"Max: {max_val}")  # 9
```

### Search:
```python
target = 4
found = False
for num in [1, 3, 4, 7, 9]:
    if num == target:
        found = True
        break

if found:
    print(f"Found {target}!")
else:
    print(f"{target} not found")
```

---

## List Comprehensions (Pythonic Loops)

A concise way to create lists:

```python
# Traditional for loop
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

# List comprehension (same result)
squares = [i ** 2 for i in range(1, 6)]

# With condition
evens = [i for i in range(10) if i % 2 == 0]

# With transformation
words = ["hello", "world"]
upper = [w.upper() for w in words]
```

---

## Quick Reference

```python
# For loop
for item in iterable:
    pass

# While loop
while condition:
    pass

# Range variations
range(5)          # 0, 1, 2, 3, 4
range(2, 5)       # 2, 3, 4
range(0, 10, 2)   # 0, 2, 4, 6, 8

# Loop control
break     # Exit loop
continue  # Skip to next iteration

# Useful functions
enumerate(list)   # Get index and value
zip(list1, list2) # Pair up elements
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
