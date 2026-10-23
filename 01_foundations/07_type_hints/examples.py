"""
Type Hints - Examples
=====================
Run this file to see type hints in action!

Note the first import below: it stores every annotation as plain text,
which is what makes the modern list[int] spellings safe on Python 3.8.
"""

from __future__ import annotations

import sys
import typing
from typing import Callable, Dict, List, Optional, Protocol, Tuple, TypedDict, TypeVar, Union

T = TypeVar("T")

print("=" * 50)
print("TYPE HINTS - Examples")
print("=" * 50)

# =============================================================================
# ANNOTATED VARIABLES
# =============================================================================
print("\n--- Annotated Variables ---\n")

level: int = 3
player_name: str = "Ada"
health: float = 98.5
is_paused: bool = False

print(f"level = {level}, health = {health}, paused = {is_paused}")

print("\nWhat Python actually recorded for these four variables:")
print("  Raw storage (plain text, thanks to the future import):")
print("   ", __annotations__)
print("\n  Resolved with typing.get_type_hints:")
print("   ", typing.get_type_hints(sys.modules[__name__]))

# =============================================================================
# ANNOTATED FUNCTIONS
# =============================================================================
print("\n--- Annotated Functions ---\n")


def greet(name: str) -> str:
    """Return a greeting built from the given name."""
    return "Hello, " + name + "!"


def announce(message: str) -> None:
    """Print an announcement; returns nothing, hence -> None."""
    print("ANNOUNCEMENT:", message)


print(greet("Ada"))
returned = announce("Type hints are labels, not locks")
print("announce() returned:", returned, "(that is what -> None promises)")

# =============================================================================
# WHAT DID PYTHON RECORD? (typing.get_type_hints)
# =============================================================================
print("\n--- What Did Python Record? ---\n")


def add(a: int, b: int) -> int:
    """Return the sum of two whole numbers."""
    return a + b


def lookup_score(scores: Dict[str, int], name: str) -> Optional[int]:
    """Return the score for a name, or None when it is missing."""
    if name in scores:
        return scores[name]
    return None


print("add:          ", typing.get_type_hints(add))
print("lookup_score: ", typing.get_type_hints(lookup_score))

print("\nThe same hints, stored raw on the function object:")
print("  ", add.__annotations__)

# Modern spelling: safe in annotations even on 3.8, because the future
# import keeps it as text. Notice it is stored as the string 'list[int]'.
def total_points(scores: list[int]) -> int:
    """Return the sum of a list of scores."""
    return sum(scores)


print("total_points (modern spelling):", total_points.__annotations__)

# =============================================================================
# HINTS ARE NOT ENFORCED
# =============================================================================
print("\n--- Hints Are Not Enforced ---\n")

print("add() promised: (a: int, b: int) -> int")
print("Now calling add('Hello, ', 'world') anyway...")
surprise = add("Hello, ", "world")
print("Result:", surprise)
print("NO ERROR! Python treated the hints as suggestions only.")
print("Hints help humans and tools (like mypy), never the interpreter.")

# =============================================================================
# OPTIONAL AND UNION
# =============================================================================
print("\n--- Optional and Union ---\n")

quiz_scores = {"Ann": 90, "Ben": 75}

print("Ann ->", lookup_score(quiz_scores, "Ann"), "(found)")
print("Zed ->", lookup_score(quiz_scores, "Zed"), "(missing, so None)")
print("Optional[int] means: an int, or None.")


def describe(value: Union[int, str]) -> str:
    """Describe a value that is allowed to be an int or a str."""
    return f"{value} (type: {type(value).__name__})"


print("\nUnion in action:")
print(" ", describe(42))
print(" ", describe("forty-two"))
print("On Python 3.10+ you may see int | str; on 3.8 use Union.")

# =============================================================================
# COLLECTIONS: LISTS AND DICTS
# =============================================================================
print("\n--- Collections: Lists and Dicts ---\n")

print("total_points([3, 5, 7]) =", total_points([3, 5, 7]))


def price_list(items: dict[str, int]) -> int:
    """Return the total cost of item -> price pairs."""
    return sum(items.values())


print("price_list({'pen': 2, 'book': 10}) =", price_list({"pen": 2, "book": 10}))
print("dict[str, int] reads: keys are str, values are int.")


def average_score(scores: List[int]) -> float:
    """Return the average of a list of scores (legacy typing spelling)."""
    return sum(scores) / len(scores)


print("average_score([90, 70, 85]) =", average_score([90, 70, 85]))
print("List[int] from typing is the legacy twin of list[int].")

# =============================================================================
# CALLABLE AND TUPLE
# =============================================================================
print("\n--- Callable and Tuple ---\n")


def transform_all(values: List[int], fn: Callable[[int], int]) -> List[int]:
    """Apply fn to every value and collect the results."""
    result = []
    for value in values:
        result.append(fn(value))
    return result


def double(n: int) -> int:
    """Return n multiplied by two."""
    return n * 2


print("Callable[[int], int] = 'a function taking one int, returning an int'")
print("transform_all([1, 2, 3], double)         ->", transform_all([1, 2, 3], double))
print("transform_all([1, 2, 3], lambda n: n+100) ->", transform_all([1, 2, 3], lambda n: n + 100))


def min_max(nums: List[int]) -> Tuple[int, int]:
    """Return the smallest and largest values as a fixed pair."""
    return min(nums), max(nums)


low, high = min_max([4, 9, 1, 7])
print(f"min_max([4, 9, 1, 7]) -> low={low}, high={high}")
print("Tuple[int, int] = exactly two values, int then int.")

# =============================================================================
# TYPEVAR: ONE FUNCTION, MANY TYPES
# =============================================================================
print("\n--- TypeVar: One Function, Many Types ---\n")


def first_item(items: List[T]) -> T:
    """Return the first element of any list."""
    return items[0]


print("first_item([10, 20, 30])  ->", first_item([10, 20, 30]))
print("first_item(['a', 'b'])    ->", first_item(["a", "b"]))
print("The T in List[T] and the T after -> are the SAME T:")
print("whatever fills the list comes back out.")

# =============================================================================
# GOING FURTHER: PROTOCOL AND TYPEDDICT (revisit after module 04)
# =============================================================================
print("\n--- Going Further: Protocol and TypedDict ---\n")


class Drawable(Protocol):
    """Anything that has a draw() -> str method qualifies."""

    def draw(self) -> str:
        ...


class Circle:
    def draw(self) -> str:
        return "O"


class Square:
    def draw(self) -> str:
        return "[+]"


def render_all(shapes: List[Drawable]) -> List[str]:
    """Render anything that can draw itself - no shared parent needed."""
    pictures = []
    for shape in shapes:
        pictures.append(shape.draw())
    return pictures


print("render_all([Circle(), Square(), Circle()]):")
print("  ", render_all([Circle(), Square(), Circle()]))
print("render_all never heard of Circle or Square - it only asked")
print("for anything with a draw() method. (Full story in module 04.)")


class Movie(TypedDict):
    """A dict that must have a str 'title' and an int 'year'."""

    title: str
    year: int


movie = Movie(title="Up", year=2009)
print(f"\nMovie: {movie['title']} ({movie['year']})")
print("Type at runtime:", type(movie).__name__, "- still just a dict!")
print("TypedDict describes the shape of a dict for humans and tools.")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
