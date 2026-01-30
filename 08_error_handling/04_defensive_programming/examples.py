"""
Defensive Programming - Examples

Demonstrates validation, guard clauses, and assertions.
Run with:
    python examples.py
"""


def validate_percentage(value):
    if not isinstance(value, (int, float)):
        raise TypeError("percentage must be a number")
    if not (0 <= value <= 100):
        raise ValueError("percentage must be between 0 and 100")
    return value


def demo_validation():
    print("Validation demo")
    try:
        validate_percentage(110)
    except Exception as exc:
        print("  Validation failed:", exc)


def transfer(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


def demo_guard_clauses():
    print("\nGuard clause demo")
    try:
        transfer(50, 75)
    except ValueError as exc:
        print("  Transfer blocked:", exc)


def average(values):
    assert values, "values must not be empty"
    return sum(values) / len(values)


def demo_assertions():
    print("\nAssertions demo")
    try:
        average([])
    except AssertionError as exc:
        print("  Assertion failed:", exc)


if __name__ == "__main__":
    demo_validation()
    demo_guard_clauses()
    demo_assertions()
    print("\n✓ Examples complete!")
