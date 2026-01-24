# 📥 Imports

The **import system** is how Python finds and loads code from other files. Understanding imports is essential for organizing larger projects.

---

## ✅ Basic Import Syntax

```python
# Import the whole module
import math
print(math.sqrt(16))  # 4.0

# Import specific names
from math import sqrt, pi
print(sqrt(16))  # 4.0

# Import with alias
import numpy as np
from datetime import datetime as dt
```

---

## ✅ What Happens During Import

When you import a module, Python:

1. **Searches** for the module in `sys.path`
2. **Compiles** the `.py` file to bytecode (cached in `__pycache__`)
3. **Executes** the module code once
4. **Caches** the module in `sys.modules`

Subsequent imports of the same module use the cached version.

---

## ✅ The Search Path (`sys.path`)

Python looks for modules in this order:

```python
import sys
print(sys.path)
# ['', '/usr/lib/python3.x', '/usr/lib/python3.x/site-packages', ...]
```

1. **Current directory** (or script directory)
2. **PYTHONPATH** environment variable directories
3. **Standard library** directories
4. **Site-packages** (installed packages)

---

## ✅ Import Styles

```python
# Style 1: Import module (preferred for large modules)
import os
os.path.join("a", "b")  # Clear where join comes from

# Style 2: Import specific names (good for frequently used items)
from os.path import join, exists
join("a", "b")  # Shorter, but origin less clear

# Style 3: Import all (generally avoid)
from os.path import *  # Pollutes namespace, hard to track origins
```

---

## ✅ Common Import Patterns

```python
# Standard library first, then third-party, then local
import os
import sys

import requests
import numpy as np

from myproject import utils
from myproject.models import User
```

---

## 🔍 Key Takeaways

- `import module` vs `from module import name` have different use cases.
- Python caches imports in `sys.modules` for efficiency.
- The search path (`sys.path`) determines where Python looks for modules.
- Follow PEP 8 import ordering: stdlib, third-party, local.

---

[Back: Module 13 README](../README.md) | [Next: Creating Modules](../02_creating_modules/)
