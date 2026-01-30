"""
Operators - Exercises
=====================
Try to solve each exercise before looking at the solution!
"""

print("=" * 50)
print("OPERATORS - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: Calculator
# =============================================================================
print("\n--- Exercise 1: Calculator ---\n")
"""
Create a simple calculator that:
1. Takes two numbers (a = 25, b = 7)
2. Prints the result of +, -, *, /, //, %, **
3. Format the output nicely
"""

a = 25
b = 7

# Your code here:


# =============================================================================
# EXERCISE 2: Age Checker
# =============================================================================
print("\n--- Exercise 2: Age Checker ---\n")
"""
Given an age, determine and print:
1. Is the person a child (0-12)?
2. Is the person a teenager (13-19)?
3. Is the person an adult (20-64)?
4. Is the person a senior (65+)?

Use chained comparisons!
"""

age = 35

# Your code here:


# =============================================================================
# EXERCISE 3: Access Control
# =============================================================================
print("\n--- Exercise 3: Access Control ---\n")
"""
A user can access a resource if:
- They are an admin, OR
- They are the owner AND the resource is not locked

Given the variables below, determine if access is granted.
"""

is_admin = False
is_owner = True
is_locked = False

# Your code here:
# can_access = ...


# =============================================================================
# EXERCISE 4: Grade Calculator
# =============================================================================
print("\n--- Exercise 4: Grade Calculator ---\n")
"""
Given a score, calculate the percentage and determine:
- Is it a passing grade (>= 60)?
- Is it an excellent grade (>= 90)?

Use compound operators to track total points.
"""

# Student got these scores on 4 tests (out of 25 each)
test1 = 22
test2 = 18
test3 = 25
test4 = 20

# Your code here:
# total = 0
# total += test1
# ...


# =============================================================================
# EXERCISE 5: Even/Odd Counter
# =============================================================================
print("\n--- Exercise 5: Even/Odd Counter ---\n")
"""
Given a list of numbers, count how many are even and odd.
Hint: Use the modulo operator (%)
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Your code here:
# even_count = 0
# odd_count = 0


# =============================================================================
# EXERCISE 6: Password Validator
# =============================================================================
print("\n--- Exercise 6: Password Validator ---\n")
"""
Check if a password is valid. A valid password must:
- Be at least 8 characters long
- Contain at least one digit (check if any single digit is 'in' the password)

Use membership operators and len().
"""

password = "secret123"

# Your code here:


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")
a, b = 25, 7
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# SOLUTION 2
print("\n--- Solution 2 ---")
age = 35
is_child = 0 <= age <= 12
is_teenager = 13 <= age <= 19
is_adult = 20 <= age <= 64
is_senior = age >= 65

print(f"Age: {age}")
print(f"Child (0-12): {is_child}")
print(f"Teenager (13-19): {is_teenager}")
print(f"Adult (20-64): {is_adult}")
print(f"Senior (65+): {is_senior}")

# SOLUTION 3
print("\n--- Solution 3 ---")
is_admin = False
is_owner = True
is_locked = False

can_access = is_admin or (is_owner and not is_locked)
print(f"is_admin: {is_admin}")
print(f"is_owner: {is_owner}")
print(f"is_locked: {is_locked}")
print(f"Can access: {can_access}")

# SOLUTION 4
print("\n--- Solution 4 ---")
total = 0
total += test1
total += test2
total += test3
total += test4

max_score = 100
percentage = (total / max_score) * 100
is_passing = percentage >= 60
is_excellent = percentage >= 90

print(f"Total: {total}/{max_score}")
print(f"Percentage: {percentage}%")
print(f"Passing (>=60%): {is_passing}")
print(f"Excellent (>=90%): {is_excellent}")

# SOLUTION 5
print("\n--- Solution 5 ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Numbers: {numbers}")
print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")

# SOLUTION 6
print("\n--- Solution 6 ---")
password = "secret123"

has_min_length = len(password) >= 8
has_digit = ("0" in password or "1" in password or "2" in password or 
             "3" in password or "4" in password or "5" in password or
             "6" in password or "7" in password or "8" in password or 
             "9" in password)

# Better way with any():
has_digit_better = any(char in password for char in "0123456789")

is_valid = has_min_length and has_digit_better

print(f"Password: {password}")
print(f"At least 8 characters: {has_min_length}")
print(f"Contains digit: {has_digit_better}")
print(f"Valid: {is_valid}")

print("\n" + "=" * 50)
print("Great job! Move on to 03_control_flow next.")
print("=" * 50)
