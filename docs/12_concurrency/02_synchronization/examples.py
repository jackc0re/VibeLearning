"""Synchronization - Examples

Demonstrations:
- using Lock to protect shared state
- using Event to coordinate thread start
- using Semaphore to limit concurrency

Run:
    python examples.py
"""

from __future__ import annotations

import threading
import time


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


if __name__ == "__main__":
    demo_lock_counter()
    demo_event_signal()
    demo_semaphore_limit()
