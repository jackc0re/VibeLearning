"""
KISS Principle - Exercises

Practice writing straightforward code with minimal nesting.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Clamp
# =============================================================================


def exercise_1_clamp(value, low, high):
    """Clamp value to the inclusive range [low, high]."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Safe Division
# =============================================================================


def exercise_2_safe_divide(a, b):
    """Return a / b, but if b is 0 return None."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Clean Username
# =============================================================================


def exercise_3_clean_username(name):
    """Return a lowercase username stripped of spaces."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Can Edit
# =============================================================================


def exercise_4_can_edit(user):
    """
    Return True if user is not None, is active, and has "edit" permission.

    Tip: Prefer clear boolean logic or early returns.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Summarize
# =============================================================================


def exercise_5_summarize(nums):
    """Return a dict: {'min': ..., 'max': ..., 'avg': ...} or None if nums empty."""
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running KISS Principle Exercises Tests")
    print("=" * 50)
    all_passed = True

    print("\nExercise 1: Clamp")
    tests_1 = [
        (5, 0, 10, 5),
        (-1, 0, 10, 0),
        (999, 0, 10, 10),
    ]
    for value, low, high, expected in tests_1:
        result = exercise_1_clamp(value, low, high)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} clamp({value},{low},{high}) = {result} (expected {expected})")

    print("\nExercise 2: Safe Divide")
    tests_2 = [
        (10, 2, 5.0),
        (1, 0, None),
    ]
    for a, b, expected in tests_2:
        result = exercise_2_safe_divide(a, b)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} safe_divide({a},{b}) = {result} (expected {expected})")

    print("\nExercise 3: Clean Username")
    tests_3 = [
        ("  Alice  ", "alice"),
        ("BOB", "bob"),
    ]
    for name, expected in tests_3:
        result = exercise_3_clean_username(name)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} clean_username({name!r}) = {result!r} (expected {expected!r})")

    print("\nExercise 4: Can Edit")
    user_ok = {"is_active": True, "permissions": ["edit"]}
    user_no = {"is_active": True, "permissions": []}
    tests_4 = [
        (None, False),
        (user_no, False),
        (user_ok, True),
    ]
    for user, expected in tests_4:
        result = exercise_4_can_edit(user)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} can_edit({user}) = {result} (expected {expected})")

    print("\nExercise 5: Summarize")
    result = exercise_5_summarize([1, 2, 3])
    expected = {"min": 1, "max": 3, "avg": 2.0}
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} summarize([1,2,3]) = {result} (expected {expected})")

    result = exercise_5_summarize([])
    expected = None
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} summarize([]) = {result} (expected {expected})")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
