# 🪄 Dunder Methods and the Data Model

**Dunder** methods (short for "double underscore", like `__len__`) are the hooks
that let your own classes plug into Python's built-in syntax. When you write
`len(playlist)` or `"Song" in playlist` or `a + b`, Python translates each piece
of syntax into a method call on your object. That translation table is called
the **data model** — and once you know it, your classes start feeling native.

> This topic builds **one `Playlist` class** from scratch, adding one dunder at
> a time. Every step is runnable in [examples.py](examples.py) — run it while
> you read.

---

## 🎬 Python Calls Dunders For You

**Analogy:** a light switch. You flip the switch (`len(x)`); you never touch the
wiring behind the wall (`x.__len__()`). The wiring is the dunder — Python owns
the connection.

```python
repr(obj)      # Python calls:  obj.__repr__()
len(obj)       # Python calls:  obj.__len__()
item in obj    # Python calls:  obj.__contains__(item)
a + b          # Python calls:  a.__add__(b)
```

You have been using dunders all along — every string, list, and dict gets its
powers from them. Writing your own just extends the same system to your classes.

The habit to build: call the friendly syntax (`repr(x)`, `len(x)`), not the
dunder (`x.__repr__()`, `x.__len__()`). The builtins are shorter, and they also
work on objects that get the behavior from somewhere else.

## 🖨️ `__repr__` vs `__str__`

**Analogy:** `__repr__` is the developer's nametag ("Employee #4021");
`__str__` is the friendly introduction ("Hi, I'm Sam from support").

By default, printing your own class is useless:

```python
<__main__.Playlist object at 0x000001E2...>   # technically true, helpful never
```

Fix it with two methods:

```python
class Playlist:
    def __init__(self, songs=None, name="Untitled"):
        self.songs = list(songs) if songs else []   # songs: (title, artist) tuples
        self.name = name

    def __repr__(self):
        # Unambiguous, for DEBUGGING. Looks like the code that built it.
        return f"Playlist(name={self.name!r}, songs={len(self.songs)})"

    def __str__(self):
        # Readable, for USERS. print() and str() use this.
        lines = [f"{self.name} ({len(self.songs)} songs)"]
        for i, (title, artist) in enumerate(self.songs, 1):
            lines.append(f"  {i}. {title} - {artist}")
        return "\n".join(lines)
```

- `print(playlist)` and `str(playlist)` call `__str__` (the pretty one).
- `repr(playlist)`, the debugger, and containers (a list of playlists) call
  `__repr__` (the precise one).
- If `__str__` is missing, Python falls back to `__repr__` — so when you only
  write one, write `__repr__`.

## ⚖️ `__eq__` and the `__hash__` Contract

By default, `==` compares identity: two playlists with identical songs are
"not equal" because they are two different objects. Define `__eq__` to compare
by content instead.

But equality comes with a contract. Defining `__eq__` sets `__hash__` to
`None`, which makes your objects **unhashable** — they can no longer be dict
keys or set members:

```python
>>> {p: "night drive"}                     # p has __eq__ but no __hash__
TypeError: unhashable type: 'Playlist'
```

The fix is to define `__hash__` too, and to keep the two consistent:

```python
def __eq__(self, other):
    if not isinstance(other, Playlist):
        return NotImplemented
    return self.songs == other.songs

def __hash__(self):
    return hash(tuple(self.songs))   # equal playlists -> equal hashes
```

> **The contract:** if `a == b`, then `hash(a) == hash(b)`. Break it and your
> objects get "lost" inside dicts and sets. If you hash mutable state (like a
> playlist that grows), either freeze the state first or reconsider hashing —
> this is the same trade-off [hash tables](../../02_data_structures/10_hash_tables/README.md)
> are built on.

## 📏 `__len__`

```python
def __len__(self):
    return len(self.songs)     # must return a whole number (an int)
```

Now `len(playlist)` reports the song count, and `if not playlist:` works too
(an empty playlist is falsy). Python checks the return value: return `"3"`
(a string) instead of `3` and you get a `TypeError`.

## 🔢 `__getitem__` (and Iteration For Free)

```python
def __getitem__(self, index):
    if isinstance(index, slice):                 # playlist[1:3]
        return Playlist(self.songs[index], name=self.name)
    return self.songs[index]                     # playlist[0], playlist[-1]
```

Now `playlist[0]` grabs the first song, `playlist[-1]` the last, and
`playlist[1:3]` returns a new `Playlist` (a slice).

Here is the aha moment: **supporting indexing gives you iteration for free.**
Long before `__iter__` existed, `for song in playlist:` already works — Python
falls back to calling `playlist[0]`, `playlist[1]`, ... until `IndexError`.

## 🔍 `__contains__`

```python
def __contains__(self, item):
    # Accept a full ("Title", "Artist") tuple OR just a title string.
    for title, artist in self.songs:
        if item == title or item == (title, artist):
            return True
    return False
```

`"Dune" in playlist` now reads like the question it is. (`in` also has a
fallback: without `__contains__`, Python tries iteration.)

## 🚶 `__iter__` (the Modern Way)

The legacy "index until IndexError" loop works, but the explicit, modern way
is a generator method — a method that `yield`s its items:

```python
def __iter__(self):
    for song in self.songs:
        yield song
```

One definition unlocks every iteration context: `for` loops, `list(playlist)`,
`tuple(playlist)`, unpacking (`for title, artist in playlist`), comprehensions,
`max`, `sum`, `sorted`... This is also what lets `__contains__` and helpers
like `random.sample` consume the playlist directly.

## 📞 `__call__`

**Analogy:** a DJ you hired once (configured at setup) but can just shout at
("drop the intro!") whenever you need them.

```python
class ShuffleIntroDJ:
    def __init__(self, playlist, intro_count=2):
        self.playlist = playlist
        self.intro_count = intro_count

    def __call__(self):
        picks = random.sample(list(self.playlist), self.intro_count)
        return Playlist(picks, name="Shuffle intro")

dj = ShuffleIntroDJ(favorites, intro_count=2)
dj()          # an object you CALL like a function
```

`__call__` shines when an object is expensive to configure once but cheap to
use many times — cached loaders, model predictors, retry policies.

## ➕ `__add__` (and a Word on `__radd__`)

```python
def __add__(self, other):
    if not isinstance(other, Playlist):
        return NotImplemented          # let Python try the other side
    return Playlist(self.songs + other.songs,
                    name=f"{self.name} + {other.name}")
```

`favorites + workout` returns a **new** `Playlist` — `+` should never mutate
either side (that would surprise every reader of `a + b`).

Returning `NotImplemented` (the object, not the string) tells Python "this
operand can't handle it", and Python then asks the *right* operand via
`__radd__` — that is how `3 + some_vector` can work even though ints know
nothing about your class. You will rarely need `__radd__`, but you should
recognize the name.

---

## ⚠️ Common Mistakes

1. **Defining `__eq__` without `__hash__`, then using the object as a dict key
   or set member** — defining `__eq__` alone makes instances unhashable and
   `{obj: value}` raises `TypeError: unhashable type`. Define both, or set
   `__hash__ = None` on purpose if the object must not be hashed.
2. **Returning a non-int from `__len__`** — `return "3"` or `return 3.0`
   raises `TypeError` when Python checks the result. `__len__` must return a
   whole number (and should never be negative).
3. **Calling dunders directly** — `x.__len__()` instead of `len(x)`,
   `x.__repr__()` instead of `repr(x)`. The builtins are the interface; the
   dunders are the wiring behind the wall.
4. **Living with `<Playlist object at 0x7f...>`** — the default repr wastes
   every debugging session it appears in. `__repr__` is usually the *first*
   dunder a class deserves, not the last.

---

## 📝 Quick Reference

| Dunder | Triggered by | Should return |
|---|---|---|
| `__repr__` | `repr(x)`, debugger, containers | unambiguous debug string |
| `__str__` | `print(x)`, `str(x)` | readable user-facing string |
| `__eq__` | `x == y` | `True`/`False` (or `NotImplemented`) |
| `__hash__` | dict key, set member | int; equal objects need equal hashes |
| `__len__` | `len(x)`, truthiness of containers | non-negative int |
| `__getitem__` | `x[k]`, slices, (legacy) for-loops | the item, or a result for a slice |
| `__contains__` | `item in x` | bool |
| `__iter__` | for-loops, `list(x)`, unpacking | iterator (usually via `yield`) |
| `__call__` | `x(...)` | anything the "call" should produce |
| `__add__` | `x + y` | a new object (or `NotImplemented`) |
| `__radd__` | `y + x` when `y` can't handle it | a new object |

---

[Next: Dataclasses](../09_dataclasses/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
