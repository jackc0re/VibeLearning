"""
Intermediate Exercise 2: Functional Programming
===============================================
Practice pure functions, immutability, map/filter/reduce,
lambda expressions, and decorators.
"""

print("=" * 50)
print("EXERCISE 2: Functional Programming")
print("=" * 50)


# =============================================================================
# EXERCISE 2.1: Pure Functions
# =============================================================================
print("\n--- Exercise 2.1: Pure Functions ---")
"""
A pure function always returns the same result for the same input
and never changes anything outside itself.

Write order_total(prices, tax_rate) that:
- Takes a list of prices and a tax rate (e.g. 0.10)
- Returns the tax-inclusive total rounded to 2 decimals
- Does NOT modify the input list and does NOT print anything
"""


# Your code below:
def order_total(prices, tax_rate):
    """Return the tax-inclusive total of the prices."""
    pass


# Test (uncomment after implementing)
# print(order_total([10.0, 2.5, 7.5], 0.10))  # 22.0


# =============================================================================
# EXERCISE 2.2: Immutability
# =============================================================================
print("\n--- Exercise 2.2: Immutability ---")
"""
Functional style avoids mutating inputs. Write functions that
return NEW values and leave their arguments untouched:

- add_task(todo, task): new list with task appended
- remove_task(todo, index): new list without the item at index
- swap_pair(pair): given a tuple (a, b), return the tuple (b, a)
"""


# Your code below:
def add_task(todo, task):
    """Return a new list with task appended."""
    pass


def remove_task(todo, index):
    """Return a new list with the item at index removed."""
    pass


def swap_pair(pair):
    """Return a new tuple with the two items swapped."""
    pass


# Test (uncomment after implementing)
# todo = ["eat", "sleep"]
# todo2 = add_task(todo, "code")
# print(todo)    # unchanged: ['eat', 'sleep']
# print(todo2)   # new list:  ['eat', 'sleep', 'code']


# =============================================================================
# EXERCISE 2.3: Map, Filter, Reduce
# =============================================================================
print("\n--- Exercise 2.3: Map, Filter, Reduce ---")
"""
Work on numbers = [3, 1, 4, 1, 5, 9, 2, 6] without any for loop:

- Use map to compute the square of every number
- Use filter to keep only squares greater than 10
- Use reduce to multiply the survivors together
"""

from functools import reduce


# Your code below:
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# squares = ...
# big = ...
# product = ...


# Test (uncomment after implementing)
# print(f"squares: {squares}")
# print(f"greater than 10: {big}")
# print(f"product: {product}")


# =============================================================================
# EXERCISE 2.4: Lambda Expressions
# =============================================================================
print("\n--- Exercise 2.4: Lambda Expressions ---")
"""
Sort data using lambda keys:

- Sort players (name, score) by score, highest first
- Sort words by length, then alphabetically for ties
"""


# Your code below:
players = [("Ann", 82), ("Bo", 95), ("Cy", 78)]
words = ["fig", "apple", "pear", "date"]

# by_score = ...
# by_length = ...


# Test (uncomment after implementing)
# print(f"by score, descending: {by_score}")
# print(f"by length, then A-Z: {by_length}")


# =============================================================================
# EXERCISE 2.5: Decorators
# =============================================================================
print("\n--- Exercise 2.5: Decorators ---")
"""
Write a decorator count_calls that:
- Counts how many times the wrapped function has been called
- Prints "[call N]" before each call
- Preserves the wrapped function's name with functools.wraps
- Use it to decorate greet(name)
"""

import functools


# Your code below:
def count_calls(func):
    """Print a call counter each time the function runs."""
    pass


# Test (uncomment after implementing)
# @count_calls
# def greet(name):
#     return f"Hello, {name}!"
#
# print(greet("Ada"))
# print(greet("Grace"))


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 2.1
print("\n--- Solution 2.1 ---")


def order_total(prices, tax_rate):
    """Return the tax-inclusive total of the prices."""
    return round(sum(prices) * (1 + tax_rate), 2)


prices = [10.0, 2.5, 7.5]
snapshot = list(prices)
print(f"order_total([10.0, 2.5, 7.5], 0.10) = {order_total(prices, 0.10)}")
print(f"Input list untouched: {prices == snapshot}")

# SOLUTION 2.2
print("\n--- Solution 2.2 ---")


def add_task(todo, task):
    """Return a new list with task appended."""
    return todo + [task]


def remove_task(todo, index):
    """Return a new list with the item at index removed."""
    return todo[:index] + todo[index + 1 :]


def swap_pair(pair):
    """Return a new tuple with the two items swapped."""
    first, second = pair
    return (second, first)


todo = ["eat", "sleep"]
todo2 = add_task(todo, "code")
todo3 = remove_task(todo2, 0)
print(f"original  : {todo}")
print(f"after add : {todo2}")
print(f"after drop: {todo3}")
print(f"swap_pair((1, 2)) = {swap_pair((1, 2))}")
if todo == ["eat", "sleep"]:
    print("Original unchanged: PASS")
else:
    print("Original was mutated: FAIL")

# SOLUTION 2.3
print("\n--- Solution 2.3 ---")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
squares = list(map(lambda n: n * n, numbers))
big = list(filter(lambda s: s > 10, squares))
product = reduce(lambda acc, n: acc * n, big, 1)

print(f"squares      : {squares}")
print(f"squares > 10 : {big}")
print(f"product      : {product}")

# SOLUTION 2.4
print("\n--- Solution 2.4 ---")

players = [("Ann", 82), ("Bo", 95), ("Cy", 78)]
words = ["fig", "apple", "pear", "date"]
by_score = sorted(players, key=lambda player: player[1], reverse=True)
by_length = sorted(words, key=lambda word: (len(word), word))

print(f"by score, descending: {by_score}")
print(f"by length, then A-Z : {by_length}")

# SOLUTION 2.5
print("\n--- Solution 2.5 ---")


def count_calls(func):
    """Print a call counter each time the function runs."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"[call {wrapper.calls}]")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count_calls
def greet(name):
    return f"Hello, {name}!"


print(greet("Ada"))
print(greet("Grace"))
print(f"greet was called {greet.calls} times")
print(f"Function name preserved: {greet.__name__ == 'greet'}")

print("\n" + "=" * 50)
print("Great job! Move on to 03_algorithms.py")
print("=" * 50)
