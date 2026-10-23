"""Memory Basics - Examples
==========================

Demonstrations:
- object identity via id()
- mutability
- avoiding copies with memoryview

Run:
    python examples.py
"""

from __future__ import annotations


# =============================================================================
# DEMO: OBJECT IDENTITY
# =============================================================================

def demo_identity() -> None:
    a = [1, 2, 3]
    b = a
    c = list(a)

    print("Identity:")
    print("  id(a) == id(b):", id(a) == id(b))
    print("  id(a) == id(c):", id(a) == id(c))


# =============================================================================
# DEMO: MUTABILITY
# =============================================================================

def demo_mutability() -> None:
    nums = [1, 2]
    alias = nums
    nums.append(3)
    print("\nMutability:")
    print("  nums:", nums)
    print("  alias:", alias, "(same list)")

    s = "hi"
    t = s
    s = s + "!"  # creates a new string
    print("  strings:")
    print("    t:", t)
    print("    s:", s)
    print("    id(t) == id(s):", id(t) == id(s))


# =============================================================================
# DEMO: VIEWS WITH MEMORYVIEW
# =============================================================================

def demo_memoryview() -> None:
    data = b"abcdef"
    view = memoryview(data)

    slice_copy = data[1:4]  # bytes slice makes a new bytes object
    slice_view = view[1:4]  # memoryview slice is a view

    print("\nViews vs copies:")
    print("  slice_copy:", slice_copy)
    print("  slice_view.tobytes():", slice_view.tobytes())
    print("  slice_view.obj is data:", slice_view.obj is data)


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    print("=" * 50)
    print("MEMORY BASICS - Examples")
    print("=" * 50)

    print("\n--- Object identity ---\n")
    demo_identity()

    print("\n--- Mutability ---")
    demo_mutability()

    print("\n--- Views with memoryview ---")
    demo_memoryview()

    print("\n" + "=" * 50)
    print("Examples complete! Try exercises.py next.")
    print("=" * 50)


if __name__ == "__main__":
    main()
