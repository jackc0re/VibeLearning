"""
Advanced Exercise 2: Performance Optimization
=============================================
Speed up slow algorithms, shrink memory use, profile hot spots,
and see what memoization buys you.
"""

import time

print("=" * 50)
print("EXERCISE 2: Performance Optimization")
print("=" * 50)


# =============================================================================
# EXERCISE 2.1: Algorithm Optimization (Quadratic -> Linear)
# =============================================================================
print("\n--- Exercise 2.1: Algorithm Optimization ---")
"""
has_duplicates_v1 (shown in the solutions) checks every pair: O(n^2).

Write has_duplicates_v2 that tracks seen values in a set so it
finishes in O(n) average time. The solution benchmarks both on
data = list(range(1500)).
"""


# Your code below:
def has_duplicates_v2(values):
    """Return True if any value appears twice. Aim for O(n)."""
    pass


# Test (uncomment after implementing)
# print(has_duplicates_v2([1, 2, 3, 2]))  # True


# =============================================================================
# EXERCISE 2.2: Big O Analysis (Two Sum)
# =============================================================================
print("\n--- Exercise 2.2: Big O Analysis (Two Sum) ---")
"""
two_sum_v1 uses nested loops: O(n^2).

Write two_sum_v2 that scans once, keeping a set of numbers already
seen; for each number check whether target - number was seen.
Return the pair (earlier, later) or None. Target O(n).
"""


# Your code below:
def two_sum_v2(numbers, target):
    """Return two numbers adding to target, or None. Aim for O(n)."""
    pass


# Test (uncomment after implementing)
# print(two_sum_v2([3, 8, 12, 5, 1, 9, 4], 13))


# =============================================================================
# EXERCISE 2.3: Memory Optimization (List -> Generator)
# =============================================================================
print("\n--- Exercise 2.3: Memory Optimization ---")
"""
sum_squares_list builds a full list of n squares before summing.

Write sum_squares_gen(n) with a generator expression so no list is
ever materialized. The solution compares results and memory use
with sys.getsizeof.
"""

import sys


# Your code below:
def sum_squares_gen(n):
    """Sum of squares 1..n using a generator expression."""
    pass


# Test (uncomment after implementing)
# print(sum_squares_gen(10))  # 385


# =============================================================================
# EXERCISE 2.4: Profiling and Benchmarking
# =============================================================================
print("\n--- Exercise 2.4: Profiling and Benchmarking ---")
"""
build_report_v1 (in the solutions) grows a string with += inside a
loop, which copies the string over and over.

Write build_report_v2(lines) using join. Then the solution profiles
v1 with cProfile and times both versions.
"""


# Your code below:
def build_report_v2(lines):
    """Build the same report with join instead of +=."""
    pass


# Test (uncomment after implementing)
# print(build_report_v2(["a", "b"]))


# =============================================================================
# EXERCISE 2.5: Memoization
# =============================================================================
print("\n--- Exercise 2.5: Memoization ---")
"""
fib_v1 (in the solutions) recomputes the same subproblems
exponentially many times.

Write fib_v2 with functools.lru_cache. The solution counts how many
calls each version needs to compute fib(25).
"""

from functools import lru_cache


# Your code below:
def fib_v2(n):
    """Return fib(n), memoized with lru_cache."""
    pass


# Test (uncomment after implementing)
# print(fib_v2(25))  # 75025


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 2.1
print("\n--- Solution 2.1 ---")


def has_duplicates_v1(values):
    """Check every pair: O(n^2)."""
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return True
    return False


def has_duplicates_v2(values):
    """Track seen values in a set: O(n) average."""
    seen = set()
    for value in values:
        if value in seen:
            return True
        seen.add(value)
    return False


data = list(range(1500))

start = time.perf_counter()
result_v1 = has_duplicates_v1(data)
seconds_v1 = time.perf_counter() - start

start = time.perf_counter()
result_v2 = has_duplicates_v2(data)
seconds_v2 = time.perf_counter() - start

print(f"v1 nested loops: {result_v1} in {seconds_v1:.4f}s")
print(f"v2 set          : {result_v2} in {seconds_v2:.5f}s")
if seconds_v2 > 0:
    print(f"Speedup: about {seconds_v1 / seconds_v2:.0f}x")

# SOLUTION 2.2
print("\n--- Solution 2.2 ---")


def two_sum_v1(numbers, target):
    """Nested loops: O(n^2)."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])
    return None


def two_sum_v2(numbers, target):
    """One pass with a set: O(n) average."""
    seen = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return (complement, number)
        seen.add(number)
    return None


values = [3, 8, 12, 5, 1, 9, 4]
print(f"v1: two_sum for 13 -> {two_sum_v1(values, 13)}")
print(f"v2: two_sum for 13 -> {two_sum_v2(values, 13)}")
print(f"Same pair found: {two_sum_v1(values, 13) == two_sum_v2(values, 13)}")

# SOLUTION 2.3
print("\n--- Solution 2.3 ---")


def sum_squares_list(n):
    """Build every square first: O(n) time AND O(n) memory."""
    squares = [i * i for i in range(1, n + 1)]
    return sum(squares)


def sum_squares_gen(n):
    """Stream the squares: O(n) time, O(1) memory."""
    return sum(i * i for i in range(1, n + 1))


n = 1_000_000
result_list = sum_squares_list(n)
result_gen = sum_squares_gen(n)
big_list = [i * i for i in range(1, n + 1)]

print(f"Results match: {result_list == result_gen} (sum is {result_list})")
print(f"A list of {n:,} squares needs about {sys.getsizeof(big_list) / 1_000_000:.1f} MB")
print(f"A generator object needs about {sys.getsizeof(i * i for i in range(10))} bytes")
del big_list

# SOLUTION 2.4
print("\n--- Solution 2.4 ---")

import cProfile
import io
import pstats


def build_report_v1(lines):
    """String += in a loop: repeated copying."""
    report = ""
    for line in lines:
        report += line + "\n"
    return report


def build_report_v2(lines):
    """join once: linear."""
    return "\n".join(lines) + "\n"


rows = [f"row {i}: some sample text" for i in range(5_000)]

profiler = cProfile.Profile()
profiler.enable()
build_report_v1(rows)
profiler.disable()

stream = io.StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats("cumulative").print_stats(3)
hot_lines = [
    line.strip() for line in stream.getvalue().splitlines() if "build_report_v1" in line
]
print("cProfile on build_report_v1:")
for line in hot_lines:
    print(f"  {line}")

start = time.perf_counter()
report_v1 = build_report_v1(rows)
seconds_v1 = time.perf_counter() - start

start = time.perf_counter()
report_v2 = build_report_v2(rows)
seconds_v2 = time.perf_counter() - start

print(f"v1 (+=)  : {seconds_v1:.4f}s")
print(f"v2 (join): {seconds_v2:.5f}s")
print(f"Identical output: {report_v1 == report_v2}")

# SOLUTION 2.5
print("\n--- Solution 2.5 ---")

fib_v1_calls = 0


def fib_v1(n):
    """Exponential: recomputes the same subproblems."""
    global fib_v1_calls
    fib_v1_calls += 1
    if n < 2:
        return n
    return fib_v1(n - 1) + fib_v1(n - 2)


fib_v2_calls = 0


@lru_cache(maxsize=None)
def fib_v2(n):
    """Memoized: each subproblem computed once."""
    global fib_v2_calls
    fib_v2_calls += 1
    if n < 2:
        return n
    return fib_v2(n - 1) + fib_v2(n - 2)


result_naive = fib_v1(25)
result_memo = fib_v2(25)
print(f"fib(25) = {result_naive}")
print(f"fib_v1 calls: {fib_v1_calls:,}")
print(f"fib_v2 calls: {fib_v2_calls:,}")
print(f"Same answer: {result_naive == result_memo}")

print("\n" + "=" * 50)
print("Great job! Move on to 03_concurrency.py")
print("=" * 50)
