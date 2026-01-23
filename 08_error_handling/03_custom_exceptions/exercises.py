"""
Custom Exceptions - Exercises

Practice creating and using your own exception types.
Run with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Custom Exception Type
# =============================================================================


class InvalidUsernameError(ValueError):
    pass


def exercise_1_validate_username(username):
    """
    Raise InvalidUsernameError if username is not a non-empty string.
    Return "OK" when valid.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Exception Hierarchy
# =============================================================================


class OrderError(Exception):
    pass


class OutOfStockError(OrderError):
    pass


class InvalidQuantityError(OrderError):
    pass


def exercise_2_place_order(quantity, stock):
    """
    Raise InvalidQuantityError if quantity <= 0.
    Raise OutOfStockError if quantity > stock.
    Return remaining stock otherwise.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Catch Specific Error
# =============================================================================


def exercise_3_safe_order(quantity, stock):
    """
    Call exercise_2_place_order and return remaining stock.
    If any OrderError occurs, return None.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Custom Exceptions Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Validate Username")
    try:
        result = exercise_1_validate_username("ada")
        status = "✓" if result == "OK" else "✗"
        if result != "OK":
            all_passed = False
        print(f"  {status} valid username -> {result}")
    except Exception as exc:
        all_passed = False
        print(f"  ✗ raised unexpectedly: {exc}")

    try:
        exercise_1_validate_username(123)
        all_passed = False
        print("  ✗ did not raise for non-string")
    except InvalidUsernameError:
        print("  ✓ raises for non-string")

    # Exercise 2
    print("\nExercise 2: Place Order")
    try:
        remaining = exercise_2_place_order(2, 5)
        status = "✓" if remaining == 3 else "✗"
        if remaining != 3:
            all_passed = False
        print(f"  {status} remaining stock -> {remaining}")
    except Exception as exc:
        all_passed = False
        print(f"  ✗ raised unexpectedly: {exc}")

    try:
        exercise_2_place_order(0, 5)
        all_passed = False
        print("  ✗ did not raise for invalid quantity")
    except InvalidQuantityError:
        print("  ✓ raises for invalid quantity")

    # Exercise 3
    print("\nExercise 3: Safe Order")
    result = exercise_3_safe_order(10, 2)
    status = "✓" if result is None else "✗"
    if result is not None:
        all_passed = False
    print(f"  {status} safe order -> {result}")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
