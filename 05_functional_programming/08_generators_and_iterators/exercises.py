"""
Generators and Iterators - Exercises

Practice iterators, generators, and lazy pipelines.
Run tests with:
    python exercises.py

Reference solutions are at the bottom of this file.
"""


# =============================================================================
# EXERCISE 1: Countdown Iterator Class
# =============================================================================

class exercise_1_countdown:
    """
    A class-based iterator that counts down from start to 1, then stops.

    Implement __iter__ (return self) and __next__ (return the current value,
    decrement it, and raise StopIteration once the value drops below 1).
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# EXERCISE 2: Fibonacci Generator
# =============================================================================

def exercise_2_fibonacci(n):
    """
    A generator that yields the first n Fibonacci numbers:
    0, 1, 1, 2, 3, 5, 8, ...
    Use `yield` and two variables that advance together.
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# EXERCISE 3: chunked(iterable, size)
# =============================================================================

def exercise_3_chunked(iterable, size):
    """
    A generator that yields lists of at most `size` items at a time.
    Example: list(chunked(range(1, 8), 3)) == [[1, 2, 3], [4, 5, 6], [7]]
    The last chunk may be shorter.
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# EXERCISE 4: Running-Max Pipeline
# =============================================================================

def exercise_4_running_max(numbers):
    """
    A generator that yields the largest value seen so far.
    Example: list(running_max([3, 1, 4, 1, 5])) == [3, 3, 4, 4, 5]
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# EXERCISE 5: Sum of Squares with a Generator Expression
# =============================================================================

def exercise_5_sum_of_squares(n):
    """
    Return 1*1 + 2*2 + ... + n*n using a generator expression inside sum().
    No lists allowed - the lazy way only.
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# EXERCISE 6: Flatten One Level with yield from
# =============================================================================

def exercise_6_flatten_once(nested):
    """
    A generator that yields every item from every sub-list, one level deep.
    Example: list(flatten_once([[1, 2], [3], [4, 5]])) == [1, 2, 3, 4, 5]
    Use `yield from`.
    """
    # YOUR CODE HERE
    # TODO: implement (a reference solution is at the bottom of this file)
    pass


# =============================================================================
# HELPERS
# =============================================================================

def safe_call(fn, *args, **kwargs):
    """Call fn; unimplemented stubs come back as None instead of a crash."""
    if not callable(fn):
        return None
    try:
        return fn(*args, **kwargs)
    except TypeError:
        return None


def drive(iterable, limit=1000):
    """Collect up to `limit` items from `iterable`; None if not iterable."""
    try:
        iterator = iter(iterable)
    except TypeError:
        return None
    collected = []
    for _ in range(limit):
        try:
            collected.append(next(iterator))
        except StopIteration:
            break
    return collected


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    print("Running Generators and Iterators Exercises Tests")
    print("=" * 50)
    all_passed = True

    # Exercise 1
    print("\nExercise 1: Countdown iterator class")
    countdown = safe_call(exercise_1_countdown, 4)
    result = drive(countdown)
    status = "PASS" if result == [4, 3, 2, 1] else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} list(Countdown(4)) = {result} (expected [4, 3, 2, 1])")

    # Exercise 2
    print("\nExercise 2: Fibonacci generator")
    fib = safe_call(exercise_2_fibonacci, 7)
    result = drive(fib)
    status = "PASS" if result == [0, 1, 1, 2, 3, 5, 8] else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} fibonacci(7) = {result} (expected [0, 1, 1, 2, 3, 5, 8])")

    # Exercise 3
    print("\nExercise 3: chunked")
    chunks = safe_call(exercise_3_chunked, range(1, 8), 3)
    result = drive(chunks)
    expected = [[1, 2, 3], [4, 5, 6], [7]]
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} chunked(range(1, 8), 3) = {result} (expected {expected})")

    # Exercise 4
    print("\nExercise 4: running_max")
    runner = safe_call(exercise_4_running_max, [3, 1, 4, 1, 5])
    result = drive(runner)
    expected = [3, 3, 4, 4, 5]
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} running_max([3, 1, 4, 1, 5]) = {result} (expected {expected})")

    # Exercise 5
    print("\nExercise 5: sum of squares via generator expression")
    result = safe_call(exercise_5_sum_of_squares, 4)
    status = "PASS" if result == 30 else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} sum_of_squares(4) = {result} (expected 30)")

    # Exercise 6
    print("\nExercise 6: flatten_once with yield from")
    flat = safe_call(exercise_6_flatten_once, [[1, 2], [3], [4, 5]])
    result = drive(flat)
    expected = [1, 2, 3, 4, 5]
    status = "PASS" if result == expected else "FAIL"
    if status == "FAIL":
        all_passed = False
    print(f"  {status} flatten_once = {result} (expected {expected})")

    print("\n" + "=" * 50)
    if all_passed:
        print(" All tests passed! Great job!")
    else:
        print("FAIL Some tests failed. Keep practicing!")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()


# =============================================================================
# SOLUTIONS (Don't peek until you've tried!)
# =============================================================================

# The FAIL lines above are expected: the stubs above are not implemented yet.
# The reference solutions below re-define the same exercise functions, and the
# same tests run again at the bottom of this file - this time they PASS.


# Solution 1: Countdown Iterator Class
class exercise_1_countdown:
    """Count down from start to 1 using the full iterator protocol."""

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


# Solution 2: Fibonacci Generator
def exercise_2_fibonacci(n):
    """Yield the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Solution 3: chunked(iterable, size)
def exercise_3_chunked(iterable, size):
    """Yield lists of at most `size` items taken from `iterable`."""
    iterator = iter(iterable)
    while True:
        chunk = []
        try:
            for _ in range(size):
                chunk.append(next(iterator))
        except StopIteration:
            pass          # fewer than `size` items left - finish this chunk
        if not chunk:
            return        # nothing left at all -> stop the generator
        yield chunk


# Solution 4: Running-Max Pipeline
def exercise_4_running_max(numbers):
    """Yield the largest value seen so far."""
    current_max = None
    for value in numbers:
        if current_max is None or value > current_max:
            current_max = value
        yield current_max


# Solution 5: Sum of Squares via Generator Expression
def exercise_5_sum_of_squares(n):
    """1*1 + 2*2 + ... + n*n, computed lazily inside sum()."""
    return sum(x * x for x in range(1, n + 1))


# Solution 6: Flatten One Level with yield from
def exercise_6_flatten_once(nested):
    """Yield every item of every sub-list, one level deep."""
    for sublist in nested:
        yield from sublist


# Re-run the same checks with the reference solutions in place.
if __name__ == "__main__":
    print("\nRe-running the same tests with the reference solutions...")
    run_tests()
