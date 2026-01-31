"""
Pure Functions - Exercises

Complete the exercises by writing pure functions.
Run tests with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Pure Addition
# =============================================================================

def exercise_1_add(a, b):
    """
    Return the sum of a and b.
    Must be pure (no print, no global state).
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Pure Discount
# =============================================================================

def exercise_2_apply_discount(price, percent):
    """
    Return the discounted price.

    Args:
        price: original price
        percent: discount percent (0-100)

    Example:
        >>> exercise_2_apply_discount(100, 25)
        75.0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Replace Without Mutation
# =============================================================================

def exercise_3_replace(items, index, value):
    """
    Return a NEW list with items[index] replaced by value.
    Do not mutate the input list.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Normalize Names
# =============================================================================

def exercise_4_normalize_names(names):
    """
    Return a NEW list of names stripped and title-cased.
    Example: ["  aLIce ", "BOB"] -> ["Alice", "Bob"]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Compute Average (Pure)
# =============================================================================

def exercise_5_average(nums):
    """
    Return the average of nums. If empty, return None.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("Running Pure Functions Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Add")
    tests_1 = [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ]
    for a, b, expected in tests_1:
        result = exercise_1_add(a, b)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} add({a}, {b}) = {result} (expected {expected})")

    # Exercise 2
    print("\nExercise 2: Apply Discount")
    tests_2 = [
        (100, 25, 75.0),
        (50, 0, 50.0),
        (80, 50, 40.0),
    ]
    for price, percent, expected in tests_2:
        result = exercise_2_apply_discount(price, percent)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} apply_discount({price}, {percent}) = {result} (expected {expected})")

    # Exercise 3
    print("\nExercise 3: Replace Without Mutation")
    original = ["a", "b", "c"]
    result = exercise_3_replace(original, 1, "B")
    status = "✓" if result == ["a", "B", "c"] and original == ["a", "b", "c"] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} replace([a,b,c],1,'B') -> {result}, original -> {original}")

    # Exercise 4
    print("\nExercise 4: Normalize Names")
    tests_4 = [
        (["  aLIce ", "BOB"], ["Alice", "Bob"]),
        (["eve"], ["Eve"]),
    ]
    for names, expected in tests_4:
        result = exercise_4_normalize_names(names)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} normalize({names}) = {result} (expected {expected})")

    # Exercise 5
    print("\nExercise 5: Average")
    tests_5 = [
        ([1, 2, 3], 2.0),
        ([10], 10.0),
        ([], None),
    ]
    for nums, expected in tests_5:
        result = exercise_5_average(nums)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} average({nums}) = {result} (expected {expected})")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
