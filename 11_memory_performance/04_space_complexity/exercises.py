"""Space Complexity - Exercises

Focus:
- allocating vs streaming
- in-place transformations

Run with:
    python exercises.py
"""

from __future__ import annotations

from typing import Iterator


# =============================================================================
# EXERCISE 1: Squares List
# =============================================================================


def exercise_1_squares_list(n: int) -> list[int]:
    """Return a list of squares: [0^2, 1^2, ..., (n-1)^2]."""

    return [i * i for i in range(n)]


# =============================================================================
# EXERCISE 2: Squares Generator
# =============================================================================


def exercise_2_squares_generator(n: int) -> Iterator[int]:
    """Yield squares one at a time: 0^2, 1^2, ..., (n-1)^2."""

    for i in range(n):
        yield i * i


# =============================================================================
# EXERCISE 3: In-Place Dedup for Sorted List
# =============================================================================


def exercise_3_dedup_sorted_in_place(nums: list[int]) -> int:
    """Remove duplicates from a sorted list in-place.

    Return the new logical length (k) such that nums[:k] contains the unique values.

    Example:
      nums = [1,1,2,2,3] -> returns 3 and nums[:3] == [1,2,3]
    """

    if not nums:
        return 0

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Space Complexity Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Squares List")
    try:
        ok = exercise_1_squares_list(5) == [0, 1, 4, 9, 16]
        print("  ", "PASS" if ok else "FAIL", "squares list")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Squares Generator")
    try:
        it = exercise_2_squares_generator(5)
        ok = list(it) == [0, 1, 4, 9, 16]
        print("  ", "PASS" if ok else "FAIL", "squares generator")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: In-Place Dedup (Sorted)")
    try:
        nums = [1, 1, 2, 2, 3]
        before_id = id(nums)
        k = exercise_3_dedup_sorted_in_place(nums)
        ok = k == 3 and nums[:k] == [1, 2, 3] and id(nums) == before_id
        print("  ", "PASS" if ok else "FAIL", "dedup in place")
        all_passed = all_passed and ok

        nums2: list[int] = []
        k2 = exercise_3_dedup_sorted_in_place(nums2)
        ok2 = k2 == 0
        print("  ", "PASS" if ok2 else "FAIL", "empty list")
        all_passed = all_passed and ok2
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

