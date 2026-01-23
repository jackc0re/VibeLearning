"""
Coupling and Cohesion - Exercises

Practice designing small, focused functions with clear boundaries.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Subtotal (High Cohesion)
# =============================================================================


def exercise_1_subtotal(items):
    """Return subtotal from list of (name, price) tuples."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Total With Tax
# =============================================================================


def exercise_2_total_with_tax(items, tax_rate):
    """Return total including tax."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Notification Function (Low Coupling)
# =============================================================================


def exercise_3_notify(notifier, message):
    """Call notifier(message)."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Build Message (Keep It Focused)
# =============================================================================


def exercise_4_build_order_message(order_id, total):
    """Return a string like 'Order #123 total $10.00'."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Validate Order (Single Responsibility)
# =============================================================================


def exercise_5_is_valid_order(items):
    """Return True if items is a non-empty list and all prices are >= 0."""
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Coupling & Cohesion Exercises Tests")
    print("=" * 50)
    all_passed = True

    items = [("a", 1.0), ("b", 2.5)]

    print("\nExercise 1: Subtotal")
    result = exercise_1_subtotal(items)
    expected = 3.5
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} subtotal(items) = {result} (expected {expected})")

    print("\nExercise 2: Total With Tax")
    result = exercise_2_total_with_tax(items, 0.10)
    expected = 3.85
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} total_with_tax(items,0.10) = {result} (expected {expected})")

    print("\nExercise 3: Notify")
    sent = []

    def capture(msg):
        sent.append(msg)

    exercise_3_notify(capture, "hello")
    status = "✓" if sent == ["hello"] else "✗"
    if status == "✗":
        all_passed = False
    print(f"  {status} notify(capture,'hello') -> sent={sent}")

    print("\nExercise 4: Build Message")
    result = exercise_4_build_order_message(123, 10)
    expected = "Order #123 total $10.00"
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} build_order_message(123,10) = {result!r} (expected {expected!r})")

    print("\nExercise 5: Validate Order")
    tests_5 = [
        (items, True),
        ([], False),
        ([('x', -1.0)], False),
    ]
    for sample, expected in tests_5:
        result = exercise_5_is_valid_order(sample)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} is_valid_order({sample}) = {result} (expected {expected})")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
