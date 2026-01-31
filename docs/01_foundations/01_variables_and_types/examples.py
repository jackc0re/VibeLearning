"""
Variables and Types - Examples
==============================
Run this file to see variables and types in action!
"""

print("=" * 50)
print("VARIABLES AND TYPES - Examples")
print("=" * 50)

# =============================================================================
# BASIC VARIABLE ASSIGNMENT
# =============================================================================
print("\n--- Basic Variable Assignment ---\n")

# Creating variables of different types
name = "Alice"
age = 25
height = 1.75
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"Is student: {is_student}")

# =============================================================================
# CHECKING TYPES
# =============================================================================
print("\n--- Checking Types ---\n")

print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")

# =============================================================================
# STRING OPERATIONS
# =============================================================================
print("\n--- String Operations ---\n")

first_name = "John"
last_name = "Doe"

# Concatenation (joining strings)
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String repetition
separator = "-" * 20
print(f"Separator: {separator}")

# String length
print(f"Length of full name: {len(full_name)} characters")

# String methods
message = "Hello, World!"
print(f"Original: {message}")
print(f"Uppercase: {message.upper()}")
print(f"Lowercase: {message.lower()}")
print(f"Replace: {message.replace('World', 'Python')}")

# =============================================================================
# NUMERIC OPERATIONS
# =============================================================================
print("\n--- Numeric Operations ---\n")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: a + b = {a + b}")
print(f"Subtraction: a - b = {a - b}")
print(f"Multiplication: a * b = {a * b}")
print(f"Division: a / b = {a / b}")
print(f"Integer division: a // b = {a // b}")
print(f"Modulo (remainder): a % b = {a % b}")
print(f"Power: a ** b = {a ** b}")

# =============================================================================
# TYPE CONVERSION
# =============================================================================
print("\n--- Type Conversion ---\n")

# String to number
age_string = "30"
age_number = int(age_string)
print(f"String '{age_string}' to integer: {age_number} (type: {type(age_number)})")

price_string = "19.99"
price_number = float(price_string)
print(f"String '{price_string}' to float: {price_number} (type: {type(price_number)})")

# Number to string
count = 42
count_string = str(count)
print(f"Integer {count} to string: '{count_string}' (type: {type(count_string)})")

# Float to integer (note: truncates, doesn't round!)
pi = 3.999
pi_int = int(pi)
print(f"Float {pi} to integer: {pi_int} (truncated, not rounded!)")

# =============================================================================
# BOOLEAN VALUES
# =============================================================================
print("\n--- Boolean Values ---\n")

is_raining = False
has_umbrella = True

print(f"Is raining: {is_raining}")
print(f"Has umbrella: {has_umbrella}")

# Booleans from comparisons
age = 25
is_adult = age >= 18
print(f"Age is {age}, is adult: {is_adult}")

temperature = 35
is_hot = temperature > 30
print(f"Temperature is {temperature}°C, is hot: {is_hot}")

# =============================================================================
# NONE TYPE
# =============================================================================
print("\n--- None Type ---\n")

result = None
print(f"Result: {result}")
print(f"Type of result: {type(result)}")

# Checking for None
if result is None:
    print("Result has no value yet")

# Assigning a value
result = 42
print(f"Result after assignment: {result}")

# =============================================================================
# MULTIPLE ASSIGNMENT
# =============================================================================
print("\n--- Multiple Assignment ---\n")

# Assign same value to multiple variables
x = y = z = 0
print(f"x = {x}, y = {y}, z = {z}")

# Assign different values in one line
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# Swap values (Python makes this easy!)
print(f"\nBefore swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

# =============================================================================
# F-STRINGS (FORMATTED STRINGS)
# =============================================================================
print("\n--- F-Strings (Formatted Strings) ---\n")

name = "Alice"
age = 25
score = 95.5

# Basic f-string
print(f"Hello, {name}!")

# F-string with expressions
print(f"Next year, {name} will be {age + 1} years old.")

# F-string with formatting
print(f"Score: {score:.1f}%")  # One decimal place
print(f"Score: {score:.0f}%")  # No decimal places

# F-string with padding
for i in range(1, 11):
    print(f"Item {i:2d}: {'*' * i}")  # :2d = width of 2 digits

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
