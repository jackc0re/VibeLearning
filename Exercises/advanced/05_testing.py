"""
Advanced Exercise 5: Testing Strategies
=======================================
Test fixtures and factories, property-based testing on random
inputs, integration tests, and a test-driven mini project -
all with a tiny assert-based harness (no pytest).
"""

import random

print("=" * 50)
print("EXERCISE 5: Testing Strategies")
print("=" * 50)


# =============================================================================
# EXERCISE 5.1: Test Fixtures and Factories
# =============================================================================
print("\n--- Exercise 5.1: Test Fixtures and Factories ---")
"""
Factories build test data with sensible defaults; fixtures build
fresh state per test.

Write UserFactory.create(**overrides):
- Defaults: {"name": "user<N>", "role": "viewer", "active": True}
  plus a unique id that increments on every call
- Overrides replace any default (e.g. create(role="admin"))
Then write tests using the factory (unique ids, override works).
"""


# Your code below:
class UserFactory:
    """Builds user dicts with defaults and unique ids."""

    pass


# Test (uncomment after implementing)
# admin = UserFactory.create(role="admin")
# print(admin)


# =============================================================================
# EXERCISE 5.2: Property-Based Testing
# =============================================================================
print("\n--- Exercise 5.2: Property-Based Testing ---")
"""
Property-based tests check invariants over many random inputs.

Write one test that runs 100 trials (seeded, so it is repeatable).
Each trial draws a random list of ints and asserts:
- sorted(xs) is non-decreasing
- sorted(xs) contains exactly the same elements as xs (Counter)
- reversing xs twice gives back xs
"""


# Your code below:
def is_non_decreasing(values):
    """Return True if each element is <= the next one."""
    pass


def test_sorted_properties():
    """Check three invariants over 100 random lists."""
    pass


# =============================================================================
# EXERCISE 5.3: Integration Tests
# =============================================================================
print("\n--- Exercise 5.3: Integration Tests ---")
"""
The Library class below is GIVEN. Integration tests run several of
its methods together in realistic flows.

Write tests that cover: checkout reduces availability, return_book
restores it, checking out an unknown title or an exhausted title
returns False, and a full add -> checkout -> return cycle works.
"""


class Library:
    """GIVEN. A tiny library catalog."""

    def __init__(self):
        self._copies = {}

    def add_book(self, title, copies=1):
        self._copies[title] = self._copies.get(title, 0) + copies

    def checkout(self, title):
        if self._copies.get(title, 0) <= 0:
            return False
        self._copies[title] -= 1
        return True

    def return_book(self, title):
        self._copies[title] = self._copies.get(title, 0) + 1
        return True

    def available(self, title):
        return self._copies.get(title, 0)


# Your code below:
def test_full_cycle():
    """Add, checkout, return - availability returns to 1."""
    pass


# =============================================================================
# EXERCISE 5.4: Test-Driven Development Mini Project
# =============================================================================
print("\n--- Exercise 5.4: TDD Mini Project ---")
"""
Roman numerals. In real TDD you write the tests FIRST, watch them
fail (red), then implement to_roman(n) to make them pass (green).

Rules: I=1 V=5 X=10 L=50 C=100 D=500 M=1000, with subtractive
pairs IV IX XL XC CD CM. Support 1..3999.

Write the tests (a dict of number -> numeral is fine), then
implement to_roman and run them.
"""


# Your code below:
def to_roman(number):
    """Convert an integer 1..3999 to a Roman numeral string."""
    pass


def test_to_roman_examples():
    """Check the classic cases."""
    pass


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# The same tiny harness as the intermediate track, reused here.
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


# SOLUTION 5.1
print("\n--- Solution 5.1 ---")


class UserFactory:
    """Builds user dicts with defaults and unique ids."""

    _next_id = 1

    @classmethod
    def create(cls, **overrides):
        user = {
            "id": cls._next_id,
            "name": f"user{cls._next_id}",
            "role": "viewer",
            "active": True,
        }
        cls._next_id += 1
        user.update(overrides)
        return user


def test_factory_defaults():
    user = UserFactory.create()
    assert user["role"] == "viewer" and user["active"] is True


def test_factory_ids_are_unique():
    ids = {UserFactory.create()["id"] for _ in range(10)}
    assert len(ids) == 10, "ids collided"


def test_factory_overrides():
    admin = UserFactory.create(role="admin")
    assert admin["role"] == "admin"
    assert admin["active"] is True  # untouched defaults survive


# SOLUTION 5.2
print("\n--- Solution 5.2 ---")


def is_non_decreasing(values):
    """Return True if each element is <= the next one."""
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


def test_sorted_properties():
    """Check three invariants over 100 random lists."""
    random.seed(42)  # seeded: failures reproduce exactly
    for _ in range(100):
        size = random.randint(0, 30)
        values = [random.randint(-50, 50) for _ in range(size)]
        result = sorted(values)
        assert is_non_decreasing(result), f"not sorted: {result}"
        assert len(result) == len(values), "sorted lost elements"
        assert sorted(result) == sorted(values), "sorted changed elements"
        assert list(reversed(list(reversed(values)))) == values, "double reverse changed the list"


# SOLUTION 5.3
print("\n--- Solution 5.3 ---")


def test_full_cycle():
    """Add, checkout, return - availability returns to 1."""
    library = Library()
    library.add_book("Clean Code")
    assert library.available("Clean Code") == 1
    assert library.checkout("Clean Code") is True
    assert library.available("Clean Code") == 0
    assert library.return_book("Clean Code") is True
    assert library.available("Clean Code") == 1


def test_checkout_unknown_or_empty_title_fails():
    library = Library()
    assert library.checkout("Ghost Book") is False
    library.add_book("Refactoring")
    assert library.checkout("Refactoring") is True
    assert library.checkout("Refactoring") is False  # exhausted


def test_copies_accumulate():
    library = Library()
    library.add_book("Pragmatic Programmer", 2)
    library.add_book("Pragmatic Programmer")
    assert library.available("Pragmatic Programmer") == 3
    assert library.checkout("Pragmatic Programmer")
    assert library.available("Pragmatic Programmer") == 2


# SOLUTION 5.4
print("\n--- Solution 5.4 ---")

ROMAN_VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def to_roman(number):
    """Convert an integer 1..3999 to a Roman numeral string."""
    parts = []
    remaining = number
    for value, numeral in ROMAN_VALUES:
        while remaining >= value:
            parts.append(numeral)
            remaining -= value
    return "".join(parts)


def test_to_roman_examples():
    """Check the classic cases."""
    cases = {
        1: "I", 4: "IV", 9: "IX", 14: "XIV", 40: "XL",
        58: "LVIII", 90: "XC", 400: "CD", 1994: "MCMXCIV",
        3999: "MMMCMXCIX",
    }
    for number, expected in cases.items():
        actual = to_roman(number)
        assert actual == expected, f"{number}: got {actual}, want {expected}"


def test_to_roman_valid_range():
    """Every result for 1..3999 uses only Roman numeral letters."""
    for number in range(1, 4000):
        result = to_roman(number)
        assert result and all(char in "MDCLXVI" for char in result), number


# Red-green note: in a real TDD session you would define
# test_to_roman_examples BEFORE to_roman exists, run it, watch it
# fail with NameError, then write to_roman to turn it green.
print("Running all tests:")
for test in [
    test_factory_defaults,
    test_factory_ids_are_unique,
    test_factory_overrides,
    test_sorted_properties,
    test_full_cycle,
    test_checkout_unknown_or_empty_title_fails,
    test_copies_accumulate,
    test_to_roman_examples,
    test_to_roman_valid_range,
]:
    run_test(test)

print(f"\n{PASSED} passed, {FAILED} failed")
if FAILED == 0:
    print("All tests passed!")

print("\n" + "=" * 50)
print("Great job! Move on to 06_algorithms.py")
print("=" * 50)
