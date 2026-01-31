"""
Code Smells - Exercises

Practice identifying smells by rewriting code into smaller, clearer functions.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Replace Magic Numbers
# =============================================================================


def exercise_1_apply_discount(amount, code):
    """Apply discount codes: SAVE10 -> 10%, SAVE20 -> 20%, else no discount."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Too Many Parameters
# =============================================================================


def exercise_2_full_name(first, last, title=None):
    """Return formatted name, e.g. 'Dr. Ada Lovelace' or 'Ada Lovelace'."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Long Condition
# =============================================================================


def exercise_3_can_publish(user):
    """Return True if user is active, is staff, and has 'publish' permission."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Duplicated Code
# =============================================================================


def exercise_4_total_prices(prices, tax_rate):
    """Return a new list with tax applied to each price."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Shotgun Surgery Avoidance
# =============================================================================


def exercise_5_build_email(subject, body):
    """Return an email dict with subject/body and a fixed sender."""
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Code Smells Exercises Tests")
    print("=" * 50)
    all_passed = True

    print("\nExercise 1: Discounts")
    tests_1 = [
        (100, "SAVE10", 90.0),
        (100, "SAVE20", 80.0),
        (100, None, 100.0),
    ]
    for amount, code, expected in tests_1:
        result = exercise_1_apply_discount(amount, code)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} apply_discount({amount},{code}) = {result} (expected {expected})")

    print("\nExercise 2: Full Name")
    tests_2 = [
        ("Ada", "Lovelace", None, "Ada Lovelace"),
        ("Ada", "Lovelace", "Dr.", "Dr. Ada Lovelace"),
    ]
    for first, last, title, expected in tests_2:
        result = exercise_2_full_name(first, last, title)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} full_name({first},{last},{title}) = {result!r} (expected {expected!r})")

    print("\nExercise 3: Can Publish")
    user_ok = {"is_active": True, "is_staff": True, "permissions": ["publish"]}
    user_no = {"is_active": True, "is_staff": True, "permissions": []}
    tests_3 = [(user_ok, True), (user_no, False), (None, False)]
    for user, expected in tests_3:
        result = exercise_3_can_publish(user)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} can_publish({user}) = {result} (expected {expected})")

    print("\nExercise 4: Total Prices")
    result = exercise_4_total_prices([10, 20], 0.10)
    expected = [11.0, 22.0]
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} total_prices([10,20],0.10) = {result} (expected {expected})")

    print("\nExercise 5: Build Email")
    result = exercise_5_build_email("Hi", "Hello")
    expected = {"from": "noreply@example.com", "subject": "Hi", "body": "Hello"}
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} build_email(...) = {result} (expected {expected})")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
