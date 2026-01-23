"""
Try/Except/Finally - Exercises

Practice safe parsing, fallback values, and cleanup logic.
Run with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Safe Parse
# =============================================================================


def exercise_1_safe_int(value, default=0):
    """
    Return int(value). If conversion fails, return default.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Lookup with else
# =============================================================================


def exercise_2_ratio(data):
    """
    data is expected to have 'count' and 'total'.
    Return count / total. If missing or zero, return None.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Finally cleanup
# =============================================================================


def exercise_3_read_first_line(path):
    """
    Read and return the first line of a file.
    Always close the file using finally.
    If the file doesn't exist, return None.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Try/Except/Finally Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Safe Parse")
    result = exercise_1_safe_int("42")
    status = "✓" if result == 42 else "✗"
    if result != 42:
        all_passed = False
    print(f"  {status} parsed '42' -> {result}")

    result = exercise_1_safe_int("bad", default=-1)
    status = "✓" if result == -1 else "✗"
    if result != -1:
        all_passed = False
    print(f"  {status} fallback -> {result}")

    # Exercise 2
    print("\nExercise 2: Ratio")
    result = exercise_2_ratio({"count": 2, "total": 4})
    status = "✓" if result == 0.5 else "✗"
    if result != 0.5:
        all_passed = False
    print(f"  {status} ratio -> {result}")

    result = exercise_2_ratio({"count": 1, "total": 0})
    status = "✓" if result is None else "✗"
    if result is not None:
        all_passed = False
    print(f"  {status} zero total -> {result}")

    # Exercise 3
    print("\nExercise 3: Read First Line")
    missing = exercise_3_read_first_line("missing_file.txt")
    status = "✓" if missing is None else "✗"
    if missing is not None:
        all_passed = False
    print(f"  {status} missing file -> {missing}")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
