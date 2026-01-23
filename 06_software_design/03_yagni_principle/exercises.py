"""
YAGNI Principle - Exercises

Practice choosing a minimal solution that meets current requirements.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Store Notes (Minimal)
# =============================================================================


def exercise_1_store_note(store, title, text):
    """Store a note in a dict-like object."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Get Note
# =============================================================================


def exercise_2_get_note(store, title):
    """Return the note text by title, or None if missing."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Count Completed Tasks
# =============================================================================


def exercise_3_count_done(tasks):
    """Return count of tasks with done=True."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Simple CSV Line
# =============================================================================


def exercise_4_to_csv_line(values):
    """Return a simple CSV line (no quoting needed) like 'a,b,c'."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Add Feature Only When Needed
# =============================================================================


def exercise_5_should_add_feature(user_requests, feature_name):
    """
    Return True if feature_name appears in user_requests (a list of strings).

    The YAGNI idea: don't add features nobody is requesting.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running YAGNI Principle Exercises Tests")
    print("=" * 50)
    all_passed = True

    print("\nExercise 1-2: Store/Get Notes")
    store = {}
    exercise_1_store_note(store, "a", "A")
    exercise_1_store_note(store, "b", "B")
    tests_12 = [
        ("a", "A"),
        ("missing", None),
    ]
    for title, expected in tests_12:
        result = exercise_2_get_note(store, title)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} get_note({title!r}) = {result!r} (expected {expected!r})")

    print("\nExercise 3: Count Done")
    tasks = [
        {"title": "x", "done": True},
        {"title": "y", "done": False},
        {"title": "z", "done": True},
    ]
    result = exercise_3_count_done(tasks)
    expected = 2
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} count_done(tasks) = {result} (expected {expected})")

    print("\nExercise 4: CSV Line")
    result = exercise_4_to_csv_line(["a", "b", "c"])
    expected = "a,b,c"
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} to_csv_line(['a','b','c']) = {result!r} (expected {expected!r})")

    print("\nExercise 5: Should Add Feature")
    requests = ["export", "dark_mode"]
    tests_5 = [
        (requests, "export", True),
        (requests, "search", False),
    ]
    for reqs, feature, expected in tests_5:
        result = exercise_5_should_add_feature(reqs, feature)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} should_add_feature({feature!r}) = {result} (expected {expected})")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
