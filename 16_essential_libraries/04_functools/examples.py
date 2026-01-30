"""
Functools Module - Examples
===========================
Higher-order functions and operations on callables.
"""

print("=" * 60)
print("FUNCTOOLS MODULE - Examples")
print("=" * 60)

from functools import partial, lru_cache, reduce, wraps, cmp_to_key

# =============================================================================
# PARTIAL FUNCTIONS
# =============================================================================
print("\n--- Partial Functions ---\n")

# Base function with multiple parameters
def format_message(level, timestamp, message):
    return f"[{timestamp}] [{level}] {message}"

# Create specialized versions
info_logger = partial(format_message, "INFO")
error_logger = partial(format_message, "ERROR")

# Use with remaining arguments
print(info_logger("2024-01-15 10:30:00", "Application started"))
print(error_logger("2024-01-15 10:31:00", "Connection failed"))

# Partial with positional arguments
base_2_log = partial(int, base=2)
print(f"\nBinary '1010' = {base_2_log('1010')}")

# Partial for common operations
multiply_by_10 = partial(lambda x, y: x * y, 10)
print(f"multiply_by_10(5) = {multiply_by_10(5)}")

# =============================================================================
# LRU CACHE
# =============================================================================
print("\n--- LRU Cache ---\n")

# Without cache - slow!
def fibonacci_no_cache(n):
    if n < 2:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

# With cache - fast!
@lru_cache(maxsize=128)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

import time

# Compare performance
n = 30

start = time.time()
result1 = fibonacci_no_cache(n)
duration1 = time.time() - start

start = time.time()
result2 = fibonacci_cached(n)
duration2 = time.time() - start

print(f"Fibonacci({n}) = {result2}")
print(f"Without cache: {duration1:.4f} seconds")
print(f"With cache: {duration2:.6f} seconds")
print(f"Speedup: {duration1/duration2:.0f}x")

# Check cache info
print(f"\nCache info: {fibonacci_cached.cache_info()}")

# Clear cache if needed
# fibonacci_cached.cache_clear()

# =============================================================================
# REDUCE
# =============================================================================
print("\n--- Reduce ---\n")

numbers = [1, 2, 3, 4, 5]

# Sum
sum_result = reduce(lambda acc, x: acc + x, numbers)
print(f"Sum of {numbers}: {sum_result}")

# Product
product = reduce(lambda acc, x: acc * x, numbers)
print(f"Product of {numbers}: {product}")

# Maximum
maximum = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(f"Maximum of {numbers}: {maximum}")

# Concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda acc, word: acc + word, words)
print(f"Concatenated: '{sentence}'")

# Flatten nested lists (not efficient but demonstrates reduce)
nested = [[1, 2], [3, 4], [5, 6]]
flat = reduce(lambda acc, lst: acc + lst, nested, [])
print(f"Flattened {nested}: {flat}")

# =============================================================================
# WRAPS - Preserving Metadata
# =============================================================================
print("\n--- Wraps Decorator ---\n")

# Without @wraps - metadata is lost
def timer_no_wraps(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time() - start:.4f} seconds")
        return result
    return wrapper

@timer_no_wraps
def greet_no_wraps():
    """Say hello to the world."""
    print("Hello!")

print("Without @wraps:")
print(f"  Function name: {greet_no_wraps.__name__}")
print(f"  Docstring: {greet_no_wraps.__doc__}")

# With @wraps - metadata preserved
def timer_with_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time() - start:.4f} seconds")
        return result
    return wrapper

@timer_with_wraps
def greet_with_wraps():
    """Say hello to the world."""
    print("Hello!")

print("\nWith @wraps:")
print(f"  Function name: {greet_with_wraps.__name__}")
print(f"  Docstring: {greet_with_wraps.__doc__}")

# =============================================================================
# CMP_TO_KEY
# =============================================================================
print("\n--- cmp_to_key ---\n")

# Custom comparison function
def compare_by_second_char(a, b):
    """Compare strings by their second character."""
    return ord(a[1]) - ord(b[1])

words = ['cat', 'dog', 'apple', 'bat', 'elephant']
sorted_words = sorted(words, key=cmp_to_key(compare_by_second_char))
print(f"Original: {words}")
print(f"Sorted by 2nd char: {sorted_words}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n--- Practical Examples ---\n")

# Example 1: Memoized recursive function
@lru_cache(maxsize=None)
def count_ways_to_climb(n, allowed_steps=(1, 2)):
    """
    Count ways to climb n stairs, taking steps of sizes in allowed_steps.
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    return sum(count_ways_to_climb(n - step, allowed_steps)
               for step in allowed_steps)

print("Ways to climb 10 stairs (steps 1 or 2):",
      count_ways_to_climb(10))
print("Ways to climb 10 stairs (steps 1, 2, or 3):",
      count_ways_to_climb(10, (1, 2, 3)))

# Example 2: Partial for API client
class APIClient:
    def request(self, method, endpoint, **kwargs):
        return f"{method} {endpoint} with {kwargs}"

client = APIClient()
get = partial(client.request, "GET")
post = partial(client.request, "POST")

print(f"\nAPI calls:")
print(get("/users"))
print(post("/users", json={"name": "Alice"}))

# Example 3: Reduce for data processing
def pipeline(data, *functions):
    """Apply a series of functions to data using reduce."""
    return reduce(lambda acc, func: func(acc), functions, data)

def double(x):
    return x * 2

def add_one(x):
    return x + 1

def to_string(x):
    return str(x)

result = pipeline(5, double, add_one, to_string)
print(f"\nPipeline result: {result}")

# Example 4: Counting with reduce
from collections import Counter

def merge_counts(c1, c2):
    """Merge two counters."""
    return c1 + c2

list_of_counters = [
    Counter(['a', 'b', 'a']),
    Counter(['b', 'c', 'c']),
    Counter(['a', 'c', 'd']),
]

total_count = reduce(merge_counts, list_of_counters)
print(f"\nMerged counts: {dict(total_count)}")

# Example 5: Compose functions
def compose(*functions):
    """Compose multiple functions right to left."""
    def composed(x):
        return reduce(lambda v, f: f(v), reversed(functions), x)
    return composed

def add5(x):
    return x + 5

def mul3(x):
    return x * 3

def square(x):
    return x ** 2

# compose(square, mul3, add5) means: square(mul3(add5(x)))
transform = compose(square, mul3, add5)
print(f"\ncompose(square, mul3, add5)(2) = {transform(2)}")  # (2+5)*3 squared = 441

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
