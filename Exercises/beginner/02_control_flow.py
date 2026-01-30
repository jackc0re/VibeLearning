"""
Beginner Exercise 2: Control Flow
=================================
Practice conditional logic with if/elif/else statements.
"""

print("=" * 50)
print("EXERCISE 2: Control Flow")
print("=" * 50)


# =============================================================================
# EXERCISE 2.1: Grade Calculator
# =============================================================================
print("\n--- Exercise 2.1: Grade Calculator ---")
"""
Given a numerical score (0-100), determine the letter grade:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

Handle edge cases: scores outside 0-100 range.
"""

score = 85

# Your code below:
grade = None  # Determine the grade
if grade:
    print(f"Score: {score} -> Grade: {grade}")
else:
    print(f"Score: {score} -> Invalid score")


# =============================================================================
# EXERCISE 2.2: Age Classifier
# =============================================================================
print("\n--- Exercise 2.2: Age Classifier ---")
"""
Classify a person into age categories:
- 0-12: Child
- 13-17: Teenager
- 18-64: Adult
- 65+: Senior
"""

age = 42

# Your code below:
category = None  # Determine the category
if category is not None:
    print(f"Age: {age} -> Category: {category}")


# =============================================================================
# EXERCISE 2.3: Leap Year Checker
# =============================================================================
print("\n--- Exercise 2.3: Leap Year Checker ---")
"""
Determine if a year is a leap year:
- Divisible by 4 AND (not divisible by 100 OR divisible by 400)
"""

year = 2024

# Your code below:
is_leap = None  # True if leap year, False otherwise
if is_leap is not None:
    print(f"Year: {year} -> Leap year: {is_leap}")


# =============================================================================
# EXERCISE 2.4: Triangle Validator
# =============================================================================
print("\n--- Exercise 2.4: Triangle Validator ---")
"""
Given three side lengths, determine if they can form a valid triangle:
- All sides must be positive
- Sum of any two sides must be greater than the third

Also classify the type:
- Equilateral: All sides equal
- Isosceles: Two sides equal
- Scalene: All sides different
"""

side1, side2, side3 = 3, 4, 5

# Your code below:
is_valid = None  # True if valid triangle
triangle_type = None  # "equilateral", "isosceles", "scalene", or "invalid"

print(f"Sides: {side1}, {side2}, {side3}")
if is_valid is not None:
    print(f"Valid triangle: {is_valid}")
    if is_valid:
        print(f"Type: {triangle_type}")


# =============================================================================
# EXERCISE 2.5: Login Simulator
# =============================================================================
print("\n--- Exercise 2.5: Login Simulator ---")
"""
Check login credentials:
- Username must be "admin"
- Password must be at least 8 characters
- Password must contain at least one number

Provide specific error messages for each case.
"""

username = "user123"
password = "secret"

# Your code below:
login_result = None  # "success" or error message
if login_result is not None:
    print(f"Login attempt: {login_result}")


# =============================================================================
# EXERCISE 2.6: Temperature Converter
# =============================================================================
print("\n--- Exercise 2.6: Temperature Converter ---")
"""
Convert temperature between Celsius and Fahrenheit.
Direction is determined by a parameter:
- "C" or "c": convert Celsius to Fahrenheit
- "F" or "f": convert Fahrenheit to Celsius
- Otherwise: return "Invalid direction"
"""

temp = 100
direction = "C"  # C = Celsius to Fahrenheit, F = Fahrenheit to Celsius

# Your code below:
converted_temp = None  # Convert the temperature
if converted_temp is not None:
    print(f"{temp}° {direction} -> {converted_temp:.2f}°")


# =============================================================================
# EXERCISE 2.7: Number Properties
# =============================================================================
print("\n--- Exercise 2.7: Number Properties ---")
"""
Check multiple properties of a number:
- Positive or negative (or zero)
- Even or odd
- Prime or composite
"""

number = 17

# Your code below:
sign = None  # "positive", "negative", or "zero"
parity = None  # "even" or "odd"
prime_status = None  # "prime" or "composite" (for numbers > 1)

print(f"Number: {number}")
if sign is not None:
    print(f"Sign: {sign}")
if parity is not None:
    print(f"Parity: {parity}")
if prime_status is not None:
    print(f"Prime status: {prime_status}")


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 2.1
print("\n--- Solution 2.1 ---")
score = 85

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = None

if grade:
    print(f"Score: {score} -> Grade: {grade}")
else:
    print(f"Score: {score} -> Invalid score")

# SOLUTION 2.2
print("\n--- Solution 2.2 ---")
age = 42

if 0 <= age <= 12:
    category = "Child"
elif 13 <= age <= 17:
    category = "Teenager"
elif 18 <= age <= 64:
    category = "Adult"
elif age >= 65:
    category = "Senior"
else:
    category = "Invalid age"

print(f"Age: {age} -> Category: {category}")

# SOLUTION 2.3
print("\n--- Solution 2.3 ---")
year = 2024

is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
print(f"Year: {year} -> Leap year: {is_leap}")

# SOLUTION 2.4
print("\n--- Solution 2.4 ---")
side1, side2, side3 = 3, 4, 5

is_valid = (
    side1 > 0
    and side2 > 0
    and side3 > 0
    and side1 + side2 > side3
    and side1 + side3 > side2
    and side2 + side3 > side1
)

if is_valid:
    if side1 == side2 == side3:
        triangle_type = "equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"
else:
    triangle_type = "invalid"

print(f"Sides: {side1}, {side2}, {side3}")
print(f"Valid triangle: {is_valid}")
if is_valid:
    print(f"Type: {triangle_type}")

# SOLUTION 2.5
print("\n--- Solution 2.5 ---")
username = "user123"
password = "secret"

if username != "admin":
    login_result = "Invalid username"
elif len(password) < 8:
    login_result = "Password too short"
elif not any(char.isdigit() for char in password):
    login_result = "Password must contain a number"
else:
    login_result = "success"

print(f"Login attempt: {login_result}")

# SOLUTION 2.6
print("\n--- Solution 2.6 ---")
temp = 100
direction = "C"

if direction.upper() == "C":
    converted_temp = (temp * 9 / 5) + 32
elif direction.upper() == "F":
    converted_temp = (temp - 32) * 5 / 9
else:
    converted_temp = None
    print("Invalid direction")

if converted_temp is not None:
    print(f"{temp}° {direction} -> {converted_temp:.2f}°")

# SOLUTION 2.7
print("\n--- Solution 2.7 ---")
number = 17

if number > 0:
    sign = "positive"
elif number < 0:
    sign = "negative"
else:
    sign = "zero"

parity = "even" if number % 2 == 0 else "odd"

if number > 1:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    prime_status = "prime" if is_prime else "composite"
else:
    prime_status = "N/A"

print(f"Number: {number}")
print(f"Sign: {sign}")
print(f"Parity: {parity}")
print(f"Prime status: {prime_status}")

print("\n" + "=" * 50)
print("Great job! Move on to 03_loops.py")
print("=" * 50)
