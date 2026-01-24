"""Big-O Notation - Exercises

Implement classic algorithms with known time complexity.

Run with:
    python exercises.py
"""

from __future__ import annotations

import heapq


# =============================================================================
# EXERCISE 1: Binary Search
# =============================================================================


def exercise_1_binary_search(nums: list[int], target: int) -> int:
    """Return the index of target in sorted nums, or -1 if not found."""

    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# =============================================================================
# EXERCISE 2: Merge Two Sorted Lists
# =============================================================================


def exercise_2_merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into a new sorted list."""

    i = 0
    j = 0
    out: list[int] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out


# =============================================================================
# EXERCISE 3: Top-K
# =============================================================================


def exercise_3_top_k(nums: list[int], k: int) -> list[int]:
    """Return the k largest numbers in descending order.

    Uses a min-heap of size k, giving O(n log k) time.
    """

    if k < 0:
        raise ValueError("k must be >= 0")
    if k == 0:
        return []

    heap: list[int] = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        else:
            if x > heap[0]:
                heapq.heapreplace(heap, x)
    return sorted(heap, reverse=True)


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Big-O Notation Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Binary Search")
    try:
        nums = [1, 3, 5, 7, 9]
        ok = exercise_1_binary_search(nums, 7) == 3 and exercise_1_binary_search(nums, 2) == -1
        print("  ", "PASS" if ok else "FAIL", "binary search")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Merge Sorted")
    try:
        ok = exercise_2_merge_sorted([1, 4, 6], [2, 3, 5]) == [1, 2, 3, 4, 5, 6]
        ok = ok and exercise_2_merge_sorted([], [1]) == [1]
        print("  ", "PASS" if ok else "FAIL", "merge")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Top-K")
    try:
        ok = exercise_3_top_k([5, 1, 5, 2, 9], 3) == [9, 5, 5]
        ok = ok and exercise_3_top_k([1, 2, 3], 0) == []
        print("  ", "PASS" if ok else "FAIL", "top-k")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()

