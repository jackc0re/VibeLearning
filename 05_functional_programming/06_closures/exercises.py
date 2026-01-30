"""
Closures - Exercises

Practice writing functions that capture enclosing state.
Run tests with:
    python exercises.py
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
    result = add5(3)
    status = "✓" if result == 8 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} add5(3) = {result} (expected 8)")

    # Exercise 2
    print("\nExercise 2: Make Counter")
    counter = exercise_2_make_counter(10)
    values = [counter(), counter(), counter()]
    status = "✓" if values == [11, 12, 13] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} counter values = {values} (expected [11, 12, 13])")

    # Exercise 3
    print("\nExercise 3: Make Multiplier")
    times4 = exercise_3_make_multiplier(4)
    result = times4(3)
    status = "✓" if result == 12 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} times4(3) = {result} (expected 12)")

    # Exercise 4
    print("\nExercise 4: Make Prefixer")
    prefixer = exercise_4_make_prefixer("Mr. ")
    result = prefixer("Jones")
    status = "✓" if result == "Mr. Jones" else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} prefixer('Jones') = {result} (expected 'Mr. Jones')")

    # Exercise 5
    print("\nExercise 5: Accumulator")
    acc = exercise_5_accumulator(5)
    values = [acc(3), acc(4), acc(-2)]
    status = "✓" if values == [8, 12, 10] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} accumulator values = {values} (expected [8, 12, 10])")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
