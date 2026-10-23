"""References vs Values - Examples
=================================

Demonstrations:
- aliasing
- shallow vs deep copy

Run:
    python examples.py
"""

from __future__ import annotations

import copy


# =============================================================================
# DEMO: ALIASING
# =============================================================================

def demo_aliasing() -> None:
    nums = [1, 2]
    alias = nums
    alias.append(3)
    print("Aliasing:")
    print("  nums:", nums)
    print("  alias:", alias)
    print("  same object:", nums is alias)


# =============================================================================
# DEMO: SHALLOW VS DEEP COPY
# =============================================================================

def demo_copying() -> None:
    nested = [[1], [2]]

    shallow = copy.copy(nested)
    deep = copy.deepcopy(nested)

    shallow[0].append(99)

    print("\nCopying:")
    print("  nested:", nested, "(changed via shallow copy)")
    print("  shallow:", shallow)
    print("  deep:", deep, "(independent)")


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("REFERENCES VS VALUES - Examples")
    print("=" * 50)

    print("\n--- Aliasing ---\n")
    demo_aliasing()

    print("\n--- Shallow vs deep copy ---")
    demo_copying()

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
