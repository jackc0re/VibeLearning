"""
Intermediate Exercise 5: Error Handling
=======================================
Practice try/except/else/finally, custom exception hierarchies,
defensive programming, and context managers.
"""

print("=" * 50)
print("EXERCISE 5: Error Handling")
print("=" * 50)


# =============================================================================
# EXERCISE 5.1: Try / Except / Else / Finally
# =============================================================================
print("\n--- Exercise 5.1: Try / Except / Else / Finally ---")
"""
Write safe_divide(a, b) that:
- Returns a / b when it works
- Returns None when b is zero or the inputs cannot be divided
- Uses try / except (no if statements needed!)

Then the solution demonstrates all four blocks: try, except,
else (runs only when nothing failed) and finally (always runs).
"""


# Your code below:
def safe_divide(a, b):
    """Return a / b, or None when the division cannot happen."""
    pass


# Test (uncomment after implementing)
# print(safe_divide(10, 4))    # 2.5
# print(safe_divide(10, 0))    # None
# print(safe_divide(10, "x"))  # None


# =============================================================================
# EXERCISE 5.2: Custom Exceptions
# =============================================================================
print("\n--- Exercise 5.2: Custom Exceptions ---")
"""
Build a small exception hierarchy for a bank:

- BankError(Exception): base class for all bank problems
- InvalidAmountError(BankError): amount is not a positive number
- InsufficientFundsError(BankError): carries .needed and .available

Write withdraw(balance, amount) that returns the new balance,
raising the right exception for bad input.
"""


# Your code below:
class BankError(Exception):
    """Base class for all bank problems."""

    pass


class InvalidAmountError(BankError):
    """Raised when an amount is not a positive number."""

    pass


class InsufficientFundsError(BankError):
    """Raised when a withdrawal exceeds the balance."""

    pass


def withdraw(balance, amount):
    """Return the new balance after withdrawing amount."""
    pass


# Test (uncomment after implementing)
# balance = 100
# try:
#     balance = withdraw(balance, 500)
# except BankError as exc:
#     print(f"Blocked: {exc}")


# =============================================================================
# EXERCISE 5.3: Defensive Programming
# =============================================================================
print("\n--- Exercise 5.3: Defensive Programming ---")
"""
Fail fast with clear messages. Write parse_age(value) that:
- Returns value unchanged when it is a valid age
- Raises TypeError for anything that is not an int
  (careful: bool is a subclass of int - reject it too!)
- Raises ValueError for ints outside 0..130
"""


# Your code below:
def parse_age(value):
    """Return a validated age (int in 0..130)."""
    pass


# Test (uncomment after implementing)
# print(parse_age(25))
# try:
#     parse_age("25")
# except TypeError as exc:
#     print(f"TypeError: {exc}")


# =============================================================================
# EXERCISE 5.4: Context Manager Class
# =============================================================================
print("\n--- Exercise 5.4: Context Manager Class ---")
"""
Write a Timer class usable as a context manager:

class interface:
- __enter__(self): record the start time, return self
- __exit__(self, exc_type, exc_value, traceback): compute the
  elapsed time, store it on self.elapsed, return False so
  exceptions are never suppressed
"""

import time


# Your code below:
class Timer:
    """Context manager that measures how long a with-block takes."""

    pass


# Test (uncomment after implementing)
# with Timer() as t:
#     total = sum(range(1_000_000))
# print(f"Took {t.elapsed:.4f}s")


# =============================================================================
# EXERCISE 5.5: Context Manager Generator
# =============================================================================
print("\n--- Exercise 5.5: Context Manager Generator ---")
"""
Now the short way, with contextlib:

Write @contextmanager-decorated section(title) that:
- Prints "[START] title" when the block begins
- Prints "[END] title" when the block ends - EVEN IF the block
  raises (use try/finally around the yield)
"""

from contextlib import contextmanager


# Your code below:
@contextmanager
def section(title):
    """Print a banner around a block, even when it raises."""
    pass


# Test (uncomment after implementing)
# with section("Calculating payroll"):
#     print("  crunching numbers...")


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 5.1
print("\n--- Solution 5.1 ---")


def safe_divide(a, b):
    """Return a / b, or None when the division cannot happen."""
    try:
        value = a / b
    except (ZeroDivisionError, TypeError):
        return None
    else:
        return value


print(f"safe_divide(10, 4)   = {safe_divide(10, 4)}")
print(f"safe_divide(10, 0)   = {safe_divide(10, 0)}")
print(f"safe_divide(10, 'x') = {safe_divide(10, 'x')}")

print("try / except / else / finally in action:")
for text in ["10", "0", "abc"]:
    try:
        number = int(text)
        result = 100 / number
    except ZeroDivisionError:
        print(f"  '{text}': cannot divide by zero")
    except ValueError:
        print(f"  '{text}': not a number")
    else:
        print(f"  '{text}': 100 / {number} = {result}")
    finally:
        print(f"  ('{text}' attempt finished)")

# SOLUTION 5.2
print("\n--- Solution 5.2 ---")


class BankError(Exception):
    """Base class for all bank problems."""


class InvalidAmountError(BankError):
    """Raised when an amount is not a positive number."""


class InsufficientFundsError(BankError):
    """Raised when a withdrawal exceeds the balance."""

    def __init__(self, needed, available):
        super().__init__(f"need ${needed}, only ${available} available")
        self.needed = needed
        self.available = available


def withdraw(balance, amount):
    """Return the new balance after withdrawing amount."""
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise InvalidAmountError(f"amount must be positive, got {amount!r}")
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount


balance = 100
for amount in [30, 500, -5]:
    try:
        balance = withdraw(balance, amount)
        print(f"Withdrew ${amount}; balance now ${balance}")
    except BankError as exc:
        print(f"Blocked ({type(exc).__name__}): {exc}")

try:
    withdraw(10, 99)
except InsufficientFundsError as exc:
    print(f"Specific catch works too: short by ${exc.needed - exc.available}")

# SOLUTION 5.3
print("\n--- Solution 5.3 ---")


def parse_age(value):
    """Return a validated age (int in 0..130)."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"age must be an int, got {type(value).__name__}")
    if not 0 <= value <= 130:
        raise ValueError(f"age must be between 0 and 130, got {value}")
    return value


for candidate in [25, "25", True, 999]:
    try:
        print(f"parse_age({candidate!r}) = {parse_age(candidate)}")
    except (TypeError, ValueError) as exc:
        print(f"parse_age({candidate!r}) rejected: {type(exc).__name__}: {exc}")

# SOLUTION 5.4
print("\n--- Solution 5.4 ---")


class Timer:
    """Context manager that measures how long a with-block takes."""

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self._start
        if exc_type is not None:
            print(f"  (timer stopped by {exc_type.__name__})")
        return False  # never suppress the exception


with Timer() as timer:
    total = sum(range(1_000_000))
print(f"Summing 1,000,000 numbers took {timer.elapsed:.4f}s")

try:
    with Timer() as timer2:
        raise ValueError("something broke")
except ValueError as exc:
    print(f"Caught outside: {exc}; timer still measured {timer2.elapsed:.5f}s")

# SOLUTION 5.5
print("\n--- Solution 5.5 ---")


@contextmanager
def section(title):
    """Print a banner around a block, even when it raises."""
    print(f"[START] {title}")
    try:
        yield
    finally:
        print(f"[END] {title}")


with section("Calculating payroll"):
    print("  crunching numbers...")

try:
    with section("Risky block"):
        raise RuntimeError("boom")
except RuntimeError as exc:
    print(f"  caught outside: {exc}")

print("\n" + "=" * 50)
print("Great job! Move on to 06_file_io.py")
print("=" * 50)
