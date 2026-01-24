"""\
Test-Driven Development - Exercises

Goal: implement a small function using a TDD mindset.
You can run this file repeatedly as you work.

Run with:
    python exercises.py
"""


# =============================================================================
# EXERCISE: Roman Numerals (I, V, X only)
# =============================================================================


def to_roman_upto_39(n: int) -> str:
    """Convert an integer to roman numerals, limited to 1..39.

Supported symbols:
  - I (1)
  - V (5)
  - X (10)

Examples:
  1 -> I
  4 -> IV
  9 -> IX
  14 -> XIV
  39 -> XXXIX
"""
    if type(n) is not int or not (1 <= n <= 39):
        raise ValueError("n must be an int in range 1..39")

    tens = n // 10
    ones = n % 10

    roman = "X" * tens
    if ones == 9:
        roman += "IX"
    elif ones >= 5:
        roman += "V" + ("I" * (ones - 5))
    elif ones == 4:
        roman += "IV"
    else:
        roman += "I" * ones
    return roman


# =============================================================================
# TESTS (start small; add more as you go)
# =============================================================================


def run_tests():
    print("Running TDD Exercises Tests")
    print("=" * 50)
    all_passed = True

    cases = [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (9, "IX"),
        (10, "X"),
        (14, "XIV"),
        (19, "XIX"),
        (20, "XX"),
        (39, "XXXIX"),
    ]

    print("\nExercise: to_roman_upto_39")
    for n, expected in cases:
        try:
            actual = to_roman_upto_39(n)
            ok = actual == expected
            print("  ", "PASS" if ok else "FAIL", n, "=>", actual)
            all_passed = all_passed and ok
        except Exception as exc:
            all_passed = False
            print("  FAIL", n, "raised:", exc)

    for bad in [0, 40, 3.14, "10"]:
        try:
            to_roman_upto_39(bad)  # type: ignore[arg-type]
            all_passed = False
            print("  FAIL did not raise for", repr(bad))
        except ValueError:
            print("  PASS raises for", repr(bad))

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

