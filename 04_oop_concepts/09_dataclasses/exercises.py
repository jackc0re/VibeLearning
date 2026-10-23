"""
Dataclasses - Exercises
=======================
Try to solve each exercise before looking at the solution!
Solutions are provided at the bottom of this file.

The self-tests run twice: once after the stubs (you will see FAIL lines
until you implement the exercises) and once after the worked solutions
(so you can see what PASS looks like). The file always exits cleanly.
"""

import random
from dataclasses import dataclass, field, FrozenInstanceError

print("=" * 50)
print("DATACLASSES - Exercises")
print("=" * 50)


# -----------------------------------------------------------------------------
# Self-test helpers (used before AND after the solutions)
# -----------------------------------------------------------------------------
def check(label, condition):
    """Print PASS or FAIL for one self-test."""
    if condition:
        print("PASS: " + label)
    else:
        print("FAIL: " + label)


def expect_raises(exc_type, builder, label):
    """PASS when calling builder() raises exc_type."""
    try:
        builder()
    except exc_type:
        check(label, True)
    except NameError:
        print("FAIL: " + label + " (name not defined yet)")
    except Exception as err:
        check(label, False)
        print("      expected " + exc_type.__name__ + ", got " + type(err).__name__)
    else:
        check(label, False)
        print("      expected " + exc_type.__name__ + ", but nothing was raised")


# -----------------------------------------------------------------------------
# Exercise 1: InventoryItem with __post_init__ validation
# -----------------------------------------------------------------------------
# 1. Make InventoryItem a @dataclass with fields: name (str), price (float),
#    quantity (int).
# 2. In __post_init__, normalize the name with .strip().
# 3. Also in __post_init__, reject a negative price by raising
#    ValueError("price cannot be negative, got <price>").
#
# TODO: write the InventoryItem dataclass here.
# (Nothing is defined yet, so the self-tests below will report FAIL
#  until you replace this comment with your class.)

# -----------------------------------------------------------------------------
# Exercise 2: A Frozen Config Dataclass
# -----------------------------------------------------------------------------
# 1. Make AppConfig a @dataclass(frozen=True) with fields: host (str),
#    port (int).
# 2. Confirm (mentally, then via the tests) that:
#    - assigning to cfg.port raises FrozenInstanceError
#    - an AppConfig can be used as a dictionary key (it is hashable)
#
# TODO: write the AppConfig dataclass here.

# -----------------------------------------------------------------------------
# Exercise 3: Deck of Cards with default_factory
# -----------------------------------------------------------------------------
# A Deck is a dataclass with ONE field: cards, a list of card names.
#
# 1. Give `cards` a default that calls standard_deck() FRESH for every new
#    Deck. Warning: `cards: list = standard_deck()` would be evaluated ONCE
#    at class definition time -- that is exactly the shared-default bug.
#    Use field(default_factory=...).
# 2. Add deal(): removes and returns the last card (list.pop()).
# 3. Add shuffle(): shuffles the deck in place (random.shuffle).
#
# TODO: write the Deck dataclass here.

# -----------------------------------------------------------------------------
# Exercise 4: Sort Laps with order=True
# -----------------------------------------------------------------------------
# 1. Make Lap a @dataclass(order=True) with fields: seconds (float),
#    runner (str).
# 2. Make sure sorting compares ONLY seconds: mark runner with
#    field(compare=False). Otherwise two equal times would be ranked by
#    the runner's name.
#
# TODO: write the Lap dataclass here.

# -----------------------------------------------------------------------------
# Exercise 5: Rectangle with Validation and a Method
# -----------------------------------------------------------------------------
# 1. Make Rectangle a @dataclass with fields: width (float), height (float).
# 2. In __post_init__, raise ValueError if width <= 0 or height <= 0.
# 3. Add a normal method area() returning width * height (dataclasses can
#    still have regular methods!).
#
# TODO: write the Rectangle dataclass here.


# -----------------------------------------------------------------------------
# Self-tests (FAIL lines are expected while the stubs are unimplemented)
# -----------------------------------------------------------------------------
def run_self_tests():
    print("\n--- Self-tests ---")

    # Exercise 1
    try:
        item = InventoryItem("  Widget  ", 9.99, 3)
        check("Ex1: name is stripped on creation", item.name == "Widget")
        check("Ex1: price and quantity stored", item.price == 9.99 and item.quantity == 3)
    except NameError:
        print("FAIL: Ex1 - InventoryItem is not defined yet")
    except Exception as err:
        print("FAIL: Ex1 - raised " + type(err).__name__ + ": " + str(err))
    expect_raises(ValueError, lambda: InventoryItem("Widget", -1, 3),
                  "Ex1: negative price raises ValueError")

    # Exercise 2
    try:
        cfg = AppConfig("localhost", 8080)
        check("Ex2: frozen config stores host/port",
              cfg.host == "localhost" and cfg.port == 8080)
    except NameError:
        print("FAIL: Ex2 - AppConfig is not defined yet")
    except Exception as err:
        print("FAIL: Ex2 - raised " + type(err).__name__ + ": " + str(err))

    def try_mutate():
        cfg = AppConfig("localhost", 8080)
        cfg.port = 9999

    expect_raises(FrozenInstanceError, try_mutate,
                  "Ex2: assigning to a frozen field raises FrozenInstanceError")

    def try_dict_key():
        cfg = AppConfig("localhost", 8080)
        table = {cfg: "dev"}
        return table[cfg]

    try:
        check("Ex2: frozen config works as a dict key", try_dict_key() == "dev")
    except NameError:
        print("FAIL: Ex2 - AppConfig is not defined yet")
    except Exception as err:
        print("FAIL: Ex2 - dict-key test raised " + type(err).__name__ +
              ": " + str(err))

    # Exercise 3
    try:
        d1 = Deck()
        d2 = Deck()
        check("Ex3: a new deck has 52 cards", len(d1.cards) == 52)
        check("Ex3: all 52 cards are unique", len(set(d1.cards)) == 52)
        check("Ex3: each Deck gets its own list", d1.cards is not d2.cards)
        before = len(d1.cards)
        card = d1.deal()
        check("Ex3: deal() returns a card and shortens the deck",
              isinstance(card, str) and len(d1.cards) == before - 1)
        d1.shuffle()
        check("Ex3: shuffle keeps every card", len(set(d1.cards)) == before - 1)
    except NameError:
        print("FAIL: Ex3 - Deck is not defined yet")
    except Exception as err:
        print("FAIL: Ex3 - raised " + type(err).__name__ + ": " + str(err))

    # Exercise 4
    try:
        race = [Lap(61.2, "Ann"), Lap(58.9, "Bob"), Lap(60.0, "Cal")]
        winner = sorted(race)[0]
        check("Ex4: laps sort by seconds", winner.seconds == 58.9)
        check("Ex4: equal times do NOT compare runner names",
              not (Lap(60.0, "Aaron") < Lap(60.0, "Zoe")))
    except NameError:
        print("FAIL: Ex4 - Lap is not defined yet")
    except Exception as err:
        print("FAIL: Ex4 - raised " + type(err).__name__ + ": " + str(err))

    # Exercise 5
    try:
        rect = Rectangle(3, 4)
        check("Ex5: area() is width * height", rect.area() == 12)
    except NameError:
        print("FAIL: Ex5 - Rectangle is not defined yet")
    except Exception as err:
        print("FAIL: Ex5 - raised " + type(err).__name__ + ": " + str(err))
    expect_raises(ValueError, lambda: Rectangle(-1, 4),
                  "Ex5: negative width raises ValueError")
    expect_raises(ValueError, lambda: Rectangle(3, 0),
                  "Ex5: zero height raises ValueError")


# -----------------------------------------------------------------------------
# Provided helper for Exercise 3 (no need to change it)
# -----------------------------------------------------------------------------
def standard_deck():
    """Return a fresh list of the 52 card names, e.g. 'Q of hearts'."""
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["hearts", "diamonds", "clubs", "spades"]
    return [rank + " of " + suit for suit in suits for rank in ranks]


run_self_tests()

# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)


# Solution 1
print("\n--- Solution 1: InventoryItem ---")


@dataclass
class InventoryItem:
    name: str
    price: float
    quantity: int

    def __post_init__(self):
        self.name = self.name.strip()
        if self.price < 0:
            raise ValueError("price cannot be negative, got " + str(self.price))


item = InventoryItem("  Widget  ", 9.99, 3)
print(f"Created: {item}")


# Solution 2
print("\n--- Solution 2: AppConfig ---")


@dataclass(frozen=True)
class AppConfig:
    host: str
    port: int


cfg = AppConfig("localhost", 8080)
print(f"Config: {cfg}")
try:
    cfg.port = 9999
except FrozenInstanceError as err:
    print(f"Mutation blocked: {err}")
print(f"Hashable, so it can be a dict key: "
      f"{ {cfg: 'dev'}[AppConfig('localhost', 8080)] }")


# Solution 3
print("\n--- Solution 3: Deck ---")


@dataclass
class Deck:
    cards: list = field(default_factory=standard_deck)

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)


d = Deck()
print(f"New deck: {len(d.cards)} cards")
d.shuffle()
print(f"After shuffle, dealt: {d.deal()} ({len(d.cards)} cards left)")


# Solution 4
print("\n--- Solution 4: Lap ---")


@dataclass(order=True)
class Lap:
    seconds: float
    runner: str = field(compare=False)


race = [Lap(61.2, "Ann"), Lap(58.9, "Bob"), Lap(60.0, "Cal")]
winner = sorted(race)[0]
print(f"Fastest lap: {winner.seconds}s by {winner.runner}")


# Solution 5
print("\n--- Solution 5: Rectangle ---")


@dataclass
class Rectangle:
    width: float
    height: float

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError(
                "width and height must be positive, got "
                + str((self.width, self.height)))

    def area(self):
        return self.width * self.height


r = Rectangle(3, 4)
print(f"Rectangle 3 x 4 has area {r.area()}")

# Run the same self-tests again -- now every line says PASS.
print("\n--- Self-tests with the solutions in place ---")
run_self_tests()

print("\n" + "=" * 50)
print("Exercises complete! Compare your classes with the solutions above.")
print("=" * 50)
