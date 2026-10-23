"""Threads Basics - Examples
===========================

Demonstrations:
- starting and joining threads
- passing data back to the main thread
- using ThreadPoolExecutor
- CPU-bound work in processes with multiprocessing (bypasses the GIL)

Run:
    python examples.py
"""

from __future__ import annotations

import multiprocessing
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor


# =============================================================================
# DEMO: START AND JOIN A THREAD
# =============================================================================

def demo_thread_start_join() -> None:
    def worker(name: str) -> None:
        print(f"[{name}] starting")
        time.sleep(0.1)
        print(f"[{name}] done")

    t = threading.Thread(target=worker, args=("worker-1",))
    t.start()
    t.join()


# =============================================================================
# DEMO: PASS RESULTS BACK VIA A SHARED LIST
# =============================================================================

def demo_return_value_via_list() -> None:
    result: list[int] = []

    def compute() -> None:
        time.sleep(0.05)
        result.append(40 + 2)

    t = threading.Thread(target=compute)
    t.start()
    t.join()
    print("Returned value:", result[0])


# =============================================================================
# DEMO: THREAD POOL (I/O-STYLE OVERLAP)
# =============================================================================

def demo_thread_pool() -> None:
    def slow_double(x: int) -> int:
        time.sleep(0.05)
        return x * 2

    items = [1, 2, 3, 4]
    with ThreadPoolExecutor(max_workers=4) as executor:
        doubled = list(executor.map(slow_double, items))
    print("Thread pool results:", doubled)


# =============================================================================
# DEMO: CPU-BOUND WORK IN PROCESSES (BYPASSES THE GIL)
# =============================================================================

def _cpu_worker(label: str, n: int) -> None:
    """Runs inside a child process: sum the squares 0..n-1.

    Must be a top-level function so it can be pickled and sent
    to the child process.
    """
    total = sum(i * i for i in range(n))
    print(f"  [{label}] sum of squares = {total}")


def demo_multiprocessing_cpu_bound() -> None:
    print("Two processes doing CPU-bound sums in parallel:")
    # Flush the parent's output first so child-process prints can't
    # appear *before* the text above in piped/redirected output.
    sys.stdout.flush()
    workers = [
        multiprocessing.Process(target=_cpu_worker, args=(f"worker-{i}", 1_500_000))
        for i in range(2)
    ]
    for w in workers:
        w.start()
    for w in workers:
        w.join(timeout=15)
        if w.is_alive():
            # Never wait forever: stop the child and report.
            w.terminate()
            w.join(timeout=5)
            print(f"  {w.name}: terminated (took too long)")
        else:
            print(f"  {w.name}: finished, exit code {w.exitcode}")
    print("-> each process has its own interpreter and GIL, so they truly run in parallel")


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("THREADS BASICS - Examples")
    print("=" * 50)

    print("\n--- Start and join a thread ---\n")
    demo_thread_start_join()

    print("\n--- Returning a value via a shared list ---")
    demo_return_value_via_list()

    print("\n--- Thread pool ---")
    demo_thread_pool()

    print("\n--- Multiprocessing for CPU-bound work ---")
    demo_multiprocessing_cpu_bound()

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
