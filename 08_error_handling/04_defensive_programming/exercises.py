"""
Defensive Programming - Exercises

Practice validation, guard clauses, and assertions.
Run with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Validate Range
# =============================================================================


def exercise_1_validate_score(score):
    """
    Raise ValueError if score is not between 0 and 100 inclusive.
    Return score when valid.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Guard Clause
# =============================================================================


def exercise_2_apply_discount(price, percent):
    """
    Guard against invalid inputs:
    - price must be >= 0
    - percent must be between 0 and 100
    Return the discounted price.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Assertion
# =============================================================================


def exercise_3_average(values):
    """
    Use an assertion to ensure values is not empty.
    Return the average.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Defensive Programming Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Validate Score")
    try:
        result = exercise_1_validate_score(88)
        status = "✓" if result == 88 else "✗"
        if result != 88:
            all_passed = False
        print(f"  {status} valid score -> {result}")
    except Exception as exc:
        all_passed = False
        print(f"  ✗ raised unexpectedly: {exc}")

    try:
        exercise_1_validate_score(120)
        all_passed = False
        print("  ✗ did not raise for invalid score")
    except ValueError:
        print("  ✓ raises for invalid score")

    # Exercise 2
    print("\nExercise 2: Apply Discount")
    try:
        result = exercise_2_apply_discount(100, 10)
        status = "✓" if result == 90 else "✗"
        if result != 90:
            all_passed = False
        print(f"  {status} discounted price -> {result}")
    except Exception as exc:
        all_passed = False
        print(f"  ✗ raised unexpectedly: {exc}")

    try:
        exercise_2_apply_discount(-5, 10)
        all_passed = False
        print("  ✗ did not raise for negative price")
    except ValueError:
        print("  ✓ raises for negative price")

    # Exercise 3
    print("\nExercise 3: Average")
    try:
        result = exercise_3_average([2, 4])
        status = "✓" if result == 3 else "✗"
        if result != 3:
            all_passed = False
        print(f"  {status} average -> {result}")
    except Exception as exc:
        all_passed = False
        print(f"  ✗ raised unexpectedly: {exc}")

    try:
        exercise_3_average([])
        all_passed = False
        print("  ✗ did not assert for empty list")
    except AssertionError:
        print("  ✓ asserts for empty list")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
