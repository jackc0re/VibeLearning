"""Packages - Examples

Demonstrations:
- creating package-like structures in memory
- understanding package imports
- exploring real packages

Run:
    python examples.py
"""

from __future__ import annotations

import sys
import os
import importlib
from types import ModuleType
from typing import Dict, List, Any


def demo_package_basics() -> None:
    """Show how packages work conceptually."""
    print("=== Package Basics ===\n")

    # The 'json' module is actually a package
    import json

    print(f"json.__name__: {json.__name__}")
    print(f"json.__package__: {json.__package__}")
    print(f"json.__file__: {json.__file__}")

    # Check if it's a package (has __path__)
    is_package = hasattr(json, "__path__")
    print(f"json is a package: {is_package}")
    print()


def demo_explore_package() -> None:
    """Explore the structure of an installed package."""
    print("=== Exploring a Package ===\n")

    import email  # A stdlib package with submodules

    print(f"Package: {email.__name__}")
    print(f"Package path: {email.__path__}")

    # List submodules (from __all__ if available)
    if hasattr(email, "__all__"):
        print(f"Exported names (__all__): {email.__all__[:5]}...")
    print()


def demo_package_vs_module() -> None:
    """Show the difference between packages and modules."""
    print("=== Package vs Module ===\n")

    import math  # Module (single file)
    import json  # Package (directory)

    print("math (module):")
    print(f"  __file__: {math.__file__}")
    print(f"  has __path__: {hasattr(math, '__path__')}")

    print("\njson (package):")
    print(f"  __file__: {json.__file__}")
    print(f"  has __path__: {hasattr(json, '__path__')}")
    print()


def demo_init_py_execution() -> None:
    """Show that __init__.py runs on import."""
    print("=== __init__.py Execution ===\n")

    # When you import a package, __init__.py executes
    # The 'logging' package does initialization in __init__.py
    import logging

    # The package provides convenient access to commonly used items
    # These are defined/imported in logging/__init__.py
    print(f"logging.DEBUG = {logging.DEBUG}")
    print(f"logging.getLogger is available: {hasattr(logging, 'getLogger')}")

    # The __init__.py makes these accessible directly
    # without needing: from logging.something import getLogger
    print()


def demo_subpackage_imports() -> None:
    """Demonstrate importing from subpackages."""
    print("=== Subpackage Imports ===\n")

    # The 'email' package has submodules
    from email import message
    from email.mime import text

    print(f"email.message: {message.__name__}")
    print(f"email.mime.text: {text.__name__}")

    # Different import styles
    import email.utils

    print(f"email.utils.formatdate: {email.utils.formatdate}")
    print()


def demo_package_all() -> None:
    """Show how __all__ works in packages."""
    print("=== Package __all__ ===\n")

    import os

    # os.__all__ defines what 'from os import *' would import
    if hasattr(os, "__all__"):
        print(f"os.__all__ has {len(os.__all__)} items")
        print(f"First 5: {os.__all__[:5]}")
    else:
        print("os doesn't define __all__")
    print()


def demo_create_mock_package() -> None:
    """Create a mock package structure in memory (for demonstration)."""
    print("=== Mock Package Structure ===\n")

    # We can create module objects programmatically
    # This shows the structure, though you'd normally use files

    # Create a "package" module
    package = ModuleType("mypackage")
    package.__path__ = ["/fake/path/mypackage"]  # Makes it a package
    package.__package__ = "mypackage"

    # Create a "submodule"
    submodule = ModuleType("mypackage.utils")
    submodule.__package__ = "mypackage"

    def helper(x: int) -> int:
        return x * 2

    submodule.helper = helper

    # Register in sys.modules
    sys.modules["mypackage"] = package
    sys.modules["mypackage.utils"] = submodule

    # Now we can import it!
    from mypackage.utils import helper as h

    print(f"helper(21) = {h(21)}")

    # Clean up
    del sys.modules["mypackage"]
    del sys.modules["mypackage.utils"]
    print("(Mock package cleaned up)")
    print()


def demo_package_resources() -> None:
    """Show how to access package resources."""
    print("=== Package Resources ===\n")

    # Modern way: importlib.resources (Python 3.9+)
    try:
        from importlib import resources

        # List files in the json package
        import json

        # Get the package path
        print(f"json package location: {json.__file__}")

        # For packages with data files, you'd use:
        # resources.files('mypackage') / 'data.txt'
        print("(Use importlib.resources to access package data files)")
    except ImportError:
        print("importlib.resources not available")
    print()


def demo_relative_vs_absolute() -> None:
    """Explain relative vs absolute imports."""
    print("=== Relative vs Absolute Imports ===\n")

    print("Absolute imports (always work):")
    print("  import package.module")
    print("  from package.module import func")

    print("\nRelative imports (only inside packages):")
    print("  from . import sibling_module      # same directory")
    print("  from .sibling import func         # from sibling")
    print("  from .. import parent_module      # parent directory")
    print("  from ..other import func          # sibling package")

    print("\nRelative imports are based on __package__, not __file__")
    print()


if __name__ == "__main__":
    demo_package_basics()
    demo_explore_package()
    demo_package_vs_module()
    demo_init_py_execution()
    demo_subpackage_imports()
    demo_package_all()
    demo_create_mock_package()
    demo_package_resources()
    demo_relative_vs_absolute()
