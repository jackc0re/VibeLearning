"""
Decorators - Exercises

Practice writing and applying decorators.
Run tests with:
    python exercises.py

Reference solutions are at the bottom of this file.
"""

from functools import wraps


# =============================================================================
# EXERCISE 1: Simple Logger Decorator
# =============================================================================

def exercise_1_logger(func):
    """
    Create a decorator that prints the function name before calling it.
    Use @wraps to preserve metadata.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Count Calls Decorator
# =============================================================================

def exercise_2_count_calls(func):
    """
    Decorator that counts how many times a function is called.
    Store the count on wrapper.calls.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Timing Decorator
# =============================================================================

def exercise_3_timing(func):
    """
    Decorator that measures execution time in seconds and prints it.
    Use time.perf_counter.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Decorator Factory
# =============================================================================

def exercise_4_repeat(times):
    """
    Return a decorator that repeats a function call `times` times.
    Return the last result.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Validate Non-Empty Strings
# =============================================================================

def exercise_5_require_non_empty(func):
    """
    Decorator that raises ValueError if any string argument is empty.
    """
    # YOUR CODE HERE
    pass


def safe_call(fn, *args, **kwargs):
    """Call fn if callable; unimplemented stubs return None, not a function."""
    if not callable(fn):
        return None
    return fn(*args, **kwargs)


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("Running Decorators Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Logger Decorator")
    @exercise_1_logger
    def hello(name):
        return f"Hi {name}"

    result = safe_call(hello, "Alice")
    status = "PASS" if result == "Hi Alice" else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} hello('Alice') = {result}")

    # Exercise 2
    print("\nExercise 2: Count Calls")
    @exercise_2_count_calls
    def add(a, b):
        return a + b

    safe_call(add, 1, 2)
    safe_call(add, 2, 3)
    call_count = getattr(add, "calls", None)
    status = "PASS" if call_count == 2 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} add.calls = {call_count} (expected 2)")

    # Exercise 3
    print("\nExercise 3: Timing")
    import time

    @exercise_3_timing
    def slow():
        time.sleep(0.01)
        return "done"

    result = safe_call(slow)
    status = "PASS" if result == "done" else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} slow() = {result}")

    # Exercise 4
    print("\nExercise 4: Repeat")
    calls = []

    def ping():
        calls.append("ping")
        return len(calls)

    ping = safe_call(exercise_4_repeat(3), ping)
    result = safe_call(ping)
    status = "PASS" if result == 3 and len(calls) == 3 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} repeat result={result}, calls={len(calls)} (expected 3)")

    # Exercise 5
    print("\nExercise 5: Require Non-Empty")
    @exercise_5_require_non_empty
    def greet(name):
        return f"Hello {name}"

    ok = safe_call(greet, "Bob")
    error_raised = False
    try:
        safe_call(greet, "")
    except ValueError:
        error_raised = True

    status = "PASS" if ok == "Hello Bob" and error_raised else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} require_non_empty works")

    print("\n" + "=" * 50)
    if all_passed:
        print(" All tests passed! Great job!")
    else:
        print("FAIL Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

# The FAIL lines above are expected: the stubs above are not implemented yet.
# The reference solutions below re-define the same exercise functions, and the
# same tests run again at the bottom of this file - this time they PASS.

import time


# Solution 1: Simple Logger Decorator
def exercise_1_logger(func):
    """Print the function name before calling it."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# Solution 2: Count Calls Decorator
def exercise_2_count_calls(func):
    """Count calls, stored on wrapper.calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


# Solution 3: Timing Decorator
def exercise_3_timing(func):
    """Print the execution time in seconds using time.perf_counter."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


# Solution 4: Decorator Factory
def exercise_4_repeat(times):
    """Return a decorator that calls the function `times` times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result  # the last call's result
        return wrapper
    return decorator


# Solution 5: Validate Non-Empty Strings
def exercise_5_require_non_empty(func):
    """Raise ValueError if any string argument is empty."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str) and arg == "":
                raise ValueError("string arguments must not be empty")
        return func(*args, **kwargs)
    return wrapper


# Re-run the same checks with the reference solutions in place.
if __name__ == "__main__":
    print("\nRe-running the same tests with the reference solutions...")
    run_tests()
