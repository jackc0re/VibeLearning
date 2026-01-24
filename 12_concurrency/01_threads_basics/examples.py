"""Threads Basics - Examples

Demonstrations:
- starting and joining threads
- passing data back to the main thread
- using ThreadPoolExecutor

Run:
    python examples.py
"""

from __future__ import annotations

import threading
import time
from concurrent.futures import ThreadPoolExecutor


def demo_thread_start_join() -> None:
    def worker(name: str) -> None:
        print(f"[{name}] starting")
        time.sleep(0.1)
        print(f"[{name}] done")

    t = threading.Thread(target=worker, args=("worker-1",))
    t.start()
    t.join()


def demo_return_value_via_list() -> None:
    result: list[int] = []

    def compute() -> None:
        time.sleep(0.05)
        result.append(40 + 2)

    t = threading.Thread(target=compute)
    t.start()
    t.join()
    print("Returned value:", result[0])


def demo_thread_pool() -> None:
    def slow_double(x: int) -> int:
        time.sleep(0.05)
        return x * 2

    items = [1, 2, 3, 4]
    with ThreadPoolExecutor(max_workers=4) as executor:
        doubled = list(executor.map(slow_double, items))
    print("Thread pool results:", doubled)


if __name__ == "__main__":
    demo_thread_start_join()
    demo_return_value_via_list()
    demo_thread_pool()
