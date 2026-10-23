# 🔌 Context Managers

A **context manager** is like the stage crew at a theater. Before the show they
set the scene. After the show — whether it was a triumph or a disaster — they
*always* come back to strike the set. The `with` statement is the contract
between your code and that crew: setup happens before the body, and cleanup is
guaranteed after it, no matter what.

---

## 🔁 A Quick Refresher: try/finally

[Topic 02](../02_try_except_finally/README.md) showed that `finally` runs no
matter what, which makes it the tool for cleanup:

```python
file = open("data.txt", "w")
try:
    file.write("hello")
finally:
    file.close()   # runs even if the write raises
```

That works — but *you* have to remember the cleanup, every single time. The
`with` statement builds the try/finally shape into the language itself:

```python
with open("data.txt", "w") as file:
    file.write("hello")
# file.close() already happened here - even if write() raised
```

Same guarantee, much less bookkeeping. You have been using context managers all
along: [reading files](../../10_file_io/01_reading_files/README.md) is full of
`with open(...)` blocks for exactly this reason.

---

## ✅ What `with` Guarantees

Any object can be a context manager if it defines two methods:

```python
class Tracer:
    def __enter__(self):
        print("setup")
        return "tracer"          # this value is bound by 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("cleanup")
        return False             # never suppress exceptions

with Tracer() as t:
    print("body sees", t)
```

The `with` statement guarantees this exact sequence:

1. `__enter__` runs, and whatever it returns is bound to the name after `as`.
2. The body runs.
3. `__exit__(exc_type, exc_val, exc_tb)` runs **always**. If the body finished
   cleanly, all three arguments are `None`. If the body raised, they carry the
   exception's type, value, and traceback — and `__exit__` still runs before
   the exception continues on its way.

---

## 🚨 Returning True Suppresses the Exception

`__exit__` has one superpower, and it is dangerous: **if it returns `True`,
Python acts as if the exception never happened.**

```python
class BlackHole:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"swallowing {exc_type.__name__}: {exc_val}")
        return True   # the exception stops here!

with BlackHole():
    raise ValueError("this error vanishes")
print("execution just carries on")
```

> **⚠️ Warning:** `return True` hides *every* error — including real bugs like
> typos and `AttributeError`s. You will almost never want it. When you truly
> mean to ignore an error, use `contextlib.suppress` with a *specific*
> exception type instead (shown below). Returning `None` — which is what a
> function does when it has no return statement — propagates the exception,
> and that is *usually exactly what you want*.

---

## 🏗️ Writing Your Own: Class-Based Managers

Two classics. First, a timer:

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"took {self.elapsed:.6f}s")
        return False

with Timer() as timer:
    total = sum(range(1_000_000))
```

Second, a database transaction — every change lands together, or none do:

```python
class Transaction:
    def __init__(self, db):
        self.db = db
        self.pending = {}

    def set(self, key, value):
        self.pending[key] = value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.db.commit(self.pending)     # success: keep the changes
        else:
            self.db.rollback()               # failure: undo everything
        return False                         # let real errors surface
```

> Want more practice? The intermediate Exercises track already has a
> [Timer exercise](../../Exercises/intermediate/05_error_handling.py) — try it
> after working through this topic.

---

## ⚡ The Short Way: @contextmanager

For simple managers, a whole class is ceremony. `contextlib.contextmanager`
lets you write one as a generator instead:

```python
from contextlib import contextmanager
import time

@contextmanager
def timed(label):
    start = time.perf_counter()
    try:
        yield label                # the with-body runs at the yield
    finally:
        print(f"[{label}] took {time.perf_counter() - start:.6f}s")

with timed("summing"):
    total = sum(range(1_000_000))
```

Read it like this: everything before the `yield` is `__enter__`, the `yield`
itself marks where the body runs, and everything after it is `__exit__`. The
`try/finally` around the `yield` is **the whole point** — without it, the
cleanup lines are skipped whenever the body raises, which defeats the entire
purpose of a context manager.

---

## 🤫 The Polite Way to Ignore Errors: contextlib.suppress

Sometimes an error is *expected* and genuinely fine — deleting a file that may
not exist, for instance. `suppress` says exactly that:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    with open("maybe_cache.tmp") as f:
        data = f.read()
# FileNotFoundError: swallowed. Any other exception: still raised.
```

This is far better than a bare `except: pass`, because it documents *which*
error is okay and hides nothing else.

---

## 📚 Many Managers at Once: ExitStack

`with A, B, C:` works when you know the names in advance. When you do not —
say, opening every file named on the command line — use `ExitStack`:

```python
from contextlib import ExitStack

paths = ["a.txt", "b.txt", "c.txt"]   # any length, decided at runtime
with ExitStack() as stack:
    files = [stack.enter_context(open(p)) for p in paths]
# every file is closed here, in reverse order, even if one open() failed
```

`enter_context` registers each manager on the stack; when the `with` block
ends (cleanly or not), they all exit, last-in-first-out.

---

## ⚠️ Common Mistakes

### 1. Thinking `__exit__` must return something truthy

Returning `None` from `__exit__` propagates the exception — and that is
*usually correct*! Only return `True` when you truly intend to swallow the
error. If you find yourself typing `return True` "so it compiles", delete it.

### 2. Suppressing by accident

A `return True` left in `__exit__` silently hides *every* later error inside
the block — crashes turn into mysterious wrong answers. Keep `__exit__`
returning `False` (or nothing at all), and reach for `contextlib.suppress`
when ignoring an error is genuinely the right call.

### 3. A generator manager without try/finally around the yield

```python
@contextmanager
def broken():
    resource = acquire()
    yield
    release(resource)   # NEVER runs if the body raises!
```

If the body raises, the lines after `yield` are skipped — the resource leaks.
Wrap the yield: `try: yield ... finally: release(resource)`.

### 4. Using `with` on something that is not a manager

```python
with 42 as x:      # TypeError... but with a plain object:
    pass

class NotAManager:
    pass

try:
    with NotAManager():
        pass
except AttributeError as exc:
    print(exc)     # 'NotAManager' object has no attribute '__enter__'
```

The `with` statement needs `__enter__`/`__exit__`. If you see
`AttributeError: ... has no attribute '__enter__'` bubble out of a
`try/except`, the object was never a context manager — give it the two
methods (or wrap it with `contextlib.contextmanager`) rather than widening
the `except`.

---

## 📋 Quick Reference

| Tool | What it guarantees | Example |
|------|--------------------|---------|
| `with expr as name` | `__exit__` runs even if the body raises | `with open(path) as f:` |
| `__enter__` | setup; return value is bound by `as` | `return self` |
| `__exit__` returning `None`/`False` | exception propagates (usually right) | `return False` |
| `__exit__` returning `True` | exception suppressed (rare, dangerous) | `return True` |
| `@contextmanager` + `yield` | class-free manager; `yield` marks the body | `try: yield` / `finally:` |
| `contextlib.suppress(SomeError)` | ignore that specific error only | `with suppress(FileNotFoundError):` |
| `ExitStack` | any number of managers, one `with` | `stack.enter_context(m)` |

---

## 🔍 Key Takeaways

- `with` is `try/finally` with the cleanup guaranteed *by the language*.
- `__exit__` always runs; it receives the exception details, or three `None`s.
- Returning `True` from `__exit__` suppresses — almost never what you want.
- Prefer `@contextmanager` with `try/finally` around the `yield` for simple
  managers; use `suppress` for expected errors and `ExitStack` for a dynamic
  number of resources.

---

[Back: Logging ←](../05_logging/README.md) | [Next: Why Testing →](../../09_testing/01_why_testing/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
