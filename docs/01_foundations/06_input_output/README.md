# 📥 Input and Output

How your program communicates with the outside world.

---

## Output: `print()`

The most basic way to show something to the user.

### Basic Print:
```python
print("Hello, World!")
print(42)
print(3.14)
print(True)
```

### Multiple Values:
```python
name = "Alice"
age = 25

print("Name:", name)               # Separated by space
print("Name:", name, "Age:", age)  # Multiple items
print(name, age, sep=", ")         # Custom separator
```

### F-Strings (Formatted Strings):
```python
name = "Alice"
age = 25
height = 1.756

print(f"Name: {name}")
print(f"Age: {age}, next year: {age + 1}")
print(f"Height: {height:.2f}m")  # 2 decimal places
```

### Formatting Options:
```python
number = 42
pi = 3.14159

# Width and alignment
print(f"|{number:5}|")    # |   42| - right aligned, width 5
print(f"|{number:<5}|")   # |42   | - left aligned
print(f"|{number:^5}|")   # | 42  | - centered

# Number formatting
print(f"{pi:.2f}")        # 3.14 - 2 decimal places
print(f"{number:04}")     # 0042 - zero-padded
print(f"{1000000:,}")     # 1,000,000 - with commas

# Percentage
print(f"{0.756:.1%}")     # 75.6%
```

### Print Controls:
```python
# No newline at end
print("Hello", end=" ")
print("World")  # Prints: Hello World

# Custom separator
print("a", "b", "c", sep="-")  # a-b-c

# Print to file (advanced)
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
```

---

## Input: `input()`

Get data from the user.

### Basic Input:
```python
name = input("What's your name? ")
print(f"Hello, {name}!")
```

### Input is Always a String!
```python
age_str = input("Enter your age: ")  # User types: 25
print(type(age_str))  # <class 'str'>

# Must convert for math
age = int(age_str)  # Now it's an integer
next_year = age + 1
```

### Common Conversions:
```python
# Integer
age = int(input("Age: "))

# Float
height = float(input("Height in meters: "))

# Multiple values on one line
x, y = input("Enter x y: ").split()  # Still strings
x, y = int(x), int(y)  # Now integers

# Or in one line
x, y = map(int, input("Enter x y: ").split())
```

### Input Validation:
```python
# Simple validation loop
while True:
    try:
        age = int(input("Enter your age: "))
        if 0 <= age <= 120:
            break
        print("Please enter a valid age (0-120)")
    except ValueError:
        print("Please enter a number")

print(f"Your age is {age}")
```

---

## String Formatting Methods

### F-Strings (recommended, Python 3.6+):
```python
name = "Alice"
age = 25
print(f"Hello, {name}. You are {age}.")
```

### `.format()` Method:
```python
print("Hello, {}. You are {}.".format(name, age))
print("Hello, {0}. You are {1}.".format(name, age))
print("Hello, {n}. You are {a}.".format(n=name, a=age))
```

### `%` Operator (old style):
```python
print("Hello, %s. You are %d." % (name, age))
# %s = string, %d = integer, %f = float
```

---

## Escape Characters

Special characters in strings:

```python
# Newline
print("Line 1\nLine 2")

# Tab
print("Column1\tColumn2")

# Backslash
print("Path: C:\\Users\\Name")

# Quote inside string
print("She said \"Hello\"")
print('It\'s working')

# Raw string (no escapes)
print(r"C:\new\folder")  # Prints: C:\new\folder
```

---

## Practical Patterns

### Menu System:
```python
def show_menu():
    print("\n=== Main Menu ===")
    print("1. Start Game")
    print("2. Settings")
    print("3. Exit")
    return input("Choose option: ")

choice = show_menu()
```

### Table Formatting:
```python
data = [
    ("Alice", 95, "A"),
    ("Bob", 82, "B"),
    ("Charlie", 67, "C"),
]

print(f"{'Name':<10} {'Score':>5} {'Grade':^5}")
print("-" * 22)
for name, score, grade in data:
    print(f"{name:<10} {score:>5} {grade:^5}")
```

### Progress Indicator:
```python
import time

for i in range(101):
    print(f"\rProgress: {i}%", end="", flush=True)
    time.sleep(0.05)
print("\nDone!")
```

---

## Quick Reference

```python
# Output
print(value)
print(a, b, sep=", ")
print("text", end="")
print(f"Value: {variable}")
print(f"{num:.2f}")     # Float formatting
print(f"{text:>10}")    # Right align

# Input
name = input("Prompt: ")
num = int(input("Number: "))
num = float(input("Decimal: "))

# Escapes
\n  # Newline
\t  # Tab
\\  # Backslash
\"  # Quote
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
