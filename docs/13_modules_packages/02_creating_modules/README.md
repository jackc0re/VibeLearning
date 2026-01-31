# 🔧 Creating Modules

A **module** is simply a Python file (`.py`) containing definitions and statements. Creating your own modules lets you organize and reuse code.

---

## ✅ Basic Module Structure

```python
# mymodule.py

"""Module docstring describing what this module does."""

# Constants
DEFAULT_TIMEOUT = 30

# Functions
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

# Classes
class Calculator:
    """A simple calculator."""
    def add(self, a: int, b: int) -> int:
        return a + b
```

---

## ✅ The `__name__` Variable

Every module has a `__name__` attribute:

```python
# mymodule.py
print(f"Module name: {__name__}")

def main():
    print("Running as main program")

if __name__ == "__main__":
    main()
```

- When run directly: `__name__` is `"__main__"`
- When imported: `__name__` is the module name (e.g., `"mymodule"`)

This pattern lets files work both as importable modules AND as runnable scripts.

---

## ✅ Controlling Public API with `__all__`

```python
# mymodule.py

__all__ = ["public_function", "PublicClass"]

def public_function():
    """This is part of the public API."""
    pass

def _private_helper():
    """Convention: underscore prefix = internal use."""
    pass

class PublicClass:
    pass

class _InternalClass:
    pass
```

- `__all__` defines what `from module import *` includes
- Names starting with `_` are conventionally private
- Users can still import private names explicitly

---

## ✅ Module-Level Code

Code at the module level runs once during import:

```python
# config.py

import os

# This runs when the module is imported
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///default.db")

def get_connection():
    return connect(DATABASE_URL)
```

Be careful with module-level code that has side effects!

---

## ✅ Module Design Guidelines

1. **One clear purpose** - Each module should do one thing well
2. **Clean public API** - Use `__all__` and `_` prefixes
3. **Minimal dependencies** - Import only what you need
4. **Document** - Add docstrings for module and public items
5. **Avoid side effects** - Module code shouldn't modify global state

---

## 🔍 Key Takeaways

- A module is just a `.py` file with definitions.
- Use `if __name__ == "__main__":` for script/module dual use.
- `__all__` defines the public API for star imports.
- Keep modules focused on a single responsibility.

---

[Back: Imports](../01_imports/) | [Next: Packages](../03_packages/)
