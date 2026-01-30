"""Threads Basics - Exercises

Goals:
- start threads and wait for completion
- get results back from threads
- use ThreadPoolExecutor for simple parallelism

Run with:
    python exercises.py
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List, TypeVar

T = TypeVar("T")


# =============================================================================
# EXERCISE 1: Run Callables In Threads
# =============================================================================


def exercise_1_run_callables(funcs: List[Callable[[], T]]) -> List[T]:
    """Run each callable in a thread and return results in the same order."""

    with ThreadPoolExecutor(max_workers=len(funcs) or 1) as executor:
        return list(executor.map(lambda f: f(), funcs))


# =============================================================================
# EXERCISE 2: Parallel Sum
# =============================================================================


def exercise_2_parallel_sum(numbers: List[int], workers: int) -> int:
    """Sum numbers by splitting into worker chunks using a thread pool."""

    if not numbers:
        return 0

    if workers <= 0:
        raise ValueError("workers must be >= 1")

    chunk_size = max(1, (len(numbers) + workers - 1) // workers)
    chunks = [numbers[i : i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    with ThreadPoolExecutor(max_workers=min(workers, len(chunks))) as executor:
        partials = list(executor.map(sum, chunks))
    return sum(partials)


# =============================================================================
# EXERCISE 3: Start And Join With Result
# =============================================================================


def exercise_3_thread_apply(fn: Callable[[int], int], value: int) -> int:
    """Run fn(value) in a separate thread and return its result."""

    result: List[int] = []

    def runner() -> None:
        result.append(fn(value))

    import threading

    t = threading.Thread(target=runner)
    t.start()
    t.join()
    return result[0]


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Threads Basics Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Run Callables In Threads")
    try:
        funcs = [lambda i=i: i * i for i in range(5)]
        got = exercise_1_run_callables(funcs)
        ok = got == [0, 1, 4, 9, 16]
        print("  ", "PASS" if ok else "FAIL", got)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Parallel Sum")
    try:
        nums = list(range(1, 1001))
        got = exercise_2_parallel_sum(nums, workers=4)
        ok = got == sum(nums)
        print("  ", "PASS" if ok else "FAIL", got)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Start And Join With Result")
    try:
        got = exercise_3_thread_apply(lambda x: x + 10, 5)
        ok = got == 15
        print("  ", "PASS" if ok else "FAIL", got)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
