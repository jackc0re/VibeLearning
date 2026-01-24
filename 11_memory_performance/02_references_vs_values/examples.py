"""References vs Values - Examples

Demonstrations:
- aliasing
- shallow vs deep copy

Run:
    python examples.py
"""

from __future__ import annotations

import copy


def demo_aliasing() -> None:
    nums = [1, 2]
    alias = nums
    alias.append(3)
    print("Aliasing:")
    print("  nums:", nums)
    print("  alias:", alias)
    print("  same object:", nums is alias)


def demo_copying() -> None:
    nested = [[1], [2]]

    shallow = copy.copy(nested)
    deep = copy.deepcopy(nested)

    shallow[0].append(99)

    print("\nCopying:")
    print("  nested:", nested, "(changed via shallow copy)")
    print("  shallow:", shallow)
    print("  deep:", deep, "(independent)")


if __name__ == "__main__":
    demo_aliasing()
    demo_copying()

