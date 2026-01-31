"""Common Bugs - Exercises

Goals:
- identify and fix common bugs
- recognize bug patterns
- write correct code avoiding common pitfalls

Run with:
    python exercises.py
"""

from __future__ import annotations

import copy
from typing import Any, Callable, Dict, List, Optional, Tuple


# =============================================================================
# EXERCISE 1: Fix Mutable Default Argument
# =============================================================================


def exercise_1_collect_items(
    item: Any, collection: Optional[List[Any]] = None
) -> List[Any]:
    """
    Add an item to a collection and return it.

    Bug to fix: Using mutable default argument.
    The correct implementation should create a NEW list each time
    if no collection is provided.
    """
    if collection is None:
        collection = []
    collection.append(item)
    return collection


def exercise_1_collect_to_dict(
    key: str, value: Any, data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Add a key-value pair to a dict and return it.

    Same fix pattern as above but for dicts.
    """
    if data is None:
        data = {}
    data[key] = value
    return data


# =============================================================================
# EXERCISE 2: Fix Off-By-One Errors
# =============================================================================


def exercise_2_get_last_n(items: List[Any], n: int) -> List[Any]:
    """
    Return the last n items from a list.

    Handle edge cases:
    - n > len(items): return all items
    - n <= 0: return empty list
    """
    if n <= 0:
        return []
    if n >= len(items):
        return list(items)
    return items[-n:]


def exercise_2_range_inclusive(start: int, end: int) -> List[int]:
    """
    Return a list of integers from start to end, INCLUSIVE.

    Example: range_inclusive(1, 5) -> [1, 2, 3, 4, 5]
    """
    if start > end:
        return []
    return list(range(start, end + 1))


def exercise_2_middle_element(items: List[Any]) -> Optional[Any]:
    """
    Return the middle element of a list.

    For even-length lists, return the earlier middle.
    Return None for empty lists.
    """
    if not items:
        return None
    middle_index = (len(items) - 1) // 2
    return items[middle_index]


# =============================================================================
# EXERCISE 3: Fix Iteration Mutation
# =============================================================================


def exercise_3_filter_in_place(items: List[int], predicate: Callable[[int], bool]) -> None:
    """
    Remove items that don't match predicate, modifying list in place.

    This must modify the original list, not create a new one.
    Must handle the iteration-mutation bug correctly.
    """
    # Iterate backwards to safely remove items
    for i in range(len(items) - 1, -1, -1):
        if not predicate(items[i]):
            del items[i]


def exercise_3_remove_duplicates_preserve_order(items: List[Any]) -> List[Any]:
    """
    Return a new list with duplicates removed, preserving order.

    Do NOT modify the original list.
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# =============================================================================
# EXERCISE 4: Fix Closure Capture
# =============================================================================


def exercise_4_make_multipliers(n: int) -> List[Callable[[int], int]]:
    """
    Create n multiplier functions.

    make_multipliers(3) should return [f0, f1, f2] where:
    - f0(x) returns x * 0
    - f1(x) returns x * 1
    - f2(x) returns x * 2

    Must handle the late binding closure bug.
    """
    return [lambda x, i=i: x * i for i in range(n)]


def exercise_4_make_adders(values: List[int]) -> List[Callable[[], int]]:
    """
    Create functions that return each value plus 10.

    make_adders([1, 2, 3]) returns [f1, f2, f3] where:
    - f1() returns 11
    - f2() returns 12
    - f3() returns 13

    Must handle the late binding closure bug.
    """
    return [lambda v=v: v + 10 for v in values]


# =============================================================================
# EXERCISE 5: Identify and Categorize Bugs
# =============================================================================


def exercise_5_identify_bug(code_snippet: str) -> str:
    """
    Identify the type of bug in the code snippet.

    Returns one of:
    - "mutable_default"
    - "off_by_one"
    - "modify_while_iterating"
    - "closure_capture"
    - "type_confusion"
    - "none_handling"
    - "shallow_copy"
    - "unknown"
    """
    code = code_snippet.lower()
    code_no_space = code.replace(" ", "")

    # Check for mutable default argument
    if "def " in code:
        lines = code_snippet.split("\n")
        for line in lines:
            line_lower = line.lower()
            if "def " in line_lower:
                # Check for =[] or ={} in the function signature
                line_no_space = line_lower.replace(" ", "")
                if "=[]" in line_no_space or "={}" in line_no_space:
                    return "mutable_default"

    # Check for modifying while iterating
    if "for " in code and ("remove" in code or "del " in code):
        if "items" in code or "list" in code:
            return "modify_while_iterating"

    # Check for closure capture bug
    if "lambda" in code and "for " in code:
        if "i=i" not in code_no_space and "v=v" not in code_no_space:
            return "closure_capture"

    # Check for off-by-one
    if "range(len" in code and "- 1)" in code:
        return "off_by_one"

    # Check for shallow copy issue
    if ".copy()" in code and "[[" in code:
        return "shallow_copy"

    # Check for None comparison
    if "== none" in code:
        return "none_handling"

    # Check for type confusion
    if "input(" in code and ("==" in code or ">" in code or "<" in code):
        if "int(" not in code and "float(" not in code:
            return "type_confusion"

    return "unknown"


def exercise_5_fix_bug(bug_type: str) -> str:
    """
    Return a short description of how to fix the bug type.
    """
    fixes = {
        "mutable_default": "Use None as default, create new list/dict inside function",
        "off_by_one": "Check loop bounds, use len() correctly, verify inclusive/exclusive",
        "modify_while_iterating": "Iterate over copy, or use list comprehension",
        "closure_capture": "Use default argument to capture value: lambda x=x: ...",
        "type_confusion": "Convert types explicitly: int(), str(), float()",
        "none_handling": "Use 'is None' instead of '== None'",
        "shallow_copy": "Use copy.deepcopy() for nested structures",
    }
    return fixes.get(bug_type, "Unknown bug type")


# =============================================================================
# TESTS
# =============================================================================


def run_tests() -> None:
    print("Running Common Bugs Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1: Fix Mutable Default Argument
    print("\nExercise 1: Fix Mutable Default Argument")
    try:
        # Should create new list each call
        r1 = exercise_1_collect_items(1)
        r2 = exercise_1_collect_items(2)
        ok1 = r1 == [1] and r2 == [2]  # Not [1, 2]!

        # Should create new dict each call
        d1 = exercise_1_collect_to_dict("a", 1)
        d2 = exercise_1_collect_to_dict("b", 2)
        ok2 = d1 == {"a": 1} and d2 == {"b": 2}

        ok = ok1 and ok2
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    List test: r1={r1}, r2={r2}")
            print(f"    Dict test: d1={d1}, d2={d2}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 2: Fix Off-By-One Errors
    print("\nExercise 2: Fix Off-By-One Errors")
    try:
        # get_last_n
        ok1 = exercise_2_get_last_n([1, 2, 3, 4, 5], 3) == [3, 4, 5]
        ok2 = exercise_2_get_last_n([1, 2], 5) == [1, 2]
        ok3 = exercise_2_get_last_n([1, 2, 3], 0) == []

        # range_inclusive
        ok4 = exercise_2_range_inclusive(1, 5) == [1, 2, 3, 4, 5]
        ok5 = exercise_2_range_inclusive(3, 3) == [3]

        # middle_element
        ok6 = exercise_2_middle_element([1, 2, 3]) == 2
        ok7 = exercise_2_middle_element([1, 2, 3, 4]) == 2  # Earlier middle
        ok8 = exercise_2_middle_element([]) is None

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7 and ok8
        print("  ", "PASS" if ok else "FAIL")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 3: Fix Iteration Mutation
    print("\nExercise 3: Fix Iteration Mutation")
    try:
        # filter_in_place
        items1 = [1, 2, 3, 4, 5, 6]
        exercise_3_filter_in_place(items1, lambda x: x % 2 == 0)
        ok1 = items1 == [2, 4, 6]

        # remove_duplicates_preserve_order
        original = [1, 2, 1, 3, 2, 4]
        result = exercise_3_remove_duplicates_preserve_order(original)
        ok2 = result == [1, 2, 3, 4]
        ok3 = original == [1, 2, 1, 3, 2, 4]  # Original unchanged

        ok = ok1 and ok2 and ok3
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    filter_in_place: {items1}")
            print(f"    remove_dups: {result}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 4: Fix Closure Capture
    print("\nExercise 4: Fix Closure Capture")
    try:
        # make_multipliers
        mults = exercise_4_make_multipliers(3)
        ok1 = mults[0](10) == 0
        ok2 = mults[1](10) == 10
        ok3 = mults[2](10) == 20

        # make_adders
        adders = exercise_4_make_adders([1, 2, 3])
        ok4 = adders[0]() == 11
        ok5 = adders[1]() == 12
        ok6 = adders[2]() == 13

        ok = ok1 and ok2 and ok3 and ok4 and ok5 and ok6
        print("  ", "PASS" if ok else "FAIL")
        if not ok:
            print(f"    mults: {[m(10) for m in mults]}")
            print(f"    adders: {[a() for a in adders]}")
        all_passed = all_passed and ok
    except Exception as exc:
        all_passed = False
        print("  FAIL raised unexpectedly:", exc)

    # Exercise 5: Identify and Categorize Bugs
    print("\nExercise 5: Identify and Categorize Bugs")
    try:
        code1 = "def foo(x, items=[]):\n    items.append(x)"
        ok1 = exercise_5_identify_bug(code1) == "mutable_default"

        code2 = "for item in items:\n    if bad:\n        items.remove(item)"
        ok2 = exercise_5_identify_bug(code2) == "modify_while_iterating"

        # Test fix descriptions
        fix = exercise_5_fix_bug("mutable_default")
        ok3 = "None" in fix

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
