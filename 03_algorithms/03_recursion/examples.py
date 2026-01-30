"""
Recursion - Examples

This file demonstrates recursive algorithms with
clear explanations and visualizations.

Run this file to see the examples in action:
    python examples.py
"""

from functools import lru_cache


# =============================================================================
# BASIC RECURSION EXAMPLES
# =============================================================================

def factorial(n):
    """
    Calculate n! (n factorial) recursively.
    
    n! = n × (n-1) × (n-2) × ... × 2 × 1
    0! = 1 (by definition)
    
    Time Complexity: O(n)
    Space Complexity: O(n) due to call stack
    """
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)


def factorial_visualized(n, depth=0):
    """Factorial with visualization of recursive calls."""
    indent = "  " * depth
    print(f"{indent}factorial({n})")
    
    if n <= 1:
        print(f"{indent}  → Base case: return 1")
        return 1
    
    result = n * factorial_visualized(n - 1, depth + 1)
    print(f"{indent}  → return {n} * {result // n} = {result}")
    return result


def countdown(n):
    """Simple countdown to demonstrate recursion flow."""
    if n <= 0:
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)


def sum_to_n(n):
    """Calculate 1 + 2 + 3 + ... + n recursively."""
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)


# =============================================================================
# FIBONACCI EXAMPLES
# =============================================================================

def fibonacci_naive(n):
    """
    Calculate nth Fibonacci number (naive recursive approach).
    
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2)
    
    Time Complexity: O(2^n) - Very slow!
    Space Complexity: O(n)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    """
    Fibonacci with memoization (cached results).
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


def fibonacci_visualized(n, depth=0, memo=None):
    """Fibonacci with visualization of call tree."""
    if memo is None:
        memo = {}
    
    indent = "  " * depth
    print(f"{indent}fib({n})")
    
    if n in memo:
        print(f"{indent}  → cached: {memo[n]}")
        return memo[n]
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    result = (fibonacci_visualized(n - 1, depth + 1, memo) + 
              fibonacci_visualized(n - 2, depth + 1, memo))
    memo[n] = result
    print(f"{indent}  → return {result}")
    return result


# =============================================================================
# LIST OPERATIONS
# =============================================================================

def sum_list(arr):
    """Sum all elements in a list recursively."""
    if not arr:
        return 0
    return arr[0] + sum_list(arr[1:])


def find_max(arr):
    """Find maximum element in a list recursively."""
    if len(arr) == 1:
        return arr[0]
    
    max_of_rest = find_max(arr[1:])
    return arr[0] if arr[0] > max_of_rest else max_of_rest


def find_element(arr, target):
    """Check if target exists in list (recursive linear search)."""
    if not arr:
        return False
    if arr[0] == target:
        return True
    return find_element(arr[1:], target)


def count_occurrences(arr, target):
    """Count how many times target appears in list."""
    if not arr:
        return 0
    count_in_rest = count_occurrences(arr[1:], target)
    return (1 if arr[0] == target else 0) + count_in_rest


def flatten_list(nested_list):
    """Flatten a nested list into a single list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


# =============================================================================
# STRING OPERATIONS
# =============================================================================

def reverse_string(s):
    """Reverse a string recursively."""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


def is_palindrome(s):
    """Check if string is a palindrome recursively."""
    # Remove spaces and convert to lowercase for comparison
    s = s.lower().replace(" ", "")
    
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])


def count_char(s, char):
    """Count occurrences of a character in string."""
    if not s:
        return 0
    return (1 if s[0] == char else 0) + count_char(s[1:], char)


# =============================================================================
# MATHEMATICAL OPERATIONS
# =============================================================================

def power(base, exp):
    """Calculate base^exp recursively."""
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)


def power_fast(base, exp):
    """
    Fast exponentiation using O(log n) calls.
    
    Uses: x^n = (x^(n/2))^2 for even n
          x^n = x * (x^(n/2))^2 for odd n
    """
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power_fast(base, -exp)
    
    if exp % 2 == 0:
        half = power_fast(base, exp // 2)
        return half * half
    else:
        half = power_fast(base, (exp - 1) // 2)
        return base * half * half


def gcd(a, b):
    """
    Greatest Common Divisor using Euclidean algorithm.
    
    GCD(a, b) = GCD(b, a mod b)
    GCD(a, 0) = a
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_visualized(a, b, depth=0):
    """GCD with visualization of steps."""
    indent = "  " * depth
    print(f"{indent}gcd({a}, {b})")
    
    if b == 0:
        print(f"{indent}  → Base case: return {a}")
        return a
    
    result = gcd_visualized(b, a % b, depth + 1)
    print(f"{indent}  → return {result}")
    return result


# =============================================================================
# TREE AND NESTED STRUCTURE OPERATIONS
# =============================================================================

def sum_nested(data):
    """
    Sum all numbers in a nested structure.
    Works with arbitrary nesting of lists.
    """
    total = 0
    for item in data:
        if isinstance(item, (int, float)):
            total += item
        elif isinstance(item, list):
            total += sum_nested(item)
    return total


def deep_copy(obj):
    """Create a deep copy of nested lists/dicts."""
    if isinstance(obj, dict):
        return {k: deep_copy(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [deep_copy(item) for item in obj]
    else:
        return obj


def count_depth(nested_list, current_depth=1):
    """Find the maximum nesting depth of a list."""
    if not isinstance(nested_list, list) or not nested_list:
        return current_depth
    
    max_depth = current_depth
    for item in nested_list:
        if isinstance(item, list):
            depth = count_depth(item, current_depth + 1)
            max_depth = max(max_depth, depth)
    
    return max_depth


# =============================================================================
# BINARY SEARCH (RECURSIVE)
# =============================================================================

def binary_search_recursive(arr, target, left=0, right=None):
    """Binary search implemented recursively."""
    if right is None:
        right = len(arr) - 1
    
    # Base case: not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Base case: found
    if arr[mid] == target:
        return mid
    
    # Recursive case
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# =============================================================================
# BACKTRACKING EXAMPLES
# =============================================================================

def generate_binary_strings(n, current=""):
    """Generate all binary strings of length n."""
    # Base case
    if len(current) == n:
        return [current]
    
    # Recursive case: try both 0 and 1
    return (generate_binary_strings(n, current + "0") +
            generate_binary_strings(n, current + "1"))


def generate_permutations(arr):
    """Generate all permutations of a list."""
    # Base case
    if len(arr) <= 1:
        return [arr]
    
    permutations = []
    for i in range(len(arr)):
        # Pick element at index i
        current = arr[i]
        # Get remaining elements
        remaining = arr[:i] + arr[i+1:]
        # Recursively get permutations of remaining
        for perm in generate_permutations(remaining):
            permutations.append([current] + perm)
    
    return permutations


def generate_subsets(arr):
    """Generate all subsets (power set) of a list."""
    # Base case
    if not arr:
        return [[]]
    
    # Get subsets without first element
    subsets_without = generate_subsets(arr[1:])
    
    # Add first element to each subset
    subsets_with = [[arr[0]] + subset for subset in subsets_without]
    
    return subsets_without + subsets_with


# =============================================================================
# TOWER OF HANOI
# =============================================================================

def hanoi(n, source, auxiliary, target, moves=None):
    """
    Solve Tower of Hanoi puzzle.
    
    Move n disks from source to target using auxiliary.
    Rules:
    1. Only one disk can be moved at a time
    2. A larger disk cannot be placed on a smaller disk
    """
    if moves is None:
        moves = []
    
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {target}")
        return moves
    
    # Move n-1 disks from source to auxiliary
    hanoi(n - 1, source, target, auxiliary, moves)
    
    # Move largest disk from source to target
    moves.append(f"Move disk {n} from {source} to {target}")
    
    # Move n-1 disks from auxiliary to target
    hanoi(n - 1, auxiliary, source, target, moves)
    
    return moves


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_basic_recursion():
    """Demonstrate basic recursive functions."""
    print("=" * 60)
    print("BASIC RECURSION EXAMPLES")
    print("=" * 60)
    
    # Countdown
    print("\n1. Countdown from 5:")
    countdown(5)
    
    # Factorial
    print("\n2. Factorial:")
    for n in [0, 1, 5, 10]:
        print(f"   {n}! = {factorial(n)}")
    
    # Factorial with visualization
    print("\n3. Factorial(4) call stack:")
    factorial_visualized(4)
    
    # Sum to N
    print("\n4. Sum from 1 to N:")
    for n in [5, 10, 100]:
        print(f"   Sum(1 to {n}) = {sum_to_n(n)}")


def demo_fibonacci():
    """Demonstrate Fibonacci implementations."""
    print("\n" + "=" * 60)
    print("FIBONACCI EXAMPLES")
    print("=" * 60)
    
    # First 10 Fibonacci numbers
    print("\n1. First 10 Fibonacci numbers:")
    fibs = [fibonacci_memoized(i) for i in range(10)]
    print(f"   {fibs}")
    
    # Visualize small Fibonacci
    print("\n2. Fibonacci(5) call tree (with memoization):")
    fibonacci_visualized(5)
    
    # Compare performance
    print("\n3. Performance comparison (computing F(30)):")
    
    import time
    
    # Memoized version
    fibonacci_memoized.cache_clear()
    start = time.perf_counter()
    result = fibonacci_memoized(30)
    memoized_time = time.perf_counter() - start
    print(f"   Memoized: F(30) = {result}, Time: {memoized_time:.6f}s")
    
    # Note: Naive version would be too slow to run
    print("   Naive: Skipped (would take ~30 seconds!)")


def demo_list_operations():
    """Demonstrate recursive list operations."""
    print("\n" + "=" * 60)
    print("LIST OPERATIONS")
    print("=" * 60)
    
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\nArray: {arr}")
    
    print(f"\n1. Sum of list: {sum_list(arr)}")
    print(f"2. Maximum element: {find_max(arr)}")
    print(f"3. Contains 5? {find_element(arr, 5)}")
    print(f"4. Count of 1s: {count_occurrences(arr, 1)}")
    
    # Flatten nested list
    nested = [1, [2, 3, [4, 5]], 6, [7, [8, [9]]]]
    print(f"\n5. Flatten nested list:")
    print(f"   Input: {nested}")
    print(f"   Output: {flatten_list(nested)}")


def demo_string_operations():
    """Demonstrate recursive string operations."""
    print("\n" + "=" * 60)
    print("STRING OPERATIONS")
    print("=" * 60)
    
    # Reverse string
    print("\n1. Reverse String:")
    for s in ["hello", "python", "recursion"]:
        print(f"   '{s}' → '{reverse_string(s)}'")
    
    # Palindrome check
    print("\n2. Palindrome Check:")
    for s in ["radar", "hello", "A man a plan a canal Panama"]:
        result = is_palindrome(s)
        print(f"   '{s}': {result}")
    
    # Count character
    print("\n3. Count Character 'a' in 'abracadabra':")
    print(f"   Count: {count_char('abracadabra', 'a')}")


def demo_math_operations():
    """Demonstrate mathematical recursive functions."""
    print("\n" + "=" * 60)
    print("MATHEMATICAL OPERATIONS")
    print("=" * 60)
    
    # Power
    print("\n1. Power function:")
    test_cases = [(2, 10), (3, 4), (5, 0), (2, -3)]
    for base, exp in test_cases:
        result = power_fast(base, exp)
        print(f"   {base}^{exp} = {result}")
    
    # GCD
    print("\n2. Greatest Common Divisor:")
    pairs = [(48, 18), (100, 35), (17, 13)]
    for a, b in pairs:
        print(f"   GCD({a}, {b}) = {gcd(a, b)}")
    
    # GCD visualization
    print("\n3. GCD(48, 18) step by step:")
    gcd_visualized(48, 18)


def demo_backtracking():
    """Demonstrate backtracking with recursion."""
    print("\n" + "=" * 60)
    print("BACKTRACKING EXAMPLES")
    print("=" * 60)
    
    # Binary strings
    print("\n1. All binary strings of length 3:")
    binary_strings = generate_binary_strings(3)
    print(f"   {binary_strings}")
    
    # Permutations
    print("\n2. All permutations of [1, 2, 3]:")
    perms = generate_permutations([1, 2, 3])
    for perm in perms:
        print(f"   {perm}")
    
    # Subsets
    print("\n3. All subsets of [1, 2, 3]:")
    subsets = generate_subsets([1, 2, 3])
    for subset in subsets:
        print(f"   {subset}")


def demo_tower_of_hanoi():
    """Demonstrate Tower of Hanoi solution."""
    print("\n" + "=" * 60)
    print("TOWER OF HANOI")
    print("=" * 60)
    
    print("\n3 disk solution:")
    print("-" * 40)
    moves = hanoi(3, 'A', 'B', 'C')
    for i, move in enumerate(moves, 1):
        print(f"   {i}. {move}")
    
    print(f"\nTotal moves: {len(moves)}")
    print("Formula: 2^n - 1 moves for n disks")


def demo_nested_structures():
    """Demonstrate operations on nested structures."""
    print("\n" + "=" * 60)
    print("NESTED STRUCTURE OPERATIONS")
    print("=" * 60)
    
    # Sum nested
    nested = [1, [2, [3, 4], 5], [6, 7], 8]
    print(f"\n1. Sum nested list:")
    print(f"   Input: {nested}")
    print(f"   Sum: {sum_nested(nested)}")
    
    # Depth
    deep_list = [1, [2, [3, [4, [5]]]]]
    print(f"\n2. Maximum depth:")
    print(f"   Input: {deep_list}")
    print(f"   Depth: {count_depth(deep_list)}")
    
    # Deep copy
    original = [[1, 2], [3, [4, 5]]]
    copied = deep_copy(original)
    copied[0][0] = 99
    print(f"\n3. Deep copy:")
    print(f"   Original: {original}")
    print(f"   Modified copy: {copied}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    demo_basic_recursion()
    demo_fibonacci()
    demo_list_operations()
    demo_string_operations()
    demo_math_operations()
    demo_backtracking()
    demo_tower_of_hanoi()
    demo_nested_structures()
    
    print("\n" + "=" * 60)
    print("✓ All recursion examples completed!")
    print("=" * 60)
