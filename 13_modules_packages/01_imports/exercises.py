"""Imports - Exercises

Goals:
- understand how Python finds modules
- practice different import patterns
- work with sys.path and sys.modules

Run with:
    python exercises.py
"""

from __future__ import annotations

import sys
from typing import List, Optional, Any


# =============================================================================
# EXERCISE 1: Check If Module Is Available
# =============================================================================


def exercise_1_is_module_available(module_name: str) -> bool:
    """
    Check if a module can be imported without actually importing it.

    Use importlib.util.find_spec to check availability.
    Returns True if the module exists, False otherwise.
    """
    import importlib.util

    spec = importlib.util.find_spec(module_name)
    return spec is not None


# =============================================================================
# EXERCISE 2: List Loaded Modules
# =============================================================================


def exercise_2_list_loaded_modules(prefix: str = "") -> List[str]:
    """
    Return a sorted list of currently loaded module names.

    If prefix is provided, only return modules starting with that prefix.
    Exclude modules starting with underscore.
    """
    modules = []
    for name in sys.modules.keys():
        if name.startswith("_"):
            continue
        if prefix and not name.startswith(prefix):
            continue
        modules.append(name)
    return sorted(modules)


# =============================================================================
# EXERCISE 3: Safe Import
# =============================================================================


def exercise_3_safe_import(module_name: str) -> Optional[Any]:
    """
    Try to import a module by name and return it.

    If the import fails, return None instead of raising an exception.
    """
    try:
        import importlib

        return importlib.import_module(module_name)
    except (ImportError, ModuleNotFoundError):
        return None


# =============================================================================
# EXERCISE 4: Get Module Path
# =============================================================================


def exercise_4_get_module_path(module_name: str) -> Optional[str]:
    """
    Return the file path of an installed module.

    Import the module and return its __file__ attribute.
    Return None if the module cannot be imported or has no __file__.
    """
    module = exercise_3_safe_import(module_name)
    if module is None:
        return None
    return getattr(module, "__file__", None)


# =============================================================================
# EXERCISE 5: Import Function By Name
# =============================================================================


def exercise_5_import_function(module_name: str, function_name: str) -> Optional[Any]:
    """
    Import a specific function from a module by name.

    Example: exercise_5_import_function("math", "sqrt") returns math.sqrt

    Return None if the module or function doesn't exist.
    """
    module = exercise_3_safe_import(module_name)
    if module is None:
        return None
    return getattr(module, function_name, None)


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Imports Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1: Check If Module Is Available
    print("\nExercise 1: Check If Module Is Available")
    try:
        # math should be available
        ok1 = exercise_1_is_module_available("math") is True
        # nonexistent should not be available
        ok2 = exercise_1_is_module_available("nonexistent_xyz_module") is False
        ok = ok1 and ok2
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    math available: {exercise_1_is_module_available('math')}")
            print(f"    nonexistent: {exercise_1_is_module_available('nonexistent_xyz_module')}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2: List Loaded Modules
    print("\nExercise 2: List Loaded Modules")
    try:
        # Import something to ensure it's loaded
        import json

        all_modules = exercise_2_list_loaded_modules()
        json_modules = exercise_2_list_loaded_modules("json")

        ok1 = isinstance(all_modules, list) and len(all_modules) > 0
        ok2 = all_modules == sorted(all_modules)  # Should be sorted
        ok3 = "json" in all_modules
        ok4 = all(m.startswith("json") for m in json_modules)
        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    is list with items: {ok1}")
            print(f"    is sorted: {ok2}")
            print(f"    contains json: {ok3}")
            print(f"    prefix filter works: {ok4}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3: Safe Import
    print("\nExercise 3: Safe Import")
    try:
        math_mod = exercise_3_safe_import("math")
        none_mod = exercise_3_safe_import("nonexistent_xyz_module")

        ok1 = math_mod is not None and hasattr(math_mod, "sqrt")
        ok2 = none_mod is None
        ok = ok1 and ok2
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 4: Get Module Path
    print("\nExercise 4: Get Module Path")
    try:
        json_path = exercise_4_get_module_path("json")
        none_path = exercise_4_get_module_path("nonexistent_xyz_module")

        ok1 = json_path is not None and "json" in json_path
        ok2 = none_path is None
        ok = ok1 and ok2
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    json path: {json_path}")
            print(f"    none path: {none_path}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 5: Import Function By Name
    print("\nExercise 5: Import Function By Name")
    try:
        sqrt_fn = exercise_5_import_function("math", "sqrt")
        none_fn = exercise_5_import_function("math", "nonexistent_function")
        none_mod = exercise_5_import_function("nonexistent_xyz_module", "func")

        ok1 = sqrt_fn is not None and sqrt_fn(16) == 4.0
        ok2 = none_fn is None
        ok3 = none_mod is None
        ok = ok1 and ok2 and ok3
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    print("\n" + "=" * 50)
    print("All tests passed!" if all_passed else "Some tests failed.")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
