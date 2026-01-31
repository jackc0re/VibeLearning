"""
Functools Module - Exercises
============================
Practice problems for functools.
"""

print("=" * 60)
print("FUNCTOOLS MODULE - Exercises")
print("=" * 60)

from functools import partial, lru_cache, reduce, wraps

# =============================================================================
# EXERCISE 1: Partial for Unit Conversion
# =============================================================================
print("\n--- Exercise 1: Unit Conversion with Partial ---\n")
"""
Create a generic conversion function, then use partial to create specific
converters for common units.

Example:
    convert(value, from_unit, to_unit, conversion_factors)

    celsius_to_fahrenheit = partial(convert, ...)
    km_to_miles = partial(convert, ...)
"""

def convert(value, from_unit, to_unit, factors):
    """
    Convert value between units using conversion factors (to base unit).
    factors is a dict: {unit: factor_to_base}
    """
    # Your code here
    # Convert to base unit, then to target unit
    pass  # TODO: Implement

# Create partial functions
# celsius_to_fahrenheit = partial(convert, ...)
# km_to_miles = partial(convert, ...)
# kg_to_pounds = partial(convert, ...)

# Test
# print(celsius_to_fahrenheit(0))   # Should be 32.0
# print(celsius_to_fahrenheit(100)) # Should be 212.0
# print(km_to_miles(10))            # Should be ~6.21

# =============================================================================
# EXERCISE 2: Cached Factorial
# =============================================================================
print("\n--- Exercise 2: Cached Factorial ---\n")
"""
Write a recursive factorial function with lru_cache.
Compare performance with and without caching for large inputs.
"""

@lru_cache(maxsize=None)
def factorial_cached(n):
    """
    Calculate factorial with caching.
    """
    # Your code here
    pass  # TODO: Implement

def factorial_no_cache(n):
    """
    Calculate factorial without caching.
    """
    # Your code here
    pass  # TODO: Implement

# Compare performance
# import time
# n = 100
# Test both versions and print cache info

# =============================================================================
# EXERCISE 3: Reduce for Statistics
# =============================================================================
print("\n--- Exercise 3: Statistics with Reduce ---\n")
"""
Use reduce to calculate statistics (mean, variance) in a single pass.

Hint: Track running sum and sum of squares using reduce.
"""

def running_stats(numbers):
    """
    Calculate mean and variance in a single pass using reduce.
    Returns (mean, variance).

    Hint: Use reduce to accumulate (count, sum, sum_of_squares)
    """
    # Your code here
    # Use reduce to get count, sum, and sum of squares
    # Calculate mean and variance from accumulated values
    pass  # TODO: Implement

# Test
# data = [1, 2, 3, 4, 5]
# mean, var = running_stats(data)
# print(f"Mean: {mean}, Variance: {var}")

# =============================================================================
# EXERCISE 4: Decorator with Wraps
# =============================================================================
print("\n--- Exercise 4: Decorator with Wraps ---\n")
"""
Create a decorator that counts how many times a function is called.
Use @wraps to preserve function metadata.
"""

def count_calls(func):
    """
    Decorator that counts function calls.
    Adds a .call_count attribute to the function.
    Use @wraps to preserve metadata.
    """
    # Your code here
    # Use wraps decorator
    # Increment counter on each call
    pass  # TODO: Implement

# Test
# @count_calls
# def greet(name):
#     '''Greet someone.'''
#     return f"Hello, {name}!"
#
# greet("Alice")
# greet("Bob")
# print(f"Called {greet.call_count} times")
# print(f"Function name: {greet.__name__}")
# print(f"Docstring: {greet.__doc__}")

# =============================================================================
# EXERCISE 5: Partial for HTML Tags
# =============================================================================
print("\n--- Exercise 5: HTML Tags with Partial ---\n")
"""
Create a function that wraps text in HTML tags.
Use partial to create shortcuts for common tags.

Example:
    wrap('Hello', 'b') -> '<b>Hello</b>'
    bold = partial(wrap, tag='b')
    italic = partial(wrap, tag='i')
"""

def wrap(text, tag):
    """
    Wrap text in an HTML tag.
    """
    # Your code here
    pass  # TODO: Implement

# Create partials for common tags
# bold = partial(wrap, ...)
# italic = partial(wrap, ...)
# underline = partial(wrap, ...)

# Test
# print(bold("Important"))
# print(italic("Emphasis"))

# =============================================================================
# EXERCISE 6: Compose with Reduce
# =============================================================================
print("\n--- Exercise 6: Function Composition ---\n")
"""
Implement function composition using reduce.
compose(f, g, h)(x) should equal f(g(h(x))).

Use functools.reduce to chain the functions together.
"""

def compose(*functions):
    """
    Compose functions right to left using reduce.
    compose(f, g, h)(x) = f(g(h(x)))
    """
    # Your code here
    # Use reduce to apply functions in reverse order
    pass  # TODO: Implement

# Test
# def add1(x): return x + 1
# def mul2(x): return x * 2
# def square(x): return x ** 2
#
# f = compose(square, mul2, add1)
# print(f(3))  # square(mul2(add1(3))) = square(mul2(4)) = square(8) = 64

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# =============================================================================
# SOLUTION 1: Unit Conversion
# =============================================================================
print("\n--- Solution 1: Unit Conversion ---\n")

def convert_solution(value, from_unit, to_unit, factors):
    base_value = value * factors[from_unit]
    return base_value / factors[to_unit]

# Temperature: treat specially (offset vs scale)
def convert_temp(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    # Convert to Celsius first
    if from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        celsius = value

    # Convert from Celsius
    if to_unit == 'F':
        return celsius * 9/5 + 32
    elif to_unit == 'K':
        return celsius + 273.15
    return celsius

celsius_to_fahrenheit = partial(convert_temp, from_unit='C', to_unit='F')
km_to_miles = partial(convert_solution, from_unit='km', to_unit='miles',
                      factors={'km': 1, 'miles': 1.60934})

print(f"0°C = {celsius_to_fahrenheit(0):.1f}°F")
print(f"100°C = {celsius_to_fahrenheit(100):.1f}°F")
print(f"10 km = {km_to_miles(10):.2f} miles")

# =============================================================================
# SOLUTION 2: Cached Factorial
# =============================================================================
print("\n--- Solution 2: Cached Factorial ---\n")

@lru_cache(maxsize=None)
def factorial_cached_solution(n):
    if n <= 1:
        return 1
    return n * factorial_cached_solution(n - 1)

def factorial_no_cache_solution(n):
    if n <= 1:
        return 1
    return n * factorial_no_cache_solution(n - 1)

import time

n = 100

# Warm up cache
factorial_cached_solution(n)
factorial_cached_solution.cache_clear()

start = time.time()
factorial_cached_solution(n)
duration_cached = time.time() - start

start = time.time()
factorial_no_cache_solution(n)
duration_no_cache = time.time() - start

print(f"Factorial({n}) cached took: {duration_cached:.6f}s")
print(f"Factorial({n}) no cache took: {duration_no_cache:.6f}s")
print(f"Cache info: {factorial_cached_solution.cache_info()}")

# =============================================================================
# SOLUTION 3: Statistics with Reduce
# =============================================================================
print("\n--- Solution 3: Statistics with Reduce ---\n")

def running_stats_solution(numbers):
    if not numbers:
        return (0, 0)

    # Accumulate (count, sum, sum_of_squares)
    def accumulate(acc, x):
        count, sum_val, sum_sq = acc
        return (count + 1, sum_val + x, sum_sq + x * x)

    count, total, sum_squares = reduce(accumulate, numbers, (0, 0, 0))

    mean = total / count
    # Variance = E[X^2] - E[X]^2
    variance = (sum_squares / count) - (mean ** 2)

    return (mean, variance)

data = [1, 2, 3, 4, 5]
mean, var = running_stats_solution(data)
print(f"Data: {data}")
print(f"Mean: {mean:.2f}, Variance: {var:.2f}")

# =============================================================================
# SOLUTION 4: Decorator with Wraps
# =============================================================================
print("\n--- Solution 4: Decorator with Wraps ---\n")

def count_calls_solution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls_solution
def greet_solution(name):
    '''Greet someone.'''
    return f"Hello, {name}!"

greet_solution("Alice")
greet_solution("Bob")
greet_solution("Charlie")
print(f"Called {greet_solution.call_count} times")
print(f"Function name: {greet_solution.__name__}")
print(f"Docstring: {greet_solution.__doc__}")

# =============================================================================
# SOLUTION 5: HTML Tags
# =============================================================================
print("\n--- Solution 5: HTML Tags ---\n")

def wrap_solution(text, tag):
    return f"<{tag}>{text}</{tag}>"

bold = partial(wrap_solution, tag='b')
italic = partial(wrap_solution, tag='i')
underline = partial(wrap_solution, tag='u')

print(bold("Important"))
print(italic("Emphasis"))
print(underline("Underlined"))

# =============================================================================
# SOLUTION 6: Function Composition
# =============================================================================
print("\n--- Solution 6: Function Composition ---\n")

def compose_solution(*functions):
    def composed(x):
        return reduce(lambda v, f: f(v), reversed(functions), x)
    return composed

def add1(x): return x + 1
def mul2(x): return x * 2
def square(x): return x ** 2

f = compose_solution(square, mul2, add1)
print(f"compose(square, mul2, add1)(3) = {f(3)}")
# square(mul2(add1(3))) = square(mul2(4)) = square(8) = 64

print("\n" + "=" * 60)
print("Exercises complete!")
print("=" * 60)
