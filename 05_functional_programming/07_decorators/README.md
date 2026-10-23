# 🎁 Decorators

Decorators are **functions that wrap other functions** to extend or modify their behavior. They are built on higher-order functions and closures.

---

## ✅ Basic Idea

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    return f"Hello, {name}!"
```

Calling `greet("Alice")` now prints a log and returns the greeting.

---

## ✅ Why Decorators?

- Add logging or timing
- Validate inputs
- Cache results
- Enforce permissions

---

## ✅ Decorator Factories: Decorators That Take Arguments

A plain decorator receives only the function. What if you want to configure it, like `@repeat(3)`? Then you need a **decorator factory**: a function that takes the arguments and *returns* a decorator. That means three nested layers:

```python
from functools import wraps

def repeat(times):                      # layer 1: factory, takes the arguments
    def decorator(func):                # layer 2: the actual decorator
        @wraps(func)
        def wrapper(*args, **kwargs):   # layer 3: the replacement function
            result = None
            for _ in range(times):      # `times` comes from the closure
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def ping():
    print("ping!")
    return "pong"

ping()          # prints "ping!" three times, returns "pong"
```

Reading `@repeat(3)` from Python's point of view helps: it is `ping = repeat(3)(ping)`. First `repeat(3)` runs and returns `decorator` (remembering `times=3` in a closure); then that decorator wraps `ping`. Two calls, one line of sugar. If you skip the parentheses and write `@repeat`, the function lands in `times` and nothing works — the arguments are what make it a factory call.

---

## ⚠️ What Happens Without `functools.wraps`

Every wrapper shadows the function it replaces, so `greet.__name__` is no longer `"greet"`. Try it:

```python
def logger_broken(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger_broken
def greet(name):
    """Say hello to someone."""
    return f"Hello, {name}!"

print(greet.__name__)   # 'wrapper'  - the real name is gone
print(greet.__doc__)    # None        - the docstring is gone too
```

The damage is not just cosmetic: tracebacks and debuggers now point at `wrapper`, `help(greet)` documents the wrong signature (`(*args, **kwargs)`), and any tool that inspects functions (docs generators, registration by name, `inspect.signature`) sees garbage. The fix is one line — `@wraps(func)` on the wrapper, which copies `__name__`, `__doc__`, `__module__`, `__qualname__`, and `__wrapped__` from the original:

```python
from functools import wraps

def logger_fixed(func):
    @wraps(func)                    # <- the only change
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger_fixed
def greet(name):
    """Say hello to someone."""
    return f"Hello, {name}!"

print(greet.__name__)   # 'greet'
print(greet.__doc__)    # 'Say hello to someone.'
```

Rule of thumb: **every** wrapper gets `@wraps(func)`. It costs nothing and saves whoever debugs the code later.

---

## ⚠️ Common Mistakes

1. **Forgetting to return the wrapper** - a decorator must `return wrapper`; returning
   `wrapper()` calls the function at import time and replaces it with its result.
2. **Skipping `@wraps(func)`** - the decorated function loses its name, docstring, and
   signature, which breaks `help()`, tracebacks, and introspection tools.
3. **Writing `@repeat` instead of `@repeat(3)`** - a decorator factory must be *called*
   first. Without parentheses the function itself is passed as `times`.
4. **Losing the return value** - a wrapper that calls `func(*args, **kwargs)` without
   `return` silently turns every result into `None`.
5. **Decorators on functions with arguments** - if the wrapper is `def wrapper():` with
   no parameters, only zero-argument functions survive. Use `*args, **kwargs` and
   forward them.

---

## 📝 Quick Reference

| Piece | What it is | Example |
|---|---|---|
| Decorator | function taking a function, returning a replacement | `logger(func)` |
| `@deco` sugar | `func = deco(func)` | `@logger` above `def greet` |
| `*args, **kwargs` | forward any arguments through the wrapper | `func(*args, **kwargs)` |
| `@wraps(func)` | copies name/docstring/signature onto the wrapper | from `functools` |
| Decorator factory | takes arguments, returns a decorator (3 layers) | `repeat(times)(func)` |

```python
from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...                         # do something before/after
        return func(*args, **kwargs)    # keep the return value!
    return wrapper
```

---

## 🔍 Key Takeaways

- Decorators wrap functions to add behavior.
- They use higher-order functions and closures.
- `@decorator` is syntax sugar for `func = decorator(func)`.
- A decorator *factory* (`@repeat(3)`) adds one more layer so decorators can take arguments.
- Always decorate wrappers with `@wraps(func)` to preserve the original's metadata.

---

[Back to Closures](../06_closures/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
