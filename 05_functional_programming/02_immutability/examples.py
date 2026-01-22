"""
Immutability - Examples

Shows how to work with immutable data patterns in Python.
Run with:
    python examples.py
"""

# =============================================================================
# IMMUTABLE TYPES
# =============================================================================

def demo_immutable_types():
    print("=" * 60)
    print("IMMUTABLE TYPES")
    print("=" * 60)

    name = "alice"
    upper = name.upper()
    print(f"Original: {name}")
    print(f"Upper   : {upper} (new string)")

    point = (2, 5)
    moved = (point[0] + 1, point[1] - 2)
    print(f"Point   : {point}")
    print(f"Moved   : {moved} (new tuple)")


# =============================================================================
# COPY-ON-WRITE WITH MUTABLE TYPES
# =============================================================================

def demo_copy_on_write():
    print("\n" + "=" * 60)
    print("COPY-ON-WRITE")
    print("=" * 60)

    nums = [1, 2, 3]
    new_nums = nums + [4]
    print(f"Original list: {nums}")
    print(f"New list     : {new_nums}")

    person = {"name": "Alice", "age": 30}
    updated = {**person, "age": 31}
    print(f"Original dict: {person}")
    print(f"Updated dict : {updated}")


# =============================================================================
# IMMUTABLE DEFAULTS
# =============================================================================

def append_item(items, item):
    """
    Returns a new list with item appended.
    Does not mutate the input list.
    """
    return items + [item]


def demo_no_mutation():
    print("\n" + "=" * 60)
    print("NO MUTATION")
    print("=" * 60)

    base = ["a", "b"]
    extended = append_item(base, "c")
    print(f"Base    : {base}")
    print(f"Extended: {extended}")


if __name__ == "__main__":
    demo_immutable_types()
    demo_copy_on_write()
    demo_no_mutation()
    print("\n✓ Examples complete!")
