"""
Closures - Exercises

Practice writing functions that capture enclosing state.
Run tests with:
    python exercises.py

Reference solutions are at the bottom of this file.
"""

# =============================================================================
# EXERCISE 1: Make Adder
# =============================================================================

def exercise_1_make_adder(n):
    """
    Return a function that adds n to its argument.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Make Counter
# =============================================================================

def exercise_2_make_counter(start=0):
    """
    Return a counter function that increments from start.
    Each call should return the next count.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Make Multiplier
# =============================================================================

def exercise_3_make_multiplier(factor):
    """
    Return a function that multiplies by factor.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Make Prefixer
# =============================================================================

def exercise_4_make_prefixer(prefix):
    """
    Return a function that prefixes strings with prefix.
    Example: prefixer("hello") -> "Mr. hello" if prefix is "Mr. "
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Accumulator
# =============================================================================

def exercise_5_accumulator(start=0):
    """
    Return a function that adds a value to an internal total and returns it.
    Uses nonlocal state.
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
    print("Running Closures Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Make Adder")
    add5 = exercise_1_make_adder(5)
    result = safe_call(add5, 3)
    status = "PASS" if result == 8 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} add5(3) = {result} (expected 8)")

    # Exercise 2
    print("\nExercise 2: Make Counter")
    counter = exercise_2_make_counter(10)
    values = [safe_call(counter), safe_call(counter), safe_call(counter)]
    status = "PASS" if values == [11, 12, 13] else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} counter values = {values} (expected [11, 12, 13])")

    # Exercise 3
    print("\nExercise 3: Make Multiplier")
    times4 = exercise_3_make_multiplier(4)
    result = safe_call(times4, 3)
    status = "PASS" if result == 12 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} times4(3) = {result} (expected 12)")

    # Exercise 4
    print("\nExercise 4: Make Prefixer")
    prefixer = exercise_4_make_prefixer("Mr. ")
    result = safe_call(prefixer, "Jones")
    status = "PASS" if result == "Mr. Jones" else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} prefixer('Jones') = {result} (expected 'Mr. Jones')")

    # Exercise 5
    print("\nExercise 5: Accumulator")
    acc = exercise_5_accumulator(5)
    values = [safe_call(acc, 3), safe_call(acc, 4), safe_call(acc, -2)]
    status = "PASS" if values == [8, 12, 10] else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} accumulator values = {values} (expected [8, 12, 10])")

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

# Solution 1: Make Adder
def exercise_1_make_adder(n):
    """Return a function that adds n to its argument."""
    def add(x):
        return x + n
    return add


# Solution 2: Make Counter
def exercise_2_make_counter(start=0):
    """Return a counter function that increments from start."""
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


# Solution 3: Make Multiplier
def exercise_3_make_multiplier(factor):
    """Return a function that multiplies by factor."""
    def multiply(x):
        return x * factor
    return multiply


# Solution 4: Make Prefixer
def exercise_4_make_prefixer(prefix):
    """Return a function that prefixes strings with prefix."""
    def prefixer(text):
        return prefix + text
    return prefixer


# Solution 5: Accumulator
def exercise_5_accumulator(start=0):
    """Return a function that adds values to an internal total."""
    total = start

    def accumulate(value):
        nonlocal total
        total += value
        return total

    return accumulate


# Re-run the same checks with the reference solutions in place.
if __name__ == "__main__":
    print("\nRe-running the same tests with the reference solutions...")
    run_tests()
