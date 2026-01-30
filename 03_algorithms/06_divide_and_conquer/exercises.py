"""
Divide and Conquer - Exercises

Practice implementing divide and conquer algorithms.
Each exercise includes test cases to verify your solution.

Run this file to test your implementations:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Merge Sort Implementation
# =============================================================================

def merge_sort(arr):
    """
    Implement merge sort using divide and conquer.
    
    Steps:
    1. Base case: array of length 0 or 1 is already sorted
    2. Divide: split array into two halves
    3. Conquer: recursively sort each half
    4. Combine: merge the sorted halves
    
    Args:
        arr: List of comparable elements
        
    Returns:
        New sorted list
        
    Example:
        >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
        [3, 9, 10, 27, 38, 43, 82]
    """
    # YOUR CODE HERE
    pass


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left: First sorted list
        right: Second sorted list
        
    Returns:
        Merged sorted list
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Binary Search (Recursive)
# =============================================================================

def binary_search(arr, target):
    """
    Find target in sorted array using recursive binary search.
    
    Args:
        arr: Sorted list of elements
        target: Element to find
        
    Returns:
        Index of target, or -1 if not found
        
    Example:
        >>> binary_search([1, 3, 5, 7, 9, 11], 7)
        3
        >>> binary_search([1, 3, 5, 7, 9, 11], 4)
        -1
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Fast Exponentiation
# =============================================================================

def power(x, n):
    """
    Calculate x^n using divide and conquer.
    
    Key insight:
    - x^n = (x^(n/2))^2 for even n
    - x^n = x * (x^(n/2))^2 for odd n
    
    Handle negative exponents: x^(-n) = 1 / x^n
    
    Args:
        x: Base number
        n: Exponent (can be negative)
        
    Returns:
        x raised to power n
        
    Example:
        >>> power(2, 10)
        1024
        >>> power(2, -2)
        0.25
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Count Inversions
# =============================================================================

def count_inversions(arr):
    """
    Count the number of inversions in an array.
    
    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
    
    Use modified merge sort to count inversions in O(n log n).
    
    Args:
        arr: List of comparable elements
        
    Returns:
        Number of inversions
        
    Example:
        >>> count_inversions([2, 4, 1, 3, 5])
        3  # (2,1), (4,1), (4,3)
        >>> count_inversions([1, 2, 3, 4, 5])
        0  # Already sorted
        >>> count_inversions([5, 4, 3, 2, 1])
        10  # Reverse sorted = n*(n-1)/2
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Maximum Subarray Sum (D&C)
# =============================================================================

def max_subarray_sum(arr):
    """
    Find maximum subarray sum using divide and conquer.
    
    Approach:
    1. Divide array at middle
    2. Max subarray is either:
       - Entirely in left half
       - Entirely in right half
       - Crossing the middle
    3. Return maximum of these three
    
    Args:
        arr: List of integers (can be negative)
        
    Returns:
        Maximum sum of any contiguous subarray
        
    Example:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6  # [4, -1, 2, 1]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 6: Find Peak Element
# =============================================================================

def find_peak(arr):
    """
    Find a peak element in array using divide and conquer.
    
    A peak element is greater than its neighbors.
    For corner elements, only one neighbor needs to be smaller.
    
    Args:
        arr: List of distinct integers
        
    Returns:
        Index of any peak element
        
    Example:
        >>> arr = [1, 3, 20, 4, 1, 0]
        >>> find_peak(arr)  # Returns 2 (arr[2]=20 is a peak)
        2
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 7: Kth Smallest Element (Quickselect)
# =============================================================================

def kth_smallest(arr, k):
    """
    Find kth smallest element using quickselect (D&C).
    
    Like quicksort but only recurse on one partition.
    
    Args:
        arr: List of comparable elements
        k: Position (1-indexed, so k=1 means smallest)
        
    Returns:
        The kth smallest element
        
    Example:
        >>> kth_smallest([3, 2, 1, 5, 6, 4], 2)
        2  # Second smallest
        >>> kth_smallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        3  # Fourth smallest
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 8: Majority Element
# =============================================================================

def majority_element(arr):
    """
    Find the majority element using divide and conquer.
    
    Majority element appears more than n/2 times.
    Assume the array always has a majority element.
    
    D&C approach:
    - If left half and right half have same majority, that's the answer
    - Otherwise, count occurrences of both candidates
    
    Args:
        arr: List with a majority element
        
    Returns:
        The majority element
        
    Example:
        >>> majority_element([3, 2, 3])
        3
        >>> majority_element([2, 2, 1, 1, 1, 2, 2])
        2
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 9: Closest Pair of Points
# =============================================================================

def closest_pair_distance(points):
    """
    Find the distance between closest pair of points.
    
    Use divide and conquer for O(n log n) solution.
    
    Args:
        points: List of (x, y) tuples
        
    Returns:
        Minimum distance between any two points
        
    Example:
        >>> points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
        >>> closest_pair_distance(points)
        1.4142...  # Distance between (2,3) and (3,4)
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 10: Median of Two Sorted Arrays
# =============================================================================

def find_median_sorted_arrays(nums1, nums2):
    """
    Find median of two sorted arrays using divide and conquer.
    
    Overall time complexity should be O(log(m+n)).
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
        
    Returns:
        Median of combined array
        
    Example:
        >>> find_median_sorted_arrays([1, 3], [2])
        2.0
        >>> find_median_sorted_arrays([1, 2], [3, 4])
        2.5
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def test_merge_sort():
    """Test merge sort implementation."""
    print("Testing merge_sort...")
    
    tests = [
        ([38, 27, 43, 3, 9, 82, 10], [3, 9, 10, 27, 38, 43, 82]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([-3, -1, -2, 0, 2, 1], [-3, -2, -1, 0, 1, 2]),
    ]
    
    for arr, expected in tests:
        result = merge_sort(arr)
        assert result == expected, f"merge_sort({arr}) = {result}, expected {expected}"
    
    print("✓ All merge_sort tests passed!")


def test_binary_search():
    """Test binary search implementation."""
    print("\nTesting binary_search...")
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    
    tests = [
        (arr, 7, 3),
        (arr, 1, 0),
        (arr, 15, 7),
        (arr, 4, -1),
        (arr, 0, -1),
        (arr, 16, -1),
        ([], 5, -1),
    ]
    
    for array, target, expected in tests:
        result = binary_search(array, target)
        assert result == expected, f"binary_search({array}, {target}) = {result}, expected {expected}"
    
    print("✓ All binary_search tests passed!")


def test_power():
    """Test fast exponentiation."""
    print("\nTesting power...")
    
    tests = [
        (2, 10, 1024),
        (2, 0, 1),
        (3, 5, 243),
        (5, 3, 125),
        (2, -2, 0.25),
        (10, 1, 10),
    ]
    
    for x, n, expected in tests:
        result = power(x, n)
        assert abs(result - expected) < 1e-9, f"power({x}, {n}) = {result}, expected {expected}"
    
    print("✓ All power tests passed!")


def test_count_inversions():
    """Test inversion counting."""
    print("\nTesting count_inversions...")
    
    tests = [
        ([2, 4, 1, 3, 5], 3),
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 10),
        ([1, 3, 2], 1),
        ([1], 0),
        ([], 0),
    ]
    
    for arr, expected in tests:
        result = count_inversions(arr)
        assert result == expected, f"count_inversions({arr}) = {result}, expected {expected}"
    
    print("✓ All count_inversions tests passed!")


def test_max_subarray_sum():
    """Test maximum subarray sum."""
    print("\nTesting max_subarray_sum...")
    
    tests = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1, 2, 3, 4, 5], 15),
        ([-1, -2, -3, -4], -1),
        ([5], 5),
        ([-2, -1], -1),
    ]
    
    for arr, expected in tests:
        result = max_subarray_sum(arr)
        assert result == expected, f"max_subarray_sum({arr}) = {result}, expected {expected}"
    
    print("✓ All max_subarray_sum tests passed!")


def test_find_peak():
    """Test peak finding."""
    print("\nTesting find_peak...")
    
    tests = [
        [1, 3, 20, 4, 1, 0],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 1, 3, 5, 6, 4],
    ]
    
    for arr in tests:
        result = find_peak(arr)
        # Verify it's actually a peak
        is_peak = True
        if result > 0 and arr[result] < arr[result - 1]:
            is_peak = False
        if result < len(arr) - 1 and arr[result] < arr[result + 1]:
            is_peak = False
        assert is_peak, f"find_peak({arr}) = {result}, but arr[{result}]={arr[result]} is not a peak"
    
    print("✓ All find_peak tests passed!")


def test_kth_smallest():
    """Test kth smallest element."""
    print("\nTesting kth_smallest...")
    
    tests = [
        ([3, 2, 1, 5, 6, 4], 2, 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 3),
        ([1], 1, 1),
        ([7, 10, 4, 3, 20, 15], 3, 7),
        ([7, 10, 4, 3, 20, 15], 6, 20),
    ]
    
    for arr, k, expected in tests:
        result = kth_smallest(arr.copy(), k)
        assert result == expected, f"kth_smallest({arr}, {k}) = {result}, expected {expected}"
    
    print("✓ All kth_smallest tests passed!")


def test_majority_element():
    """Test majority element finding."""
    print("\nTesting majority_element...")
    
    tests = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1, 1, 1, 1], 1),
        ([6, 5, 5], 5),
    ]
    
    for arr, expected in tests:
        result = majority_element(arr)
        assert result == expected, f"majority_element({arr}) = {result}, expected {expected}"
    
    print("✓ All majority_element tests passed!")


def test_closest_pair_distance():
    """Test closest pair of points."""
    print("\nTesting closest_pair_distance...")
    
    import math
    
    tests = [
        ([(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)], math.sqrt(2)),
        ([(0, 0), (1, 1), (10, 10)], math.sqrt(2)),
        ([(0, 0), (3, 4)], 5.0),
    ]
    
    for points, expected in tests:
        result = closest_pair_distance(points)
        assert abs(result - expected) < 1e-6, f"closest_pair_distance({points}) = {result}, expected {expected}"
    
    print("✓ All closest_pair_distance tests passed!")


def test_find_median_sorted_arrays():
    """Test median of two sorted arrays."""
    print("\nTesting find_median_sorted_arrays...")
    
    tests = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
        ([1, 3, 5], [2, 4, 6], 3.5),
    ]
    
    for nums1, nums2, expected in tests:
        result = find_median_sorted_arrays(nums1, nums2)
        assert abs(result - expected) < 1e-6, f"find_median_sorted_arrays({nums1}, {nums2}) = {result}, expected {expected}"
    
    print("✓ All find_median_sorted_arrays tests passed!")


# =============================================================================
# SOLUTIONS (Hidden - Try to solve without looking!)
# =============================================================================

def _show_solutions():
    """Display solutions for all exercises."""
    solutions = '''
# =============================================================================
# SOLUTIONS
# =============================================================================

# Exercise 1: Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Exercise 2: Binary Search
def binary_search(arr, target):
    def helper(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)
    
    return helper(0, len(arr) - 1)


# Exercise 3: Fast Exponentiation
def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    
    half = power(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


# Exercise 4: Count Inversions
def count_inversions(arr):
    def merge_count(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, left_inv = merge_count(arr[:mid])
        right, right_inv = merge_count(arr[mid:])
        
        merged = []
        inversions = left_inv + right_inv
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += len(left) - i
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, inversions
    
    _, total = merge_count(arr)
    return total


# Exercise 5: Maximum Subarray Sum
def max_subarray_sum(arr):
    def helper(left, right):
        if left == right:
            return arr[left]
        
        mid = (left + right) // 2
        
        left_max = helper(left, mid)
        right_max = helper(mid + 1, right)
        
        # Max crossing middle
        left_sum = float('-inf')
        curr = 0
        for i in range(mid, left - 1, -1):
            curr += arr[i]
            left_sum = max(left_sum, curr)
        
        right_sum = float('-inf')
        curr = 0
        for i in range(mid + 1, right + 1):
            curr += arr[i]
            right_sum = max(right_sum, curr)
        
        cross_max = left_sum + right_sum
        
        return max(left_max, right_max, cross_max)
    
    if not arr:
        return 0
    return helper(0, len(arr) - 1)


# Exercise 6: Find Peak Element
def find_peak(arr):
    def helper(left, right):
        mid = (left + right) // 2
        
        # Check if mid is peak
        is_peak = True
        if mid > 0 and arr[mid] < arr[mid - 1]:
            is_peak = False
        if mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
            is_peak = False
        
        if is_peak:
            return mid
        
        # Go towards higher neighbor
        if mid > 0 and arr[mid - 1] > arr[mid]:
            return helper(left, mid - 1)
        else:
            return helper(mid + 1, right)
    
    return helper(0, len(arr) - 1)


# Exercise 7: Kth Smallest Element
def kth_smallest(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k <= len(left):
        return kth_smallest(left, k)
    elif k <= len(left) + len(middle):
        return pivot
    else:
        return kth_smallest(right, k - len(left) - len(middle))


# Exercise 8: Majority Element
def majority_element(arr):
    def helper(left, right):
        if left == right:
            return arr[left]
        
        mid = (left + right) // 2
        left_maj = helper(left, mid)
        right_maj = helper(mid + 1, right)
        
        if left_maj == right_maj:
            return left_maj
        
        left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_maj)
        right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_maj)
        
        return left_maj if left_count > right_count else right_maj
    
    return helper(0, len(arr) - 1)


# Exercise 9: Closest Pair Distance
def closest_pair_distance(points):
    import math
    
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def brute_force(pts):
        min_dist = float('inf')
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                min_dist = min(min_dist, distance(pts[i], pts[j]))
        return min_dist
    
    def strip_closest(strip, d):
        min_dist = d
        strip.sort(key=lambda p: p[1])
        
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and strip[j][1] - strip[i][1] < min_dist:
                min_dist = min(min_dist, distance(strip[i], strip[j]))
                j += 1
        
        return min_dist
    
    def closest_util(pts_x):
        n = len(pts_x)
        
        if n <= 3:
            return brute_force(pts_x)
        
        mid = n // 2
        mid_point = pts_x[mid]
        
        dl = closest_util(pts_x[:mid])
        dr = closest_util(pts_x[mid:])
        d = min(dl, dr)
        
        strip = [p for p in pts_x if abs(p[0] - mid_point[0]) < d]
        
        return min(d, strip_closest(strip, d))
    
    points_sorted = sorted(points, key=lambda p: p[0])
    return closest_util(points_sorted)


# Exercise 10: Median of Two Sorted Arrays
def find_median_sorted_arrays(nums1, nums2):
    # Ensure nums1 is smaller
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    
    if m == 0:
        if n % 2 == 0:
            return (nums2[n // 2 - 1] + nums2[n // 2]) / 2
        return float(nums2[n // 2])
    
    left, right = 0, m
    
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]
        
        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]
        
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            return float(max(max_left1, max_left2))
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1
    
    return 0.0
'''
    print(solutions)


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--solutions":
        _show_solutions()
    else:
        print("=" * 60)
        print("DIVIDE AND CONQUER - EXERCISES")
        print("=" * 60)
        print("\nImplement each function and run this file to test.")
        print("Use 'python exercises.py --solutions' to see solutions.\n")
        
        try:
            test_merge_sort()
        except (AssertionError, TypeError) as e:
            print(f"✗ merge_sort: {e}")
        
        try:
            test_binary_search()
        except (AssertionError, TypeError) as e:
            print(f"✗ binary_search: {e}")
        
        try:
            test_power()
        except (AssertionError, TypeError) as e:
            print(f"✗ power: {e}")
        
        try:
            test_count_inversions()
        except (AssertionError, TypeError) as e:
            print(f"✗ count_inversions: {e}")
        
        try:
            test_max_subarray_sum()
        except (AssertionError, TypeError) as e:
            print(f"✗ max_subarray_sum: {e}")
        
        try:
            test_find_peak()
        except (AssertionError, TypeError) as e:
            print(f"✗ find_peak: {e}")
        
        try:
            test_kth_smallest()
        except (AssertionError, TypeError) as e:
            print(f"✗ kth_smallest: {e}")
        
        try:
            test_majority_element()
        except (AssertionError, TypeError) as e:
            print(f"✗ majority_element: {e}")
        
        try:
            test_closest_pair_distance()
        except (AssertionError, TypeError) as e:
            print(f"✗ closest_pair_distance: {e}")
        
        try:
            test_find_median_sorted_arrays()
        except (AssertionError, TypeError) as e:
            print(f"✗ find_median_sorted_arrays: {e}")
        
        print("\n" + "=" * 60)
        print("Testing complete!")
        print("=" * 60)
