"""References vs Values - Exercises

Focus:
- in-place mutation
- safe (non-mutating) operations
- deep copy of nested lists

Run with:
    python exercises.py
"""

from __future__ import annotations


# =============================================================================
# EXERCISE 1: Mutate In Place
# =============================================================================


def exercise_1_add_key_in_place(d: dict[str, int], key: str, value: int) -> None:
    """Set d[key] = value in-place and return None."""

    d[key] = value


# =============================================================================
# EXERCISE 2: Safe Append (No Mutation)
# =============================================================================


def exercise_2_safe_append(items: list[int], value: int) -> list[int]:
    """Return a *new* list with value appended; do not mutate items."""

    return items + [value]


# =============================================================================
# EXERCISE 3: Clone Nested List
# =============================================================================


def exercise_3_clone_nested_list(nested: list[list[int]]) -> list[list[int]]:
    """Deep-copy a list of lists (copy inner lists too).

    Assumption: nested is a list of lists of ints.
    """

    return [inner[:] for inner in nested]


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running References vs Values Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Mutate In Place")
    try:
        d: dict[str, int] = {"a": 1}
        before_id = id(d)
        exercise_1_add_key_in_place(d, "b", 2)
        ok = d == {"a": 1, "b": 2} and id(d) == before_id
        print("  ", "PASS" if ok else "FAIL", "dict mutated")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Safe Append")
    try:
        items = [1, 2]
        before_id = id(items)
        out = exercise_2_safe_append(items, 3)
        ok = items == [1, 2] and id(items) == before_id and out == [1, 2, 3] and out is not items
        print("  ", "PASS" if ok else "FAIL", "no mutation")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Clone Nested List")
    try:
        nested = [[1], [2]]
        clone = exercise_3_clone_nested_list(nested)
        clone[0].append(99)
        ok = nested == [[1], [2]] and clone == [[1, 99], [2]] and clone is not nested and clone[0] is not nested[0]
        print("  ", "PASS" if ok else "FAIL", "deep copy for list-of-lists")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

