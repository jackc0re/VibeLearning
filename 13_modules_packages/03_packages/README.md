# 📁 Packages

A **package** is a directory containing Python modules and a special `__init__.py` file. Packages help organize larger projects into hierarchical namespaces.

---

## ✅ Package Structure

```
mypackage/
├── __init__.py          # Makes this directory a package
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

---

## ✅ The `__init__.py` File

The `__init__.py` file:
- Makes a directory a Python package
- Runs when the package is imported
- Can be empty or contain initialization code

```python
# mypackage/__init__.py

"""MyPackage - A sample package."""

__version__ = "1.0.0"

# Import commonly used items for convenience
from .module1 import important_function
from .module2 import UsefulClass

__all__ = ["important_function", "UsefulClass", "module1", "module2"]
```

---

## ✅ Importing from Packages

```python
# Import the package
import mypackage
mypackage.important_function()

# Import a module from the package
from mypackage import module1
module1.some_function()

# Import specific items
from mypackage.module1 import some_function

# Import from subpackage
from mypackage.subpackage import module3
from mypackage.subpackage.module3 import deep_function
```

---

## ✅ Relative Imports

Inside a package, use relative imports with dots:

```python
# mypackage/module2.py

# Import from same package (one dot)
from . import module1
from .module1 import helper_function

# Import from parent package (two dots)
from .. import parent_module
from ..sibling_package import other_module
```

- `.` means current package
- `..` means parent package
- Only works inside packages (not in scripts run directly)

---

## ✅ Namespace Packages (Python 3.3+)

Packages without `__init__.py` are namespace packages. They allow splitting a package across multiple directories:

```
location1/
└── mypkg/
    └── module_a.py

location2/
└── mypkg/
    └── module_b.py

# Both contribute to the same 'mypkg' namespace
import mypkg.module_a
import mypkg.module_b
```

---

## 🔍 Key Takeaways

- Packages are directories with `__init__.py`
- Use `__init__.py` to define package-level imports and `__all__`
- Relative imports (`.`, `..`) work within packages
- Organize large projects into logical package hierarchies

---

[Back: Creating Modules](../02_creating_modules/README.md) | [Next: Virtual Environments](../04_virtual_environments/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
