"""Common Bugs - Examples

Demonstrations:
- frequently occurring bugs
- why they happen
- how to fix them

Run:
    python examples.py
"""

from __future__ import annotations

import copy
from typing import Any, Callable, Dict, List, Optional


def demo_off_by_one() -> None:
    """Demonstrate off-by-one errors."""
    print("=== Off-By-One Errors ===\n")

    items = ["a", "b", "c", "d"]

    print("Bug 1: Missing last element")
    print(f"  items = {items}")
    print("  for i in range(len(items) - 1):  # Misses 'd'")
    result = []
    for i in range(len(items) - 1):
        result.append(items[i])
    print(f"  Result: {result}")

    print("\nBug 2: Index out of bounds")
    print(f"  items[len(items)] would crash (index 4, max is 3)")

    print("\nBug 3: Fence-post error")
    print("  range(1, 10) gives 1-9, not 1-10")
    print(f"  list(range(1, 10)) = {list(range(1, 10))}")
    print()


def demo_mutable_default() -> None:
    """Demonstrate mutable default argument bug."""
    print("=== Mutable Default Argument ===\n")

    # The bug
    def bad_append(item: Any, items: List = []) -> List:
        items.append(item)
        return items

    print("def bad_append(item, items=[]):")
    print("    items.append(item)")
    print("    return items")
    print()

    result1 = bad_append(1)
    print(f"bad_append(1) = {result1}")

    result2 = bad_append(2)
    print(f"bad_append(2) = {result2}  # Surprise! Same list!")

    result3 = bad_append(3)
    print(f"bad_append(3) = {result3}  # Keeps growing!")

    # The fix
    def good_append(item: Any, items: Optional[List] = None) -> List:
        if items is None:
            items = []
        items.append(item)
        return items

    print("\nFix: Use None as default")
    print(f"good_append(1) = {good_append(1)}")
    print(f"good_append(2) = {good_append(2)}")
    print()


def demo_modify_while_iterating() -> None:
    """Demonstrate modifying while iterating bug."""
    print("=== Modifying While Iterating ===\n")

    # The bug
    items = [1, 2, 3, 4, 5, 6]
    print(f"Original: {items}")
    print("Trying to remove even numbers while iterating:")

    items_copy = items.copy()
    for item in items_copy:
        if item % 2 == 0:
            items_copy.remove(item)
    print(f"Result: {items_copy}")  # [1, 3, 5] - seems ok in this case

    items2 = [2, 4, 6, 8]
    print(f"\nOriginal: {items2}")
    for item in items2:
        if item % 2 == 0:
            items2.remove(item)
    print(f"Result: {items2}  # Bug! Skipped 4 and 8!")

    print("\nFix 1: List comprehension")
    items3 = [2, 4, 6, 8]
    items3 = [x for x in items3 if x % 2 != 0]
    print(f"Result: {items3}")

    print("\nFix 2: Iterate over copy")
    items4 = [2, 4, 6, 8]
    for item in items4.copy():
        if item % 2 == 0:
            items4.remove(item)
    print(f"Result: {items4}")
    print()


def demo_scope_issues() -> None:
    """Demonstrate variable scope bugs."""
    print("=== Variable Scope Issues ===\n")

    # The bug
    counter = 0

    def show_bug() -> None:
        # This would raise UnboundLocalError:
        # counter += 1  # Python thinks counter is local
        pass

    print("Bug: UnboundLocalError")
    print("  counter = 0")
    print("  def increment():")
    print("      counter += 1  # Error!")
    print()
    print("Python sees 'counter =' and assumes it's local,")
    print("but it doesn't exist locally yet.")

    # Fix with global (not recommended)
    def increment_global() -> int:
        global counter
        counter += 1
        return counter

    print("\nFix 1: global keyword (not recommended)")
    print(f"  increment_global() = {increment_global()}")

    # Better fix: pass and return
    def increment_better(value: int) -> int:
        return value + 1

    print("\nFix 2: Pass and return (better)")
    local_counter = 0
    local_counter = increment_better(local_counter)
    print(f"  increment_better(0) = {local_counter}")
    print()


def demo_type_confusion() -> None:
    """Demonstrate type confusion bugs."""
    print("=== Type Confusion ===\n")

    # String vs int
    user_input = "5"
    print(f'user_input = "5"  # String from input()')

    print(f"\nuser_input == 5: {user_input == 5}  # Always False!")
    print(f"int(user_input) == 5: {int(user_input) == 5}  # Correct")

    # String concatenation vs addition
    a, b = "3", "4"
    print(f'\na, b = "3", "4"')
    print(f"a + b = {a + b}  # String concatenation!")
    print(f"int(a) + int(b) = {int(a) + int(b)}  # Addition")
    print()


def demo_none_issues() -> None:
    """Demonstrate None-related bugs."""
    print("=== None Issues ===\n")

    # Comparison
    value = None
    print("Use 'is' for None comparison:")
    print(f"  value == None: {value == None}  # Works but not idiomatic")
    print(f"  value is None: {value is None}  # Preferred")

    # Not handling None
    def bad_process(data: Optional[str]) -> str:
        return data.upper()  # type: ignore  # Crashes if None

    def good_process(data: Optional[str]) -> str:
        if data is None:
            return ""
        return data.upper()

    print("\nHandling None:")
    print(f"  good_process(None) = '{good_process(None)}'")
    print(f"  good_process('hello') = '{good_process('hello')}'")
    print()


def demo_shallow_vs_deep_copy() -> None:
    """Demonstrate shallow vs deep copy."""
    print("=== Shallow vs Deep Copy ===\n")

    # Shallow copy
    original = [[1, 2], [3, 4]]
    print(f"original = {original}")

    shallow = original.copy()
    print(f"shallow = original.copy()")

    shallow[0][0] = 99
    print(f"shallow[0][0] = 99")
    print(f"shallow = {shallow}")
    print(f"original = {original}  # Also changed!")

    # Deep copy
    original2 = [[1, 2], [3, 4]]
    print(f"\noriginal2 = {original2}")

    deep = copy.deepcopy(original2)
    print("deep = copy.deepcopy(original2)")

    deep[0][0] = 99
    print("deep[0][0] = 99")
    print(f"deep = {deep}")
    print(f"original2 = {original2}  # Unchanged!")
    print()


def demo_boolean_traps() -> None:
    """Demonstrate boolean evaluation traps."""
    print("=== Boolean Traps ===\n")

    print("Falsy values in Python:")
    falsies = [None, False, 0, 0.0, "", [], {}, set()]
    for val in falsies:
        print(f"  bool({val!r:10}) = {bool(val)}")

    print("\nBug: Zero is falsy")
    count = 0
    print(f"count = {count}")
    print(f"if count: ... # Never runs! 0 is falsy")

    print("\nFix: Be explicit")
    print("if count is not None:  # Check for None specifically")
    print("if count > 0:          # Check for positive specifically")
    print("if count != 0:         # Check for non-zero specifically")
    print()


def demo_late_binding_closure() -> None:
    """Demonstrate late binding in closures."""
    print("=== Late Binding in Closures ===\n")

    # The bug
    print("Bug:")
    print("funcs = []")
    print("for i in range(3):")
    print("    funcs.append(lambda: i)")

    funcs_bad: List[Callable[[], int]] = []
    for i in range(3):
        funcs_bad.append(lambda: i)

    results_bad = [f() for f in funcs_bad]
    print(f"[f() for f in funcs] = {results_bad}  # All 2!")

    # The fix
    print("\nFix: Capture with default argument")
    print("for i in range(3):")
    print("    funcs.append(lambda i=i: i)  # i=i captures current value")

    funcs_good: List[Callable[[], int]] = []
    for i in range(3):
        funcs_good.append(lambda i=i: i)

    results_good = [f() for f in funcs_good]
    print(f"[f() for f in funcs] = {results_good}  # [0, 1, 2]")
    print()


def demo_dict_iteration() -> None:
    """Demonstrate dict modification during iteration."""
    print("=== Dict Modification During Iteration ===\n")

    # The bug
    data = {"a": 1, "b": 2, "c": 3}
    print(f"data = {data}")
    print("Trying to remove items while iterating:")

    # This would raise RuntimeError:
    # for key in data:
    #     if data[key] > 1:
    #         del data[key]  # RuntimeError!

    print("  RuntimeError: dictionary changed size during iteration")

    # Fix: Iterate over keys copy
    data2 = {"a": 1, "b": 2, "c": 3}
    for key in list(data2.keys()):
        if data2[key] > 1:
            del data2[key]
    print(f"\nFix: Iterate over list(data.keys())")
    print(f"Result: {data2}")

    # Or use dict comprehension
    data3 = {"a": 1, "b": 2, "c": 3}
    data3 = {k: v for k, v in data3.items() if v <= 1}
    print(f"\nFix: Dict comprehension")
    print(f"Result: {data3}")
    print()


def demo_equality_vs_identity() -> None:
    """Demonstrate == vs is confusion."""
    print("=== Equality (==) vs Identity (is) ===\n")

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = a")

    print(f"\na == b: {a == b}  # Equal values")
    print(f"a is b: {a is b}  # Different objects")
    print(f"a is c: {a is c}  # Same object")

    print("\nUse == for value comparison")
    print("Use 'is' only for None, True, False, or identity checks")
    print()


if __name__ == "__main__":
    demo_off_by_one()
    demo_mutable_default()
    demo_modify_while_iterating()
    demo_scope_issues()
    demo_type_confusion()
    demo_none_issues()
    demo_shallow_vs_deep_copy()
    demo_boolean_traps()
    demo_late_binding_closure()
    demo_dict_iteration()
    demo_equality_vs_identity()
