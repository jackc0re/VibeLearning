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
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, input_password):
        return self.__password == input_password

    def change_password(self, old_password, new_password):
        if not self.check_password(old_password):
            print("Old password is incorrect.")
            return False
        if len(new_password) < 6:
            print("New password must be at least 6 characters.")
            return False
        self.__password = new_password
        return True

# Tests
print("\n--- Exercise 1 Output ---")

user = User("alice", "secret123")
print(user.check_password("wrong"))
print(user.check_password("secret123"))
print(user.change_password("secret123", "short"))
print(user.change_password("secret123", "newpass"))
print(user.check_password("newpass"))


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
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
            return
        self._price = value

# Tests
print("\n--- Exercise 2 Output ---")

product = Product(10)
print(product.price)
product.price = -5
product.price = 25
print(product.price)
