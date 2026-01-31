"""
Variables and Types - Exercises
===============================
Try to solve each exercise before looking at the solution!
Solutions are provided at the bottom of this file.
"""

print("=" * 50)
print("VARIABLES AND TYPES - Exercises")
print("=" * 50)

# =============================================================================
# EXERCISE 1: Variable Creation
# =============================================================================
print("\n--- Exercise 1: Variable Creation ---\n")
"""
Create variables for the following:
1. Your name (string)
2. Your age (integer)
3. Your height in meters (float)
4. Whether you like coding (boolean)

Then print them all using an f-string.
"""

# Your code here:
# name = ...
# age = ...
# height = ...
# likes_coding = ...
# print(f"...")

# =============================================================================
# EXERCISE 2: Type Conversion
# =============================================================================
print("\n--- Exercise 2: Type Conversion ---\n")
"""
You have the following string variables:
- year_str = "2024"
- price_str = "49.99"
- quantity_str = "5"

1. Convert them to appropriate numeric types
2. Calculate the total cost (price * quantity)
3. Print the result with 2 decimal places
"""

year_str = "2024"
price_str = "49.99"
quantity_str = "5"

# Your code here:
# year = ...
# price = ...
# quantity = ...
# total = ...
# print(f"...")

# =============================================================================
# EXERCISE 3: String Operations
# =============================================================================
print("\n--- Exercise 3: String Operations ---\n")
"""
Given the string: "   Python Programming   "
1. Remove the extra whitespace
2. Convert to uppercase
3. Replace "PYTHON" with "COOL"
4. Print the final result
"""

text = "   Python Programming   "

# Your code here:
# step1 = text...
# step2 = step1...
# step3 = step2...
# print(...)

# =============================================================================
# EXERCISE 4: Variable Swap
# =============================================================================
print("\n--- Exercise 4: Variable Swap ---\n")
"""
You have two variables:
- first = "apple"
- second = "banana"

Swap their values WITHOUT using a third variable.
Print before and after to verify.
"""

first = "apple"
second = "banana"

print(f"Before: first = {first}, second = {second}")

# Your code here (swap them):
# ...

# Uncomment to verify:
# print(f"After: first = {first}, second = {second}")

# =============================================================================
# EXERCISE 5: Type Checking
# =============================================================================
print("\n--- Exercise 5: Type Checking ---\n")
"""
Write code that checks if a variable is a string.
If it is, print it in uppercase.
If it's not, print "Not a string".

Test with these variables:
- test1 = "hello"
- test2 = 42
- test3 = ["a", "b", "c"]
"""

test1 = "hello"
test2 = 42
test3 = ["a", "b", "c"]

# Your code here:
# Hint: Use isinstance(variable, str) or type(variable) == str

# =============================================================================
# EXERCISE 6: Create a Profile
# =============================================================================
print("\n--- Exercise 6: Create a Profile ---\n")
"""
Create a user profile with these requirements:
1. username: all lowercase, no spaces (use _ instead)
2. display_name: properly capitalized
3. bio: a short description (use a multiline string)
4. age: as an integer
5. account_active: as a boolean

Print a formatted profile card.
"""

# Your code here:


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 1
print("\n--- Solution 1 ---")
name = "Alice"
age = 25
height = 1.68
likes_coding = True
print(f"Hi, I'm {name}, {age} years old, {height}m tall. Likes coding: {likes_coding}")

# SOLUTION 2
print("\n--- Solution 2 ---")
year = int(year_str)
price = float(price_str)
quantity = int(quantity_str)
total = price * quantity
print(f"Year: {year}, Total cost: ${total:.2f}")

# SOLUTION 3
print("\n--- Solution 3 ---")
step1 = text.strip()
step2 = step1.upper()
step3 = step2.replace("PYTHON", "COOL")
print(f"Result: '{step3}'")

# SOLUTION 4
print("\n--- Solution 4 ---")
first = "apple"
second = "banana"
first, second = second, first
print(f"After swap: first = {first}, second = {second}")

# SOLUTION 5
print("\n--- Solution 5 ---")
for test in [test1, test2, test3]:
    if isinstance(test, str):
        print(f"{test} -> {test.upper()}")
    else:
        print(f"{test} -> Not a string")

# SOLUTION 6
print("\n--- Solution 6 ---")
username = "cool_coder_42"
display_name = "Cool Coder"
bio = """Python enthusiast.
Learning to code one day at a time.
Coffee lover ☕"""
age = 25
account_active = True

print(f"""
╔══════════════════════════════╗
║         USER PROFILE         ║
╠══════════════════════════════╣
║ Username: @{username:<17}║
║ Display:  {display_name:<18}║
║ Age:      {age:<18}║
║ Active:   {str(account_active):<18}║
╠══════════════════════════════╣
║ Bio:                         ║
║ {bio.split(chr(10))[0]:<27} ║
║ {bio.split(chr(10))[1]:<27} ║
║ {bio.split(chr(10))[2]:<27} ║
╚══════════════════════════════╝
""")

print("\n" + "=" * 50)
print("Great job! Move on to 02_operators next.")
print("=" * 50)
