"""
Refactoring - Exercises

These exercises focus on writing small, behavior-preserving improvements.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Extract a Helper
# =============================================================================


def exercise_1_normalize_name(raw):
    """Return a title-cased name; None/empty becomes '<unknown>'."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Replace Conditional With Helper
# =============================================================================


def exercise_2_format_age(age):
    """Return 'age: ?' if None, else 'age: <age>'."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Build Summary (Reuse Helpers)
# =============================================================================


def exercise_3_user_summary(user):
    """
    Return '<missing user>' if user is None.
    Otherwise: '<Name> (age: X, active|inactive)'

    Tip: use exercise_1_normalize_name and exercise_2_format_age.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Extract Validation
# =============================================================================


def exercise_4_is_valid_email(email):
    """Return True if email contains exactly one '@' and at least one '.' after it."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Rename for Clarity
# =============================================================================


def exercise_5_total_seconds(hours, minutes, seconds):
    """Return total seconds represented by hours/minutes/seconds."""
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Refactoring Exercises Tests")
    print("=" * 50)
    all_passed = True

    print("\nExercise 1: Normalize Name")
    tests_1 = [
        ("  ada ", "Ada"),
        (None, "<unknown>"),
        ("", "<unknown>"),
    ]
    for raw, expected in tests_1:
        result = exercise_1_normalize_name(raw)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} normalize_name({raw!r}) = {result!r} (expected {expected!r})")

    print("\nExercise 2: Format Age")
    tests_2 = [(None, "age: ?"), (10, "age: 10")]
    for age, expected in tests_2:
        result = exercise_2_format_age(age)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} format_age({age}) = {result!r} (expected {expected!r})")

    print("\nExercise 3: User Summary")
    user = {"name": "  alice ", "age": 30, "is_active": True}
    result = exercise_3_user_summary(user)
    expected = "Alice (age: 30, active)"
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} user_summary(user) = {result!r} (expected {expected!r})")

    result = exercise_3_user_summary(None)
    expected = "<missing user>"
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} user_summary(None) = {result!r} (expected {expected!r})")

    print("\nExercise 4: Email Validation")
    tests_4 = [
        ("a@b.com", True),
        ("a@b", False),
        ("ab.com", False),
        ("a@@b.com", False),
    ]
    for email, expected in tests_4:
        result = exercise_4_is_valid_email(email)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} is_valid_email({email!r}) = {result} (expected {expected})")

    print("\nExercise 5: Total Seconds")
    result = exercise_5_total_seconds(1, 2, 3)
    expected = 3723
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} total_seconds(1,2,3) = {result} (expected {expected})")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
