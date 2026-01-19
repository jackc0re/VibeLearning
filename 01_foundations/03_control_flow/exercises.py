"""
Control Flow - Exercises
========================
Practice making decisions with code!
"""

print("=" * 50)
print("CONTROL FLOW - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: Number Classifier
# =============================================================================
print("\n--- Exercise 1: Number Classifier ---\n")
"""
Write code that classifies a number as:
- "positive" if greater than 0
- "negative" if less than 0
- "zero" if equal to 0

Test with: 10, -5, 0
"""

number = 10

# Your code here:


# =============================================================================
# EXERCISE 2: Ticket Pricing
# =============================================================================
print("\n--- Exercise 2: Ticket Pricing ---\n")
"""
A movie theater charges:
- Children (0-12): $8
- Teens (13-17): $12
- Adults (18-64): $15
- Seniors (65+): $10

Calculate the ticket price for a given age.
"""

age = 25

# Your code here:


# =============================================================================
# EXERCISE 3: Login System
# =============================================================================
print("\n--- Exercise 3: Login System ---\n")
"""
Create a simple login check:
- Correct username: "admin"
- Correct password: "secret123"

Print appropriate messages for:
- Successful login
- Wrong password (correct username)
- Wrong username
"""

username = "admin"
password = "wrongpass"

# Your code here:


# =============================================================================
# EXERCISE 4: Leap Year Checker
# =============================================================================
print("\n--- Exercise 4: Leap Year Checker ---\n")
"""
A year is a leap year if:
- Divisible by 4 AND
- (NOT divisible by 100 OR divisible by 400)

Check if a year is a leap year.
Test with: 2024, 2023, 2000, 1900
"""

year = 2024

# Your code here:


# =============================================================================
# EXERCISE 5: FizzBuzz
# =============================================================================
print("\n--- Exercise 5: FizzBuzz ---\n")
"""
Classic programming challenge!
For a number:
- If divisible by 3 and 5: print "FizzBuzz"
- If divisible by 3 only: print "Fizz"
- If divisible by 5 only: print "Buzz"
- Otherwise: print the number

Do this for numbers 1-20.
"""

# Your code here:


# =============================================================================
# EXERCISE 6: BMI Calculator
# =============================================================================
print("\n--- Exercise 6: BMI Calculator ---\n")
"""
Calculate BMI and determine category:
- BMI = weight / (height ** 2)
- Underweight: BMI < 18.5
- Normal: 18.5 <= BMI < 25
- Overweight: 25 <= BMI < 30
- Obese: BMI >= 30

weight is in kg, height is in meters
"""

weight = 70  # kg
height = 1.75  # meters

# Your code here:


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")
for number in [10, -5, 0]:
    if number > 0:
        classification = "positive"
    elif number < 0:
        classification = "negative"
    else:
        classification = "zero"
    print(f"{number} is {classification}")

# SOLUTION 2
print("\n--- Solution 2 ---")
for age in [5, 15, 25, 70]:
    if age <= 12:
        price = 8
        category = "Child"
    elif age <= 17:
        price = 12
        category = "Teen"
    elif age <= 64:
        price = 15
        category = "Adult"
    else:
        price = 10
        category = "Senior"
    print(f"Age {age} ({category}): ${price}")

# SOLUTION 3
print("\n--- Solution 3 ---")
correct_user = "admin"
correct_pass = "secret123"

test_cases = [
    ("admin", "secret123"),
    ("admin", "wrongpass"),
    ("user", "secret123"),
]

for username, password in test_cases:
    print(f"\nTrying: {username} / {password}")
    if username == correct_user:
        if password == correct_pass:
            print("✅ Login successful! Welcome, admin.")
        else:
            print("❌ Incorrect password. Please try again.")
    else:
        print("❌ Username not found.")

# SOLUTION 4
print("\n--- Solution 4 ---")
for year in [2024, 2023, 2000, 1900]:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = "IS a leap year"
    else:
        result = "is NOT a leap year"
    print(f"{year} {result}")

# SOLUTION 5
print("\n--- Solution 5 ---")
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# SOLUTION 6
print("\n--- Solution 6 ---")
test_cases = [(70, 1.75), (50, 1.60), (100, 1.80), (45, 1.70)]

for weight, height in test_cases:
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    print(f"Weight: {weight}kg, Height: {height}m")
    print(f"  BMI: {bmi:.1f} - {category}\n")

print("=" * 50)
print("Great job! Move on to 04_loops next.")
print("=" * 50)
