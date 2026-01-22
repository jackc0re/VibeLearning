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
    # TODO: Implement this class
    pass

class VideoFile:
    # TODO: Implement this class
    pass

def play_media(media):
    # TODO: Implement this function
    pass

# TODO: Test your code
print("\n--- Exercise 1 Output ---")


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
    # TODO: Implement this class
    pass

# TODO: Test your code
print("\n--- Exercise 2 Output ---")
