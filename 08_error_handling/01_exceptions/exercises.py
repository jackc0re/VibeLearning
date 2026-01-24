"""
Exceptions - Exercises

Practice raising and identifying exceptions.
Run with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Validate Age
# =============================================================================


def exercise_1_validate_age(age):
    """
    Raise ValueError if age is not an int or is negative.
    Return "OK" when valid.
    """
    # NOTE: bool is a subclass of int in Python, so we exclude it explicitly.
    if type(age) is not int or age < 0:
        raise ValueError("age must be a non-negative integer")
    return "OK"


# =============================================================================
# EXERCISE 2: Safe Lookup
# =============================================================================


def exercise_2_safe_lookup(mapping, key):
    """
    Return mapping[key]. If key is missing, raise KeyError with a helpful message.
    """
    try:
        return mapping[key]
    except KeyError as exc:
        raise KeyError(f"Missing key: {key!r}") from exc


# =============================================================================
# EXERCISE 3: Divide
# =============================================================================


def exercise_3_divide(a, b):
    """
    Raise ZeroDivisionError if b is zero, otherwise return a / b.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Exceptions Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Validate Age")
    try:
        result = exercise_1_validate_age(21)
        status = "PASS" if result == "OK" else "FAIL"
        if result != "OK":
            all_passed = False
        print(f"  {status} valid age returns: {result}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    try:
        exercise_1_validate_age(-1)
        all_passed = False
        print("  FAIL did not raise for negative age")
    except ValueError:
        print("  PASS raises for negative age")

    # Exercise 2
    print("\nExercise 2: Safe Lookup")
    data = {"name": "Ada"}
    try:
        result = exercise_2_safe_lookup(data, "name")
        status = "PASS" if result == "Ada" else "FAIL"
        if result != "Ada":
            all_passed = False
        print(f"  {status} found value: {result}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    try:
        exercise_2_safe_lookup(data, "missing")
        all_passed = False
        print("  FAIL did not raise for missing key")
    except KeyError:
        print("  PASS raises for missing key")

    # Exercise 3
    print("\nExercise 3: Divide")
    try:
        result = exercise_3_divide(10, 2)
        status = "PASS" if result == 5 else "FAIL"
        if result != 5:
            all_passed = False
        print(f"  {status} division result: {result}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    try:
        exercise_3_divide(10, 0)
        all_passed = False
        print("  FAIL did not raise for divide by zero")
    except ZeroDivisionError:
        print("  PASS raises for divide by zero")

    print("\n" + "=" * 50)
    if all_passed:
        print("All tests passed! Great job!")
    else:
        print("Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
