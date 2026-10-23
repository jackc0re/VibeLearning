"""
Lambda Expressions - Exercises

Practice using lambda expressions with common patterns.
Run tests with:
    python exercises.py

Reference solutions are at the bottom of this file.
"""

# =============================================================================
# EXERCISE 1: Lambda Square
# =============================================================================

def exercise_1_lambda_square():
    """
    Return a lambda that squares a number.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Lambda Add
# =============================================================================

def exercise_2_lambda_add():
    """
    Return a lambda that adds two numbers.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Sort by Length
# =============================================================================

def exercise_3_sort_by_length(words):
    """
    Return a new list of words sorted by length (shortest first).
    Use sorted(..., key=lambda ...).
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Filter Odds
# =============================================================================

def exercise_4_filter_odds(nums):
    """
    Return a list of odd numbers using filter and lambda.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Map to Uppercase
# =============================================================================

def exercise_5_uppercase(names):
    """
    Return a list of names uppercased using map and lambda.
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
    print("Running Lambda Expressions Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Lambda Square")
    square = exercise_1_lambda_square()
    result = safe_call(square, 5)
    status = "PASS" if result == 25 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} square(5) = {result} (expected 25)")

    # Exercise 2
    print("\nExercise 2: Lambda Add")
    add = exercise_2_lambda_add()
    result = safe_call(add, 2, 3)
    status = "PASS" if result == 5 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} add(2, 3) = {result} (expected 5)")

    # Exercise 3
    print("\nExercise 3: Sort by Length")
    words = ["a", "aaaa", "bb", "ccc"]
    result = exercise_3_sort_by_length(words)
    status = "PASS" if result == ["a", "bb", "ccc", "aaaa"] else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} sort_by_length({words}) = {result}")

    # Exercise 4
    print("\nExercise 4: Filter Odds")
    nums = [1, 2, 3, 4, 5]
    result = exercise_4_filter_odds(nums)
    status = "PASS" if result == [1, 3, 5] else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} filter_odds({nums}) = {result}")

    # Exercise 5
    print("\nExercise 5: Map to Uppercase")
    names = ["alice", "Bob"]
    result = exercise_5_uppercase(names)
    status = "PASS" if result == ["ALICE", "BOB"] else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} uppercase({names}) = {result}")

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

# Solution 1: Lambda Square
def exercise_1_lambda_square():
    """Return a lambda that squares a number."""
    return lambda x: x * x


# Solution 2: Lambda Add
def exercise_2_lambda_add():
    """Return a lambda that adds two numbers."""
    return lambda a, b: a + b


# Solution 3: Sort by Length
def exercise_3_sort_by_length(words):
    """Return words sorted by length, shortest first."""
    return sorted(words, key=lambda word: len(word))


# Solution 4: Filter Odds
def exercise_4_filter_odds(nums):
    """Return the odd numbers using filter and lambda."""
    return list(filter(lambda n: n % 2 != 0, nums))


# Solution 5: Map to Uppercase
def exercise_5_uppercase(names):
    """Return the names uppercased using map and lambda."""
    return list(map(lambda name: name.upper(), names))


# Re-run the same checks with the reference solutions in place.
if __name__ == "__main__":
    print("\nRe-running the same tests with the reference solutions...")
    run_tests()
