"""Race Conditions - Examples

Demonstrations:
- an unsafe shared counter (race)
- the same counter protected by a lock

Run:
    python examples.py
"""

from __future__ import annotations

import threading
import time


def demo_race_counter() -> None:
    counter = {"value": 0}

    def inc_many(times: int) -> None:
        for _ in range(times):
            # Intentionally widen the race window a bit.
            value = counter["value"]
            time.sleep(0)
            counter["value"] = value + 1

    threads = [threading.Thread(target=inc_many, args=(20_000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Unsafe counter expected 80000, got:", counter["value"])


def demo_fixed_with_lock() -> None:
    lock = threading.Lock()
    counter = {"value": 0}

    def inc_many(times: int) -> None:
        for _ in range(times):
            with lock:
                counter["value"] += 1

    threads = [threading.Thread(target=inc_many, args=(20_000,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Locked counter expected 80000, got:", counter["value"])


if __name__ == "__main__":
    demo_race_counter()
    demo_fixed_with_lock()
