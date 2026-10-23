"""
Dataclasses - Examples
======================
How @dataclass removes class boilerplate: generated __init__, __repr__ and
__eq__, defaults with default_factory, frozen (immutable) classes, the
__post_init__ hook, and the decorator flags. Python 3.8 compatible.
"""

import random
from collections import namedtuple
from dataclasses import dataclass, field, FrozenInstanceError

print("=" * 50)
print("DATACLASSES - Examples")
print("=" * 50)

# -----------------------------------------------------------------------------
# 1. The Boilerplate Problem
# -----------------------------------------------------------------------------
print("\n--- 1. The Boilerplate Problem ---\n")


class BookPlain:
    """A regular class: __init__, __repr__ and __eq__ written by hand."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return (f"BookPlain(title={self.title!r}, "
                f"author={self.author!r}, year={self.year!r})")

    def __eq__(self, other):
        if not isinstance(other, BookPlain):
            return NotImplemented
        return ((self.title, self.author, self.year)
                == (other.title, other.author, other.year))


@dataclass
class Book:
    """The same class as a dataclass: 4 lines instead of ~20."""
    title: str
    author: str
    year: int


plain = BookPlain("Dune", "Frank Herbert", 1965)
fancy = Book("Dune", "Frank Herbert", 1965)

print(f"Plain class repr:  {plain!r}")
print(f"Dataclass repr:    {fancy!r}")
print(f"Plain == plain:    {plain == BookPlain('Dune', 'Frank Herbert', 1965)}")
print(f"Dataclass == same: {fancy == Book('Dune', 'Frank Herbert', 1965)}")
print("Same behavior -- the dataclass just wrote the plumbing for us.")

# -----------------------------------------------------------------------------
# 2. What @dataclass Generates (init, repr, eq)
# -----------------------------------------------------------------------------
print("\n--- 2. What @dataclass Generates ---\n")


@dataclass
class GameProfile:
    player: str
    level: int = 1
    is_active: bool = True


p1 = GameProfile("Ann")                       # defaults fill level/is_active
p2 = GameProfile(player="Bob", level=7)

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1.level default:  {p1.level}")
print(f"p1 == GameProfile('Ann'): {p1 == GameProfile('Ann')}")
print("Fields are declared as type-annotated names in the class body;")
print("the decorator reads them and writes __init__ to match.")

# -----------------------------------------------------------------------------
# 3. The Mutable-Default Trap (run honestly!)
# -----------------------------------------------------------------------------
print("\n--- 3. The Mutable-Default Trap ---\n")

print("What happens with a bare list default? Let's actually try it...")

try:
    @dataclass
    class BadPlaylist:
        name: str
        songs: list = []          # mutable default: dataclasses refuses this
except ValueError as err:
    print("The class definition itself FAILED with ValueError:")
    print(f"  {err}")

print()
print("Unlike a plain function default (def f(items=[])), @dataclass does")
print("not create a broken shared list -- it refuses to build the class")
print("at all. The error message even names the fix: default_factory.")

# -----------------------------------------------------------------------------
# 4. The Fix: field(default_factory=...)
# -----------------------------------------------------------------------------
print("\n--- 4. field(default_factory=...) ---\n")


def standard_deck():
    """Build a fresh 52-card deck (used as a default_factory below)."""
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
             "J", "Q", "K", "A"]
    suits = ["hearts", "diamonds", "clubs", "spades"]
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]


@dataclass
class Deck:
    cards: list = field(default_factory=standard_deck)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


deck1 = Deck()
deck2 = Deck()
print(f"Each deck gets its OWN list: deck1 has {len(deck1.cards)} cards, "
      f"deck2 has {len(deck2.cards)} cards.")

deck1.shuffle()
deck1.deal()
print(f"After shuffling and dealing one card, deck1 has {len(deck1.cards)} cards.")
print(f"Untouched deck2 still has {len(deck2.cards)} cards (no shared list!).")

# default_factory also takes simple builders like list, dict, set:
@dataclass
class Playlist:
    name: str
    songs: list = field(default_factory=list)


monday = Playlist("Monday Mix")
monday.songs.append("Bohemian Rhapsody")
friday = Playlist("Friday Mix")
print(f"friday.songs after appending to monday's: {friday.songs}")

# -----------------------------------------------------------------------------
# 5. frozen=True: Immutable and (Back) Hashable
# -----------------------------------------------------------------------------
print("\n--- 5. frozen=True ---\n")


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class MutablePoint:
    x: int
    y: int


p = Point(3, 4)
print(f"p = {p}")

try:
    p.x = 99
except FrozenInstanceError as err:
    print(f"Assigning to a frozen field raises FrozenInstanceError: {err}")

try:
    hash(p)
    print("hash(p) works: frozen + eq=True -> __hash__ is generated.")
except TypeError as err:
    print(f"hash(p) failed: {err}")

try:
    hash(MutablePoint(1, 2))
    print("A mutable dataclass is hashable too (unexpected!).")
except TypeError as err:
    print(f"A MUTABLE dataclass is not: hash(MutablePoint) -> {err}")

locations = {Point(0, 0): "home", Point(3, 4): "school"}
print(f"Frozen dataclasses work as dict keys: {locations[Point(3, 4)]}")

# -----------------------------------------------------------------------------
# 6. __post_init__: Validation and Normalization
# -----------------------------------------------------------------------------
print("\n--- 6. __post_init__ ---\n")


@dataclass
class Product:
    name: str
    email: str
    price: float

    def __post_init__(self):
        # Runs right after the generated __init__.
        self.email = self.email.strip().lower()      # normalization
        if self.price < 0:                           # validation
            raise ValueError(f"price cannot be negative, got {self.price}")


item = Product("Widget", "  ANN@Example.COM ", 9.99)
print(f"Normalized email: {item.email}")

try:
    Product("Widget", "ann@example.com", -1)
except ValueError as err:
    print(f"Bad price rejected by __post_init__: {err}")

# -----------------------------------------------------------------------------
# 7. The Decorator Flags: eq, order, repr, unsafe_hash
# -----------------------------------------------------------------------------
print("\n--- 7. Decorator Flags ---\n")

print("Defaults: init=True, repr=True, eq=True, order=False,")
print("          unsafe_hash=False, frozen=False.")


@dataclass(order=True)
class Lap:
    seconds: float
    runner: str = field(compare=False)   # stored, but NOT part of comparisons


laps = [Lap(61.2, "Ann"), Lap(58.9, "Bob"), Lap(60.0, "Cal")]
fastest = sorted(laps)[0]
print(f"order=True lets us sort: fastest lap is {fastest.seconds}s by {fastest.runner}")
print("compare=False keeps 'runner' out of the comparison (lists/objects")
print("that do not support < would otherwise raise TypeError when sorting).")


@dataclass(eq=False)
class TrackedCell:
    value: int


a = TrackedCell(1)
b = TrackedCell(1)
print(f"eq=False -> equality falls back to identity: (a == b) is {a == b}, "
      f"(a is a) is {a is a}")
print("unsafe_hash=True would force __hash__ onto a MUTABLE class -- the")
print("word 'unsafe' is a warning: hashing something that can change is")
print("usually a bug. Prefer frozen=True when you need hashability.")

# -----------------------------------------------------------------------------
# 8. dataclass vs namedtuple vs Plain Class
# -----------------------------------------------------------------------------
print("\n--- 8. dataclass vs namedtuple vs Plain Class ---\n")

PointNT = namedtuple("PointNT", ["x", "y"])
nt = PointNT(3, 4)
dc = Point(3, 4)

print(f"namedtuple repr: {nt}   (it is a tuple that also answers .x and .y)")
print(f"dataclass  repr: {dc}   (a normal object with named fields)")
print(f"Unpack a namedtuple: x, y = {nt} -> x={nt[0]}, y={nt[1]}")

try:
    nt.x = 10
except AttributeError as err:
    print(f"namedtuples are frozen by nature: {err}")

print()
print("Rule of thumb: methods or defaults -> @dataclass;")
print("naming a small fixed tuple -> namedtuple;")
print("behavior-heavy object -> plain class.")
print()
print("Version note: slots=True and kw_only=True need Python 3.10+;")
print("this repo targets 3.8, so they are never used in these examples.")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
