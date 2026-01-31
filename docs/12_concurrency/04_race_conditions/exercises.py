"""Race Conditions - Exercises

Focus on correctness:
- protect read-modify-write operations
- prefer message passing via Queue when possible

Run with:
    python exercises.py
"""

from __future__ import annotations

import queue
import threading
from typing import Dict, List


# =============================================================================
# EXERCISE 1: Thread-Safe Counter Increment
# =============================================================================


def exercise_1_safe_increment(n_threads: int, increments: int) -> int:
    """Return the final count after n_threads increment it safely."""

    if n_threads <= 0 or increments < 0:
        raise ValueError("invalid n_threads/increments")

    lock = threading.Lock()
    counter = {"value": 0}

    def worker() -> None:
        for _ in range(increments):
            with lock:
                counter["value"] += 1

    threads = [threading.Thread(target=worker) for _ in range(n_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return counter["value"]


# =============================================================================
# EXERCISE 2: Safe Dictionary Update
# =============================================================================


def exercise_2_safe_dict_add(counter: Dict[str, int], key: str, delta: int, lock: threading.Lock) -> None:
    """Safely add delta to counter[key] (creating it if missing)."""

    with lock:
        counter[key] = counter.get(key, 0) + delta


# =============================================================================
# EXERCISE 3: Sum Using Queue (Message Passing)
# =============================================================================


def exercise_3_sum_with_queue(values: List[int], workers: int) -> int:
    """Sum values using worker threads pulling from a Queue."""

    if workers <= 0:
        raise ValueError("workers must be >= 1")

    q: "queue.Queue[int]" = queue.Queue()
    for v in values:
        q.put(v)

    results: List[int] = []
    results_lock = threading.Lock()

    def worker() -> None:
        local_sum = 0
        while True:
            try:
                v = q.get_nowait()
            except queue.Empty:
                break
            try:
                local_sum += v
            finally:
                q.task_done()

        with results_lock:
            results.append(local_sum)

    threads = [threading.Thread(target=worker) for _ in range(min(workers, len(values) or 1))]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return sum(results)


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Race Conditions Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Thread-Safe Counter Increment")
    try:
        got = exercise_1_safe_increment(n_threads=4, increments=25_000)
        ok = got == 100_000
        print("  ", "PASS" if ok else "FAIL", got)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Safe Dictionary Update")
    try:
        lock = threading.Lock()
        counter: Dict[str, int] = {}

        def worker() -> None:
            for _ in range(10_000):
                exercise_2_safe_dict_add(counter, "hits", 1, lock)

        threads = [threading.Thread(target=worker) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        got = counter.get("hits")
        ok = got == 40_000
        print("  ", "PASS" if ok else "FAIL", got)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Sum Using Queue")
    try:
        values = list(range(1, 5001))
        got = exercise_3_sum_with_queue(values, workers=8)
        ok = got == sum(values)
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
