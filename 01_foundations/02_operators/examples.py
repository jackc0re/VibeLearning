"""
Operators - Examples
====================
Run this file to see operators in action!
"""

print("=" * 50)
print("OPERATORS - Examples")
print("=" * 50)

# =============================================================================
# ARITHMETIC OPERATORS
# =============================================================================
print("\n--- Arithmetic Operators ---\n")

a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"a + b  = {a + b}")      # Addition
print(f"a - b  = {a - b}")      # Subtraction
print(f"a * b  = {a * b}")      # Multiplication
print(f"a / b  = {a / b}")      # Division (float)
print(f"a // b = {a // b}")     # Floor division (integer)
print(f"a % b  = {a % b}")      # Modulo (remainder)
print(f"a ** b = {a ** b}")     # Exponentiation (power)

# Division comparison
print("\n--- Division Types ---")
print(f"17 / 5  = {17 / 5}")    # 3.4 (regular division)
print(f"17 // 5 = {17 // 5}")   # 3 (floor division)
print(f"17 % 5  = {17 % 5}")    # 2 (remainder)

# Practical use of modulo: checking even/odd
print("\n--- Modulo Use Case: Even/Odd ---")
for num in range(1, 6):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# =============================================================================
# COMPARISON OPERATORS
# =============================================================================
print("\n--- Comparison Operators ---\n")

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"x == y  → {x == y}")    # Equal to
print(f"x != y  → {x != y}")    # Not equal to
print(f"x < y   → {x < y}")     # Less than
print(f"x > y   → {x > y}")     # Greater than
print(f"x <= y  → {x <= y}")    # Less than or equal
print(f"x >= y  → {x >= y}")    # Greater than or equal

# Chained comparisons
print("\n--- Chained Comparisons ---")
age = 25
print(f"age = {age}")
print(f"18 <= age <= 65  → {18 <= age <= 65}")  # Working age
print(f"13 <= age <= 19  → {13 <= age <= 19}")  # Teenager

# String comparison
print("\n--- String Comparison ---")
print(f"'apple' < 'banana'  → {'apple' < 'banana'}")
print(f"'Apple' < 'apple'   → {'Apple' < 'apple'}")  # Uppercase first
print(f"'10' < '9'          → {'10' < '9'}")  # String, not numeric!

# =============================================================================
# LOGICAL OPERATORS
# =============================================================================
print("\n--- Logical Operators ---\n")

has_ticket = True
is_adult = False

print(f"has_ticket = {has_ticket}")
print(f"is_adult = {is_adult}")

# AND - both must be True
print(f"\nhas_ticket and is_adult  → {has_ticket and is_adult}")

# OR - at least one must be True
print(f"has_ticket or is_adult   → {has_ticket or is_adult}")

# NOT - inverts the value
print(f"not has_ticket           → {not has_ticket}")
print(f"not is_adult             → {not is_adult}")

# Practical example
print("\n--- Practical Example: Access Control ---")
is_admin = False
is_owner = True
password_correct = True

can_access = (is_admin or is_owner) and password_correct
print(f"is_admin = {is_admin}")
print(f"is_owner = {is_owner}")
print(f"password_correct = {password_correct}")
print(f"Can access: {can_access}")

# =============================================================================
# ASSIGNMENT OPERATORS
# =============================================================================
print("\n--- Assignment Operators ---\n")

x = 10
print(f"Starting x = {x}")

x += 5
print(f"x += 5  → x = {x}")   # x = x + 5

x -= 3
print(f"x -= 3  → x = {x}")   # x = x - 3

x *= 2
print(f"x *= 2  → x = {x}")   # x = x * 2

x //= 3
print(f"x //= 3 → x = {x}")   # x = x // 3

x **= 2
print(f"x **= 2 → x = {x}")   # x = x ** 2

x %= 7
print(f"x %= 7  → x = {x}")   # x = x % 7

# =============================================================================
# MEMBERSHIP OPERATORS
# =============================================================================
print("\n--- Membership Operators ---\n")

# In strings
text = "Hello, World!"
print(f"Text: '{text}'")
print(f"'World' in text     → {'World' in text}")
print(f"'world' in text     → {'world' in text}")  # Case sensitive!
print(f"'x' not in text     → {'x' not in text}")

# In lists
fruits = ["apple", "banana", "cherry"]
print(f"\nFruits: {fruits}")
print(f"'apple' in fruits   → {'apple' in fruits}")
print(f"'grape' in fruits   → {'grape' in fruits}")
print(f"'grape' not in fruits → {'grape' not in fruits}")

# In dictionaries (checks keys, not values)
person = {"name": "Alice", "age": 25}
print(f"\nPerson: {person}")
print(f"'name' in person    → {'name' in person}")
print(f"'Alice' in person   → {'Alice' in person}")  # Values are not checked!

# =============================================================================
# IDENTITY OPERATORS
# =============================================================================
print("\n--- Identity Operators ---\n")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")

print(f"\nlist1 == list2  → {list1 == list2}")  # Same values?
print(f"list1 is list2  → {list1 is list2}")    # Same object?
print(f"list1 is list3  → {list1 is list3}")    # Same object!

# Modifying to prove identity
print("\n--- Proof of Identity ---")
list3.append(4)
print(f"After list3.append(4):")
print(f"list1 = {list1}")  # Also changed!
print(f"list3 = {list3}")

# None check
print("\n--- None Check ---")
result = None
print(f"result = {result}")
print(f"result is None  → {result is None}")  # ✅ Recommended

# =============================================================================
# OPERATOR PRECEDENCE
# =============================================================================
print("\n--- Operator Precedence ---\n")

# Without parentheses
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")  # 14, not 20

# With parentheses
result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")  # 20

# Mixed operators
result3 = 10 > 5 and 3 < 7
print(f"10 > 5 and 3 < 7 = {result3}")  # Comparisons before 'and'

# Complex expression
result4 = 2 ** 3 ** 2  # Right to left for exponents
print(f"2 ** 3 ** 2 = {result4}")  # 512, not 64

# Clear with parentheses
result5 = (2 ** 3) ** 2
print(f"(2 ** 3) ** 2 = {result5}")  # 64

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
