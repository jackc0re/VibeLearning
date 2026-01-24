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
    if not (0 <= score <= 100):
        raise ValueError("score must be between 0 and 100")
    return score


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
    if price < 0:
        raise ValueError("price must be >= 0")
    if not (0 <= percent <= 100):
        raise ValueError("percent must be between 0 and 100")
    return price * (1 - (percent / 100))


# =============================================================================
# EXERCISE 3: Assertion
# =============================================================================


def exercise_3_average(values):
    """
    Use an assertion to ensure values is not empty.
    Return the average.
    """
    assert values, "values must not be empty"
    return sum(values) / len(values)


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
        status = "PASS" if result == 88 else "FAIL"
        if result != 88:
            all_passed = False
        print(f"  {status} valid score -> {result}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    try:
        exercise_1_validate_score(120)
        all_passed = False
        print("  FAIL did not raise for invalid score")
    except ValueError:
        print("  PASS raises for invalid score")

    # Exercise 2
    print("\nExercise 2: Apply Discount")
    try:
        result = exercise_2_apply_discount(100, 10)
        status = "PASS" if result == 90 else "FAIL"
        if result != 90:
            all_passed = False
        print(f"  {status} discounted price -> {result}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    try:
        exercise_2_apply_discount(-5, 10)
        all_passed = False
        print("  FAIL did not raise for negative price")
    except ValueError:
        print("  PASS raises for negative price")

    # Exercise 3
    print("\nExercise 3: Average")
    try:
        result = exercise_3_average([2, 4])
        status = "PASS" if result == 3 else "FAIL"
        if result != 3:
            all_passed = False
        print(f"  {status} average -> {result}")
    except Exception as exc:
        all_passed = False
        print(f"  FAIL raised unexpectedly: {exc}")

    try:
        exercise_3_average([])
        all_passed = False
        print("  FAIL did not assert for empty list")
    except AssertionError:
        print("  PASS asserts for empty list")

    print("\n" + "=" * 50)
    if all_passed:
        print("All tests passed! Great job!")
    else:
        print("Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
