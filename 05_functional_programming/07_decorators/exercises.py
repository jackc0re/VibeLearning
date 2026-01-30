"""
Decorators - Exercises

Practice writing and applying decorators.
Run tests with:
    python exercises.py
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

    result = hello("Alice")
    status = "✓" if result == "Hi Alice" else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} hello('Alice') = {result}")

    # Exercise 2
    print("\nExercise 2: Count Calls")
    @exercise_2_count_calls
    def add(a, b):
        return a + b

    add(1, 2)
    add(2, 3)
    status = "✓" if add.calls == 2 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} add.calls = {add.calls} (expected 2)")

    # Exercise 3
    print("\nExercise 3: Timing")
    import time

    @exercise_3_timing
    def slow():
        time.sleep(0.01)
        return "done"

    result = slow()
    status = "✓" if result == "done" else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} slow() = {result}")

    # Exercise 4
    print("\nExercise 4: Repeat")
    calls = []

    @exercise_4_repeat(3)
    def ping():
        calls.append("ping")
        return len(calls)

    result = ping()
    status = "✓" if result == 3 and len(calls) == 3 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} repeat result={result}, calls={len(calls)} (expected 3)")

    # Exercise 5
    print("\nExercise 5: Require Non-Empty")
    @exercise_5_require_non_empty
    def greet(name):
        return f"Hello {name}"

    ok = greet("Bob")
    error_raised = False
    try:
        greet("")
    except ValueError:
        error_raised = True

    status = "✓" if ok == "Hello Bob" and error_raised else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} require_non_empty works")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
