"""\
Why Testing - Examples

Demonstrates:
  - A tiny bug and how a test would catch it
  - Arrange / Act / Assert style

Run with:
    python examples.py
"""


def buggy_is_even(n: int) -> bool:
    """Intentional bug: returns True for odd numbers too."""
    return n % 2 == 0 or n == 1


def fixed_is_even(n: int) -> bool:
    return n % 2 == 0


def demo_manual_test():
    print("Manual checks (not ideal)")
    print("buggy_is_even(2) =>", buggy_is_even(2))
    print("buggy_is_even(3) =>", buggy_is_even(3), "(WRONG)")


def demo_simple_assertions():
    print("\nSimple assertions (tiny test suite)")

    # Arrange
    values = [0, 1, 2, 3, 4]

    # Act + Assert
    for v in values:
        expected = (v % 2 == 0)
        actual = fixed_is_even(v)
        assert actual == expected, f"Expected {v} even? {expected}, got {actual}"

    print("OK - All assertions passed")


if __name__ == "__main__":
    demo_manual_test()
    demo_simple_assertions()

