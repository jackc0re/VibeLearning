# 🔧 Functions Basics

Functions are reusable blocks of code. Write once, use many times.

---

## Why Functions?

Without functions:
```python
# Calculate area of rectangle 1
length1 = 5
width1 = 3
area1 = length1 * width1
print(f"Area: {area1}")

# Calculate area of rectangle 2 (copy-paste, error-prone!)
length2 = 8
width2 = 4
area2 = length2 * width2
print(f"Area: {area2}")
```

With functions:
```python
def calculate_area(length, width):
    return length * width

area1 = calculate_area(5, 3)
area2 = calculate_area(8, 4)
```

---

## Defining Functions

Basic syntax:
```python
def function_name(parameters):
    """Docstring: describes what the function does"""
    # Function body
    return result  # Optional
```

### Examples:
```python
# No parameters, no return
def say_hello():
    print("Hello!")

# With parameters, with return
def add(a, b):
    return a + b

# With docstring
def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"
```

---

## Calling Functions

```python
# Define
def greet(name):
    return f"Hello, {name}!"

# Call
message = greet("Alice")  # "Hello, Alice!"
print(greet("Bob"))       # Prints: Hello, Bob!

# Can call multiple times
for person in ["Alice", "Bob", "Charlie"]:
    print(greet(person))
```

---

## Parameters vs Arguments

- **Parameters**: Variables in the function definition
- **Arguments**: Actual values passed when calling

```python
def add(a, b):     # a and b are PARAMETERS
    return a + b

result = add(5, 3)  # 5 and 3 are ARGUMENTS
```

---

## Return Values

### Single Return:
```python
def square(n):
    return n ** 2

result = square(5)  # 25
```

### Multiple Returns:
```python
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Returns a tuple

q, r = divide_with_remainder(17, 5)  # q=3, r=2
```

### No Return (returns None):
```python
def print_greeting(name):
    print(f"Hello, {name}!")
    # No return statement

result = print_greeting("Alice")  # Prints, but...
print(result)  # None
```

### Early Return:
```python
def get_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"  # Exit early
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    # etc.
```

---

## Default Parameters

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Alice", "Hi"))     # Hi, Alice!
print(greet("Alice", "Howdy"))  # Howdy, Alice!
```

### Rules for Defaults:
```python
# ✅ Correct: defaults come after non-defaults
def func(required, optional="default"):
    pass

# ❌ Wrong: non-default after default
def func(optional="default", required):  # SyntaxError
    pass
```

---

## Keyword Arguments

Call with parameter names for clarity:

```python
def create_user(name, age, city):
    return f"{name}, {age}, from {city}"

# Positional arguments (order matters)
create_user("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_user(city="NYC", name="Alice", age=25)

# Mix (positional first, then keyword)
create_user("Alice", city="NYC", age=25)
```

---

## `*args` and `**kwargs`

### `*args` - Variable Positional Arguments:
```python
def add_all(*args):
    """Add any number of arguments."""
    total = 0
    for num in args:
        total += num
    return total

add_all(1, 2)           # 3
add_all(1, 2, 3, 4, 5)  # 15
```

### `**kwargs` - Variable Keyword Arguments:
```python
def print_info(**kwargs):
    """Print any key-value pairs."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
# name: Alice
# age: 25
# city: NYC
```

### Combined:
```python
def func(required, *args, default="value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

func(1, 2, 3, default="custom", extra="data")
```

---

## Scope

Variables have **scope** — where they can be accessed.

### Local Scope:
```python
def my_function():
    x = 10  # Local to this function
    print(x)

my_function()
print(x)  # ❌ NameError: x is not defined
```

### Global Scope:
```python
x = 10  # Global variable

def my_function():
    print(x)  # Can read global

my_function()  # Prints 10
print(x)       # Also 10
```

### Modifying Global (avoid if possible):
```python
count = 0

def increment():
    global count  # Declare intention to modify global
    count += 1

increment()
print(count)  # 1
```

---

## Lambda Functions

Anonymous (unnamed) functions for simple operations:

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

# Both work the same
print(square(5))  # 25
```

### Common Usage:
```python
# Sorting with custom key
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
sorted_by_age = sorted(people, key=lambda p: p[1])

# With map/filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

---

## Docstrings

Document your functions:

```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.
    
    Args:
        weight: Weight in kilograms
        height: Height in meters
    
    Returns:
        BMI as a float
    
    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    return weight / (height ** 2)

# Access docstring
print(calculate_bmi.__doc__)
help(calculate_bmi)
```

---

## Quick Reference

```python
# Basic function
def function_name(param1, param2):
    return result

# Default parameter
def func(param="default"):
    pass

# Variable args
def func(*args, **kwargs):
    pass

# Lambda
lambda x: x * 2

# Docstring
def func():
    """Description of function."""
    pass
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
