"""
Searching Algorithms - Exercises

Practice implementing and using searching algorithms.
Complete each exercise by filling in the function body.

Run tests with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Basic Linear Search
# =============================================================================

def exercise_1_linear_search(arr, target):
    """
    Implement linear search.
    
    Search through the array from beginning to end.
    Return the index of target if found, -1 otherwise.
    
    Args:
        arr: List of elements
        target: Element to find
        
    Returns:
        int: Index of target, or -1 if not found
        
    Example:
        >>> exercise_1_linear_search([5, 3, 8, 4, 2], 8)
        2
        >>> exercise_1_linear_search([5, 3, 8, 4, 2], 9)
        -1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Binary Search (Iterative)
# =============================================================================

def exercise_2_binary_search(arr, target):
    """
    Implement binary search (iterative version).
    
    The input array is SORTED in ascending order.
    Use left and right pointers to narrow down the search space.
    
    Args:
        arr: SORTED list of elements
        target: Element to find
        
    Returns:
        int: Index of target, or -1 if not found
        
    Example:
        >>> exercise_2_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
        5
        >>> exercise_2_binary_search([1, 2, 3, 4, 5], 10)
        -1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Binary Search (Recursive)
# =============================================================================

def exercise_3_binary_search_recursive(arr, target, left=None, right=None):
    """
    Implement binary search (recursive version).
    
    The input array is SORTED in ascending order.
    Use recursion to divide the search space.
    
    Args:
        arr: SORTED list of elements
        target: Element to find
        left: Left boundary (default: 0)
        right: Right boundary (default: len(arr) - 1)
        
    Returns:
        int: Index of target, or -1 if not found
        
    Example:
        >>> exercise_3_binary_search_recursive([10, 20, 30, 40, 50], 30)
        2
    """
    # Initialize boundaries on first call
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Find First and Last Position
# =============================================================================

def exercise_4_find_first_last(arr, target):
    """
    Find the first and last position of target in a sorted array.
    
    The array may contain duplicates.
    Return [-1, -1] if target is not found.
    
    Args:
        arr: SORTED list of elements (may have duplicates)
        target: Element to find
        
    Returns:
        List[int]: [first_index, last_index] or [-1, -1]
        
    Example:
        >>> exercise_4_find_first_last([1, 2, 2, 2, 3, 4], 2)
        [1, 3]
        >>> exercise_4_find_first_last([1, 2, 3, 4], 5)
        [-1, -1]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Search Insert Position
# =============================================================================

def exercise_5_search_insert(arr, target):
    """
    Find the index where target should be inserted in sorted array.
    
    If target exists, return its index.
    If not, return the index where it would be inserted to maintain order.
    
    Args:
        arr: SORTED list of distinct integers
        target: Target value
        
    Returns:
        int: Index where target is or should be inserted
        
    Example:
        >>> exercise_5_search_insert([1, 3, 5, 6], 5)
        2
        >>> exercise_5_search_insert([1, 3, 5, 6], 2)
        1
        >>> exercise_5_search_insert([1, 3, 5, 6], 7)
        4
        >>> exercise_5_search_insert([1, 3, 5, 6], 0)
        0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 6: Find Peak Element
# =============================================================================

def exercise_6_find_peak(arr):
    """
    Find a peak element in the array.
    
    A peak element is greater than its neighbors.
    The array has no duplicates.
    arr[-1] and arr[n] are considered as -infinity.
    
    You must solve it in O(log n) time.
    
    Args:
        arr: List of integers (no duplicates)
        
    Returns:
        int: Index of any peak element
        
    Example:
        >>> exercise_6_find_peak([1, 2, 3, 1])  # Peak is 3 at index 2
        2
        >>> exercise_6_find_peak([1, 2, 1, 3, 5, 6, 4])  # Peaks at 2 or 6
        5  # (index of 6, which is a peak)
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 7: Search in Rotated Sorted Array
# =============================================================================

def exercise_7_search_rotated(arr, target):
    """
    Search for target in a rotated sorted array.
    
    Example of rotated array: [4,5,6,7,0,1,2] (rotated from [0,1,2,4,5,6,7])
    
    All values are unique.
    Must achieve O(log n) time complexity.
    
    Args:
        arr: Rotated sorted array
        target: Element to find
        
    Returns:
        int: Index of target, or -1 if not found
        
    Example:
        >>> exercise_7_search_rotated([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> exercise_7_search_rotated([4, 5, 6, 7, 0, 1, 2], 3)
        -1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 8: Find Minimum in Rotated Sorted Array
# =============================================================================

def exercise_8_find_min_rotated(arr):
    """
    Find the minimum element in a rotated sorted array.
    
    The array was originally sorted in ascending order,
    then rotated between 1 and n times.
    
    All elements are unique.
    Must achieve O(log n) time complexity.
    
    Args:
        arr: Rotated sorted array
        
    Returns:
        int: The minimum element
        
    Example:
        >>> exercise_8_find_min_rotated([3, 4, 5, 1, 2])
        1
        >>> exercise_8_find_min_rotated([4, 5, 6, 7, 0, 1, 2])
        0
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 9: Search a 2D Matrix
# =============================================================================

def exercise_9_search_matrix(matrix, target):
    """
    Search for target in a 2D matrix.
    
    Matrix properties:
    - Each row is sorted in ascending order
    - The first integer of each row is greater than the last of the previous row
    
    Args:
        matrix: 2D list of integers
        target: Element to find
        
    Returns:
        bool: True if target exists, False otherwise
        
    Example:
        >>> matrix = [
        ...     [1, 3, 5, 7],
        ...     [10, 11, 16, 20],
        ...     [23, 30, 34, 60]
        ... ]
        >>> exercise_9_search_matrix(matrix, 3)
        True
        >>> exercise_9_search_matrix(matrix, 13)
        False
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 10: Square Root (Binary Search Application)
# =============================================================================

def exercise_10_sqrt(x):
    """
    Compute the integer square root of x.
    
    Return the largest integer where integer^2 <= x.
    Do not use built-in sqrt functions.
    Use binary search for O(log x) complexity.
    
    Args:
        x: Non-negative integer
        
    Returns:
        int: Integer square root of x
        
    Example:
        >>> exercise_10_sqrt(4)
        2
        >>> exercise_10_sqrt(8)
        2  # sqrt(8) = 2.828..., floor is 2
        >>> exercise_10_sqrt(16)
        4
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# BONUS EXERCISE: Kth Smallest Element
# =============================================================================

def bonus_kth_smallest(arr, k):
    """
    BONUS: Find the kth smallest element in an unsorted array.
    
    Can you do it in O(n) average time using QuickSelect?
    
    Args:
        arr: Unsorted list of integers
        k: Position (1-indexed) of the element to find
        
    Returns:
        int: The kth smallest element
        
    Example:
        >>> bonus_kth_smallest([3, 2, 1, 5, 6, 4], 2)
        2  # Sorted: [1, 2, 3, 4, 5, 6], 2nd smallest is 2
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests():
    """Run all test cases."""
    print("Running Searching Algorithm Exercises Tests")
    print("=" * 50)
    
    all_passed = True
    
    # Test Exercise 1: Linear Search
    print("\nExercise 1: Linear Search")
    tests_1 = [
        ([5, 3, 8, 4, 2], 8, 2),
        ([5, 3, 8, 4, 2], 9, -1),
        ([1], 1, 0),
        ([], 5, -1),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
    ]
    for arr, target, expected in tests_1:
        result = exercise_1_linear_search(arr, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} linear_search({arr}, {target}) = {result} (expected {expected})")
    
    # Test Exercise 2: Binary Search (Iterative)
    print("\nExercise 2: Binary Search (Iterative)")
    tests_2 = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 5),
        ([1, 2, 3, 4, 5], 10, -1),
        ([1], 1, 0),
        ([1, 3, 5, 7, 9], 3, 1),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 9, 4),
    ]
    for arr, target, expected in tests_2:
        result = exercise_2_binary_search(arr, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} binary_search({arr}, {target}) = {result} (expected {expected})")
    
    # Test Exercise 3: Binary Search (Recursive)
    print("\nExercise 3: Binary Search (Recursive)")
    tests_3 = [
        ([10, 20, 30, 40, 50], 30, 2),
        ([10, 20, 30, 40, 50], 25, -1),
        ([1], 1, 0),
        ([1, 2, 3], 1, 0),
        ([1, 2, 3], 3, 2),
    ]
    for arr, target, expected in tests_3:
        result = exercise_3_binary_search_recursive(arr, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} binary_search_recursive({arr}, {target}) = {result} (expected {expected})")
    
    # Test Exercise 4: Find First and Last
    print("\nExercise 4: Find First and Last Position")
    tests_4 = [
        ([1, 2, 2, 2, 3, 4], 2, [1, 3]),
        ([1, 2, 3, 4], 5, [-1, -1]),
        ([1, 1, 1, 1], 1, [0, 3]),
        ([1], 1, [0, 0]),
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ]
    for arr, target, expected in tests_4:
        result = exercise_4_find_first_last(arr, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} find_first_last({arr}, {target}) = {result} (expected {expected})")
    
    # Test Exercise 5: Search Insert Position
    print("\nExercise 5: Search Insert Position")
    tests_5 = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
    ]
    for arr, target, expected in tests_5:
        result = exercise_5_search_insert(arr, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} search_insert({arr}, {target}) = {result} (expected {expected})")
    
    # Test Exercise 6: Find Peak Element
    print("\nExercise 6: Find Peak Element")
    tests_6 = [
        ([1, 2, 3, 1], [2]),
        ([1, 2, 1, 3, 5, 6, 4], [1, 5]),  # Multiple valid answers
        ([1], [0]),
        ([1, 2], [1]),
        ([2, 1], [0]),
    ]
    for arr, valid_answers in tests_6:
        result = exercise_6_find_peak(arr)
        is_valid = result in valid_answers
        status = "✓" if is_valid else "✗"
        if not is_valid:
            all_passed = False
        print(f"  {status} find_peak({arr}) = {result} (valid: {valid_answers})")
    
    # Test Exercise 7: Search in Rotated Sorted Array
    print("\nExercise 7: Search in Rotated Sorted Array")
    tests_7 = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([3, 1], 1, 1),
    ]
    for arr, target, expected in tests_7:
        result = exercise_7_search_rotated(arr, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} search_rotated({arr}, {target}) = {result} (expected {expected})")
    
    # Test Exercise 8: Find Minimum in Rotated Array
    print("\nExercise 8: Find Minimum in Rotated Sorted Array")
    tests_8 = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([1], 1),
        ([2, 1], 1),
        ([1, 2, 3, 4, 5], 1),
    ]
    for arr, expected in tests_8:
        result = exercise_8_find_min_rotated(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} find_min_rotated({arr}) = {result} (expected {expected})")
    
    # Test Exercise 9: Search 2D Matrix
    print("\nExercise 9: Search a 2D Matrix")
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    tests_9 = [
        (matrix, 3, True),
        (matrix, 13, False),
        (matrix, 1, True),
        (matrix, 60, True),
        ([[1]], 1, True),
        ([[1]], 2, False),
    ]
    for mat, target, expected in tests_9:
        result = exercise_9_search_matrix(mat, target)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} search_matrix(matrix, {target}) = {result} (expected {expected})")
    
    # Test Exercise 10: Integer Square Root
    print("\nExercise 10: Integer Square Root")
    tests_10 = [
        (4, 2),
        (8, 2),
        (16, 4),
        (0, 0),
        (1, 1),
        (100, 10),
        (99, 9),
    ]
    for x, expected in tests_10:
        result = exercise_10_sqrt(x)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} sqrt({x}) = {result} (expected {expected})")
    
    # Test Bonus: Kth Smallest Element
    print("\nBonus Exercise: Kth Smallest Element")
    tests_bonus = [
        ([3, 2, 1, 5, 6, 4], 2, 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 3),
        ([1], 1, 1),
        ([7, 10, 4, 3, 20, 15], 3, 7),
    ]
    for arr, k, expected in tests_bonus:
        result = bonus_kth_smallest(arr, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} kth_smallest({arr}, {k}) = {result} (expected {expected})")
    
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

# Exercise 1: Linear Search
def exercise_1_linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Exercise 2: Binary Search (Iterative)
def exercise_2_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Exercise 3: Binary Search (Recursive)
def exercise_3_binary_search_recursive(arr, target, left=None, right=None):
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
        return exercise_3_binary_search_recursive(arr, target, mid + 1, right)
    else:
        return exercise_3_binary_search_recursive(arr, target, left, mid - 1)

# Exercise 4: Find First and Last Position
def exercise_4_find_first_last(arr, target):
    def find_first(arr, target):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    def find_last(arr, target):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
    
    return [find_first(arr, target), find_last(arr, target)]

# Exercise 5: Search Insert Position
def exercise_5_search_insert(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Exercise 6: Find Peak Element
def exercise_6_find_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

# Exercise 7: Search in Rotated Sorted Array
def exercise_7_search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Exercise 8: Find Minimum in Rotated Sorted Array
def exercise_8_find_min_rotated(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]

# Exercise 9: Search a 2D Matrix
def exercise_9_search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // cols, mid % cols
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Exercise 10: Integer Square Root
def exercise_10_sqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Bonus: Kth Smallest Element (QuickSelect)
def bonus_kth_smallest(arr, k):
    def partition(arr, left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i
    
    def quickselect(arr, left, right, k):
        if left == right:
            return arr[left]
        pivot_index = partition(arr, left, right)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect(arr, left, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, right, k)
    
    return quickselect(arr.copy(), 0, len(arr) - 1, k - 1)
"""


if __name__ == "__main__":
    run_tests()
