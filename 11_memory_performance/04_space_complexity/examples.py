"""Space Complexity - Examples

Demonstrations:
- list vs generator expressions
- in-place vs out-of-place operations

Run:
    python examples.py
"""

from __future__ import annotations


def demo_list_vs_generator() -> None:
    squares_list = [x * x for x in range(10)]
    squares_gen = (x * x for x in range(10))

    print("List vs generator:")
    print("  list:", squares_list)
    print("  gen first three:", [next(squares_gen), next(squares_gen), next(squares_gen)])


def demo_in_place() -> None:
    nums = [3, 1, 2]
    print("\nSorting:")
    print("  original:", nums)
    nums.sort()  # in-place
    print("  after sort():", nums)


if __name__ == "__main__":
    demo_list_vs_generator()
    demo_in_place()

