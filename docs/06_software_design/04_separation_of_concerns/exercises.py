"""
Separation of Concerns - Exercises

Practice splitting parsing, logic, and formatting responsibilities.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Parse CSV Integers
# =============================================================================


def exercise_1_parse_csv_ints(text):
    """Parse comma-separated integers. Ignore empty parts."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Business Rule
# =============================================================================


def exercise_2_total_with_tip(amount, tip_percent):
    """Return total including tip. Example: 10, 20 -> 12.0"""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Formatting
# =============================================================================


def exercise_3_format_receipt(total):
    """Return a receipt line like 'TOTAL: $12.00'."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Pipeline Function
# =============================================================================


def exercise_4_compute_receipt(text, tip_percent):
    """
    Combine parsing + logic + formatting:
    - parse numbers from text
    - sum them
    - apply tip
    - format receipt

    Tip: call the other exercises instead of duplicating logic.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Pure Validation
# =============================================================================


def exercise_5_is_positive_int(text):
    """Return True if text represents a positive integer."""
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Separation of Concerns Exercises Tests")
    print("=" * 50)
    all_passed = True

    print("\nExercise 1: Parse")
    tests_1 = [
        ("1,2,3", [1, 2, 3]),
        (" 10 , , 5 ", [10, 5]),
        ("", []),
    ]
    for text, expected in tests_1:
        result = exercise_1_parse_csv_ints(text)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} parse({text!r}) = {result} (expected {expected})")

    print("\nExercise 2: Tip")
    result = exercise_2_total_with_tip(10, 20)
    expected = 12.0
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} total_with_tip(10,20) = {result} (expected {expected})")

    print("\nExercise 3: Format")
    result = exercise_3_format_receipt(12)
    expected = "TOTAL: $12.00"
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} format_receipt(12) = {result!r} (expected {expected!r})")

    print("\nExercise 4: Pipeline")
    result = exercise_4_compute_receipt("10, 5", 20)
    expected = "TOTAL: $18.00"
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} compute_receipt('10, 5',20) = {result!r} (expected {expected!r})")

    print("\nExercise 5: Validate")
    tests_5 = [
        ("10", True),
        ("0", False),
        ("-1", False),
        ("abc", False),
    ]
    for text, expected in tests_5:
        result = exercise_5_is_positive_int(text)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} is_positive_int({text!r}) = {result} (expected {expected})")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
