"""\
Unit Testing - Exercises

Implement the functions and run the included tests.

Run with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Parse Positive Int
# =============================================================================


def exercise_1_parse_positive_int(text: str) -> int:
    """Parse text as an integer and ensure it is > 0.

Rules:
  - Strip whitespace.
  - Raise ValueError if parsing fails or value <= 0.
"""
    value = int(text.strip())
    if value <= 0:
        raise ValueError("value must be positive")
    return value


# =============================================================================
# EXERCISE 2: Mean
# =============================================================================


def exercise_2_mean(values):
    """Return the arithmetic mean of a non-empty list of numbers.

Rules:
  - Raise ValueError for empty input.
"""
    if not values:
        raise ValueError("values must be non-empty")
    return sum(values) / len(values)


# =============================================================================
# EXERCISE 3: Is Palindrome
# =============================================================================


def exercise_3_is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome (case-insensitive, ignore spaces).

Examples:
  "racecar" -> True
  "Never odd or even" -> True
  "hello" -> False
"""
    normalized = "".join(ch.lower() for ch in text if ch != " ")
    return normalized == normalized[::-1]


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Unit Testing Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Parse Positive Int")
    try:
        ok = exercise_1_parse_positive_int(" 42 ") == 42
        print("  ", "PASS" if ok else "FAIL", "parses 42")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    for bad in ["0", "-1", "abc"]:
        try:
            exercise_1_parse_positive_int(bad)
            all_passed = False
            print("  FAIL did not raise for", repr(bad))
        except ValueError:
            print("  PASS raises for", repr(bad))

    # Exercise 2
    print("\nExercise 2: Mean")
    try:
        result = exercise_2_mean([1, 2, 3, 4])
        ok = abs(result - 2.5) < 1e-9
        print("  ", "PASS" if ok else "FAIL", "mean is", result)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    try:
        exercise_2_mean([])
        all_passed = False
        print("  FAIL did not raise for empty list")
    except ValueError:
        print("  PASS raises for empty list")

    # Exercise 3
    print("\nExercise 3: Is Palindrome")
    try:
        cases = [
            ("racecar", True),
            ("Never odd or even", True),
            ("hello", False),
        ]
        for text, expected in cases:
            actual = exercise_3_is_palindrome(text)
            ok = actual == expected
            print("  ", "PASS" if ok else "FAIL", repr(text), "=>", actual)
            all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

