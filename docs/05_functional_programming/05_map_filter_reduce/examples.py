"""
Map, Filter, Reduce - Examples

Demonstrates map, filter, reduce and comprehensions.
Run with:
    python examples.py
"""

from functools import reduce


def demo_map():
    print("=" * 60)
    print("MAP")
    print("=" * 60)
    nums = [1, 2, 3, 4]
    squares = list(map(lambda x: x * x, nums))
    print(f"Nums   : {nums}")
    print(f"Squares: {squares}")


def demo_filter():
    print("\n" + "=" * 60)
    print("FILTER")
    print("=" * 60)
    nums = [1, 2, 3, 4, 5, 6]
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(f"Nums : {nums}")
    print(f"Evens: {evens}")


def demo_reduce():
    print("\n" + "=" * 60)
    print("REDUCE")
    print("=" * 60)
    nums = [1, 2, 3, 4]
    total = reduce(lambda acc, x: acc + x, nums, 0)
    product = reduce(lambda acc, x: acc * x, nums, 1)
    print(f"Nums   : {nums}")
    print(f"Sum    : {total}")
    print(f"Product: {product}")


def demo_comprehensions():
    print("\n" + "=" * 60)
    print("COMPREHENSIONS (ALTERNATIVE)")
    print("=" * 60)
    nums = [1, 2, 3, 4]
    squares = [x * x for x in nums]
    evens = [x for x in nums if x % 2 == 0]
    print(f"Nums   : {nums}")
    print(f"Squares: {squares}")
    print(f"Evens  : {evens}")


if __name__ == "__main__":
    demo_map()
    demo_filter()
    demo_reduce()
    demo_comprehensions()
    print("\n✓ Examples complete!")
