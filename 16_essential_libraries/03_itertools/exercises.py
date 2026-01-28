"""
Itertools Module - Exercises
============================
Practice problems for itertools.
"""

print("=" * 60)
print("ITERTOOLS MODULE - Exercises")
print("=" * 60)

import itertools

# =============================================================================
# EXERCISE 1: Infinite Counter with Step
# =============================================================================
print("\n--- Exercise 1: Custom Range Generator ---\n")
"""
Write a generator function that yields numbers from start to end (inclusive)
with a given step, but use itertools.count() internally.

Example:
    custom_range(0, 10, 2) -> 0, 2, 4, 6, 8, 10
"""

def custom_range(start, end, step):
    """
    Generate numbers from start to end with given step using itertools.count.
    """
    # Your code here
    # Use itertools.count and itertools.takewhile
    pass  # TODO: Implement

# Test
# print(list(custom_range(0, 10, 2)))
# print(list(custom_range(5, 20, 5)))

# =============================================================================
# EXERCISE 2: All Pairs
# =============================================================================
print("\n--- Exercise 2: All Pairs from Two Lists ---\n")
"""
Given two lists, create all possible pairs where the first element comes
from list1 and the second from list2, but only if the elements are different.

Example:
    list1 = [1, 2]
    list2 = [2, 3]
    Result: [(1, 2), (1, 3), (2, 3)]  # (2, 2) excluded
"""

def different_pairs(list1, list2):
    """
    Create pairs from two lists where elements are different.
    """
    # Your code here
    # Use itertools.product and filter
    pass  # TODO: Implement

# Test
# print(different_pairs([1, 2], [2, 3]))
# print(different_pairs(['a', 'b'], ['a', 'c', 'd']))

# =============================================================================
# EXERCISE 3: Group By Length
# =============================================================================
print("\n--- Exercise 3: Group Words by Length ---\n")
"""
Given a list of words, group them by their length and return a dictionary
where keys are lengths and values are lists of words of that length.

Use itertools.groupby for this.

Example:
    words = ["cat", "dog", "bird", "fish", "ant"]
    Result: {3: ['cat', 'dog', 'ant'], 4: ['bird', 'fish']}
"""

def group_by_length(words):
    """
    Group words by their length using groupby.
    """
    # Your code here
    # Sort words by length first
    # Use groupby with len as key
    # Build dictionary
    pass  # TODO: Implement

# Test
# words = ["cat", "dog", "bird", "fish", "ant", "elephant", "a", "at"]
# print(group_by_length(words))

# =============================================================================
# EXERCISE 4: Alternating Iterator
# =============================================================================
print("\n--- Exercise 4: Alternating Iterator ---\n")
"""
Write a function that takes two iterables and returns an iterator that
alternates between them until both are exhausted.

Example:
    alternate([1, 2, 3], ['a', 'b', 'c', 'd', 'e'])
    Result: [1, 'a', 2, 'b', 3, 'c', 'd', 'e']
"""

def alternate(iter1, iter2):
    """
    Alternate between two iterables.
    """
    # Your code here
    # Use itertools.chain and zip_longest
    # Be careful with None values from zip_longest
    pass  # TODO: Implement

# Test
# print(list(alternate([1, 2, 3], ['a', 'b', 'c', 'd', 'e'])))
# print(list(alternate(['x'], ['y', 'z', 'w'])))

# =============================================================================
# EXERCISE 5: Running Average
# =============================================================================
print("\n--- Exercise 5: Running Average ---\n")
"""
Write a generator that yields the running average of a stream of numbers.

Example:
    Input: [10, 20, 30, 40]
    Output: [10, 15, 20, 25]  (10/1, 30/2, 60/3, 100/4)
"""

def running_average(numbers):
    """
    Yield running average of numbers.
    """
    # Your code here
    # Keep track of sum and count
    # Yield average after each number
    pass  # TODO: Implement

# Test
# print(list(running_average([10, 20, 30, 40])))
# print(list(running_average([5, 5, 10, 0])))

# =============================================================================
# EXERCISE 6: Power Set
# =============================================================================
print("\n--- Exercise 6: Power Set ---\n")
"""
Write a function that returns the power set of a given set (all possible subsets).

Use itertools.combinations to generate all subsets of all possible sizes.

Example:
    power_set([1, 2, 3])
    Result: [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
"""

def power_set(elements):
    """
    Return all subsets of the given elements (power set).
    """
    # Your code here
    # Use combinations for lengths 0 to len(elements)
    # Chain all results together
    pass  # TODO: Implement

# Test
# print(power_set([1, 2, 3]))
# print(power_set(['a', 'b']))

print("\n" + "=" * 60)
print("SOLUTIONS")
print("=" * 60)

# =============================================================================
# SOLUTION 1: Custom Range Generator
# =============================================================================
print("\n--- Solution 1: Custom Range Generator ---\n")

def custom_range_solution(start, end, step):
    counter = itertools.count(start, step)
    return itertools.takewhile(lambda x: x <= end, counter)

print(list(custom_range_solution(0, 10, 2)))
print(list(custom_range_solution(5, 20, 5)))

# =============================================================================
# SOLUTION 2: All Pairs
# =============================================================================
print("\n--- Solution 2: All Pairs ---\n")

def different_pairs_solution(list1, list2):
    pairs = itertools.product(list1, list2)
    return [(a, b) for a, b in pairs if a != b]

print(different_pairs_solution([1, 2], [2, 3]))
print(different_pairs_solution(['a', 'b'], ['a', 'c', 'd']))

# =============================================================================
# SOLUTION 3: Group By Length
# =============================================================================
print("\n--- Solution 3: Group Words by Length ---\n")

def group_by_length_solution(words):
    sorted_words = sorted(words, key=len)
    result = {}
    for length, group in itertools.groupby(sorted_words, key=len):
        result[length] = list(group)
    return result

words = ["cat", "dog", "bird", "fish", "ant", "elephant", "a", "at"]
print(group_by_length_solution(words))

# =============================================================================
# SOLUTION 4: Alternating Iterator
# =============================================================================
print("\n--- Solution 4: Alternating Iterator ---\n")

def alternate_solution(iter1, iter2):
    # Zip pairs, then flatten, filtering out None
    pairs = itertools.zip_longest(iter1, iter2)
    for a, b in pairs:
        if a is not None:
            yield a
        if b is not None:
            yield b

print(list(alternate_solution([1, 2, 3], ['a', 'b', 'c', 'd', 'e'])))
print(list(alternate_solution(['x'], ['y', 'z', 'w'])))

# =============================================================================
# SOLUTION 5: Running Average
# =============================================================================
print("\n--- Solution 5: Running Average ---\n")

def running_average_solution(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
        yield total / count

print(list(running_average_solution([10, 20, 30, 40])))
print(list(running_average_solution([5, 5, 10, 0])))

# =============================================================================
# SOLUTION 6: Power Set
# =============================================================================
print("\n--- Solution 6: Power Set ---\n")

def power_set_solution(elements):
    n = len(elements)
    all_combinations = (itertools.combinations(elements, r) for r in range(n + 1))
    return list(itertools.chain.from_iterable(all_combinations))

print(power_set_solution([1, 2, 3]))
print(power_set_solution(['a', 'b']))

print("\n" + "=" * 60)
print("Exercises complete!")
print("=" * 60)
