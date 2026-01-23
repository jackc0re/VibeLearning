"""
DRY Principle - Exercises

These exercises practice extracting repeated logic into reusable helpers.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Shared Helper
# =============================================================================


def exercise_1_apply_tax(amount, tax_rate):
    """Return amount with tax applied (e.g., 100, 0.1 -> 110)."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Subtotal
# =============================================================================


def exercise_2_subtotal(items):
    """Return subtotal from a list of (name, price) tuples."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Total Price (Reuse Helpers)
# =============================================================================


def exercise_3_total(items, tax_rate, shipping_fee):
    """
    Return total price: (subtotal + tax) + shipping.

    Tip: Use exercise_2_subtotal and exercise_1_apply_tax.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Refund Amount (Reuse Helpers)
# =============================================================================


def exercise_4_refund(items, tax_rate, restocking_fee):
    """
    Return refund amount: (subtotal + tax) - restocking_fee.

    Tip: Use exercise_2_subtotal and exercise_1_apply_tax.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Currency Formatting
# =============================================================================


def exercise_5_format_currency(amount):
    """Return a string formatted like "$12.50"."""
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running DRY Principle Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Apply Tax")
    tests_1 = [
        (100, 0.10, 110.0),
        (50, 0.00, 50.0),
        (80, 0.25, 100.0),
    ]
    for amount, rate, expected in tests_1:
        result = exercise_1_apply_tax(amount, rate)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} apply_tax({amount}, {rate}) = {result} (expected {expected})")

    # Exercise 2
    print("\nExercise 2: Subtotal")
    tests_2 = [
        ([('a', 1.0), ('b', 2.5)], 3.5),
        ([], 0.0),
    ]
    for items, expected in tests_2:
        result = exercise_2_subtotal(items)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} subtotal({items}) = {result} (expected {expected})")

    # Exercise 3
    print("\nExercise 3: Total")
    items = [("book", 10.0), ("pen", 2.0)]
    result = exercise_3_total(items, 0.10, 5.0)
    expected = 18.2
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} total(items, 0.10, 5.0) = {result} (expected {expected})")

    # Exercise 4
    print("\nExercise 4: Refund")
    result = exercise_4_refund(items, 0.10, 1.0)
    expected = 12.2
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} refund(items, 0.10, 1.0) = {result} (expected {expected})")

    # Exercise 5
    print("\nExercise 5: Format Currency")
    tests_5 = [
        (12.5, "$12.50"),
        (0, "$0.00"),
        (100.999, "$101.00"),
    ]
    for amount, expected in tests_5:
        result = exercise_5_format_currency(amount)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} format_currency({amount}) = {result} (expected {expected})")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
