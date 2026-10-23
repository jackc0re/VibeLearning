"""Race Conditions - Examples
============================

Demonstrations:
- an unsafe shared counter (race)
- the same counter protected by a lock

Run:
    python examples.py
"""

from __future__ import annotations

import threading
import time


# =============================================================================
# DEMO: UNSAFE COUNTER (RACE CONDITION)
# =============================================================================

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
    if counter["value"] == 80_000:
        print("  (No lost updates this run - the race depends on timing.)")
    else:
        print("  (Increments were lost - the exact count varies between runs.)")


# =============================================================================
# DEMO: SAME COUNTER PROTECTED BY A LOCK
# =============================================================================

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


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("RACE CONDITIONS - Examples")
    print("=" * 50)

    print("\n--- Unsafe counter (race) ---\n")
    demo_race_counter()

    print("\n--- Fixed with a lock ---")
    demo_fixed_with_lock()

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
