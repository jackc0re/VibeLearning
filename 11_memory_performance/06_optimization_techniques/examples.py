"""Optimization Techniques - Examples
====================================

Demonstrations:
- measuring wall-clock time with time.perf_counter
- micro-benchmarks with timeit (list vs set membership)
- finding hot spots with cProfile
- caching with functools.lru_cache
- string joining

The theme is "measure first": every optimization below is backed
by a measurement, not a guess.

Run:
    python examples.py
"""

from __future__ import annotations

import cProfile
import io
import pstats
import time
import timeit
from functools import lru_cache
from pathlib import Path


# =============================================================================
# MEASURING HELPERS
# =============================================================================

def concat_with_plus(parts: list[str]) -> str:
    """Build one string with += in a loop (creates many intermediates)."""
    result = ""
    for part in parts:
        result += part
    return result


def concat_with_join(parts: list[str]) -> str:
    """Build one string with ''.join (one pass, no intermediates)."""
    return "".join(parts)


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def slow_pair_count(items: list[int]) -> int:
    """Deliberately O(n^2): count pairs (used for the cProfile demo)."""
    count = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] < items[j]:
                count += 1
    return count


# =============================================================================
# DEMO: MEASURE WITH time.perf_counter
# =============================================================================

def demo_perf_counter() -> None:
    parts = ["abc"] * 20_000

    start = time.perf_counter()
    concat_with_plus(parts)
    plus_seconds = time.perf_counter() - start

    start = time.perf_counter()
    concat_with_join(parts)
    join_seconds = time.perf_counter() - start

    print("Measuring with time.perf_counter (string building, 20000 parts):")
    print(f"  += in loop : {plus_seconds:.6f} seconds")
    print(f"  ''.join    : {join_seconds:.6f} seconds")
    if join_seconds > 0:
        print(f"  join was about {plus_seconds / join_seconds:.1f}x faster this run")
    print("  (exact numbers vary - the point is to measure, not to memorize)")


# =============================================================================
# DEMO: MICRO-BENCHMARKS WITH timeit
# =============================================================================

def demo_timeit() -> None:
    # timeit runs the statement many times and reports total seconds,
    # so tiny differences don't fool us. repeat() runs it several times;
    # taking the minimum filters out noise from other programs.
    list_setup = "data = list(range(2000)); target = 1999"
    set_setup = "data = set(range(2000)); target = 1999"

    list_seconds = min(
        timeit.repeat("target in data", setup=list_setup, number=200, repeat=3)
    )
    set_seconds = min(
        timeit.repeat("target in data", setup=set_setup, number=200, repeat=3)
    )

    print("\nMicro-benchmark with timeit (membership check, 200 x 2000 items):")
    print(f"  target in list: {list_seconds:.6f} seconds")
    print(f"  target in set : {set_seconds:.6f} seconds")
    print("  sets win for membership because hashing skips the scan")


# =============================================================================
# DEMO: FIND HOT SPOTS WITH cProfile
# =============================================================================

def demo_cprofile() -> None:
    data = list(range(1500))

    profiler = cProfile.Profile()
    profiler.enable()
    slow_pair_count(data)
    profiler.disable()

    # Render the stats into a string so we control exactly what is printed,
    # and keep the report machine-independent (file name, not full path).
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("cumulative").print_stats(3)
    report = stream.getvalue().replace(str(Path(__file__).resolve().parent), ".")
    print("\ncProfile on a deliberately slow function (pair counting):")
    print(report.strip())
    print("-> one function dominates: optimize THIS, not the rest")


# =============================================================================
# DEMO: CACHING AND JOINING
# =============================================================================

def demo_caching_and_joining() -> None:
    print("Caching with functools.lru_cache:")
    print("  fib(10):", fib(10))
    print("  fib(20):", fib(20))
    print("  cache info:", fib.cache_info())

    join_demo = "".join(["a", "b", "c"])
    print("\nJoining strings:")
    print("  join_demo:", join_demo)


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("OPTIMIZATION TECHNIQUES - Examples")
    print("=" * 50)

    print("\n--- Measuring with time.perf_counter ---\n")
    demo_perf_counter()

    print("\n--- Micro-benchmarks with timeit ---")
    demo_timeit()

    print("\n--- Finding hot spots with cProfile ---")
    demo_cprofile()

    print("\n--- Caching and joining ---")
    demo_caching_and_joining()

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
