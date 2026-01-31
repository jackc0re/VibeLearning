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
    if not isinstance(username, str) or username == "":
        raise InvalidUsernameError("username must be a non-empty string")
    return "OK"


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
    if quantity <= 0:
        raise InvalidQuantityError("quantity must be > 0")
    if quantity > stock:
        raise OutOfStockError("not enough stock")
    return stock - quantity


# =============================================================================
# EXERCISE 3: Catch Specific Error
# =============================================================================


def exercise_3_safe_order(quantity, stock):
    """
    Call exercise_2_place_order and return remaining stock.
    If any OrderError occurs, return None.
    """
    try:
        return exercise_2_place_order(quantity, stock)
    except OrderError:
        return None


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
        status = "PASS" if result == "OK" else "FAIL"
        if result != "OK":
            all_passed = False
        print(f"  {status} valid username -> {result}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    try:
        exercise_1_validate_username(123)
        all_passed = False
        print("  FAIL did not raise for non-string")
    except InvalidUsernameError:
        print("  PASS raises for non-string")

    # Exercise 2
    print("\nExercise 2: Place Order")
    try:
        remaining = exercise_2_place_order(2, 5)
        status = "PASS" if remaining == 3 else "FAIL"
        if remaining != 3:
            all_passed = False
        print(f"  {status} remaining stock -> {remaining}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    try:
        exercise_2_place_order(0, 5)
        all_passed = False
        print("  FAIL did not raise for invalid quantity")
    except InvalidQuantityError:
        print("  PASS raises for invalid quantity")

    # Exercise 3
    print("\nExercise 3: Safe Order")
    result = exercise_3_safe_order(10, 2)
    status = "PASS" if result is None else "FAIL"
    if result is not None:
        all_passed = False
    print(f"  {status} safe order -> {result}")

    print("\n" + "=" * 50)
    if all_passed:
        print("All tests passed! Great job!")
    else:
        print("Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
