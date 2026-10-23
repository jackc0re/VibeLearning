"""
Behavioral Design Patterns - Exercises

Practice Observer, Strategy, and Command ideas.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Observer
# =============================================================================


class StockTicker:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, fn):
        self._subscribers.append(fn)

    def publish(self, price):
        for fn in self._subscribers:
            fn(price)


def exercise_1_capture_updates():
    """
    Return a list of prices collected by two subscribers.

    Publish 10, then 12, then 15; both subscribers add to the same list.
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Strategy
# =============================================================================


class FlatDiscount:
    def apply(self, total):
        return total - 5


class PercentDiscount:
    def apply(self, total):
        return total * 0.9


def checkout(total, discount_strategy):
    return discount_strategy.apply(total)


def exercise_2_strategy():
    """Return a tuple (flat_total, percent_total) for total=50."""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Command
# =============================================================================


class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1
        return self.value

    def dec(self):
        self.value -= 1
        return self.value


class Command:
    def execute(self):
        raise NotImplementedError


class Increment(Command):
    def __init__(self, counter):
        self.counter = counter

    def execute(self):
        return self.counter.inc()


class Decrement(Command):
    def __init__(self, counter):
        self.counter = counter

    def execute(self):
        return self.counter.dec()


def exercise_3_command_sequence():
    """Execute commands to return final counter value of 1."""
    # YOUR CODE HERE
    pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Behavioral Patterns Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Observer")
    prices = exercise_1_capture_updates()
    expected = [10, 10, 12, 12, 15, 15]
    status = "PASS" if prices == expected else "FAIL"
    if prices != expected:
        all_passed = False
    print(f"  {status} captured updates: {prices}")

    # Exercise 2
    print("\nExercise 2: Strategy")
    totals = exercise_2_strategy()
    expected = (45, 45.0)
    status = "PASS" if totals == expected else "FAIL"
    if totals != expected:
        all_passed = False
    print(f"  {status} totals: {totals}")

    # Exercise 3
    print("\nExercise 3: Command")
    value = exercise_3_command_sequence()
    expected = 1
    status = "PASS" if value == expected else "FAIL"
    if value != expected:
        all_passed = False
    print(f"  {status} final value: {value}")

    print("\n" + "=" * 50)
    if all_passed:
        print(" All tests passed! Great job!")
    else:
        print("FAIL Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
