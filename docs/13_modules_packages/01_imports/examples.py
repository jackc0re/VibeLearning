"""Imports - Examples

Demonstrations:
- different import styles
- exploring sys.path and sys.modules
- conditional imports and import errors

Run:
    python examples.py
"""

from __future__ import annotations

import sys


def demo_import_styles() -> None:
    """Show different ways to import."""
    print("=== Import Styles ===\n")

    # Style 1: Import whole module
    import math

    print(f"math.sqrt(16) = {math.sqrt(16)}")
    print(f"math.pi = {math.pi}")

    # Style 2: Import specific names
    from math import factorial, ceil

    print(f"factorial(5) = {factorial(5)}")
    print(f"ceil(3.2) = {ceil(3.2)}")

    # Style 3: Import with alias
    from datetime import datetime as dt

    print(f"Current time: {dt.now()}")
    print()


def demo_sys_path() -> None:
    """Show the module search path."""
    print("=== sys.path (Module Search Path) ===\n")

    for i, path in enumerate(sys.path[:5]):  # Show first 5
        print(f"  {i}: {path or '(current directory)'}")

    if len(sys.path) > 5:
        print(f"  ... and {len(sys.path) - 5} more paths")
    print()


def demo_sys_modules() -> None:
    """Show cached modules."""
    print("=== sys.modules (Cached Modules) ===\n")

    # Import a module
    import json

    # It's now in sys.modules
    print(f"'json' in sys.modules: {'json' in sys.modules}")
    print(f"Module location: {json.__file__}")

    # Show some loaded modules
    loaded = sorted(k for k in sys.modules.keys() if not k.startswith("_"))[:10]
    print(f"\nSome loaded modules: {loaded}")
    print()


def demo_import_once() -> None:
    """Demonstrate that module code runs only once."""
    print("=== Import Runs Once ===\n")

    # First import executes the module
    import math

    # Second import uses cached version
    import math as m

    # They're the same object
    print(f"Same object: {math is m}")
    print(f"Module id: {id(math)}")
    print()


def demo_conditional_import() -> None:
    """Show conditional/optional imports."""
    print("=== Conditional Imports ===\n")

    # Try to import an optional package
    try:
        import numpy as np

        print(f"numpy is available: version {np.__version__}")
    except ImportError:
        print("numpy is not installed (optional dependency)")

    # Check before importing
    import importlib.util

    spec = importlib.util.find_spec("requests")
    if spec is not None:
        import requests

        print(f"requests is available: version {requests.__version__}")
    else:
        print("requests is not installed")
    print()


def demo_import_error_handling() -> None:
    """Show how to handle import errors gracefully."""
    print("=== Import Error Handling ===\n")

    # Handling missing module
    try:
        import nonexistent_module
    except ModuleNotFoundError as e:
        print(f"ModuleNotFoundError: {e}")

    # Handling missing attribute
    try:
        from math import nonexistent_function
    except ImportError as e:
        print(f"ImportError: {e}")
    print()


def demo_reload_module() -> None:
    """Show how to reload a module (rarely needed)."""
    print("=== Reloading Modules ===\n")

    import json
    import importlib

    print(f"Before reload - id: {id(json)}")

    # Reload the module (gets fresh version)
    json = importlib.reload(json)

    print(f"After reload - id: {id(json)}")
    print("(Note: Reloading is rarely needed in practice)")
    print()


if __name__ == "__main__":
    demo_import_styles()
    demo_sys_path()
    demo_sys_modules()
    demo_import_once()
    demo_conditional_import()
    demo_import_error_handling()
    demo_reload_module()
