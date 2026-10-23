"""
Custom Exceptions - Examples

Demonstrates defining, raising, and catching custom exceptions.
Run with:
    python examples.py
"""


class InvalidEmailError(ValueError):
    pass


class PaymentError(Exception):
    pass


class CardDeclinedError(PaymentError):
    pass


class InsufficientFundsError(PaymentError):
    pass


class InvalidAmountError(PaymentError):
    pass


def register(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain '@'")
    return True


def charge(amount):
    if amount > 100:
        raise CardDeclinedError("Card limit exceeded")
    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than 0")
    return "charged"


def demo_custom_exceptions():
    print("Custom exceptions demo")
    try:
        register("not-an-email")
    except InvalidEmailError as exc:
        print("  Registration failed:", exc)


def demo_hierarchy():
    print("\nHierarchy demo")
    try:
        charge(150)
    except CardDeclinedError as exc:
        print("  Declined:", exc)
    except PaymentError as exc:
        print("  Payment error:", exc)

    try:
        charge(-5)
    except InvalidAmountError as exc:
        print("  Invalid amount:", exc)


if __name__ == "__main__":
    demo_custom_exceptions()
    demo_hierarchy()
    print("\nPASS Examples complete!")
