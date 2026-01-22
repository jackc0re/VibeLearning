"""
04_polymorphism/exercises.py

Practice polymorphism and magic methods!
"""

# -----------------------------------------------------------------------------
# Exercise 1: Media Player (Duck Typing)
# -----------------------------------------------------------------------------
# 1. Create a class `AudioFile` with a method `play()` that prints "Playing audio...".
# 2. Create a class `VideoFile` with a method `play()` that prints "Playing video...".
# 3. Create a function `play_media(media)` that calls `media.play()`.
# 4. Create a list containing instances of both classes and loop through it, calling `play_media`.

class AudioFile:
    def play(self):
        print("Playing audio...")

class VideoFile:
    def play(self):
        print("Playing video...")

def play_media(media):
    media.play()

# Tests
print("\n--- Exercise 1 Output ---")

playlist = [AudioFile(), VideoFile(), AudioFile()]
for item in playlist:
    play_media(item)


# -----------------------------------------------------------------------------
# Exercise 2: Bank Account Math (Operator Overloading)
# -----------------------------------------------------------------------------
# 1. Reuse (or redefine) the `BankAccount` class. It should have a `owner` and `balance`.
# 2. Implement `__str__` to return "Account(owner=<name>, balance=<amount>)".
# 3. Implement `__add__` to allow merging two accounts:
#    - It should accept another `BankAccount`.
#    - It should return a NEW `BankAccount` with:
#      - owner: "<owner1> & <owner2>"
#      - balance: sum of both balances.
# 4. Test it by adding two accounts together.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account(owner={self.owner}, balance={self.balance})"

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        owner = f"{self.owner} & {other.owner}"
        balance = self.balance + other.balance
        return BankAccount(owner, balance)

# Tests
print("\n--- Exercise 2 Output ---")

acc1 = BankAccount("Alice", 100)
acc2 = BankAccount("Bob", 250)
merged = acc1 + acc2
print(acc1)
print(acc2)
print(merged)
