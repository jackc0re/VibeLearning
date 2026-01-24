# Functional Programming Cheatsheet

Quick reference for functional programming in Python: lambdas, higher-order functions, map/filter/reduce, closures, and decorators.

---

## Pure Functions

### What Makes a Function Pure?
```python
# Pure: Same input → Same output, no side effects
def add(a, b):
    return a + b

# Impure: Has side effects
def impure_add(a, b):
    print("Adding...")      # Side effect
    return a + b

# Impure: Depends on external state
counter = 0
def increment():
    global counter
    counter += 1           # Modifies external state
    return counter
```

### Benefits of Pure Functions
- Predictable: Same input always gives same output
- Testable: Easy to unit test
- Cacheable: Results can be memoized
- Parallelizable: No shared state issues

---

## Lambda Functions

### Syntax & Basics
```python
# Basic lambda
add = lambda x, y: x + y
print(add(2, 3))          # 5

# Without name (immediately invoked)
print((lambda x: x * 2)(5))  # 10

# Multiple parameters
mult = lambda x, y, z: x * y * z
print(mult(2, 3, 4))      # 24
```

### Lambda Use Cases
```python
# With sort (key function)
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
people.sort(key=lambda p: p[1])  # Sort by age
# [("Bob", 20), ("Alice", 25), ("Charlie", 30)]

# With max/min
people = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 20}]
oldest = max(people, key=lambda p: p["age"])

# With filter
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# With map
squares = list(map(lambda x: x ** 2, numbers))  # [1, 4, 9, 16, 25]
```

### Lambda vs Regular Function
```python
# Lambda (short, simple)
is_even = lambda x: x % 2 == 0

# Regular function (can do more)
def is_even(x):
    """Check if number is even."""
    return x % 2 == 0

# Use lambda for short, throwaway functions
# Use regular functions for anything reusable or complex
```

---

## Higher-Order Functions

### Functions as Arguments
```python
def apply_operation(x, y, operation):
    """Apply operation to x and y."""
    return operation(x, y)

result = apply_operation(5, 3, lambda a, b: a + b)  # 8
result = apply_operation(5, 3, lambda a, b: a * b)  # 15
```

### Functions Returning Functions
```python
def make_multiplier(n):
    """Return a function that multiplies by n."""
    return lambda x: x * n

times_three = make_multiplier(3)
print(times_three(10))  # 30

times_five = make_multiplier(5)
print(times_five(10))   # 50
```

### Built-in Higher-Order Functions

#### map()
```python
# Apply function to all elements
numbers = [1, 2, 3, 4, 5]

# Map single function
squares = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

# Map with two iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
# [5, 7, 9]

# List comprehension alternative
squares = [x ** 2 for x in numbers]
```

#### filter()
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8, 10]

# Filter strings longer than 5
words = ["apple", "banana", "cherry", "date"]
long_words = list(filter(lambda w: len(w) > 5, words))
# ["banana", "cherry"]

# List comprehension alternative
evens = [x for x in numbers if x % 2 == 0]
```

#### reduce()
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda acc, x: acc + x, numbers)
# 15

# Product of all numbers
product = reduce(lambda acc, x: acc * x, numbers)
# 120

# Find maximum
maximum = reduce(lambda acc, x: acc if acc > x else x, numbers)
# 5

# With initial value
total = reduce(lambda acc, x: acc + x, numbers, 10)
# 25 (starts with 10)
```

#### sorted() with key
```python
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]

# Sort by age
sorted_people = sorted(people, key=lambda p: p[1])
# [("Bob", 20), ("Alice", 25), ("Charlie", 30)]

# Sort by name length
sorted_by_len = sorted(people, key=lambda p: len(p[0]))
```

---

## Closures

### Basic Closure
```python
def outer_function(x):
    """Outer function creates closure."""

    def inner_function(y):
        """Inner function captures x from outer scope."""
        return x + y

    return inner_function  # Return the closure

# Create closure
add_five = outer_function(5)

# Use closure
print(add_five(3))  # 8
print(add_five(10)) # 15
```

### Closure for State
```python
def make_counter():
    """Create a counter function that remembers state."""
    count = 0

    def increment():
        nonlocal count  # Modify outer variable
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### Closure for Configuration
```python
def make_multiplier(factor):
    """Create function that multiplies by factor."""
    return lambda x: x * factor

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

---

## Decorators

### Basic Decorator
```python
def my_decorator(func):
    """Wrapper function."""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

### Decorator with Arguments
```python
def timing_decorator(func):
    """Measure execution time."""
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done"

print(slow_function())
# slow_function took 1.0001s
# Done
```

### Decorator with Parameters
```python
def repeat(n):
    """Decorator factory."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
# Hello!
# Hello!
# Hello!
```

### Preserving Function Metadata
```python
from functools import wraps

def logging_decorator(func):
    @wraps(func)  # Preserves name, docstring, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logging_decorator
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)   # "add" (not "wrapper")
print(add.__doc__)    # "Add two numbers."
```

### Built-in Decorators

#### @staticmethod
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        """Doesn't access class or instance."""
        return a + b

MathUtils.add(1, 2)  # No self needed
```

#### @classmethod
```python
class Person:
    count = 0

    @classmethod
    def get_count(cls):
        """Alternative constructor or class method."""
        return cls.count

    @classmethod
    def from_birth_year(cls, name, year):
        """Create instance from birth year."""
        age = 2024 - year
        return cls(name, age)
```

#### @property
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value

    @property
    def area(self):
        """Computed property (read-only)."""
        return 3.14 * self._radius ** 2
```

---

## itertools Module

### Infinite Iterators
```python
from itertools import count, cycle, repeat

# count() - infinite counter
counter = count(start=10, step=2)
print(next(counter))  # 10
print(next(counter))  # 12

# cycle() - repeat iterable infinitely
colors = cycle(["red", "green", "blue"])
print(next(colors))  # red
print(next(colors))  # green
print(next(colors))  # blue
print(next(colors))  # red (cycles back)

# repeat() - repeat element
ones = repeat(1, 5)
print(list(ones))     # [1, 1, 1, 1, 1]
```

### Finite Iterators
```python
from itertools import chain, accumulate, takewhile, dropwhile

# chain() - combine iterables
a = [1, 2, 3]
b = [4, 5, 6]
print(list(chain(a, b)))  # [1, 2, 3, 4, 5, 6]

# accumulate() - running total
print(list(accumulate([1, 2, 3, 4])))  # [1, 3, 6, 10]

# takewhile() - take while condition true
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(takewhile(lambda x: x < 5, numbers)))  # [1, 2, 3, 4]

# dropwhile() - drop while condition true
print(list(dropwhile(lambda x: x < 5, numbers)))  # [5, 6, 7, 8, 9, 10]
```

### Combinatorics
```python
from itertools import permutations, combinations, product

# permutations() - all orderings
print(list(permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations() - all combinations (order doesn't matter)
print(list(combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]

# product() - Cartesian product
print(list(product([1, 2], [3, 4])))
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```

---

## functools Module

### lru_cache (Memoization)
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    """Cached Fibonacci function."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Much faster with caching
print(fibonacci(100))  # 354224848179261915075
print(fibonacci.cache_info())  # Cache statistics
```

### partial
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))    # 125
```

### reduce
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)  # 120
```

---

## List Comprehensions vs Functional

### List Comprehension (More Pythonic)
```python
# Map
squares = [x ** 2 for x in range(10)]

# Filter
evens = [x for x in range(10) if x % 2 == 0]

# Combined
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
```

### Functional Style
```python
from functools import reduce

# Map
squares = list(map(lambda x: x ** 2, range(10)))

# Filter
evens = list(filter(lambda x: x % 2 == 0, range(10)))

# Reduce
total = reduce(lambda acc, x: acc + x, numbers)
```

---

## Quick Reference

| Concept | Syntax | Description |
|---------|--------|-------------|
| **Lambda** | `lambda x: x * 2` | Anonymous function |
| **map** | `map(func, iterable)` | Apply to all |
| **filter** | `filter(func, iterable)` | Keep matching |
| **reduce** | `reduce(func, iterable)` | Combine all |
| **Closure** | Inner function captures outer | State retention |
| **Decorator** | `@decorator` | Wrap function |
| **partial** | `partial(func, arg)` | Fix arguments |
| **lru_cache** | `@lru_cache()` | Memoization |

---

**Back to [Resources](../README.md)**
