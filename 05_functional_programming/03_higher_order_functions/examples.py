"""
Higher-Order Functions - Examples

Demonstrates passing functions as arguments and returning functions.
Run with:
    python examples.py
"""

# =============================================================================
# FUNCTIONS AS ARGUMENTS
# =============================================================================

def apply_twice(func, value):
    """Apply a function twice to a value."""
    return func(func(value))


def double(x):
    return x * 2


def demo_apply_twice():
    print("=" * 60)
    print("FUNCTIONS AS ARGUMENTS")
    print("=" * 60)
    result = apply_twice(double, 3)
    print(f"apply_twice(double, 3) = {result}")


# =============================================================================
# FUNCTIONS RETURNING FUNCTIONS
# =============================================================================

def make_multiplier(factor):
    """Return a new function that multiplies by factor."""
    def multiply(x):
        return x * factor
    return multiply


def demo_make_multiplier():
    print("\n" + "=" * 60)
    print("FUNCTIONS RETURNING FUNCTIONS")
    print("=" * 60)
    times3 = make_multiplier(3)
    times5 = make_multiplier(5)
    print(f"times3(4) = {times3(4)}")
    print(f"times5(4) = {times5(4)}")


# =============================================================================
# FUNCTION COMPOSITION
# =============================================================================

def compose(f, g):
    """Return a function that applies f(g(x))."""
    return lambda x: f(g(x))


def add1(x):
    return x + 1


def square(x):
    return x * x


def demo_composition():
    print("\n" + "=" * 60)
    print("FUNCTION COMPOSITION")
    print("=" * 60)
    add1_then_square = compose(square, add1)
    print(f"add1_then_square(3) = {add1_then_square(3)}")


if __name__ == "__main__":
    demo_apply_twice()
    demo_make_multiplier()
    demo_composition()
    print("\n✓ Examples complete!")
