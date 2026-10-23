# 🏷️ Type Hints

Type hints are labels that say what kind of value each variable, parameter, and
return value is meant to be.

---

## The Idea: Labels on Your Boxes

You already know that a variable is a **labeled box**. A type hint upgrades the
label: it says not just *what* the box is called, but *what belongs inside*.

```python
age: int = 25          # a box labeled "age" that should hold whole numbers
name: str = "Alice"    # a box labeled "name" that should hold text
```

Think of jars in a kitchen. The lid says "SUGAR", but the label does not glue
the lid shut — you could still pour in salt. What the label buys you is that
everyone who opens the cupboard knows what the jar is *supposed* to hold, and
they will notice when something is off.

Type hints work the same way:

- They **document your code**: anyone reading a function signature instantly
  knows what goes in and what comes out.
- They **power tooling**: editors autocomplete better and flag mismatches.
  Checker tools such as **mypy** read the hints and find bugs before you run
  the code. (mypy is an external tool — this lesson needs nothing installed;
  everything here works with plain Python.)

---

## Type Hints Are NOT Enforced

Here is the most surprising fact in this lesson: **Python ignores type hints
when it runs your code.**

```python
def add(a: int, b: int) -> int:
    return a + b

result = add("Hello, ", "world")
print(result)   # Hello, world   <- no error!
```

We promised `int`, we passed `str`, and Python ran it anyway — string `+`
still works, so `add` happily returns `"Hello, world"`. The hint was a label,
not a lock. That is why they are called *hints*: they help humans and tools,
but the interpreter itself does not check them.

---

## Annotating Variables and Functions

Put a colon and the type after a name:

```python
level: int = 3
player_name: str = "Ada"
health: float = 98.5
is_paused: bool = False
```

For functions, annotate each parameter the same way, and describe the return
value after a `->` arrow:

```python
def greet(name: str) -> str:
    return "Hello, " + name + "!"

def announce(message: str) -> None:   # -> None: prints, returns nothing
    print("ANNOUNCEMENT:", message)
```

The `-> None` part means "this function hands nothing back" — perfect for
functions that only print or save. Reading `greet` you know in one glance:
give me text, I give you text back.

---

## What Python Records

The hints are not thrown away — Python stores them on the function, and
`typing.get_type_hints()` reads them back:

```python
import typing

print(typing.get_type_hints(greet))
# {'name': <class 'str'>, 'return': <class 'str'>}
```

`examples.py` demonstrates this live. Tools like mypy start from exactly this
record.

---

## Optional: "This Type, or None"

A lookup often returns a value **or** `None` when the thing was not found.
`Optional[int]` means exactly that: an int, *or* None.

```python
from typing import Optional

def find_score(scores: dict, name: str) -> Optional[int]:
    if name in scores:
        return scores[name]
    return None
```

> ⚠️ `Optional` does **not** mean "you may skip this parameter" (that is a
> default value like `name="Bob"`). It always means "this value, or None".

## Union: "One of These Types"

```python
from typing import Union

def describe(value: Union[int, str]) -> str:
    return f"{value} (type: {type(value).__name__})"
```

Modern Python (3.10+) lets you write `int | str` as a shortcut. **This repo
supports Python 3.8**, where that spelling does not work, so lesson code uses
`Optional` and `Union` from `typing`. When you later work on a 3.10+ project,
you will recognize both spellings as the same thing.

---

## Collections: Lists and Dictionaries

Hints can describe what is *inside* a collection:

```python
def total_points(scores: list[int]) -> int:
    return sum(scores)

def word_counts(text: str) -> dict[str, int]:
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

`list[int]` reads "a list of ints"; `dict[str, int]` reads "a dict mapping
str keys to int values".

### Why `list[int]` works on Python 3.8 in this repo

On Python 3.9+, `list[int]` is a real object. On 3.8 it would crash — *if
Python evaluated it*. The line at the top of the lesson files:

```python
from __future__ import annotations
```

tells Python: **store every annotation as plain text and never evaluate it**.
The hints become documentation that humans and tools understand, and the
interpreter never chokes on them at runtime.

You will also meet the older spellings in the wild: `List[int]`,
`Dict[str, int]`, imported from `typing`. They mean exactly the same thing.
Lesson code uses both: modern `list[int]` in annotations, and the `typing`
spellings wherever a hint must actually be *evaluated* (for example by
`typing.get_type_hints` on Python 3.8).

---

## Callable and Tuple

### Callable: a hint for functions passed to functions

`Callable[[int], int]` reads "a function that takes one int and returns an
int". The inner list is the argument types; the last item is the return type.

```python
from typing import Callable, List

def transform_all(values: List[int], fn: Callable[[int], int]) -> List[int]:
    result = []
    for value in values:
        result.append(fn(value))
    return result

doubled = transform_all([1, 2, 3], lambda n: n * 2)   # [2, 4, 6]
```

### Tuple: fixed size, fixed positions

A `Tuple[str, int]` is a pair where position 0 holds text and position 1 holds
an int — different from `List[str]`, which is *any number* of strings.

```python
from typing import Tuple

def min_max(nums: List[int]) -> Tuple[int, int]:
    return min(nums), max(nums)
```

---

## TypeVar: One Function, Many Types

What is the return type of `first_item` below? Whatever is inside the list!
`T` is a **type variable** — a placeholder that links the two.

```python
from typing import List, TypeVar

T = TypeVar("T")

def first_item(items: List[T]) -> T:
    return items[0]

first_item([10, 20, 30])      # T means int -> the hint promises an int back
first_item(["a", "b", "c"])   # T means str -> the hint promises a str back
```

Call it with a list of ints and `T` means int, so the return hint promises an
int too. Call it with strings and `T` means str. One definition, honest hints
for every type — that is what `T` buys you.

---

## Going Further: Protocol and TypedDict

*Revisit this section after you finish
[module 04 (OOP concepts)](../../04_oop_concepts/01_classes_and_objects/README.md) —
it will make twice as much sense. The demo below still runs fine right now.*

- **Protocol** describes "anything that can do X" — a function asks for a
  *capability*, not a specific class.
- **TypedDict** describes the *shape of a dictionary*: which keys it has and
  what type each value holds.

```python
from typing import List, Protocol, TypedDict


class Drawable(Protocol):
    def draw(self) -> str:
        ...


class Circle:
    def draw(self) -> str:
        return "O"


class Square:
    def draw(self) -> str:
        return "[ ]"


def render_all(shapes: List[Drawable]) -> List[str]:
    return [shape.draw() for shape in shapes]


class Movie(TypedDict):
    title: str
    year: int


movie = Movie(title="Up", year=2009)
print(movie["title"], movie["year"])   # Up 2009 (still just a dict at runtime)
```

`render_all` never heard of `Circle` or `Square` — it only asked for *anything
with a draw method*. Hold onto that idea for module 04.

---

## Common Mistakes

### 1. Thinking hints are enforced
```python
def add(a: int, b: int) -> int:
    return a + b

add("Hello, ", "world")   # Runs fine - hints are not checked at runtime
```
Hints guide humans and tools (like mypy), never the interpreter itself.

### 2. Forgetting the return annotation
```python
def double(n: int):         # What comes out? Nobody knows.
    return n * 2

def double(n: int) -> int:  # The full story: takes an int, returns an int.
    return n * 2
```
Annotate `-> None` when a function returns nothing.

### 3. Over-annotating obvious locals
```python
name: str = "Alice"   # Unnecessary - "Alice" is obviously text

def greet(name: str) -> str:     # Hints shine at function boundaries...
    greeting = "Hi, " + name     # ...obvious locals can stay plain.
    return greeting
```
The sweet spot: annotate parameters, return values, and module-level
constants. Skip hints on locals a reader can understand at a glance.

---

## Quick Reference

| Hint | Reads as | Example |
|------|----------|---------|
| `int` `str` `float` `bool` | basic types | `age: int = 25` |
| `-> str` | returns text | `def greet(name: str) -> str:` |
| `-> None` | returns nothing | `def log(msg: str) -> None:` |
| `Optional[int]` | an int, or None | `def find(...) -> Optional[int]:` |
| `Union[int, str]` | an int or a str | `def f(v: Union[int, str]):` |
| `list[int]` | list of ints (modern) | `def total(nums: list[int]) -> int:` |
| `List[int]` | list of ints (legacy, from `typing`) | `List[int]` |
| `dict[str, int]` | dict: str keys, int values | `dict[str, int]` / `Dict[str, int]` |
| `Tuple[str, int]` | fixed pair: str then int | `def split(...) -> Tuple[str, int]:` |
| `Callable[[int], int]` | function: int in, int out | `fn: Callable[[int], int]` |
| `TypeVar("T")` | placeholder linking types | `def first(items: List[T]) -> T:` |

Remember: `from __future__ import annotations` at the top of a file makes the
modern `list[int]` spellings safe even on Python 3.8.

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
