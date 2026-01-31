"""Print Debugging - Examples

Demonstrations:
- strategic print placement
- formatting debug output
- using logging for debugging

Run:
    python examples.py
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional


def demo_basic_print_debugging() -> None:
    """Show basic print debugging techniques."""
    print("=== Basic Print Debugging ===\n")

    def buggy_sum(numbers: List[int]) -> int:
        """Sum numbers - with debug prints."""
        print(f"[DEBUG] Input: {numbers}")
        print(f"[DEBUG] Input type: {type(numbers)}")

        total = 0
        for i, num in enumerate(numbers):
            print(f"[DEBUG] Iteration {i}: num={num}, total before={total}")
            total += num
            print(f"[DEBUG] Iteration {i}: total after={total}")

        print(f"[DEBUG] Final result: {total}")
        return total

    result = buggy_sum([1, 2, 3, 4, 5])
    print(f"Result: {result}\n")


def demo_f_string_equals() -> None:
    """Show the f-string = syntax for quick debugging."""
    print("=== F-String = Syntax (Python 3.8+) ===\n")

    x = 42
    name = "Alice"
    items = [1, 2, 3]

    # The = automatically includes the variable name
    print(f"{x=}")
    print(f"{name=}")
    print(f"{items=}")

    # Works with expressions too
    print(f"{len(items)=}")
    print(f"{x * 2=}")
    print(f"{name.upper()=}")
    print()


def demo_type_debugging() -> None:
    """Show how to debug type issues."""
    print("=== Type Debugging ===\n")

    def mystery_function(data: Any) -> None:
        # When you're not sure what type you're getting:
        print(f"data = {data!r}")  # !r shows repr (quotes for strings)
        print(f"type(data) = {type(data)}")
        print(f"type(data).__name__ = {type(data).__name__}")

        if hasattr(data, "__len__"):
            print(f"len(data) = {len(data)}")

        if hasattr(data, "__iter__"):
            print("data is iterable")

    mystery_function("hello")
    print()
    mystery_function([1, 2, 3])
    print()
    mystery_function({"a": 1})
    print()


def demo_conditional_debugging() -> None:
    """Show conditional debug output."""
    print("=== Conditional Debugging ===\n")

    DEBUG = True  # Toggle this to enable/disable debug output

    def process_items(items: List[int]) -> int:
        if DEBUG:
            print(f"[DEBUG] Starting with {len(items)} items")

        total = 0
        for item in items:
            if DEBUG and item > 5:
                print(f"[DEBUG] Large item found: {item}")
            total += item

        if DEBUG:
            print(f"[DEBUG] Finished, total={total}")

        return total

    result = process_items([1, 2, 8, 3, 10, 4])
    print(f"Result: {result}\n")


def demo_entry_exit_tracing() -> None:
    """Show function entry/exit tracing."""
    print("=== Entry/Exit Tracing ===\n")

    def outer(x: int) -> int:
        print(f">>> ENTER outer({x})")
        result = inner(x * 2)
        print(f"<<< EXIT outer() -> {result}")
        return result

    def inner(y: int) -> int:
        print(f"  >>> ENTER inner({y})")
        result = y + 10
        print(f"  <<< EXIT inner() -> {result}")
        return result

    final = outer(5)
    print(f"Final result: {final}\n")


def demo_checkpoint_markers() -> None:
    """Show using visual markers for checkpoints."""
    print("=== Checkpoint Markers ===\n")

    def complex_process(data: List[int]) -> int:
        print("=" * 40)
        print("STARTING complex_process")
        print("=" * 40)

        # Phase 1
        print("\n--- Phase 1: Filtering ---")
        filtered = [x for x in data if x > 0]
        print(f"After filtering: {filtered}")

        # Phase 2
        print("\n--- Phase 2: Transforming ---")
        transformed = [x * 2 for x in filtered]
        print(f"After transform: {transformed}")

        # Phase 3
        print("\n--- Phase 3: Aggregating ---")
        result = sum(transformed)
        print(f"Final sum: {result}")

        print("\n" + "=" * 40)
        print("COMPLETED complex_process")
        print("=" * 40)

        return result

    complex_process([-1, 2, -3, 4, 5])
    print()


def demo_dict_debugging() -> None:
    """Show debugging dictionary operations."""
    print("=== Dictionary Debugging ===\n")

    def process_user(user: Dict[str, Any]) -> str:
        print(f"[DEBUG] Received user dict:")
        for key, value in user.items():
            print(f"  {key}: {value!r} ({type(value).__name__})")

        # Check for expected keys
        expected_keys = {"name", "email", "age"}
        actual_keys = set(user.keys())
        missing = expected_keys - actual_keys
        extra = actual_keys - expected_keys

        if missing:
            print(f"[DEBUG] Missing keys: {missing}")
        if extra:
            print(f"[DEBUG] Extra keys: {extra}")

        name = user.get("name", "Unknown")
        return f"Processed: {name}"

    result = process_user({"name": "Alice", "email": "a@b.com", "role": "admin"})
    print(f"Result: {result}\n")


def demo_logging_debugging() -> None:
    """Show using logging module for debugging."""
    print("=== Using Logging Module ===\n")

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s - %(message)s",
    )
    logger = logging.getLogger("demo")

    def calculate(a: int, b: int) -> int:
        logger.debug(f"calculate called with a={a}, b={b}")

        if b == 0:
            logger.warning("Division by zero avoided, using 1 instead")
            b = 1

        result = a * b
        logger.info(f"Calculation complete: {result}")
        return result

    calculate(5, 3)
    calculate(10, 0)

    # Reset logging for other examples
    logging.getLogger().handlers.clear()
    print()


def demo_loop_debugging() -> None:
    """Show debugging loop issues."""
    print("=== Loop Debugging ===\n")

    def find_target(items: List[int], target: int) -> Optional[int]:
        print(f"[DEBUG] Searching for {target} in {items}")
        print(f"[DEBUG] List length: {len(items)}")

        for i in range(len(items)):
            print(f"[DEBUG] i={i}, items[i]={items[i]}, checking if == {target}")
            if items[i] == target:
                print(f"[DEBUG] Found at index {i}!")
                return i

        print(f"[DEBUG] Not found after checking all {len(items)} items")
        return None

    result = find_target([10, 20, 30, 40], 30)
    print(f"Result: {result}\n")


if __name__ == "__main__":
    demo_basic_print_debugging()
    demo_f_string_equals()
    demo_type_debugging()
    demo_conditional_debugging()
    demo_entry_exit_tracing()
    demo_checkpoint_markers()
    demo_dict_debugging()
    demo_logging_debugging()
    demo_loop_debugging()
