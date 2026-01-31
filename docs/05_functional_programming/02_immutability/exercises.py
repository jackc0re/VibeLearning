"""
Immutability - Exercises

Practice writing functions that avoid mutation.
Run tests with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Append Without Mutation
# =============================================================================

def exercise_1_append(items, value):
    """
    Return a new list with value appended.
    Do not mutate the input list.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Update Dict Immutably
# =============================================================================

def exercise_2_update_dict(data, key, value):
    """
    Return a new dict with key set to value.
    Do not mutate the input dict.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Remove Item Without Mutation
# =============================================================================

def exercise_3_remove(items, value):
    """
    Return a new list with ALL occurrences of value removed.
    Do not mutate the input list.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Toggle Boolean (Tuple)
# =============================================================================

def exercise_4_toggle(flags, index):
    """
    Return a NEW tuple where flags[index] is toggled.
    Example: (True, False) -> (True, True) when index=1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Merge Lists (No Mutation)
# =============================================================================

def exercise_5_merge(a, b):
    """
    Return a new list containing elements of a followed by b.
    Do not mutate inputs.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("Running Immutability Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Append Without Mutation")
    base = [1, 2]
    result = exercise_1_append(base, 3)
    status = "✓" if result == [1, 2, 3] and base == [1, 2] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} append({base}, 3) = {result} (base unchanged)")

    # Exercise 2
    print("\nExercise 2: Update Dict Immutably")
    data = {"a": 1}
    result = exercise_2_update_dict(data, "b", 2)
    status = "✓" if result == {"a": 1, "b": 2} and data == {"a": 1} else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} update_dict({data}, 'b', 2) = {result} (data unchanged)")

    # Exercise 3
    print("\nExercise 3: Remove Without Mutation")
    items = [1, 2, 2, 3]
    result = exercise_3_remove(items, 2)
    status = "✓" if result == [1, 3] and items == [1, 2, 2, 3] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} remove({items}, 2) = {result} (items unchanged)")

    # Exercise 4
    print("\nExercise 4: Toggle Tuple")
    flags = (True, False, True)
    result = exercise_4_toggle(flags, 1)
    status = "✓" if result == (True, True, True) and flags == (True, False, True) else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} toggle({flags}, 1) = {result} (flags unchanged)")

    # Exercise 5
    print("\nExercise 5: Merge Lists")
    a = [1]
    b = [2, 3]
    result = exercise_5_merge(a, b)
    status = "✓" if result == [1, 2, 3] and a == [1] and b == [2, 3] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} merge({a}, {b}) = {result} (inputs unchanged)")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
