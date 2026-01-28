"""Synchronization - Exercises

Focus:
- protect shared state with Lock
- coordinate work using Queue and Event

Run with:
    python exercises.py
"""

from __future__ import annotations

import queue
import threading
import time
from typing import List


# =============================================================================
# EXERCISE 1: ThreadSafeCounter
# =============================================================================


class ThreadSafeCounter:
    def __init__(self) -> None:
        self._value = 0
        self._lock = threading.Lock()

    def increment(self, amount: int = 1) -> None:
        """Increase the counter safely."""

        with self._lock:
            self._value += amount

    def get(self) -> int:
        """Read the counter safely."""

        with self._lock:
            return self._value


# =============================================================================
# EXERCISE 2: Producer/Consumer
# =============================================================================


def exercise_2_double_with_workers(items: List[int], workers: int) -> List[int]:
    """Use worker threads + Queue to return [item*2] for each item.

    The order does not matter.
    """

    if workers <= 0:
        raise ValueError("workers must be >= 1")

    work_q: "queue.Queue[int]" = queue.Queue()
    for item in items:
        work_q.put(item)

    results: List[int] = []
    results_lock = threading.Lock()

    def worker() -> None:
        while True:
            try:
                item = work_q.get_nowait()
            except queue.Empty:
                return
            try:
                out = item * 2
                with results_lock:
                    results.append(out)
            finally:
                work_q.task_done()

    threads = [threading.Thread(target=worker) for _ in range(min(workers, len(items) or 1))]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return results


# =============================================================================
# EXERCISE 3: Wait For Event
# =============================================================================


def exercise_3_wait_for_event(timeout: float) -> bool:
    """Return True if an event is set within timeout seconds."""

    event = threading.Event()

    def setter() -> None:
        time.sleep(0.05)
        event.set()

    t = threading.Thread(target=setter)
    t.start()
    ok = event.wait(timeout=timeout)
    t.join()
    return ok


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Synchronization Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: ThreadSafeCounter")
    try:
        counter = ThreadSafeCounter()

        def inc_many() -> None:
            for _ in range(25_000):
                counter.increment()

        threads = [threading.Thread(target=inc_many) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        got = counter.get()
        ok = got == 100_000
        print("  ", "PASS" if ok else "FAIL", got)
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2
    print("\nExercise 2: Producer/Consumer")
    try:
        items = list(range(20))
        got = exercise_2_double_with_workers(items, workers=4)
        ok = sorted(got) == sorted([i * 2 for i in items])
        print("  ", "PASS" if ok else "FAIL", got[:5], "...")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3
    print("\nExercise 3: Wait For Event")
    try:
        ok1 = exercise_3_wait_for_event(timeout=0.5) is True
        ok2 = exercise_3_wait_for_event(timeout=0.01) is False
        ok = ok1 and ok2
        print("  ", "PASS" if ok else "FAIL", "timeouts behave")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
