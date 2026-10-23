# 🎯 Structural Pattern Matching (`match`/`case`)

> ⚠️ **Requires Python 3.10+** (released 2021). Older Pythons cannot even *parse*
> `match`/`case` — the file fails before a single line runs. This is the one topic
> in this repo that needs a newer Python; everything else supports 3.8+.
>
> The topic **degrades gracefully**: `examples.py` and `exercises.py` contain no
> `match` syntax themselves, check your version, and run everywhere. On 3.10+ they
> pull in the `match`-only companions (`match_demo.py` and `match_solutions.py`);
> on older Pythons they print a friendly notice and still exit cleanly.

Pattern matching lets a value "announce itself" to your program — including what
it is *made of* — and your code picks the branch shaped like it.

---

## What is Pattern Matching?

Think of a **mail-sorting clerk**. With `if`/`elif`, the clerk asks yes/no questions
one at a time: "Is it for room 0? Is the second line 0? Is it fragile?" With
`match`, the clerk glances at the whole label at once — "a parcel addressed to
`[0, 0]`", "any letter that starts *say* followed by a message" — and drops it
straight into the right bin.

That glance-at-the-shape is called **structural** pattern matching: the pattern
describes the *structure* of the data (a two-item list, a dict with a `"type"`
key, the number `0`), not just one yes/no question about it.

---

## The `match` Statement

`match` takes one subject and compares it against `case` patterns, top to bottom:

```python
code = 404

match code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Something else")
# Prints: Not Found
```

### Key Points:
- The **first** matching case wins; the rest are skipped (like `elif` chains)
- There is **no fallthrough**: at most one case body ever runs
- `case _:` is the catch-all "else" — optional, but usually what you want
- Matching a case *may also bind names* (you'll see this below)

---

## Literal Patterns

The simplest pattern: a literal value, compared with `==`.

```python
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")
```

This reads like a C `switch`, but each case is checked with `==` and only the
matching branch runs.

---

## Capture Patterns

A **bare name** in a pattern always matches and binds the subject to that name.

```python
match value:
    case anything:              # matches ANY value, binds it to `anything`
        print(f"Got: {anything}")
```

⚠️ Big gotcha: `case anything:` does **not** compare against an existing variable
called `anything` — it *captures*. To compare against a variable, use a guard
(below) or a dotted value like `case settings.limit:`.

---

## The Wildcard `_`

`_` matches anything but binds nothing. It is the "else" of pattern matching.

```python
match reply:
    case "y" | "yes":
        print("Agreed")
    case "n" | "no":
        print("Declined")
    case _:
        print("Unclear answer")
```

---

## Or-Patterns

The `|` operator lets one case accept several alternatives.

```python
match answer.lower():
    case "y" | "yes":
        agreed = True
    case "n" | "no":
        agreed = False
```

Without an or-pattern you would repeat the whole body for each spelling — this is
one place `match` is clearly tidier than `if`/`elif`.

---

## Guards: `case pattern if condition`

A guard is an extra condition attached to a case. The case matches only when
**both** the pattern and the guard are true.

```python
match n:
    case 0:
        print("exactly zero")
    case n if n > 0:            # anything positive
        print("positive")
    case _:
        print("negative")
```

Read `case n if n > 0` as: "match anything, bind it to `n`, but only take this
branch when `n > 0`."

---

## Sequence Patterns (Destructuring)

A sequence pattern checks the **shape** of a list/tuple and unpacks it in one step:

```python
match point:
    case [0, 0]:
        print("the origin")
    case [0, y]:
        print(f"on the y-axis (y={y})")
    case [x, 0]:
        print(f"on the x-axis (x={x})")
    case [x, y]:
        print(f"somewhere in the plane ({x}, {y})")
```

`case [x, y]` matches *any* two-item sequence — and binds `x` and `y` to its items.

Add `*rest` to gather "everything else", however many items that is:

```python
match parts:
    case ["say", *words]:
        print("You said: " + " ".join(words))
    case ["go", direction]:
        print(f"Walking {direction}")
```

The `if`/`elif` version of that needs `len()`, slicing, and indexing; the `match`
version says exactly what it accepts.

---

## Mapping Patterns (Dictionaries)

A mapping pattern checks the keys you list — extra keys are fine — and binds the
values you name:

```python
match event:
    case {"type": "click", "x": x, "y": y}:
        print(f"Click at ({x}, {y})")
    case {"type": "key", "key": key}:
        print(f"Key: {key}")
    case {"type": other}:
        print(f"Event: {other}")
```

A click event that also carries `"button": "left"` still matches the first case.
`**rest` collects leftover keys, like `*rest` does for sequences.

---

## Class Patterns (a peek)

Patterns can also name a class and match its attributes, e.g.
`case Point(x=0, y=0):` for a `Point` instance at the origin. They need classes
(and optionally `__match_args__`), so we return to them in
[04_oop_concepts](../../04_oop_concepts/README.md).

---

## When `match` Beats `if`/`elif`

Reach for `match` when the interesting part is the **shape** of the data:

```python
# if/elif: unpack, len(), index, repeat — easy to get subtly wrong
if len(parts) >= 2 and parts[0] == "say":
    message = " ".join(parts[1:])
elif parts == ["help"]:
    message = "Showing help."
# ...

# match: say exactly what you accept, in one line per shape
match parts:
    case ["help"]:
        message = "Showing help."
    case ["say", *words]:
        message = " ".join(words)
```

`match` shines at: **destructuring** (`[x, y]`, `["say", *words]`), **or-patterns**
(`case "y" | "yes":`), and **dict-with-known-keys** matching. For plain value
ranges ("score >= 90", "age <= 12"), a plain `if`/`elif` chain from
[03_control_flow](../03_control_flow/README.md) is still the right tool.

---

## Common Mistakes

### 1. Expecting fallthrough (or expecting an error)
There is no C-style fallthrough: at most one case runs. And if **nothing**
matches and there is no `case _:`? The value simply falls past the whole `match`
and the program carries on — silently.

```python
value = "banana"
match value:
    case "apple":
        print("fruit A")
# Prints NOTHING. No error. Execution just moves on.
```

That's why the wildcard `case _:` is your friend: it makes "none of the above"
explicit instead of silent.

### 2. Thinking a sequence pattern matches a specific list
Patterns match **structure, not identity**. `case [0, 0]:` doesn't mean "the list
called `[0, 0]`" — it means "any two-item sequence whose items are both `0`".
Likewise `case [x, y]:` matches *every* two-item sequence, so order your cases
from most specific (`[0, 0]`) to least (`[x, y]`).

### 3. Forgetting `case _:` as the catch-all
Without it, unmatched input does nothing — which can hide bugs for a long time.
Either end with `case _:` or be *deliberately* ignoring the rest.

### Bonus: bare names capture, they don't compare
`case limit:` (bare name) matches everything and *binds* `limit`. Comparing
against a variable needs a guard: `case v if v == limit:`.

---

## Quick Reference

| Pattern | Example | Matches |
|---------|---------|---------|
| Literal | `case 404:` | value equal to `404` (compared with `==`) |
| Capture | `case name:` | anything; binds it to `name` |
| Wildcard | `case _:` | anything; binds nothing (catch-all) |
| Or-pattern | `case "y" \| "yes":` | either alternative |
| Guard | `case n if n > 0:` | pattern **and** the extra condition |
| Sequence | `case [x, y]:` | any two-item list/tuple; unpacks into `x`, `y` |
| Star | `case [first, *rest]:` | one item, then zero or more gathered in `rest` |
| Mapping | `case {"type": t}:` | dict having a `"type"` key; extra keys allowed |
| Class | `case Point(x=0, y=0):` | `Point` instance with those attribute values |

**Files in this topic:** `examples.py` and `exercises.py` run on any Python (3.8+)
and gate the version for you; `match_demo.py` and `match_solutions.py` are the
`match`-only companions, imported on 3.10+.

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py) —
it starts from if/elif versions you already understand and walks you up to
`match`/`case`. The worked `match` rewrites live in
[match_solutions.py](match_solutions.py).

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
