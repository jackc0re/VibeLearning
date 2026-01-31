"""
Recursion - Exercises

Practice implementing recursive algorithms.
Complete each exercise by filling in the function body.

Run tests with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Factorial
# =============================================================================

def exercise_1_factorial(n):
    """
    Calculate n! (n factorial) recursively.
    
    n! = n × (n-1) × (n-2) × ... × 2 × 1
    0! = 1 (by definition)
    
    Args:
        n: Non-negative integer
        
    Returns:
        int: n factorial
        
    Example:
        >>> exercise_1_factorial(5)
        120
        >>> exercise_1_factorial(0)
        1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Sum of Digits
# =============================================================================

def exercise_2_sum_digits(n):
    """
    Calculate the sum of digits of a non-negative integer recursively.
    
    Args:
        n: Non-negative integer
        
    Returns:
        int: Sum of all digits
        
    Example:
        >>> exercise_2_sum_digits(12345)
        15  # 1 + 2 + 3 + 4 + 5
        >>> exercise_2_sum_digits(7)
        7
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Power Function
# =============================================================================

def exercise_3_power(base, exp):
    """
    Calculate base^exp recursively.
    Handle positive, negative, and zero exponents.
    
    Args:
        base: The base number
        exp: The exponent (can be negative, zero, or positive)
        
    Returns:
        float: base raised to the power of exp
        
    Example:
        >>> exercise_3_power(2, 10)
        1024
        >>> exercise_3_power(3, 0)
        1
        >>> exercise_3_power(2, -2)
        0.25
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Reverse String
# =============================================================================

def exercise_4_reverse_string(s):
    """
    Reverse a string recursively.
    
    Args:
        s: Input string
        
    Returns:
        str: Reversed string
        
    Example:
        >>> exercise_4_reverse_string("hello")
        "olleh"
        >>> exercise_4_reverse_string("a")
        "a"
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Fibonacci
# =============================================================================

def exercise_5_fibonacci(n):
    """
    Calculate the nth Fibonacci number recursively.
    
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1
    
    Args:
        n: Non-negative integer
        
    Returns:
        int: The nth Fibonacci number
        
    Example:
        >>> exercise_5_fibonacci(0)
        0
        >>> exercise_5_fibonacci(1)
        1
        >>> exercise_5_fibonacci(10)
        55
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 6: Sum of List
# =============================================================================

def exercise_6_sum_list(arr):
    """
    Calculate the sum of all elements in a list recursively.
    
    Args:
        arr: List of numbers
        
    Returns:
        int/float: Sum of all elements
        
    Example:
        >>> exercise_6_sum_list([1, 2, 3, 4, 5])
        15
        >>> exercise_6_sum_list([])
        0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 7: Count Occurrences
# =============================================================================

def exercise_7_count(arr, target):
    """
    Count occurrences of target in list recursively.
    
    Args:
        arr: List of elements
        target: Element to count
        
    Returns:
        int: Number of times target appears
        
    Example:
        >>> exercise_7_count([1, 2, 1, 3, 1, 4], 1)
        3
        >>> exercise_7_count([1, 2, 3], 5)
        0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 8: Is Palindrome
# =============================================================================

def exercise_8_is_palindrome(s):
    """
    Check if a string is a palindrome recursively.
    Ignore case and spaces.
    
    Args:
        s: Input string
        
    Returns:
        bool: True if palindrome, False otherwise
        
    Example:
        >>> exercise_8_is_palindrome("radar")
        True
        >>> exercise_8_is_palindrome("hello")
        False
        >>> exercise_8_is_palindrome("A man a plan a canal Panama")
        True
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 9: Binary Search (Recursive)
# =============================================================================

def exercise_9_binary_search(arr, target, left=None, right=None):
    """
    Implement binary search recursively.
    
    Args:
        arr: Sorted list of elements
        target: Element to find
        left: Left boundary (default: 0)
        right: Right boundary (default: len(arr) - 1)
        
    Returns:
        int: Index of target, or -1 if not found
        
    Example:
        >>> exercise_9_binary_search([1, 2, 3, 4, 5, 6, 7], 5)
        4
        >>> exercise_9_binary_search([1, 2, 3, 4, 5], 10)
        -1
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 10: GCD (Greatest Common Divisor)
# =============================================================================

def exercise_10_gcd(a, b):
    """
    Calculate GCD using Euclidean algorithm recursively.
    
    GCD(a, b) = GCD(b, a mod b)
    GCD(a, 0) = a
    
    Args:
        a: First positive integer
        b: Second positive integer
        
    Returns:
        int: Greatest common divisor
        
    Example:
        >>> exercise_10_gcd(48, 18)
        6
        >>> exercise_10_gcd(17, 13)
        1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 11: Flatten Nested List
# =============================================================================

def exercise_11_flatten(nested_list):
    """
    Flatten a nested list into a single list recursively.
    
    Args:
        nested_list: List that may contain other lists
        
    Returns:
        list: Flattened list
        
    Example:
        >>> exercise_11_flatten([1, [2, 3, [4, 5]], 6])
        [1, 2, 3, 4, 5, 6]
        >>> exercise_11_flatten([[1, 2], [3, [4, [5]]]])
        [1, 2, 3, 4, 5]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 12: Generate Permutations
# =============================================================================

def exercise_12_permutations(arr):
    """
    Generate all permutations of a list recursively.
    
    Args:
        arr: List of elements
        
    Returns:
        list: List of all permutations
        
    Example:
        >>> sorted(exercise_12_permutations([1, 2, 3]))
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# BONUS: Tower of Hanoi
# =============================================================================

def bonus_hanoi(n, source, auxiliary, target):
    """
    BONUS: Solve Tower of Hanoi puzzle.
    
    Return list of moves to transfer n disks from source to target.
    
    Args:
        n: Number of disks
        source: Source peg name
        auxiliary: Auxiliary peg name
        target: Target peg name
        
    Returns:
        list: List of move descriptions
        
    Example:
        >>> bonus_hanoi(2, 'A', 'B', 'C')
        ['Move disk 1 from A to B', 'Move disk 2 from A to C', 'Move disk 1 from B to C']
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests():
    """Run all test cases."""
    print("Running Recursion Exercises Tests")
    print("=" * 50)
    
    all_passed = True
    
    # Test Exercise 1: Factorial
    print("\nExercise 1: Factorial")
    tests_1 = [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
    ]
    for n, expected in tests_1:
        result = exercise_1_factorial(n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} factorial({n}) = {result} (expected {expected})")
    
    # Test Exercise 2: Sum of Digits
    print("\nExercise 2: Sum of Digits")
    tests_2 = [
        (12345, 15),
        (7, 7),
        (0, 0),
        (999, 27),
    ]
    for n, expected in tests_2:
        result = exercise_2_sum_digits(n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} sum_digits({n}) = {result} (expected {expected})")
    
    # Test Exercise 3: Power
    print("\nExercise 3: Power")
    tests_3 = [
        (2, 10, 1024),
        (3, 0, 1),
        (5, 3, 125),
        (2, -2, 0.25),
    ]
    for base, exp, expected in tests_3:
        result = exercise_3_power(base, exp)
        status = "✓" if abs(result - expected) < 0.0001 else "✗"
        if abs(result - expected) >= 0.0001:
            all_passed = False
        print(f"  {status} power({base}, {exp}) = {result} (expected {expected})")
    
    # Test Exercise 4: Reverse String
    print("\nExercise 4: Reverse String")
    tests_4 = [
        ("hello", "olleh"),
        ("a", "a"),
        ("", ""),
        ("python", "nohtyp"),
    ]
    for s, expected in tests_4:
        result = exercise_4_reverse_string(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} reverse('{s}') = '{result}' (expected '{expected}')")
    
    # Test Exercise 5: Fibonacci
    print("\nExercise 5: Fibonacci")
    tests_5 = [
        (0, 0),
        (1, 1),
        (2, 1),
        (10, 55),
        (15, 610),
    ]
    for n, expected in tests_5:
        result = exercise_5_fibonacci(n)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} fibonacci({n}) = {result} (expected {expected})")
    
    # Test Exercise 6: Sum of List
    print("\nExercise 6: Sum of List")
    tests_6 = [
        ([1, 2, 3, 4, 5], 15),
        ([], 0),
        ([10], 10),
        ([-1, 1, -1, 1], 0),
    ]
    for arr, expected in tests_6:
        result = exercise_6_sum_list(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} sum_list({arr}) = {result} (expected {expected})")
    
    # Test Exercise 7: Count Occurrences
    print("\nExercise 7: Count Occurrences")
    tests_7 = [
        ([1, 2, 1, 3, 1, 4], 1, 3),
        ([1, 2, 3], 5, 0),
        ([5, 5, 5, 5], 5, 4),
        ([], 1, 0),
    ]
    for arr, target, expected in tests_7:
        result = exercise_7_count(arr, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} count({arr}, {target}) = {result} (expected {expected})")
    
    # Test Exercise 8: Is Palindrome
    print("\nExercise 8: Is Palindrome")
    tests_8 = [
        ("radar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("", True),
        ("a", True),
    ]
    for s, expected in tests_8:
        result = exercise_8_is_palindrome(s)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} is_palindrome('{s}') = {result} (expected {expected})")
    
    # Test Exercise 9: Binary Search
    print("\nExercise 9: Binary Search")
    tests_9 = [
        ([1, 2, 3, 4, 5, 6, 7], 5, 4),
        ([1, 2, 3, 4, 5], 10, -1),
        ([1], 1, 0),
        ([1, 3, 5, 7, 9], 3, 1),
    ]
    for arr, target, expected in tests_9:
        result = exercise_9_binary_search(arr, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} binary_search({arr}, {target}) = {result} (expected {expected})")
    
    # Test Exercise 10: GCD
    print("\nExercise 10: GCD")
    tests_10 = [
        (48, 18, 6),
        (17, 13, 1),
        (100, 25, 25),
        (12, 12, 12),
    ]
    for a, b, expected in tests_10:
        result = exercise_10_gcd(a, b)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} gcd({a}, {b}) = {result} (expected {expected})")
    
    # Test Exercise 11: Flatten
    print("\nExercise 11: Flatten Nested List")
    tests_11 = [
        ([1, [2, 3, [4, 5]], 6], [1, 2, 3, 4, 5, 6]),
        ([[1, 2], [3, [4, [5]]]], [1, 2, 3, 4, 5]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
    ]
    for nested, expected in tests_11:
        result = exercise_11_flatten(nested)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} flatten({nested}) = {result}")
    
    # Test Exercise 12: Permutations
    print("\nExercise 12: Permutations")
    result_12 = exercise_12_permutations([1, 2, 3])
    expected_12 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
    # Sort both for comparison
    if result_12:
        result_sorted = sorted([tuple(p) for p in result_12])
        expected_sorted = sorted([tuple(p) for p in expected_12])
        is_correct = result_sorted == expected_sorted
    else:
        is_correct = False
    
    status = "✓" if is_correct else "✗"
    if not is_correct:
        all_passed = False
    print(f"  {status} permutations([1,2,3]) has {len(result_12) if result_12 else 0} results (expected 6)")
    
    # Test Bonus: Hanoi
    print("\nBonus: Tower of Hanoi")
    result_bonus = bonus_hanoi(2, 'A', 'B', 'C')
    expected_bonus = ['Move disk 1 from A to B', 'Move disk 2 from A to C', 'Move disk 1 from B to C']
    status = "✓" if result_bonus == expected_bonus else "✗"
    if result_bonus != expected_bonus:
        all_passed = False
    print(f"  {status} hanoi(2, 'A', 'B', 'C') = {result_bonus}")
    
    # Summary
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All tests passed! Great job!")
    else:
        print("❌ Some tests failed. Keep practicing!")
    print("=" * 50)


# =============================================================================
# SOLUTIONS (Hidden - Try to solve on your own first!)
# =============================================================================

"""
SOLUTIONS - Scroll down only after attempting the exercises!

.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.

# Exercise 1: Factorial
def exercise_1_factorial(n):
    if n <= 1:
        return 1
    return n * exercise_1_factorial(n - 1)

# Exercise 2: Sum of Digits
def exercise_2_sum_digits(n):
    if n < 10:
        return n
    return n % 10 + exercise_2_sum_digits(n // 10)

# Exercise 3: Power
def exercise_3_power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / exercise_3_power(base, -exp)
    return base * exercise_3_power(base, exp - 1)

# Exercise 4: Reverse String
def exercise_4_reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + exercise_4_reverse_string(s[:-1])

# Exercise 5: Fibonacci
def exercise_5_fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return exercise_5_fibonacci(n - 1) + exercise_5_fibonacci(n - 2)

# Exercise 6: Sum of List
def exercise_6_sum_list(arr):
    if not arr:
        return 0
    return arr[0] + exercise_6_sum_list(arr[1:])

# Exercise 7: Count Occurrences
def exercise_7_count(arr, target):
    if not arr:
        return 0
    return (1 if arr[0] == target else 0) + exercise_7_count(arr[1:], target)

# Exercise 8: Is Palindrome
def exercise_8_is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return exercise_8_is_palindrome(s[1:-1])

# Exercise 9: Binary Search
def exercise_9_binary_search(arr, target, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return exercise_9_binary_search(arr, target, mid + 1, right)
    else:
        return exercise_9_binary_search(arr, target, left, mid - 1)

# Exercise 10: GCD
def exercise_10_gcd(a, b):
    if b == 0:
        return a
    return exercise_10_gcd(b, a % b)

# Exercise 11: Flatten
def exercise_11_flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(exercise_11_flatten(item))
        else:
            result.append(item)
    return result

# Exercise 12: Permutations
def exercise_12_permutations(arr):
    if len(arr) <= 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for perm in exercise_12_permutations(remaining):
            result.append([current] + perm)
    return result

# Bonus: Hanoi
def bonus_hanoi(n, source, auxiliary, target):
    if n == 1:
        return [f'Move disk 1 from {source} to {target}']
    moves = []
    moves.extend(bonus_hanoi(n - 1, source, target, auxiliary))
    moves.append(f'Move disk {n} from {source} to {target}')
    moves.extend(bonus_hanoi(n - 1, auxiliary, source, target))
    return moves
"""


if __name__ == "__main__":
    run_tests()
