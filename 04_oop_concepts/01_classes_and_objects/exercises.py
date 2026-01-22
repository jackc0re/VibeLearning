"""
01_classes_and_objects/exercises.py

Practice creating classes and objects!
"""

# -----------------------------------------------------------------------------
# Exercise 1: The Book Class
# -----------------------------------------------------------------------------
# 1. Create a class called `Book`.
# 2. It should have an `__init__` method that accepts `title`, `author`, and `pages`.
# 3. Add a method called `description` that returns a string formatted like:
#    "<Title> by <Author>, <Pages> pages"
# 4. Create two instances of `Book` and print their descriptions.

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

# Tests
print("\n--- Exercise 1 Output ---")

book1 = Book("1984", "George Orwell", 328)
book2 = Book("Dune", "Frank Herbert", 412)
print(book1.description())
print(book2.description())


# -----------------------------------------------------------------------------
# Exercise 2: Bank Account
# -----------------------------------------------------------------------------
# 1. Create a class called `BankAccount`.
# 2. In `__init__`, initialize an attribute `balance` to 0 (or a starting amount).
# 3. Add a method `deposit(amount)` that adds to the balance.
# 4. Add a method `withdraw(amount)` that subtracts from the balance.
#    - Optional: Add a check to ensure they can't withdraw more than they have!
# 5. Add a method `check_balance()` that prints the current balance.
# 6. Test your class by creating an account, depositing money, withdrawing, and checking balance.

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount

    def check_balance(self):
        print(f"Current balance: {self.balance}")

# Tests
print("\n--- Exercise 2 Output ---")

account = BankAccount(100)
account.check_balance()
account.deposit(50)
account.check_balance()
account.withdraw(30)
account.check_balance()
account.withdraw(1000)
