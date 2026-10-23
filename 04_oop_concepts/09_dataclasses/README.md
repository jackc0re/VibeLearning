# 📋 Dataclasses

You already know how to write a class: define `__init__`, assign every parameter
to `self`, maybe add `__repr__` so printing looks nice, maybe add `__eq__` so
objects compare by value. That is the same housekeeping every single time.

A **dataclass** is a class whose repetitive plumbing is written *for* you.
You describe the fields; Python generates the boilerplate.

**Real-world Analogy:**
- **Plain class**: you hand-draw every form yourself — boxes, labels, lines —
  before anyone can fill it in.
- **`@dataclass`**: a pre-printed form. You only write the field names, and the
  boxes, printing, and comparison logic come ready-made.

## 🧱 The Boilerplate Problem

Here is a plain class that stores a book. Count the lines spent on plumbing:

```python
class BookPlain:
    def __init__(self, title, author, year):   # plumbing: __init__
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):                        # plumbing: nice printing
        return f"BookPlain(title={self.title!r}, author={self.author!r}, year={self.year!r})"

    def __eq__(self, other):                   # plumbing: value equality
        if not isinstance(other, BookPlain):
            return NotImplemented
        return (self.title, self.author, self.year) == (other.title, other.author, other.year)
```

Around 15-20 lines for three fields. Here is the *same* class as a dataclass:

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
```

Four lines. `@dataclass` inspects those annotated fields and generates
`__init__`, `__repr__`, and `__eq__` for you.

## 🏷️ Fields Are Type-Annotated Attributes

Notice the odd part: `title: str` sits in the class body with **no value
assigned**. In a dataclass, a bare annotated name declares a *field*. The
decorator collects the fields (in order) and writes an `__init__` whose
parameters match them:

```python
book = Book("Dune", "Frank Herbert", 1965)   # positional works...
book = Book(title="Dune", author="Frank Herbert", year=1965)  # ...and so does keyword

print(book)          # Book(title='Dune', author='Frank Herbert', year=1965)
print(book == Book("Dune", "Frank Herbert", 1965))   # True (value equality!)
```

We met [Type Hints](../../01_foundations/07_type_hints/README.md) back in the
foundations module. Here they do real work: the decorator *reads* them.
(They are still only annotations, though — see Common Mistakes below.)

What `@dataclass` generates for you:

| Method | Generated? | What you get |
|--------|-----------|--------------|
| `__init__` | ✅ always | one parameter per field, in declaration order |
| `__repr__` | ✅ by default | `Book(title='Dune', author='...', year=1965)` |
| `__eq__`   | ✅ by default | two instances are equal when all fields are equal |
| `__hash__` | ⛔ by default | hashable only if the class is frozen (see below) |

## 🎁 Defaults — and the Mutable-Default Trap

Fields can have default values, exactly like function parameters
(without defaults first, with defaults after):

```python
@dataclass
class GameProfile:
    player: str
    level: int = 1
    is_active: bool = True
```

Now the trap. In *plain* functions, a mutable default like `def f(items=[])`
is shared between calls — a famous Python gotcha. What does `@dataclass` do
with a bare list default? **It refuses the class entirely.** This code does
not create a broken class; it raises `ValueError` the moment the decorator
runs (we verified this by running it — see Section 3 of `examples.py`):

```python
@dataclass
class BadPlaylist:        # ValueError: mutable default <class 'list'>
    name: str             #   for field songs is not allowed: use default_factory
    songs: list = []
```

Python is protecting you here: a shared list would silently link all
instances together. The fix is `field(default_factory=...)` — pass a
*function* that builds a fresh value for each new instance:

```python
from dataclasses import dataclass, field

@dataclass
class Playlist:
    name: str
    songs: list = field(default_factory=list)   # a NEW list per instance

monday = Playlist("Monday Mix")
monday.songs.append("Bohemian Rhapsody")
friday = Playlist("Friday Mix")
print(friday.songs)     # []  -- monday's song did not leak in
```

## 🧊 frozen=True: Immutable Dataclasses

Sometimes you want records that nobody can change after creation — settings,
coordinates, currency amounts. Pass `frozen=True`:

```python
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(3, 4)
p.x = 99    # FrozenInstanceError: cannot assign to field 'x'
```

Wrap the assignment in `try/except FrozenInstanceError` when you want to
*demonstrate* immutability rather than crash.

A bonus you get for free: a frozen dataclass **is hashable** (with the default
`eq=True`), so it works as a dictionary key or inside a set:

```python
origin = Point(0, 0)
locations = {origin: "home"}     # works: frozen + eq -> __hash__ exists
```

A plain (non-frozen) dataclass is *not* hashable — `hash(p)` raises
`TypeError`, because an object that can change must not be used as a key.

## 🔧 `__post_init__`: Validation and Normalization

Need code to run right after the generated `__init__`? Define `__post_init__`.
It receives the freshly-set fields and can clean them up or reject bad input:

```python
@dataclass
class Product:
    name: str
    email: str        # example: normalize contact email
    price: float

    def __post_init__(self):
        self.email = self.email.strip().lower()      # normalization
        if self.price < 0:                           # validation
            raise ValueError(f"price cannot be negative, got {self.price}")
```

```python
p = Product("Widget", "  ANN@Example.COM ", 9.99)
print(p.email)   # ann@example.com

Product("Widget", "ann@example.com", -1)
# ValueError: price cannot be negative, got -1
```

## ⚙️ The Decorator Flags

`@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)`
— every flag has a default; you only pass the ones you want to flip.

| Flag | Default | What flipping it does |
|------|---------|----------------------|
| `init` | `True` | set `init=False` if you write your own `__init__` |
| `repr` | `True` | set `repr=False` for quieter printing |
| `eq` | `True` | set `eq=False` to fall back to identity (`is`) equality |
| `order` | `False` | set `order=True` to generate `<`, `<=`, `>`, `>=` (field by field) — great with `sorted()` |
| `unsafe_hash` | `False` | force `__hash__` on a mutable class — usually a bug; the name warns you |
| `frozen` | `False` | forbid field assignment; restores hashability (see above) |

```python
@dataclass(order=True)
class Lap:
    seconds: float
    runner: str = field(compare=False)   # runner is stored but NOT compared

laps = [Lap(61.2, "Ann"), Lap(58.9, "Bob"), Lap(60.0, "Cal")]
print(sorted(laps)[0].runner)   # Bob -- sorted by seconds only
```

Without `compare=False`, `order=True` compares *all* fields left to right —
and comparing a field that does not support `<` (like a list) breaks sorting
with `TypeError`. Compare only what ordering should mean.

## ⚖️ dataclass vs namedtuple vs Plain Class

```python
from collections import namedtuple
PointNT = namedtuple("PointNT", ["x", "y"])    # one line, immutable, tuple-ish
```

| | Plain class | `@dataclass` | `namedtuple` |
|---|---|---|---|
| Boilerplate | all of it (`__init__`, ...) | generated for you | generated for you |
| Mutable | yes | yes (by default) | no (it is a tuple) |
| `obj.field` access | yes | yes | yes |
| Index access `obj[0]` | no | no | yes (it *is* a tuple) |
| Unpacking `x, y = obj` | no | no | yes |
| Defaults / methods / `__post_init__` | yes | yes | limited |
| Best for | behavior-heavy objects | data records with logic | tiny fixed records |

Rule of thumb: need methods or defaults? `@dataclass`. Just naming a small
tuple? `namedtuple`. Lots of behavior, little data? plain class.

## 🐍 A Note on Python Versions

Two `@dataclass` options you will meet in the wild — `slots=True` and
`kw_only=True` — **require Python 3.10 or newer**. This repository targets
Python 3.8, so you will not see them in our examples: `slots=True` makes
instances more memory-efficient, and `kw_only=True` forces keyword arguments
in the generated `__init__`. Just recognize the names; you can adopt them
when your project moves to 3.10+.

---

## Common Mistakes

### 1. A mutable default without `default_factory`
```python
@dataclass
class Bad:
    items: list = []      # ValueError at class DEFINITION time (not runtime!)

@dataclass
class Good:
    items: list = field(default_factory=list)   # fresh list per instance
```
Unlike plain functions, dataclasses catch this for you — the error names the
fix. Lists, dicts, and sets all need `default_factory`.

### 2. Expecting runtime type enforcement
```python
@dataclass
class Item:
    price: float

item = Item(price="free")   # No error! Annotations are not validated.
```
The annotation tells the decorator *that a field exists*, and tells readers
(and type checkers like mypy) what should go there. Python itself will happily
store `"free"` in a `float` field. Validation is your job — `__post_init__`.

### 3. `order=True` with non-comparable fields
```python
@dataclass(order=True)
class BadLap:
    seconds: float
    gear: list = field(default_factory=list)   # lists cannot be compared with <

sorted([BadLap(60.0, [1]), BadLap(59.0, [])])  # TypeError: '<' not supported
```
Fix: mark fields that should not affect ordering with `field(compare=False)`.

---

## Quick Reference

```python
from dataclasses import dataclass, field, FrozenInstanceError

@dataclass                          # auto: __init__, __repr__, __eq__
class Product:
    name: str                       # plain field
    price: float = 0.0              # default value
    tags: list = field(default_factory=list)    # mutable default, done right

    def __post_init__(self):        # runs right after __init__
        if self.price < 0:
            raise ValueError("price cannot be negative")

@dataclass(frozen=True)             # immutable AND hashable
class Config:
    host: str
    port: int

@dataclass(order=True)              # adds <, <=, >, >=
class Lap:
    seconds: float
    runner: str = field(compare=False)
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!

---

[Return to Module Overview](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
