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

## ✅ Using `functools.wraps`

To preserve the original function’s metadata (like `__name__` and docstring):

```python
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

---

## 🔍 Key Takeaways

- Decorators wrap functions to add behavior.
- They use higher-order functions and closures.
- `@decorator` is syntax sugar for `func = decorator(func)`.

---

[Back to Closures](../06_closures/README.md)
