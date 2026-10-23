"""Space Complexity - Examples
=============================

Demonstrations:
- list vs generator expressions
- in-place vs out-of-place operations

Run:
    python examples.py
"""

from __future__ import annotations


# =============================================================================
# DEMO: LIST VS GENERATOR
# =============================================================================

def demo_list_vs_generator() -> None:
    squares_list = [x * x for x in range(10)]
    squares_gen = (x * x for x in range(10))

    print("List vs generator:")
    print("  list:", squares_list)
    print("  gen first three:", [next(squares_gen), next(squares_gen), next(squares_gen)])


# =============================================================================
# DEMO: IN-PLACE VS OUT-OF-PLACE
# =============================================================================

def demo_in_place() -> None:
    nums = [3, 1, 2]
    print("\nSorting:")
    print("  original:", nums)
    nums.sort()  # in-place
    print("  after sort():", nums)


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("SPACE COMPLEXITY - Examples")
    print("=" * 50)

    print("\n--- List vs generator ---\n")
    demo_list_vs_generator()

    print("\n--- In-place vs out-of-place ---")
    demo_in_place()

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
