"""
Functions Basics - Examples
===========================
Run this file to see functions in action!
"""

print("=" * 50)
print("FUNCTIONS BASICS - Examples")
print("=" * 50)

# =============================================================================
# BASIC FUNCTION DEFINITION
# =============================================================================
print("\n--- Basic Function Definition ---\n")

# Simple function with no parameters
def say_hello():
    print("Hello, World!")

say_hello()

# Function with parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

# =============================================================================
# RETURN VALUES
# =============================================================================
print("\n--- Return Values ---\n")

# Function that returns a value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Using return value directly
print(f"10 + 20 = {add(10, 20)}")

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
minimum, maximum = get_min_max(nums)
print(f"Numbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}")

# =============================================================================
# DEFAULT PARAMETERS
# =============================================================================
print("\n--- Default Parameters ---\n")

def power(base, exponent=2):
    """Calculate base raised to exponent. Default is square."""
    return base ** exponent

print(f"power(5) = {power(5)}")        # 25 (5^2)
print(f"power(5, 2) = {power(5, 2)}")  # 25
print(f"power(5, 3) = {power(5, 3)}")  # 125 (5^3)
print(f"power(2, 10) = {power(2, 10)}")  # 1024

# Multiple defaults
def create_profile(name, age=0, city="Unknown"):
    return f"{name}, {age} years old, from {city}"

print()
print(create_profile("Alice"))
print(create_profile("Bob", 25))
print(create_profile("Charlie", 30, "NYC"))

# =============================================================================
# KEYWORD ARGUMENTS
# =============================================================================
print("\n--- Keyword Arguments ---\n")

def describe_pet(animal, name, age):
    return f"{name} is a {age}-year-old {animal}"

# Positional arguments
print(describe_pet("dog", "Buddy", 3))

# Keyword arguments (order doesn't matter)
print(describe_pet(name="Whiskers", age=5, animal="cat"))

# Mixed
print(describe_pet("hamster", name="Fluffy", age=1))

# =============================================================================
# *ARGS - VARIABLE POSITIONAL ARGUMENTS
# =============================================================================
print("\n--- *args ---\n")

def sum_all(*args):
    """Sum any number of arguments."""
    print(f"Received args: {args}")
    return sum(args)

print(f"sum_all(1, 2) = {sum_all(1, 2)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# Practical example
def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(f"\nAverage of 10, 20, 30: {average(10, 20, 30)}")
print(f"Average of 5, 10: {average(5, 10)}")

# =============================================================================
# **KWARGS - VARIABLE KEYWORD ARGUMENTS
# =============================================================================
print("\n--- **kwargs ---\n")

def print_info(**kwargs):
    """Print any key-value pairs."""
    print("Received kwargs:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_info(name="Alice", age=25)
print()
print_info(product="Laptop", price=999, in_stock=True)

# Practical example: building a config
def create_config(**settings):
    config = {"debug": False, "timeout": 30}  # Defaults
    config.update(settings)  # Override with provided settings
    return config

print("\nDefault config:", create_config())
print("Custom config:", create_config(debug=True, timeout=60, retries=3))

# =============================================================================
# COMBINING PARAMETERS
# =============================================================================
print("\n--- Combining Parameters ---\n")

def full_example(required, *args, default="value", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

full_example("must have", 1, 2, 3, default="custom", extra1="a", extra2="b")

# =============================================================================
# SCOPE
# =============================================================================
print("\n--- Scope ---\n")

global_var = "I'm global"

def demonstrate_scope():
    local_var = "I'm local"
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")

demonstrate_scope()
print(f"Outside function - global_var: {global_var}")
# print(local_var)  # Would raise NameError

# Modifying global (generally avoid this pattern)
counter = 0

def increment():
    global counter
    counter += 1

print(f"\nCounter before: {counter}")
increment()
increment()
increment()
print(f"Counter after 3 increments: {counter}")

# =============================================================================
# LAMBDA FUNCTIONS
# =============================================================================
print("\n--- Lambda Functions ---\n")

# Simple lambda
double = lambda x: x * 2
print(f"double(5) = {double(5)}")

# Lambda with multiple parameters
multiply = lambda x, y: x * y
print(f"multiply(3, 4) = {multiply(3, 4)}")

# Common use: sorting
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# Sort by age
sorted_people = sorted(people, key=lambda p: p["age"])
print("\nSorted by age:")
for person in sorted_people:
    print(f"  {person['name']}: {person['age']}")

# Common use: with map and filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"\nNumbers: {numbers}")
print(f"Squared: {squared}")
print(f"Evens: {evens}")

# =============================================================================
# DOCSTRINGS
# =============================================================================
print("\n--- Docstrings ---\n")

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area as a number (length * width)
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

# Access docstring
print("Function docstring:")
print(calculate_area.__doc__)

# Using help()
print("\nhelp() output:")
help(calculate_area)

print("=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
