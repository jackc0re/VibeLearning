"""
Lambda Expressions - Exercises

Practice using lambda expressions with common patterns.
Run tests with:
    python exercises.py
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
    result = square(5)
    status = "✓" if result == 25 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} square(5) = {result} (expected 25)")

    # Exercise 2
    print("\nExercise 2: Lambda Add")
    add = exercise_2_lambda_add()
    result = add(2, 3)
    status = "✓" if result == 5 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} add(2, 3) = {result} (expected 5)")

    # Exercise 3
    print("\nExercise 3: Sort by Length")
    words = ["a", "aaaa", "bb", "ccc"]
    result = exercise_3_sort_by_length(words)
    status = "✓" if result == ["a", "bb", "ccc", "aaaa"] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} sort_by_length({words}) = {result}")

    # Exercise 4
    print("\nExercise 4: Filter Odds")
    nums = [1, 2, 3, 4, 5]
    result = exercise_4_filter_odds(nums)
    status = "✓" if result == [1, 3, 5] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} filter_odds({nums}) = {result}")

    # Exercise 5
    print("\nExercise 5: Map to Uppercase")
    names = ["alice", "Bob"]
    result = exercise_5_uppercase(names)
    status = "✓" if result == ["ALICE", "BOB"] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} uppercase({names}) = {result}")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
