"""
Pure Functions - Examples

Demonstrates pure vs impure functions and why purity matters.
Run with:
    python examples.py
"""

# =============================================================================
# PURE FUNCTIONS
# =============================================================================

def add(a, b):
    """Pure: output depends only on inputs."""
    return a + b


def celsius_to_fahrenheit(c):
    """Pure: deterministic conversion."""
    return (c * 9 / 5) + 32


def replace_item(items, index, value):
    """
    Pure: returns a NEW list with one item changed.
    Does not mutate the input list.
    """
    new_items = items.copy()
    new_items[index] = value
    return new_items


# =============================================================================
# IMPURE FUNCTIONS (FOR CONTRAST)
# =============================================================================

counter = 0


def next_id():
    """Impure: depends on and mutates global state."""
    global counter
    counter += 1
    return counter


def add_and_print(a, b):
    """Impure: has a side effect (printing)."""
    result = a + b
    print(f"Result is {result}")
    return result


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_pure_functions():
    print("=" * 60)
    print("PURE FUNCTIONS")
    print("=" * 60)

    print("\n1) Deterministic outputs")
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"add(2, 3) = {add(2, 3)} (same inputs, same output)")

    print("\n2) Conversion function")
    for c in [0, 25, 100]:
        print(f"{c}°C -> {celsius_to_fahrenheit(c)}°F")

    print("\n3) Avoiding mutation")
    items = ["a", "b", "c"]
    updated = replace_item(items, 1, "B")
    print(f"Original: {items}")
    print(f"Updated : {updated}")


def demo_impure_functions():
    print("\n" + "=" * 60)
    print("IMPURE FUNCTIONS (CONTRAST)")
    print("=" * 60)

    print("\n1) Global state")
    print(f"next_id() -> {next_id()}")
    print(f"next_id() -> {next_id()} (same call, different result)")

    print("\n2) Side effects")
    add_and_print(4, 5)


if __name__ == "__main__":
    demo_pure_functions()
    demo_impure_functions()
    print("\n✓ Examples complete!")
