"""Big-O Notation - Examples

This file includes small functions with typical Big-O behaviors.

Run:
    python examples.py
"""

from __future__ import annotations


def constant_time_first(items: list[int]) -> int | None:
    """O(1): first element access."""
    return items[0] if items else None


def linear_sum(items: list[int]) -> int:
    """O(n): sum over all items."""
    total = 0
    for x in items:
        total += x
    return total


def quadratic_pairs(items: list[int]) -> int:
    """O(n^2): count pairs."""
    count = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            _ = (items[i], items[j])
            count += 1
    return count


if __name__ == "__main__":
    data = list(range(10))
    print("O(1) first:", constant_time_first(data))
    print("O(n) sum:", linear_sum(data))
    print("O(n^2) pairs:", quadratic_pairs(data))

