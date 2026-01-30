"""Optimization Techniques - Exercises

Implement small, practical optimizations:
- caching repeated computations
- joining strings efficiently
- counting words using efficient patterns

Run with:
    python exercises.py
"""

from __future__ import annotations

from functools import lru_cache


# =============================================================================
# EXERCISE 1: Cached Fibonacci
# =============================================================================


@lru_cache(maxsize=None)
def exercise_1_fib_cached(n: int) -> int:
    """Compute Fibonacci numbers with caching.

    fib(0)=0, fib(1)=1, fib(2)=1, ...
    """

    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return exercise_1_fib_cached(n - 1) + exercise_1_fib_cached(n - 2)


# =============================================================================
# EXERCISE 2: Join Strings
# =============================================================================


def exercise_2_join_strings(parts: list[str], sep: str = "") -> str:
    """Join parts using sep efficiently."""

    return sep.join(parts)


# =============================================================================
# EXERCISE 3: Word Count
# =============================================================================


def exercise_3_word_count(text: str) -> dict[str, int]:
    """Return a word-frequency dictionary.

    Rules:
      - words are split by whitespace
      - counting is case-insensitive
      - ignore empty input
    """

    counts: dict[str, int] = {}
    for raw in text.split():
        w = raw.lower()
        counts[w] = counts.get(w, 0) + 1
    return counts


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Optimization Techniques Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Cached Fibonacci")
    try:
        ok = exercise_1_fib_cached(10) == 55 and exercise_1_fib_cached(0) == 0 and exercise_1_fib_cached(1) == 1
        print("  ", "PASS" if ok else "FAIL", "fib values")
        all_passed = all_passed and ok

        try:
            exercise_1_fib_cached(-1)
            ok2 = False
        except ValueError:
            ok2 = True
        print("  ", "PASS" if ok2 else "FAIL", "raises for negative")
        all_passed = all_passed and ok2
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Join Strings")
    try:
        ok = exercise_2_join_strings(["a", "b", "c"]) == "abc" and exercise_2_join_strings(["a", "b", "c"], ",") == "a,b,c"
        print("  ", "PASS" if ok else "FAIL", "join")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Word Count")
    try:
        ok = exercise_3_word_count("One two two") == {"one": 1, "two": 2}
        ok = ok and exercise_3_word_count("") == {}
        print("  ", "PASS" if ok else "FAIL", "word count")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

