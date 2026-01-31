"""
Map, Filter, Reduce - Exercises

Practice transforming collections using functional tools.
Run tests with:
    python exercises.py
"""

from functools import reduce


# =============================================================================
# EXERCISE 1: Map to Squares
# =============================================================================

def exercise_1_map_squares(nums):
    """
    Return a list of squares using map and lambda.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Filter Long Words
# =============================================================================

def exercise_2_filter_long(words, min_length):
    """
    Return words with length >= min_length using filter and lambda.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Reduce Sum
# =============================================================================

def exercise_3_reduce_sum(nums):
    """
    Return the sum of nums using reduce.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Reduce Max
# =============================================================================

def exercise_4_reduce_max(nums):
    """
    Return the max value using reduce.
    Assume nums is non-empty.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Pipeline
# =============================================================================

def exercise_5_pipeline(nums):
    """
    Using map/filter/reduce, do the following:
    1) Keep even numbers
    2) Square them
    3) Sum the result
    Return the sum.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("Running Map/Filter/Reduce Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Map Squares")
    nums = [1, 2, 3]
    result = exercise_1_map_squares(nums)
    status = "✓" if result == [1, 4, 9] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} map_squares({nums}) = {result}")

    # Exercise 2
    print("\nExercise 2: Filter Long Words")
    words = ["a", "tree", "bird", "sky"]
    result = exercise_2_filter_long(words, 4)
    status = "✓" if result == ["tree", "bird"] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} filter_long({words}, 4) = {result}")

    # Exercise 3
    print("\nExercise 3: Reduce Sum")
    nums = [1, 2, 3, 4]
    result = exercise_3_reduce_sum(nums)
    status = "✓" if result == 10 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} reduce_sum({nums}) = {result}")

    # Exercise 4
    print("\nExercise 4: Reduce Max")
    nums = [5, 1, 9, 2]
    result = exercise_4_reduce_max(nums)
    status = "✓" if result == 9 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} reduce_max({nums}) = {result}")

    # Exercise 5
    print("\nExercise 5: Pipeline")
    nums = [1, 2, 3, 4]
    result = exercise_5_pipeline(nums)
    status = "✓" if result == 20 else "✗"  # evens: 2,4 -> squares 4,16 -> sum 20
    if status == "✗":
        all_passed = False
    print(f"  {status} pipeline({nums}) = {result}")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
