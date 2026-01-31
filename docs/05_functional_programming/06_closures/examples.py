"""
Closures - Examples

Shows how functions can capture enclosing variables.
Run with:
    python examples.py
"""

# =============================================================================
# FUNCTION FACTORY
# =============================================================================

def make_adder(n):
    """Return a function that adds n."""
    def add(x):
        return x + n
    return add


def demo_function_factory():
    print("=" * 60)
    print("FUNCTION FACTORY")
    print("=" * 60)
    add5 = make_adder(5)
    add10 = make_adder(10)
    print(f"add5(3) = {add5(3)}")
    print(f"add10(3) = {add10(3)}")


# =============================================================================
# NONLOCAL STATE
# =============================================================================

def make_counter(start=0):
    """Return a counter function that remembers state."""
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


def demo_counter():
    print("\n" + "=" * 60)
    print("NONLOCAL STATE")
    print("=" * 60)
    counter = make_counter(10)
    print(counter())  # 11
    print(counter())  # 12
    print(counter())  # 13


if __name__ == "__main__":
    demo_function_factory()
    demo_counter()
    print("\n✓ Examples complete!")
