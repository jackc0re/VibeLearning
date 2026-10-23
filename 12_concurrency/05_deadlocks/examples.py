"""Deadlocks - Examples
======================

This file shows:
- a deadlock-prone pattern (handled with timeouts so it doesn't hang)
- a safe lock-ordering approach

Run:
    python examples.py
"""

from __future__ import annotations

import threading
import time


# =============================================================================
# DEMO: DEADLOCK-PRONE PATTERN, RESCUED BY TIMEOUTS
# =============================================================================

def demo_deadlock_prone_with_timeouts() -> None:
    a = threading.Lock()
    b = threading.Lock()

    def t1() -> None:
        with a:  # t1 holds lock a...
            time.sleep(0.05)  # ...long enough for t2 to take lock b
            got = b.acquire(timeout=0.1)  # t1 wants b (held by t2)
            try:
                print("t1 got b:", got)
            finally:
                if got:
                    b.release()

    def t2() -> None:
        with b:  # t2 holds lock b...
            time.sleep(0.05)  # ...long enough for t1 to take lock a
            got = a.acquire(timeout=0.1)  # t2 wants a (held by t1)
            try:
                print("t2 got a:", got)
            finally:
                if got:
                    a.release()

    print("Deadlock-prone pattern (crossed lock acquisition):")
    x = threading.Thread(target=t1)
    y = threading.Thread(target=t2)
    x.start()
    y.start()
    x.join()
    y.join()

    # Why you see False above:
    #   t1 holds a and waits for b, while t2 holds b and waits for a.
    #   Each is waiting for a lock the other one holds - a deadlock.
    #   The timeout=0.1 rescues us: instead of waiting forever, each
    #   acquire() gives up after 0.1 seconds and returns False.
    #   False = "I did NOT get the lock", so no one froze; both threads
    #   then finish and release the lock they were holding.
    #   Without the timeout, BOTH prints would never run at all -
    #   the program would just hang.
    print("\nWhy False? Each thread wanted the lock the other one held.")
    print("acquire(timeout=0.1) gave up and returned False instead of")
    print("blocking forever. Without a timeout this demo would hang: a real deadlock.")


# =============================================================================
# DEMO: SAFE LOCK ORDERING
# =============================================================================

def demo_lock_ordering() -> None:
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    def acquire_in_order(l1: threading.Lock, l2: threading.Lock) -> None:
        first, second = (l1, l2) if id(l1) < id(l2) else (l2, l1)
        with first:
            with second:
                time.sleep(0.01)

    threads = [threading.Thread(target=acquire_in_order, args=(lock1, lock2)) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("\nLock ordering demo completed")
    print("-> everyone acquires in the same global order, so no cycle can form")


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("DEADLOCKS - Examples")
    print("=" * 50)

    print("\n--- Deadlock-prone pattern with timeouts ---\n")
    demo_deadlock_prone_with_timeouts()

    print("\n--- Prevention: lock ordering ---")
    demo_lock_ordering()

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
