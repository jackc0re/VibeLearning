"""Packages - Exercises

Goals:
- understand package structure
- work with package imports
- explore installed packages

Run with:
    python exercises.py
"""

from __future__ import annotations

import sys
from types import ModuleType
from typing import Any, Dict, List, Optional


# =============================================================================
# EXERCISE 1: Check If Module Is Package
# =============================================================================


def exercise_1_is_package(module_name: str) -> Optional[bool]:
    """
    Check if an imported module is a package.

    A package has a __path__ attribute.
    Returns True if package, False if regular module, None if can't import.
    """
    try:
        import importlib

        module = importlib.import_module(module_name)
        return hasattr(module, "__path__")
    except (ImportError, ModuleNotFoundError):
        return None


# =============================================================================
# EXERCISE 2: List Package Submodules
# =============================================================================


def exercise_2_list_submodules(package_name: str) -> List[str]:
    """
    Return a sorted list of direct submodule names for a package.

    Only return submodules that are already loaded in sys.modules.
    For example, for "email" might return ["email.message", "email.utils"]

    Return empty list if package not found or not a package.
    """
    if package_name not in sys.modules:
        try:
            import importlib

            importlib.import_module(package_name)
        except (ImportError, ModuleNotFoundError):
            return []

    prefix = package_name + "."
    submodules = []

    for name in sys.modules:
        if name.startswith(prefix):
            # Check if it's a direct submodule (no more dots after prefix)
            remainder = name[len(prefix) :]
            if "." not in remainder:
                submodules.append(name)

    return sorted(submodules)


# =============================================================================
# EXERCISE 3: Get Package Version
# =============================================================================


def exercise_3_get_version(package_name: str) -> Optional[str]:
    """
    Get the version string of an installed package.

    Try these attributes in order: __version__, VERSION, version
    Return None if package not found or has no version.
    """
    try:
        import importlib

        module = importlib.import_module(package_name)
    except (ImportError, ModuleNotFoundError):
        return None

    # Try common version attributes
    for attr in ("__version__", "VERSION", "version"):
        if hasattr(module, attr):
            version = getattr(module, attr)
            if isinstance(version, str):
                return version

    return None


# =============================================================================
# EXERCISE 4: Create Mock Package Hierarchy
# =============================================================================


def exercise_4_create_mock_package(
    name: str, submodules: Dict[str, Dict[str, Any]]
) -> ModuleType:
    """
    Create a mock package with submodules and register in sys.modules.

    Args:
        name: Package name (e.g., "myapp")
        submodules: Dict mapping submodule names to their attributes
                   e.g., {"utils": {"helper": lambda x: x*2}}

    Returns:
        The created package module

    Example:
        pkg = exercise_4_create_mock_package(
            "testpkg",
            {"utils": {"double": lambda x: x*2}}
        )
        # Now: from testpkg.utils import double  # works!
    """
    # Create the main package
    package = ModuleType(name)
    package.__path__ = [f"/mock/{name}"]
    package.__package__ = name
    package.__file__ = f"/mock/{name}/__init__.py"

    sys.modules[name] = package

    # Create submodules
    for submod_name, attributes in submodules.items():
        full_name = f"{name}.{submod_name}"
        submodule = ModuleType(full_name)
        submodule.__package__ = name
        submodule.__file__ = f"/mock/{name}/{submod_name}.py"

        for attr_name, attr_value in attributes.items():
            setattr(submodule, attr_name, attr_value)

        sys.modules[full_name] = submodule
        setattr(package, submod_name, submodule)

    return package


def exercise_4_cleanup_mock_package(name: str) -> None:
    """Remove a mock package and its submodules from sys.modules."""
    to_remove = [key for key in sys.modules if key == name or key.startswith(name + ".")]
    for key in to_remove:
        del sys.modules[key]


# =============================================================================
# EXERCISE 5: Resolve Import Path
# =============================================================================


def exercise_5_resolve_import(
    current_package: str, import_statement: str
) -> Optional[str]:
    """
    Resolve a relative import to an absolute module path.

    Args:
        current_package: The package where the import is written
                        (e.g., "myapp.utils")
        import_statement: A relative import like ".helpers" or "..models"

    Returns:
        The absolute module path, or None if invalid

    Examples:
        resolve("myapp.utils", ".helpers") -> "myapp.utils.helpers"
        resolve("myapp.utils", "..models") -> "myapp.models"
        resolve("myapp", "..something") -> None (can't go above root)
    """
    if not import_statement.startswith("."):
        # Absolute import, return as-is
        return import_statement

    # Count leading dots
    dots = 0
    for char in import_statement:
        if char == ".":
            dots += 1
        else:
            break

    remainder = import_statement[dots:]

    # Split current package
    parts = current_package.split(".")

    # One dot means current package, two dots means parent, etc.
    levels_up = dots - 1

    if levels_up >= len(parts):
        return None  # Can't go above root

    # Remove levels from parts
    if levels_up > 0:
        parts = parts[:-levels_up]

    # Add the remainder
    if remainder:
        parts.append(remainder)

    return ".".join(parts)


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Packages Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1: Check If Module Is Package
    print("\nExercise 1: Check If Module Is Package")
    try:
        # json is a package
        ok1 = exercise_1_is_package("json") is True
        # math is a module
        ok2 = exercise_1_is_package("math") is False
        # nonexistent should return None
        ok3 = exercise_1_is_package("nonexistent_xyz") is None

        ok = ok1 and ok2 and ok3
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    json is package: {exercise_1_is_package('json')}")
            print(f"    math is package: {exercise_1_is_package('math')}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2: List Package Submodules
    print("\nExercise 2: List Package Submodules")
    try:
        # Import some email submodules first
        import email.message
        import email.utils

        submodules = exercise_2_list_submodules("email")
        ok1 = "email.message" in submodules
        ok2 = "email.utils" in submodules
        ok3 = submodules == sorted(submodules)
        ok4 = exercise_2_list_submodules("nonexistent_xyz") == []

        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3: Get Package Version
    print("\nExercise 3: Get Package Version")
    try:
        # sys has a version
        sys_version = exercise_3_get_version("sys")
        # It should be a string or None
        ok1 = sys_version is None or isinstance(sys_version, str)
        # Nonexistent returns None
        ok2 = exercise_3_get_version("nonexistent_xyz") is None

        ok = ok1 and ok2
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 4: Create Mock Package Hierarchy
    print("\nExercise 4: Create Mock Package Hierarchy")
    try:
        pkg = exercise_4_create_mock_package(
            "testpkg_ex4", {"utils": {"double": lambda x: x * 2, "VALUE": 42}}
        )

        # Should be able to import
        ok1 = "testpkg_ex4" in sys.modules
        ok2 = "testpkg_ex4.utils" in sys.modules

        # Should have attributes
        from testpkg_ex4.utils import double, VALUE

        ok3 = double(21) == 42
        ok4 = VALUE == 42

        # Package should have __path__
        ok5 = hasattr(pkg, "__path__")

        # Cleanup
        exercise_4_cleanup_mock_package("testpkg_ex4")
        ok6 = "testpkg_ex4" not in sys.modules

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)
        exercise_4_cleanup_mock_package("testpkg_ex4")

    # Exercise 5: Resolve Import Path
    print("\nExercise 5: Resolve Import Path")
    try:
        # Test cases
        ok1 = exercise_5_resolve_import("myapp.utils", ".helpers") == "myapp.utils.helpers"
        ok2 = exercise_5_resolve_import("myapp.utils", "..models") == "myapp.models"
        ok3 = exercise_5_resolve_import("myapp.sub.deep", "...top") == "myapp.top"
        ok4 = exercise_5_resolve_import("myapp", "..something") is None  # Can't go above
        ok5 = exercise_5_resolve_import("pkg", "absolute") == "absolute"  # Absolute import

        ok = ok1 and ok2 and ok3 and ok4 and ok5
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    Test 1: {exercise_5_resolve_import('myapp.utils', '.helpers')}")
            print(f"    Test 2: {exercise_5_resolve_import('myapp.utils', '..models')}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
