"""
Exceptions - Examples

Demonstrates built-in exceptions, raising errors, and tracebacks.
Run with:
    python examples.py
"""


def demo_builtin_exceptions():
    print("Built-in exceptions demo")
    samples = [
        ("ValueError", lambda: int("abc")),
        ("TypeError", lambda: "3" + 4),
        ("ZeroDivisionError", lambda: 10 / 0),
        ("KeyError", lambda: {"a": 1}["missing"]),
        ("IndexError", lambda: [1, 2][5]),
    ]

    for name, action in samples:
        try:
            action()
        except Exception as exc:
            print(f"  Caught {name}: {exc}")


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


def demo_raise():
    print("\nRaise demo")
    try:
        new_balance = withdraw(100, 150)
        print("New balance:", new_balance)
    except ValueError as exc:
        print("  Withdraw failed:", exc)


def demo_stack_trace():
    print("\nStack trace demo")

    def inner():
        return int("not-a-number")

    def outer():
        return inner()

    try:
        outer()
    except ValueError as exc:
        print("  Error surfaced with traceback:", exc)


if __name__ == "__main__":
    demo_builtin_exceptions()
    demo_raise()
    demo_stack_trace()
    print("\n✓ Examples complete!")
