"""Creating Modules - Exercises

Goals:
- create module-like structures with proper organization
- implement __all__ and naming conventions
- use the __name__ == "__main__" pattern

Run with:
    python exercises.py
"""

from __future__ import annotations

from typing import Any, Callable, Dict, List, Optional


# =============================================================================
# EXERCISE 1: Define Public API
# =============================================================================

# Define __all__ to export only: calculate_area, calculate_perimeter, Shape
__all__ = ["calculate_area", "calculate_perimeter", "Shape"]


def calculate_area(width: float, height: float) -> float:
    """Calculate area of a rectangle (public API)."""
    return _validate_positive(width) * _validate_positive(height)


def calculate_perimeter(width: float, height: float) -> float:
    """Calculate perimeter of a rectangle (public API)."""
    return 2 * (_validate_positive(width) + _validate_positive(height))


def _validate_positive(value: float) -> float:
    """Internal helper to validate positive numbers."""
    if value <= 0:
        raise ValueError("Value must be positive")
    return value


class Shape:
    """A shape class (public API)."""

    def __init__(self, name: str) -> None:
        self.name = name


class _InternalHelper:
    """Internal implementation class (not exported)."""

    pass


# =============================================================================
# EXERCISE 2: Module Registry Pattern
# =============================================================================

_registry: Dict[str, Callable[..., Any]] = {}


def exercise_2_register(name: str) -> Callable[[Callable], Callable]:
    """
    Create a decorator that registers a function in the module registry.

    Usage:
        @exercise_2_register("greet")
        def say_hello(name):
            return f"Hello, {name}!"

    Then get_registered("greet")("World") returns "Hello, World!"
    """

    def decorator(func: Callable) -> Callable:
        _registry[name] = func
        return func

    return decorator


def exercise_2_get_registered(name: str) -> Optional[Callable]:
    """Get a registered function by name, or None if not found."""
    return _registry.get(name)


def exercise_2_list_registered() -> List[str]:
    """Return sorted list of all registered function names."""
    return sorted(_registry.keys())


# Register some example functions for testing
@exercise_2_register("add")
def _add(a: int, b: int) -> int:
    return a + b


@exercise_2_register("multiply")
def _multiply(a: int, b: int) -> int:
    return a * b


# =============================================================================
# EXERCISE 3: Configuration Module Pattern
# =============================================================================


class _Config:
    """Module-level configuration singleton."""

    def __init__(self) -> None:
        self._settings: Dict[str, Any] = {
            "debug": False,
            "log_level": "INFO",
            "max_connections": 10,
        }

    def get(self, key: str, default: Any = None) -> Any:
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._settings[key] = value

    def all_settings(self) -> Dict[str, Any]:
        return dict(self._settings)


# Module-level singleton instance
_config = _Config()


def exercise_3_get_config(key: str, default: Any = None) -> Any:
    """Get a configuration value."""
    return _config.get(key, default)


def exercise_3_set_config(key: str, value: Any) -> None:
    """Set a configuration value."""
    _config.set(key, value)


def exercise_3_get_all_config() -> Dict[str, Any]:
    """Get all configuration as a dictionary."""
    return _config.all_settings()


# =============================================================================
# EXERCISE 4: Lazy Module Initialization
# =============================================================================

_expensive_resource: Optional[Dict[str, int]] = None


def exercise_4_get_resource() -> Dict[str, int]:
    """
    Get an expensive resource, initializing it lazily on first access.

    The resource is a dictionary mapping letters to their positions (a=1, b=2, etc.)
    It should only be created once, on the first call.
    """
    global _expensive_resource
    if _expensive_resource is None:
        # Simulate expensive initialization
        _expensive_resource = {chr(ord("a") + i): i + 1 for i in range(26)}
    return _expensive_resource


def exercise_4_is_initialized() -> bool:
    """Check if the resource has been initialized."""
    return _expensive_resource is not None


def exercise_4_reset() -> None:
    """Reset the resource (for testing purposes)."""
    global _expensive_resource
    _expensive_resource = None


# =============================================================================
# EXERCISE 5: Module Introspection
# =============================================================================


def exercise_5_get_public_functions(module: Any) -> List[str]:
    """
    Return a sorted list of public function names in a module.

    A function is public if:
    - It doesn't start with underscore
    - It's callable
    - It's not a class (use callable() and not isinstance(..., type))
    """
    public_funcs = []
    for name in dir(module):
        if name.startswith("_"):
            continue
        obj = getattr(module, name)
        if callable(obj) and not isinstance(obj, type):
            public_funcs.append(name)
    return sorted(public_funcs)


def exercise_5_get_module_exports(module: Any) -> List[str]:
    """
    Return the module's __all__ list if it exists, otherwise return
    a sorted list of all public names (not starting with underscore).
    """
    if hasattr(module, "__all__"):
        return list(module.__all__)
    return sorted(name for name in dir(module) if not name.startswith("_"))


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Creating Modules Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1: Define Public API
    print("\nExercise 1: Define Public API")
    try:
        # __all__ should contain exactly these names
        ok1 = set(__all__) == {"calculate_area", "calculate_perimeter", "Shape"}

        # Public functions should work
        ok2 = calculate_area(5, 3) == 15.0
        ok3 = calculate_perimeter(5, 3) == 16.0

        # Shape should be accessible
        ok4 = Shape("test").name == "test"

        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2: Module Registry Pattern
    print("\nExercise 2: Module Registry Pattern")
    try:
        # Check registered functions exist
        add_fn = exercise_2_get_registered("add")
        mult_fn = exercise_2_get_registered("multiply")

        ok1 = add_fn is not None and add_fn(2, 3) == 5
        ok2 = mult_fn is not None and mult_fn(2, 3) == 6
        ok3 = exercise_2_get_registered("nonexistent") is None
        ok4 = "add" in exercise_2_list_registered()

        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3: Configuration Module Pattern
    print("\nExercise 3: Configuration Module Pattern")
    try:
        # Get default config
        ok1 = exercise_3_get_config("debug") is False
        ok2 = exercise_3_get_config("log_level") == "INFO"
        ok3 = exercise_3_get_config("nonexistent", "default") == "default"

        # Set and get config
        exercise_3_set_config("debug", True)
        ok4 = exercise_3_get_config("debug") is True

        # Get all config
        all_cfg = exercise_3_get_all_config()
        ok5 = isinstance(all_cfg, dict) and "debug" in all_cfg

        # Reset for other tests
        exercise_3_set_config("debug", False)

        ok = ok1 and ok2 and ok3 and ok4 and ok5
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 4: Lazy Module Initialization
    print("\nExercise 4: Lazy Module Initialization")
    try:
        # Reset first
        exercise_4_reset()
        ok1 = exercise_4_is_initialized() is False

        # Get resource initializes it
        resource = exercise_4_get_resource()
        ok2 = exercise_4_is_initialized() is True
        ok3 = resource["a"] == 1 and resource["z"] == 26

        # Second call returns same object
        resource2 = exercise_4_get_resource()
        ok4 = resource is resource2  # Same object

        ok = ok1 and ok2 and ok3 and ok4
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 5: Module Introspection
    print("\nExercise 5: Module Introspection")
    try:
        import math

        # Get public functions from math module
        math_funcs = exercise_5_get_public_functions(math)
        ok1 = "sqrt" in math_funcs and "sin" in math_funcs
        ok2 = all(not f.startswith("_") for f in math_funcs)

        # Get exports from this module (has __all__)
        import sys

        this_module = sys.modules[__name__]
        exports = exercise_5_get_module_exports(this_module)
        ok3 = set(exports) == set(__all__)

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
