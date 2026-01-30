"""
Decorators - Examples

Shows how to build and use decorators in Python.
Run with:
    python examples.py
"""

from functools import wraps
import time


# =============================================================================
# BASIC LOGGER DECORATOR
# =============================================================================

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@logger
def greet(name):
    return f"Hello, {name}!"


# =============================================================================
# TIMING DECORATOR
# =============================================================================

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper


@timing
def slow_add(a, b):
    time.sleep(0.1)
    return a + b


# =============================================================================
# DECORATOR FACTORY (WITH ARGUMENTS)
# =============================================================================

def repeat(times):
    """Repeat a function call multiple times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Hi!")


if __name__ == "__main__":
    print("=" * 60)
    print("DECORATORS EXAMPLES")
    print("=" * 60)
    greet("Alice")
    slow_add(2, 3)
    say_hi()
    print("\n✓ Examples complete!")
