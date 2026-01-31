"""Time Complexity - Exercises

Implement functions with different (and improved) time complexity.

Run with:
    python exercises.py
"""

from __future__ import annotations


# =============================================================================
# EXERCISE 1: Linear Contains
# =============================================================================


def exercise_1_contains_linear(items: list[int], target: int) -> bool:
    """Return True if target is in items using a manual loop (linear scan)."""

    for x in items:
        if x == target:
            return True
    return False


# =============================================================================
# EXERCISE 2: Set Contains
# =============================================================================


def exercise_2_contains_set(items: list[int], target: int) -> bool:
    """Return True if target is in items by converting items to a set first."""

    return target in set(items)


# =============================================================================
# EXERCISE 3: Count Pairs with Sum
# =============================================================================


def exercise_3_count_pairs_with_sum(nums: list[int], target: int) -> int:
    """Count pairs (i < j) such that nums[i] + nums[j] == target.

    Implement in O(n) average time using a dictionary of counts.

    Example:
      nums=[1, 2, 3, 2], target=4 -> pairs: (1,3) and (2,2) => 2
    """

    counts: dict[int, int] = {}
    total = 0
    for x in nums:
        need = target - x
        total += counts.get(need, 0)
        counts[x] = counts.get(x, 0) + 1
    return total


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Time Complexity Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Linear Contains")
    try:
        ok = exercise_1_contains_linear([1, 2, 3], 2) is True and exercise_1_contains_linear([1, 2, 3], 9) is False
        print("  ", "PASS" if ok else "FAIL", "linear contains")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Set Contains")
    try:
        ok = exercise_2_contains_set([1, 2, 3], 3) is True and exercise_2_contains_set([1, 2, 3], 0) is False
        print("  ", "PASS" if ok else "FAIL", "set contains")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Count Pairs with Sum")
    try:
        ok = (
            exercise_3_count_pairs_with_sum([1, 2, 3, 2], 4) == 2
            and exercise_3_count_pairs_with_sum([], 0) == 0
            and exercise_3_count_pairs_with_sum([0, 0, 0], 0) == 3
        )
        print("  ", "PASS" if ok else "FAIL", "pair counting")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

