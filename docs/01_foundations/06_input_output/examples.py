"""
Input and Output - Examples
===========================
Run this file to see I/O in action!
"""

print("=" * 50)
print("INPUT AND OUTPUT - Examples")
print("=" * 50)

# =============================================================================
# BASIC PRINT
# =============================================================================
print("\n--- Basic Print ---\n")

print("Hello, World!")
print(42)
print(3.14159)
print(True)
print(None)

# =============================================================================
# PRINTING MULTIPLE VALUES
# =============================================================================
print("\n--- Multiple Values ---\n")

name = "Alice"
age = 25
city = "NYC"

print("Method 1 - comma separated:")
print("Name:", name, "Age:", age)

print("\nMethod 2 - concatenation:")
print("Name: " + name + ", Age: " + str(age))

print("\nMethod 3 - f-string (recommended):")
print(f"Name: {name}, Age: {age}, City: {city}")

# =============================================================================
# F-STRING FORMATTING
# =============================================================================
print("\n--- F-String Formatting ---\n")

pi = 3.14159265
large_num = 1234567890
percentage = 0.756

# Decimal places
print(f"Pi with 2 decimals: {pi:.2f}")
print(f"Pi with 4 decimals: {pi:.4f}")

# Thousands separator
print(f"Large number: {large_num:,}")

# Percentage
print(f"Percentage: {percentage:.1%}")

# Width and alignment
print("\nAlignment examples:")
print(f"|{'left':<10}|")    # Left aligned
print(f"|{'right':>10}|")   # Right aligned
print(f"|{'center':^10}|")  # Centered

# Numeric alignment
print("\nNumeric alignment:")
for num in [1, 42, 256, 1000]:
    print(f"  {num:>6}")

# Zero padding
print("\nZero padding:")
for num in [1, 42, 256]:
    print(f"  {num:05}")

# =============================================================================
# PRINT CONTROLS
# =============================================================================
print("\n--- Print Controls ---\n")

# No newline (end parameter)
print("Hello", end=" ")
print("World", end="!\n")

# Custom separator
print("a", "b", "c", "d", sep=" -> ")

# Building output
print("\nProgress simulation:")
import time
for i in range(5):
    print(f"Loading{'.' * (i+1)}", end="\r", flush=True)
    time.sleep(0.3)
print("Loading..... Done!")

# =============================================================================
# INPUT EXAMPLES
# =============================================================================
print("\n--- Input Examples ---\n")

# Note: We'll simulate input for demo purposes
print("Simulating user input (in real code, user would type):")

# Simulated input values
simulated_name = "Bob"
simulated_age = "30"

print(f"\nSimulated: name = '{simulated_name}'")
print(f"Simulated: age = '{simulated_age}'")

# Show what we'd do with the input
print(f"\nGreeting: Hello, {simulated_name}!")
print(f"Age as string: {simulated_age} (type: {type(simulated_age)})")

age_int = int(simulated_age)
print(f"Age as integer: {age_int} (type: {type(age_int)})")
print(f"Next year you'll be: {age_int + 1}")

# =============================================================================
# STRING FORMATTING METHODS COMPARISON
# =============================================================================
print("\n--- Formatting Methods Comparison ---\n")

name = "Charlie"
age = 35

# F-strings (Python 3.6+) - RECOMMENDED
result1 = f"Hello, {name}. You are {age} years old."

# .format() method
result2 = "Hello, {}. You are {} years old.".format(name, age)

# % operator (old style)
result3 = "Hello, %s. You are %d years old." % (name, age)

print("F-string:   ", result1)
print(".format():  ", result2)
print("% operator: ", result3)

# =============================================================================
# ESCAPE CHARACTERS
# =============================================================================
print("\n--- Escape Characters ---\n")

print("Newline (\\n):")
print("Line 1\nLine 2\nLine 3")

print("\nTab (\\t):")
print("Col1\tCol2\tCol3")
print("A\tB\tC")

print("\nBackslash (\\\\):")
print("Path: C:\\Users\\Documents")

print("\nQuotes:")
print("She said \"Hello!\"")
print('It\'s working!')

print("\nRaw string (r prefix):")
print(r"Raw: C:\new\folder doesn't interpret \n")

# =============================================================================
# PRACTICAL TABLE FORMATTING
# =============================================================================
print("\n--- Table Formatting ---\n")

students = [
    ("Alice", 95, "A"),
    ("Bob", 82, "B+"),
    ("Charlie", 78, "C+"),
    ("Diana", 91, "A-"),
]

# Header
print(f"{'Name':<12} {'Score':>6} {'Grade':^6}")
print("-" * 26)

# Data rows
for name, score, grade in students:
    print(f"{name:<12} {score:>6} {grade:^6}")

# Footer
avg = sum(s[1] for s in students) / len(students)
print("-" * 26)
print(f"{'Average':<12} {avg:>6.1f}")

# =============================================================================
# FORMATTED NUMBER EXAMPLES
# =============================================================================
print("\n--- Number Formatting ---\n")

price = 1234.5
big_number = 9876543210
small = 0.00123

print(f"Currency:      ${price:,.2f}")
print(f"Big number:    {big_number:,}")
print(f"Scientific:    {small:.2e}")
print(f"Percentage:    {0.8523:.1%}")

# Binary, Octal, Hex
num = 255
print(f"\nNumber {num} in different bases:")
print(f"  Binary: {num:b}")
print(f"  Octal:  {num:o}")
print(f"  Hex:    {num:x}")
print(f"  Hex:    {num:X}")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
