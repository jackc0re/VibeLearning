"""Memory Basics - Exercises

Keep the focus on *observable* behavior:
- identity
- mutation vs copying
- using memoryview for views

Run with:
    python exercises.py
"""

from __future__ import annotations


# =============================================================================
# EXERCISE 1: Same Object?
# =============================================================================


def exercise_1_is_same_object(a: object, b: object) -> bool:
    """Return True if a and b are the exact same object (same identity)."""

    return a is b


# =============================================================================
# EXERCISE 2: Mutate In Place
# =============================================================================


def exercise_2_append_in_place(items: list[int], value: int) -> None:
    """Append value to items in-place (mutate the list) and return None."""

    items.append(value)


# =============================================================================
# EXERCISE 3: Bytes View
# =============================================================================


def exercise_3_slice_as_view(data: bytes, start: int, end: int) -> memoryview:
    """Return a memoryview slice into data without copying."""

    return memoryview(data)[start:end]


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Memory Basics Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Same Object?")
    try:
        x = []
        y = x
        z = []
        ok = exercise_1_is_same_object(x, y) is True and exercise_1_is_same_object(x, z) is False
        print("  ", "PASS" if ok else "FAIL", "identity checks")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Mutate In Place")
    try:
        items = [1, 2]
        before_id = id(items)
        exercise_2_append_in_place(items, 3)
        ok = items == [1, 2, 3] and id(items) == before_id
        print("  ", "PASS" if ok else "FAIL", "list mutated in place")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Bytes View")
    try:
        data = b"abcdef"
        mv = exercise_3_slice_as_view(data, 1, 4)
        ok = isinstance(mv, memoryview) and mv.tobytes() == b"bcd" and mv.obj is data
        print("  ", "PASS" if ok else "FAIL", "memoryview slice")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

