"""
Higher-Order Functions - Exercises

Practice passing functions and returning functions.
Run tests with:
    python exercises.py
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
    status = "✓" if result == 8 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} apply(double, 4) = {result} (expected 8)")

    # Exercise 2
    print("\nExercise 2: Apply Twice")
    result = exercise_2_apply_twice(add1, 3)
    status = "✓" if result == 5 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} apply_twice(add1, 3) = {result} (expected 5)")

    # Exercise 3
    print("\nExercise 3: Make Power")
    square = exercise_3_make_power(2)
    cube = exercise_3_make_power(3)
    status = "✓" if square(4) == 16 and cube(2) == 8 else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} square(4)={square(4)}, cube(2)={cube(2)}")

    # Exercise 4
    print("\nExercise 4: Compose")
    composed = exercise_4_compose(double, add1)
    result = composed(3)
    status = "✓" if result == 8 else "✗"  # double(add1(3)) = 8
    if status == "✗":
        all_passed = False
    print(f"  {status} compose(double, add1)(3) = {result} (expected 8)")

    # Exercise 5
    print("\nExercise 5: Filter")
    items = [1, 2, 3, 4, 5]
    result = exercise_5_filter(items, lambda x: x % 2 == 0)
    status = "✓" if result == [2, 4] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} filter(evens) = {result} (expected [2, 4])")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
