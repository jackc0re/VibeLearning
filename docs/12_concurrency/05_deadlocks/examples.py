"""Deadlocks - Examples

This file shows:
- a deadlock-prone pattern (handled with timeouts so it doesn't hang)
- a safe lock-ordering approach

Run:
    python examples.py
"""

from __future__ import annotations

import threading
import time


def demo_deadlock_prone_with_timeouts() -> None:
    a = threading.Lock()
    b = threading.Lock()

    def t1() -> None:
        with a:
            time.sleep(0.05)
            got = b.acquire(timeout=0.1)
            try:
                print("t1 got b:", got)
            finally:
                if got:
                    b.release()

    def t2() -> None:
        with b:
            time.sleep(0.05)
            got = a.acquire(timeout=0.1)
            try:
                print("t2 got a:", got)
            finally:
                if got:
                    a.release()

    x = threading.Thread(target=t1)
    y = threading.Thread(target=t2)
    x.start()
    y.start()
    x.join()
    y.join()


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

    print("Lock ordering demo completed")


if __name__ == "__main__":
    demo_deadlock_prone_with_timeouts()
    demo_lock_ordering()
