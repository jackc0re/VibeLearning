"""
Higher-Order Functions - Exercises

Practice passing functions and returning functions.
Run tests with:
    python exercises.py

Reference solutions are at the bottom of this file.
"""

# =============================================================================
# EXERCISE 1: Apply Function
# =============================================================================

def exercise_1_apply(func, value):
    """
    Return func(value).
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Apply Twice
# =============================================================================

def exercise_2_apply_twice(func, value):
    """
    Return func(func(value)).
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Make Power Function
# =============================================================================

def exercise_3_make_power(exponent):
    """
    Return a function that raises a number to the given exponent.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Compose Two Functions
# =============================================================================

def exercise_4_compose(f, g):
    """
    Return a function that computes f(g(x)).
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Filter With Predicate
# =============================================================================

def exercise_5_filter(items, predicate):
    """
    Return a list of items where predicate(item) is True.
    Implement without using built-in filter.
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
    print("Running Higher-Order Functions Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Helpers
    def double(x):
        return x * 2

    def add1(x):
        return x + 1

    # Exercise 1
    print("\nExercise 1: Apply")
    result = exercise_1_apply(double, 4)
    status = "PASS" if result == 8 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} apply(double, 4) = {result} (expected 8)")

    # Exercise 2
    print("\nExercise 2: Apply Twice")
    result = exercise_2_apply_twice(add1, 3)
    status = "PASS" if result == 5 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} apply_twice(add1, 3) = {result} (expected 5)")

    # Exercise 3
    print("\nExercise 3: Make Power")
    square = exercise_3_make_power(2)
    cube = exercise_3_make_power(3)
    status = "PASS" if safe_call(square, 4) == 16 and safe_call(cube, 2) == 8 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} square(4)={safe_call(square, 4)}, cube(2)={safe_call(cube, 2)}")

    # Exercise 4
    print("\nExercise 4: Compose")
    composed = exercise_4_compose(double, add1)
    result = safe_call(composed, 3)
    status = "PASS" if result == 8 else "FAIL"  # double(add1(3)) = 8
    if status == "FAIL":
        all_passed = False
    print(f"  {status} compose(double, add1)(3) = {result} (expected 8)")

    # Exercise 5
    print("\nExercise 5: Filter")
    items = [1, 2, 3, 4, 5]
    result = exercise_5_filter(items, lambda x: x % 2 == 0)
    status = "PASS" if result == [2, 4] else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} filter(evens) = {result} (expected [2, 4])")

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

# Solution 1: Apply Function
def exercise_1_apply(func, value):
    """Return func(value)."""
    return func(value)


# Solution 2: Apply Twice
def exercise_2_apply_twice(func, value):
    """Return func(func(value))."""
    return func(func(value))


# Solution 3: Make Power Function
def exercise_3_make_power(exponent):
    """Return a function that raises its argument to exponent."""
    def power(base):
        return base ** exponent
    return power


# Solution 4: Compose Two Functions
def exercise_4_compose(f, g):
    """Return a function that computes f(g(x))."""
    def composed(x):
        return f(g(x))
    return composed


# Solution 5: Filter With Predicate
def exercise_5_filter(items, predicate):
    """Return items where predicate(item) is True (no built-in filter)."""
    result = []
    for item in items:
        if predicate(item):
            result.append(item)
    return result


# Re-run the same checks with the reference solutions in place.
if __name__ == "__main__":
    print("\nRe-running the same tests with the reference solutions...")
    run_tests()
