"""
Lambda Expressions - Examples

Demonstrates common lambda use cases.
Run with:
    python examples.py
"""

# =============================================================================
# BASIC LAMBDAS
# =============================================================================

def demo_basic_lambdas():
    print("=" * 60)
    print("BASIC LAMBDAS")
    print("=" * 60)

    square = lambda x: x * x
    add = lambda a, b: a + b

    print(f"square(5) = {square(5)}")
    print(f"add(2, 3) = {add(2, 3)}")


# =============================================================================
# LAMBDAS WITH SORT
# =============================================================================

def demo_sorting():
    print("\n" + "=" * 60)
    print("LAMBDAS WITH SORT")
    print("=" * 60)

    names = ["alice", "Bob", "charlie", "Diana"]
    sorted_names = sorted(names, key=lambda n: n.lower())
    print(f"Original: {names}")
    print(f"Sorted  : {sorted_names}")


# =============================================================================
# LAMBDAS WITH FILTER/MAP
# =============================================================================

def demo_filter_map():
    print("\n" + "=" * 60)
    print("LAMBDAS WITH FILTER/MAP")
    print("=" * 60)

    nums = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, nums))
    squares = list(map(lambda x: x * x, nums))
    print(f"Nums   : {nums}")
    print(f"Evens  : {evens}")
    print(f"Squares: {squares}")


if __name__ == "__main__":
    demo_basic_lambdas()
    demo_sorting()
    demo_filter_map()
    print("\n✓ Examples complete!")
