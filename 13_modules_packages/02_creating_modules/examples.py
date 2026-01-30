"""Creating Modules - Examples

Demonstrations:
- module structure and organization
- __name__ and __all__ usage
- module-level initialization

Run:
    python examples.py
"""

from __future__ import annotations

import sys
from typing import List


# =============================================================================
# Example: Module Constants and Configuration
# =============================================================================

# Module-level constants (run once when imported)
VERSION = "1.0.0"
DEBUG = False
MAX_RETRIES = 3


def demo_module_constants() -> None:
    """Show how module constants work."""
    print("=== Module Constants ===\n")
    print(f"VERSION: {VERSION}")
    print(f"DEBUG: {DEBUG}")
    print(f"MAX_RETRIES: {MAX_RETRIES}")
    print()


# =============================================================================
# Example: Public vs Private Names
# =============================================================================

# Public API (no underscore prefix)
__all__ = ["public_function", "PublicClass", "VERSION"]


def public_function(x: int) -> int:
    """A public function - part of the module's API."""
    return _private_helper(x) * 2


def _private_helper(x: int) -> int:
    """A private helper - not part of the public API."""
    return x + 10


class PublicClass:
    """A public class - part of the module's API."""

    def __init__(self, value: int) -> None:
        self.value = value
        self._internal_state = _private_helper(value)

    def get_result(self) -> int:
        return self._internal_state


class _InternalClass:
    """An internal class - implementation detail."""

    pass


def demo_public_private() -> None:
    """Demonstrate public vs private conventions."""
    print("=== Public vs Private Names ===\n")

    print(f"__all__ defines public API: {__all__}")
    print()

    # Public usage
    result = public_function(5)
    print(f"public_function(5) = {result}")

    obj = PublicClass(10)
    print(f"PublicClass(10).get_result() = {obj.get_result()}")

    # Private is still accessible (but discouraged)
    helper_result = _private_helper(5)
    print(f"_private_helper(5) = {helper_result} (internal use only)")
    print()


# =============================================================================
# Example: __name__ Variable
# =============================================================================


def demo_name_variable() -> None:
    """Show how __name__ works."""
    print("=== __name__ Variable ===\n")
    print(f"This module's __name__: {__name__}")

    if __name__ == "__main__":
        print("This file is being run directly")
    else:
        print("This file was imported")
    print()


# =============================================================================
# Example: Module Documentation
# =============================================================================


def demo_module_documentation() -> None:
    """Show module documentation features."""
    print("=== Module Documentation ===\n")

    # Module docstring (first string in file)
    print(f"Module docstring: {__doc__[:50]}...")

    # Function docstring
    print(f"Function docstring: {demo_module_documentation.__doc__}")

    # Module file location
    print(f"Module file: {__file__}")
    print()


# =============================================================================
# Example: Module as a Namespace
# =============================================================================


def demo_module_as_namespace() -> None:
    """Show how modules act as namespaces."""
    print("=== Module as Namespace ===\n")

    # Get all public names in this module
    current_module = sys.modules[__name__]
    public_names = [
        name for name in dir(current_module) if not name.startswith("_")
    ]

    print("Public names in this module:")
    for name in sorted(public_names)[:10]:  # Show first 10
        obj = getattr(current_module, name)
        obj_type = type(obj).__name__
        print(f"  {name}: {obj_type}")
    print()


# =============================================================================
# Example: Factory Pattern in Module
# =============================================================================

# Module-level registry
_handlers: dict[str, type] = {}


def register_handler(name: str):
    """Decorator to register a handler class."""

    def decorator(cls: type) -> type:
        _handlers[name] = cls
        return cls

    return decorator


@register_handler("json")
class JsonHandler:
    def parse(self, data: str) -> dict:
        import json

        return json.loads(data)


@register_handler("csv")
class CsvHandler:
    def parse(self, data: str) -> List[List[str]]:
        return [line.split(",") for line in data.strip().split("\n")]


def get_handler(name: str):
    """Factory function to get handler by name."""
    if name not in _handlers:
        raise ValueError(f"Unknown handler: {name}")
    return _handlers[name]()


def demo_factory_pattern() -> None:
    """Demonstrate module-level factory pattern."""
    print("=== Module Factory Pattern ===\n")

    print(f"Registered handlers: {list(_handlers.keys())}")

    json_handler = get_handler("json")
    result = json_handler.parse('{"key": "value"}')
    print(f"JSON parsed: {result}")

    csv_handler = get_handler("csv")
    result = csv_handler.parse("a,b,c\n1,2,3")
    print(f"CSV parsed: {result}")
    print()


# =============================================================================
# Main Entry Point
# =============================================================================


def main() -> None:
    """Main function - runs when script is executed directly."""
    demo_module_constants()
    demo_public_private()
    demo_name_variable()
    demo_module_documentation()
    demo_module_as_namespace()
    demo_factory_pattern()


# This block only runs when the file is executed directly
if __name__ == "__main__":
    main()
