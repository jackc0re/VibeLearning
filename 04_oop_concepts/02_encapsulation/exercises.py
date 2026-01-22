"""
02_encapsulation/exercises.py

Practice encapsulation and properties!
"""

# -----------------------------------------------------------------------------
# Exercise 1: Secure Login
# -----------------------------------------------------------------------------
# 1. Create a class `User`.
# 2. In `__init__`, accept `username` and `password`.
# 3. Store `password` as a private attribute (using double underscore).
# 4. Create a method `check_password(input_password)` that returns True if it matches, False otherwise.
# 5. Create a method `change_password(old_password, new_password)`:
#    - It should only update the password if `old_password` is correct.
#    - Optional: Add rules for the new password (e.g., length > 5).

class User:
    # TODO: Implement this class
    pass

# TODO: Test your class
print("\n--- Exercise 1 Output ---")


# -----------------------------------------------------------------------------
# Exercise 2: Product Price
# -----------------------------------------------------------------------------
# 1. Create a class `Product`.
# 2. It should have a private attribute `_price`.
# 3. Use the `@property` decorator to create a getter for `price`.
# 4. Use the `@price.setter` decorator to create a setter that:
#    - Prevents setting a negative price (print an error or raise ValueError).
# 5. Test it by trying to set valid and invalid prices.

class Product:
    # TODO: Implement this class
    pass

# TODO: Test your class
print("\n--- Exercise 2 Output ---")
