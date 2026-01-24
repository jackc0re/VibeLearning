"""\
Why Testing - Exercises

Practice writing small, deterministic tests.

Run with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Normalize Username
# =============================================================================


def exercise_1_normalize_username(name: str) -> str:
    """Return a normalized username.

Rules:
  - strip surrounding whitespace
  - lowercase
  - replace spaces with underscores

Examples:
  "  Ada Lovelace " -> "ada_lovelace"
  "BOB" -> "bob"
"""
    return name.strip().lower().replace(" ", "_")


# =============================================================================
# EXERCISE 2: Safe Percentage
# =============================================================================


def exercise_2_safe_percentage(part: float, total: float) -> float:
    """Return (part/total) * 100.

Rules:
  - If total is 0, raise ZeroDivisionError.
  - Accept ints/floats.
"""
    if total == 0:
        raise ZeroDivisionError("total must not be zero")
    return (part / total) * 100


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Why Testing Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Normalize Username")
    try:
        result = exercise_1_normalize_username("  Ada Lovelace ")
        ok = result == "ada_lovelace"
        print("  ", "PASS" if ok else "FAIL", "expected ada_lovelace got", result)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Safe Percentage")
    try:
        result = exercise_2_safe_percentage(1, 4)
        ok = abs(result - 25.0) < 1e-9
        print("  ", "PASS" if ok else "FAIL", "expected 25 got", result)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    try:
        exercise_2_safe_percentage(1, 0)
        all_passed = False
        print("  FAIL did not raise for total=0")
    except ZeroDivisionError:
        print("  PASS raises for total=0")

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

