"""
Generators and Iterators - Examples

Shows how iteration works under the hood and how generators
produce values lazily, one at a time.
Run with:
    python examples.py
"""

import sys
from itertools import islice


# =============================================================================
# CLASS-BASED ITERATOR (THE PRE-GENERATOR WAY)
# =============================================================================

class Countdown:
    """Iterator that counts down from start to 1 using the full protocol."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# =============================================================================
# GENERATOR FUNCTION WITH A TRACE (SEE YIELD PAUSE AND RESUME)
# =============================================================================

def traced_counter(limit):
    """Print before and after each yield to show pause/resume interleaving."""
    for value in range(1, limit + 1):
        print(f"    [gen] about to yield {value}")
        yield value
        print(f"    [gen] resumed after yielding {value}")
    print("    [gen] function finished -> StopIteration next")


# =============================================================================
# GENERATOR DELEGATION WITH YIELD FROM
# =============================================================================

def flatten_once(nested):
    """Yield the items of each sub-list, one level deep."""
    for sublist in nested:
        yield from sublist


# =============================================================================
# INFINITE GENERATOR (CONSUMERS MUST BOUND IT)
# =============================================================================

def fibonacci():
    """Yield Fibonacci numbers forever: 0, 1, 1, 2, 3, 5, 8, ..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# =============================================================================
# LAZY PIPELINE STAGES
# =============================================================================

def evens(numbers):
    """Pass through only the even numbers."""
    for n in numbers:
        if n % 2 == 0:
            yield n


def doubled(numbers):
    """Pass through every number, times two."""
    for n in numbers:
        yield n * 2


if __name__ == "__main__":
    print("=" * 60)
    print("GENERATORS AND ITERATORS EXAMPLES")
    print("=" * 60)

    # ---------------------------------------------------------------------
    print("\n--- What for really does: iter() + next() + StopIteration ---\n")

    numbers = [10, 20, 30]
    for n in numbers:
        print(f"    loop got {n}")

    print("    ...is the same as...")
    iterator = iter(numbers)
    while True:
        try:
            n = next(iterator)
            print(f"    next() returned {n}")
        except StopIteration:
            print("    next() raised StopIteration -> loop ends")
            break

    # ---------------------------------------------------------------------
    print("\n--- Driving an iterator by hand, with a default ---\n")

    it = iter(["a", "b"])
    print(f"    next(it) -> {next(it)}")
    print(f"    next(it) -> {next(it)}")
    print(f"    next(it, 'empty') -> {next(it, 'empty')}")
    print(f"    next(it, 'empty') -> {next(it, 'empty')}")

    # ---------------------------------------------------------------------
    print("\n--- Class-based iterator: Countdown ---\n")

    print(f"    list(Countdown(3)) -> {list(Countdown(3))}")
    for n in Countdown(2):
        print(f"    for got {n}")

    # ---------------------------------------------------------------------
    print("\n--- yield pauses and resumes the function ---\n")

    gen = traced_counter(2)
    print("    [main] generator created - body has NOT run yet")
    print(f"    [main] next() -> {next(gen)}")
    print(f"    [main] next() -> {next(gen)}")
    try:
        next(gen)
    except StopIteration:
        print("    [main] StopIteration - the generator is done")

    # ---------------------------------------------------------------------
    print("\n--- Generator expressions vs list comprehensions ---\n")

    squares_list = [x * x for x in range(5)]
    squares_gen = (x * x for x in range(5))
    print(f"    list comprehension -> {squares_list}")
    print(f"    genexp type        -> {type(squares_gen).__name__}")
    print(f"    sum(squares_gen)   -> {sum(squares_gen)}")
    print(f"    max(x * x for x in range(10)) -> {max(x * x for x in range(10))}")

    # ---------------------------------------------------------------------
    print("\n--- A generator is one-shot: the second pass is empty ---\n")

    gen = (x * x for x in range(4))
    print(f"    first sum(gen)  -> {sum(gen)}")
    print(f"    second sum(gen) -> {sum(gen)}  (already exhausted)")
    print(f"    list(gen) after -> {list(gen)}")

    # ---------------------------------------------------------------------
    print("\n--- yield from delegates to another iterable ---\n")

    nested = [[1, 2], [3], [4, 5]]
    print(f"    nested            -> {nested}")
    print(f"    flatten_once(...) -> {list(flatten_once(nested))}")

    # ---------------------------------------------------------------------
    print("\n--- Infinite generators need a bounded consumer ---\n")

    gen = fibonacci()
    first_six = []
    for _ in range(6):
        first_six.append(next(gen))
    print(f"    manual counter   -> {first_six}")
    print(f"    islice(gen, 8)   -> {list(islice(fibonacci(), 8))}")

    # ---------------------------------------------------------------------
    print("\n--- Lazy pipeline: stages feed each other one value at a time ---\n")

    pipeline = doubled(evens(range(10)))
    print(f"    doubled(evens(range(10))) -> {list(pipeline)}")

    n = 1_000_000
    as_list = [x * 2 for x in range(n)]
    as_gen = (x * 2 for x in range(n))
    list_bytes = sys.getsizeof(as_list)
    gen_bytes = sys.getsizeof(as_gen)
    print(f"    sys.getsizeof(list of {n:,}) -> {list_bytes:,} bytes")
    print(f"    sys.getsizeof(genexp)        -> {gen_bytes:,} bytes")
    print(f"    the list costs about {list_bytes // max(gen_bytes, 1)}x more memory")

    print("\n" + "=" * 60)
    print("Examples complete! Try exercises.py next.")
    print("=" * 60)
