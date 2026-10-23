"""Synchronization - Examples
============================

Demonstrations:
- using Lock to protect shared state
- using RLock for genuinely re-entrant call paths
- using Event to coordinate thread start
- using Semaphore to limit concurrency

Run:
    python examples.py
"""

from __future__ import annotations

import threading
import time


# =============================================================================
# DEMO: LOCK PROTECTS SHARED STATE
# =============================================================================

def demo_lock_counter() -> None:
    lock = threading.Lock()
    counter = {"value": 0}

    def inc_many(times: int) -> None:
        for _ in range(times):
            with lock:
                counter["value"] += 1

    threads = [threading.Thread(target=inc_many, args=(50_000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Counter value (expected 200000):", counter["value"])


# =============================================================================
# DEMO: RLOCK FOR RE-ENTRANT CALLS
# =============================================================================

class Basket:
    """A tiny class whose public method calls another locked method.

    Both methods acquire the same lock. With an RLock this works,
    because the owning thread may re-enter. With a plain Lock the
    second acquire would block forever: the thread would be waiting
    for a lock it already holds.
    """

    def __init__(self) -> None:
        self.items: list[str] = []
        self._lock = threading.RLock()

    def add(self, item: str) -> None:
        with self._lock:  # acquire 1
            self._audit()
            self.items.append(item)

    def _audit(self) -> None:
        with self._lock:  # acquire 2 - same thread re-entering: OK for RLock
            print(f"  audit: {len(self.items)} item(s) so far")


def demo_rlock_reentrancy() -> None:
    print("Re-entrant calls with RLock:")
    basket = Basket()
    basket.add("apple")
    basket.add("banana")
    print("  basket:", basket.items)

    # Contrast: a plain Lock does NOT let the same thread re-acquire it.
    # We probe without blocking, so this can never deadlock the demo.
    plain = threading.Lock()
    plain.acquire()
    got_again = plain.acquire(blocking=False)
    print("Same thread re-acquiring a plain Lock (blocking=False):", got_again)
    print("-> that False is the freeze an RLock avoids; release it and move on")
    plain.release()


# =============================================================================
# DEMO: EVENT SIGNALS
# =============================================================================

def demo_event_signal() -> None:
    started = threading.Event()

    def worker() -> None:
        print("Worker waiting...")
        started.wait()
        print("Worker running!")

    t = threading.Thread(target=worker)
    t.start()

    time.sleep(0.1)
    print("Main: signaling event")
    started.set()
    t.join()


# =============================================================================
# DEMO: SEMAPHORE LIMITS CONCURRENCY
# =============================================================================

def demo_semaphore_limit() -> None:
    sem = threading.Semaphore(2)

    def task(i: int) -> None:
        with sem:
            print(f"Task {i} entered")
            time.sleep(0.1)
            print(f"Task {i} leaving")

    threads = [threading.Thread(target=task, args=(i,)) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("SYNCHRONIZATION - Examples")
    print("=" * 50)

    print("\n--- Lock protects shared state ---\n")
    demo_lock_counter()

    print("\n--- RLock for re-entrant calls ---")
    demo_rlock_reentrancy()

    print("\n--- Event signals ---")
    demo_event_signal()

    print("\n--- Semaphore limits concurrency ---")
    demo_semaphore_limit()

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
