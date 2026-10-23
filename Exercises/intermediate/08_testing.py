"""
Intermediate Exercise 8: Testing
================================
Practice unit tests, fixtures, hand-rolled mocks, and integration
tests using a tiny assert-based harness - no pytest required.
"""

print("=" * 50)
print("EXERCISE 8: Testing")
print("=" * 50)


# =============================================================================
# EXERCISE 8.1: Unit Tests
# =============================================================================
print("\n--- Exercise 8.1: Unit Tests ---")
"""
The function below is GIVEN - your job is to test it.

Write test functions that use plain assert statements to check:
- 0 percent off returns the same price
- 50 percent off 80.00 returns 40.00
- the result is rounded to 2 decimals (try 19.99 at 15 percent)
- 100 percent off returns 0
"""


def calculate_discount(price, percent):
    """GIVEN. Return price after percent-off, rounded to 2 decimals."""
    return round(price * (100 - percent) / 100, 2)


# Your code below:
def test_full_price():
    """0 percent off returns the same price."""
    pass


def test_half_off():
    """50 percent off 80.00 returns 40.00."""
    pass


# =============================================================================
# EXERCISE 8.2: Test Fixtures
# =============================================================================
print("\n--- Exercise 8.2: Test Fixtures ---")
"""
A fixture builds fresh state for each test so tests never share
or leak data.

The Cart class is GIVEN. Write a fixture make_cart(*prices) that
returns a brand-new Cart preloaded with those prices, then tests
that prove two carts made from the fixture are independent.
"""


class Cart:
    """GIVEN. A simple shopping cart."""

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(self.items)


# Your code below:
def make_cart(*prices):
    """Fixture: a fresh Cart preloaded with priced items."""
    pass


# =============================================================================
# EXERCISE 8.3: Mocking (Hand-Rolled Fakes)
# =============================================================================
print("\n--- Exercise 8.3: Mocking (Hand-Rolled Fakes) ---")
"""
NotificationService (GIVEN below) calls sender.send(user, message)
on whatever object you hand it.

Write a FakeSender test double that:
- Records every (user, message) pair in a list instead of sending
- Then write tests proving send_welcome sends exactly one message
  with the right user and a message containing "Welcome"
"""


class NotificationService:
    """GIVEN. Sends a welcome message through any sender object."""

    def __init__(self, sender):
        self.sender = sender

    def send_welcome(self, username):
        self.sender.send(username, f"Welcome, {username}!")


# Your code below:
class FakeSender:
    """Hand-rolled test double: records calls instead of sending."""

    pass


# =============================================================================
# EXERCISE 8.4: Integration Tests
# =============================================================================
print("\n--- Exercise 8.4: Integration Tests ---")
"""
Integration tests exercise several pieces working together.

Inventory and place_order are GIVEN. Write tests that run the two
together: a successful order decrements stock, a failed order
leaves stock untouched, and ordering until the shelf is empty works.
"""


class Inventory:
    """GIVEN. Stock levels per SKU."""

    def __init__(self, stock=None):
        self._stock = dict(stock or {})

    def available(self, sku):
        return self._stock.get(sku, 0)

    def release(self, sku, quantity):
        self._stock[sku] = self.available(sku) + quantity


def place_order(inventory, sku, quantity):
    """GIVEN. Decrement stock and return True, or False if short."""
    if inventory.available(sku) < quantity:
        return False
    inventory.release(sku, -quantity)
    return True


# Your code below:
def test_successful_order_decrements_stock():
    """Ordering 2 of 3 widgets leaves 1."""
    pass


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# A tiny harness: run one test, report PASS/FAIL without stopping.
PASSED = 0
FAILED = 0


def run_test(test_fn):
    """Run one test function and record the outcome."""
    global PASSED, FAILED
    try:
        test_fn()
    except AssertionError as exc:
        FAILED += 1
        detail = str(exc) or "assertion failed"
        print(f"FAIL: {test_fn.__name__} - {detail}")
    else:
        PASSED += 1
        print(f"PASS: {test_fn.__name__}")


# SOLUTION 8.1
print("\n--- Solution 8.1 ---")


def test_full_price():
    """0 percent off returns the same price."""
    assert calculate_discount(80.0, 0) == 80.0


def test_half_off():
    """50 percent off 80.00 returns 40.00."""
    assert calculate_discount(80.0, 50) == 40.0


def test_rounding():
    """Results are rounded to 2 decimals."""
    assert calculate_discount(19.99, 15) == 16.99


def test_full_discount():
    """100 percent off returns 0."""
    assert calculate_discount(80.0, 100) == 0.0


# SOLUTION 8.2
print("\n--- Solution 8.2 ---")


def make_cart(*prices):
    """Fixture: a fresh Cart preloaded with priced items."""
    cart = Cart()
    for price in prices:
        cart.add(price)
    return cart


def test_empty_cart_totals_zero():
    assert make_cart().total() == 0


def test_fixture_totals_items():
    assert make_cart(10.0, 2.5).total() == 12.5


def test_fixture_instances_are_independent():
    first = make_cart(10.0)
    second = make_cart(20.0)
    first.add(5.0)
    assert second.total() == 20.0, "changes leaked between carts"


# SOLUTION 8.3
print("\n--- Solution 8.3 ---")


class FakeSender:
    """Hand-rolled test double: records calls instead of sending."""

    def __init__(self):
        self.sent = []

    def send(self, username, message):
        self.sent.append((username, message))


def test_welcome_message_is_sent_once():
    sender = FakeSender()
    service = NotificationService(sender)
    service.send_welcome("grace")
    assert len(sender.sent) == 1
    username, message = sender.sent[0]
    assert username == "grace"
    assert "Welcome" in message


def test_welcome_goes_only_to_that_user():
    sender = FakeSender()
    NotificationService(sender).send_welcome("ada")
    assert [user for user, _ in sender.sent] == ["ada"]


# SOLUTION 8.4
print("\n--- Solution 8.4 ---")


def test_successful_order_decrements_stock():
    """Ordering 2 of 3 widgets leaves 1."""
    inventory = Inventory({"widget": 3})
    assert place_order(inventory, "widget", 2) is True
    assert inventory.available("widget") == 1


def test_failed_order_keeps_stock():
    """Too-big orders change nothing."""
    inventory = Inventory({"widget": 1})
    assert place_order(inventory, "widget", 5) is False
    assert inventory.available("widget") == 1


def test_orders_until_empty():
    """Ordering one at a time works until the shelf is bare."""
    inventory = Inventory({"widget": 2})
    assert place_order(inventory, "widget", 1) is True
    assert place_order(inventory, "widget", 1) is True
    assert place_order(inventory, "widget", 1) is False


# Run everything and print a summary.
print("\nRunning all tests:")
for test in [
    test_full_price,
    test_half_off,
    test_rounding,
    test_full_discount,
    test_empty_cart_totals_zero,
    test_fixture_totals_items,
    test_fixture_instances_are_independent,
    test_welcome_message_is_sent_once,
    test_welcome_goes_only_to_that_user,
    test_successful_order_decrements_stock,
    test_failed_order_keeps_stock,
    test_orders_until_empty,
]:
    run_test(test)

print(f"\n{PASSED} passed, {FAILED} failed")
if FAILED == 0:
    print("All tests passed!")

print("\n" + "=" * 50)
print("Great job! You finished the intermediate track.")
print("Move on to Exercises/advanced/01_system_design.py")
print("=" * 50)
