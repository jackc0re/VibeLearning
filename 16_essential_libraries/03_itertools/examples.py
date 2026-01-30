"""
Itertools Module - Examples
===========================
Efficient iteration with itertools.
"""

print("=" * 60)
print("ITERTOOLS MODULE - Examples")
print("=" * 60)

import itertools

# =============================================================================
# INFINITE ITERATORS
# =============================================================================
print("\n--- Infinite Iterators ---\n")

# count() - Counting with step
print("count(10, 2) - first 5:")
for i in itertools.islice(itertools.count(10, 2), 5):
    print(f"  {i}")

# cycle() - Repeating sequence
colors = itertools.cycle(['red', 'green', 'blue'])
print("\ncycle(['red', 'green', 'blue']) - first 7:")
for _ in range(7):
    print(f"  {next(colors)}")

# repeat() - Repeat value
print("\nrepeat('X', 5):")
print(f"  {list(itertools.repeat('X', 5))}")

# =============================================================================
# COMBINATORIC ITERATORS
# =============================================================================
print("\n--- Combinatoric Iterators ---\n")

items = ['A', 'B', 'C']

# permutations - all orderings
print(f"permutations({items}, 2):")
for p in itertools.permutations(items, 2):
    print(f"  {p}")

# combinations - order doesn't matter
print(f"\ncombinations({items}, 2):")
for c in itertools.combinations(items, 2):
    print(f"  {c}")

# combinations_with_replacement - can pick same item twice
print(f"\ncombinations_with_replacement({items}, 2):")
for c in itertools.combinations_with_replacement(items, 2):
    print(f"  {c}")

# product - cartesian product
print(f"\nproduct([1, 2], ['a', 'b']):")
for p in itertools.product([1, 2], ['a', 'b']):
    print(f"  {p}")

# =============================================================================
# COMBINING ITERATORS
# =============================================================================
print("\n--- Combining Iterators ---\n")

# chain - concatenate
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
print(f"chain({list1}, {list2}, {list3}):")
print(f"  {list(itertools.chain(list1, list2, list3))}")

# chain.from_iterable - flatten
nested = [[1, 2], [3, 4], [5, 6]]
print(f"\nchain.from_iterable({nested}):")
print(f"  {list(itertools.chain.from_iterable(nested))}")

# zip_longest - zip with fill value
names = ['Alice', 'Bob', 'Carol']
scores = [95, 87]
print(f"\nzip_longest({names}, {scores}, fillvalue='N/A'):")
print(f"  {list(itertools.zip_longest(names, scores, fillvalue='N/A'))}")

# =============================================================================
# FILTERING AND SLICING
# =============================================================================
print("\n--- Filtering and Slicing ---\n")

# islice - slice an iterator
numbers = range(100)
print(f"islice(range(100), 5, 15, 2):")
print(f"  {list(itertools.islice(numbers, 5, 15, 2))}")

# compress - filter with selectors
data = ['a', 'b', 'c', 'd', 'e', 'f']
selectors = [1, 0, 1, 0, 1, 0]
print(f"\ncompress({data}, {selectors}):")
print(f"  {list(itertools.compress(data, selectors))}")

# takewhile - take while condition holds
data = [1, 2, 3, 4, 5, 1, 2, 3]
print(f"\ntakewhile(x < 4, {data}):")
print(f"  {list(itertools.takewhile(lambda x: x < 4, data))}")

# dropwhile - drop while condition holds
print(f"\ndropwhile(x < 4, {data}):")
print(f"  {list(itertools.dropwhile(lambda x: x < 4, data))}")

# filterfalse - opposite of filter
data = [1, 2, 3, 4, 5, 6]
print(f"\nfilterfalse(x % 2 == 0, {data}):")
print(f"  {list(itertools.filterfalse(lambda x: x % 2 == 0, data))}")

# =============================================================================
# GROUPING
# =============================================================================
print("\n--- Grouping ---\n")

# groupby - group consecutive equal elements
data = ['A', 'A', 'B', 'B', 'B', 'A', 'C', 'C']
print(f"groupby({data}):")
for key, group in itertools.groupby(data):
    print(f"  {key}: {list(group)}")

# groupby with key function
people = [
    ('Alice', 'Engineering'),
    ('Bob', 'Engineering'),
    ('Carol', 'Sales'),
    ('David', 'Sales'),
    ('Eve', 'Engineering'),
]
# Must sort first!
people.sort(key=lambda x: x[1])
print(f"\ngroupby people by department:")
for dept, group in itertools.groupby(people, key=lambda x: x[1]):
    names = [name for name, _ in group]
    print(f"  {dept}: {names}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================
print("\n--- Practical Examples ---\n")

# Example 1: Flatten a deeply nested list
def flatten(nested):
    """Flatten arbitrarily nested lists."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3], [[4, 5], 6], [[[7]]]]
print(f"Flatten {nested}:")
print(f"  {list(flatten(nested))}")

# Example 2: Sliding window
def sliding_window(iterable, n):
    """Generate sliding windows of size n."""
    iterators = itertools.tee(iterable, n)
    for i, it in enumerate(iterators):
        for _ in range(i):
            next(it, None)
    return zip(*iterators)

data = [1, 2, 3, 4, 5, 6]
print(f"\nSliding window (size 3) of {data}:")
for window in sliding_window(data, 3):
    print(f"  {window}")

# Example 3: Round-robin tournament pairings
def round_robin(players):
    """Generate all unique pairings for a round-robin tournament."""
    return list(itertools.combinations(players, 2))

players = ['Alice', 'Bob', 'Carol', 'David']
pairings = round_robin(players)
print(f"\nRound-robin pairings for {players}:")
for i, (p1, p2) in enumerate(pairings, 1):
    print(f"  Match {i}: {p1} vs {p2}")

# Example 4: Chunking an iterator
def chunks(iterable, n):
    """Split iterable into chunks of size n."""
    iterator = iter(iterable)
    while True:
        chunk = list(itertools.islice(iterator, n))
        if not chunk:
            return
        yield chunk

data = range(10)
print(f"\nChunks of size 3 from range(10):")
for chunk in chunks(data, 3):
    print(f"  {chunk}")

# Example 5: Unique consecutive elements
def unique_consecutive(iterable):
    """Return unique consecutive elements."""
    return (key for key, _ in itertools.groupby(iterable))

data = [1, 1, 2, 2, 2, 3, 3, 1, 1]
print(f"\nUnique consecutive from {data}:")
print(f"  {list(unique_consecutive(data))}")

# Example 6: Cartesian product for configuration
colors = ['red', 'green', 'blue']
sizes = ['small', 'medium', 'large']
styles = ['round', 'square']

print(f"\nAll product configurations:")
configurations = list(itertools.product(colors, sizes, styles))
for i, config in enumerate(configurations, 1):
    print(f"  {i}: {' '.join(config)}")

print("\n" + "=" * 60)
print("Examples complete! Try exercises.py next.")
print("=" * 60)
