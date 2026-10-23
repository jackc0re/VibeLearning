# Debugging Cheatsheet

Quick reference for hunting bugs: print-debugging moves, `pdb` commands, how to read a traceback, and the usual suspects behind common symptoms.

---

## Print Debugging Checklist

`print()` is the fastest debugger you own — if you use it on purpose.

```python
print(f"entering process_order: items={items!r}")   # !r shows quotes/None clearly
print(f"total={total}, type={type(total)}")         # wrong type is a classic
print(f"len(names)={len(names)}")                   # off-by-one checks
```

Work through it in order:

1. **Reproduce** — make the bug happen on demand, every time.
2. **Narrow** — put a print before and after the suspect line. Does the value go in right and come out wrong? The bug is *inside*.
3. **Check types, not just values** — `"5"` vs `5` and `None` vs `0` print almost the same; use `!r` or `type()`.
4. **Label every print** — `print(value)` alone becomes mystery output. Use `f"var={var!r}"`.
5. **One change at a time** — if you change three things and it works, you don't know why.
6. **Delete your prints when done** — or graduate them to `logging` (see [08_error_handling](../../08_error_handling/README.md)).

When prints get overwhelming, step up to the debugger.

---

## pdb: breakpoint() and Commands

Drop `breakpoint()` (Python 3.7+) anywhere to pause there:

```python
def average(values):
    breakpoint()          # execution pauses here, (Pdb) prompt appears
    return sum(values) / len(values)
```

| Command | Short | Does |
|---------|-------|------|
| `next` | `n` | Execute the current line, step **over** calls |
| `step` | `s` | Step **into** a function call |
| `continue` | `c` | Run until the next `breakpoint()` (or the end) |
| `print expr` | `p expr` | Evaluate and print an expression, e.g. `p len(items)` |
| `list` | `l` | Show the code around the current line |
| `where` | `w` | Print the call stack — how you got here |
| `return` | `r` | Run until the current function returns |
| `up` / `down` | `u` / `d` | Move around the call stack |
| `pp expr` | | Pretty-print (great for dicts/lists) |
| `quit` | `q` | Exit the debugger |

You can also start a whole script under the debugger: `python -m pdb script.py`.

---

## Anatomy of a Traceback

Read it **bottom-up**: the last line tells you *what* broke, the lines above tell you *how you got there*.

```text
Traceback (most recent call last):
  File "main.py", line 8, in <module>
    total = average(numbers)
  File "main.py", line 5, in average
    return sum(values) / len(values)
ZeroDivisionError: division by zero
```

| Part | Meaning |
|------|---------|
| `Traceback (most recent call last):` | Header — the frames below are ordered oldest → newest |
| `File "main.py", line 8, in <module>` | A frame: file, line number, function name |
| The code line under each frame | The exact source that was running |
| `ZeroDivisionError: division by zero` | **Last line** — the exception type and message. Start here. |

How to use it:

1. Read the **last line** first — the error type usually names the problem.
2. Look at the **bottom-most frame** — that's where the exception was raised.
3. Walk **up** the frames to see who called it with what.
4. If you see *"During handling of the above exception, another exception occurred"* in the middle, there are two tracebacks — read each bottom-up.

---

## Common Bug Patterns

| Bug | Symptom | First check |
|-----|---------|-------------|
| **Off-by-one** | Loop runs once too often/too few, or `IndexError` | `range(n)` gives 0..n-1; the last index is `len(x) - 1`; slice ends are **exclusive** |
| **Mutable default** | A list/dict argument "remembers" old data between calls | `def f(x, items=[])` — the default is created **once**; use `items=None` and create inside |
| **Shadowed variable** | Value is `None` or stale; or `NameError` on a builtin | A local reuses a global's name (or you named a variable `list`, `sum`, `max`); check what's in scope at that line |
| **`==` vs `is`** | Comparison is `False` when values look equal (or `True` by accident) | `==` compares **values**, `is` compares **identity** — reserve `is` for `None`/`True`/`False` |
| **Integer division** | Expected `2.5`, got `2` (or `2.0`) | `/` is float division, `//` floors; check for `int(input())` and `//` where you meant `/` |
| **Encoding** | `UnicodeDecodeError`, or file text is garbled (mojibake) | `open()` without `encoding=` uses the platform default (e.g. cp1252 on Windows) — pass `encoding="utf-8"` |

Two of the sneakiest, side by side:

```python
# Mutable default — every call shares ONE list
def add_item(item, cart=[]):        # BUG
    cart.append(item)
    return cart

def add_item(item, cart=None):      # FIX
    if cart is None:
        cart = []
    cart.append(item)
    return cart

# == vs is — values vs identity
a = [1, 2]
b = [1, 2]
a == b   # True  — same contents
a is b   # False — different objects
x is None  # the one place `is` is exactly right
```

---

## Quick Reference

| Situation | Move |
|-----------|------|
| "What is this variable right now?" | `print(f"x={x!r}")` |
| "Where did the crash happen?" | Last traceback line, then bottom-most frame |
| "Slow down, show me each step" | `breakpoint()` + `n` / `s` / `p` |
| "How did I get into this function?" | `w` in pdb (or read the traceback frames) |
| "It only fails sometimes" | Reproduce first — add prints at the boundary |
| "Loop count feels wrong" | `print(len(seq))` and check `range` bounds |

---

**Full module:** [14_debugging](../../14_debugging/README.md) — start at [01_print_debugging](../../14_debugging/01_print_debugging/README.md), then [02_using_debuggers](../../14_debugging/02_using_debuggers/README.md), [03_reading_tracebacks](../../14_debugging/03_reading_tracebacks/README.md) and [04_common_bugs](../../14_debugging/04_common_bugs/README.md).

**Back to [Resources](../README.md)**
