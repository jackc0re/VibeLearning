"""
Structural Design Patterns - Exercises

Practice Adapter, Decorator, and Facade ideas.
Run with:
    python exercises.py
"""

# =============================================================================
# EXERCISE 1: Adapter
# =============================================================================


class LegacyTemperatureSensor:
    def read_fahrenheit(self):
        return 77.0


class TemperatureAdapter:
    def __init__(self, sensor):
        self.sensor = sensor

    def read_celsius(self):
        """Return temperature in Celsius based on the legacy sensor."""
        # YOUR CODE HERE
        pass


# =============================================================================
# EXERCISE 2: Decorator
# =============================================================================


class Message:
    def text(self):
        return "hello"


class ExclaimDecorator:
    def __init__(self, message):
        self.message = message

    def text(self):
        return self.message.text() + "!"


class UppercaseDecorator:
    def __init__(self, message):
        self.message = message

    def text(self):
        return self.message.text().upper()


def exercise_2_decorate_message():
    """Return a decorated message that becomes 'HELLO!'"""
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Facade
# =============================================================================


class InventoryService:
    def reserve(self, item):
        return f"reserved {item}"


class ShippingService:
    def ship(self, item):
        return f"shipped {item}"


class NotificationService:
    def notify(self, item):
        return f"notified {item}"


class OrderFacade:
    def __init__(self):
        self.inventory = InventoryService()
        self.shipping = ShippingService()
        self.notification = NotificationService()

    def place_order(self, item):
        """Return a list of steps performed by the facade."""
        # YOUR CODE HERE
        pass


# =============================================================================
# TESTS
# =============================================================================


def run_tests():
    print("Running Structural Patterns Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Adapter")
    adapter = TemperatureAdapter(LegacyTemperatureSensor())
    result = adapter.read_celsius()
    expected = 25.0
    status = "✓" if result == expected else "✗"
    if result != expected:
        all_passed = False
    print(f"  {status} read_celsius() = {result} (expected {expected})")

    # Exercise 2
    print("\nExercise 2: Decorator")
    msg = exercise_2_decorate_message()
    expected = "HELLO!"
    status = "✓" if msg == expected else "✗"
    if msg != expected:
        all_passed = False
    print(f"  {status} decorated message: {msg} (expected {expected})")

    # Exercise 3
    print("\nExercise 3: Facade")
    facade = OrderFacade()
    steps = facade.place_order("book")
    expected_steps = ["reserved book", "shipped book", "notified book"]
    status = "✓" if steps == expected_steps else "✗"
    if steps != expected_steps:
        all_passed = False
    print(f"  {status} facade steps: {steps}")

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
