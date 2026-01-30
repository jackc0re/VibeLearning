"""
Searching Algorithms - Examples

This file demonstrates various searching algorithms with
clear explanations and practical examples.

Run this file to see the examples in action:
    python examples.py
"""


# =============================================================================
# LINEAR SEARCH
# =============================================================================

def linear_search(arr, target):
    """
    Search for target in arr by checking each element sequentially.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr: List of elements to search
        target: Element to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_with_steps(arr, target):
    """
    Linear search that prints each step for educational purposes.
    """
    print(f"Searching for {target} in {arr}")
    print("-" * 40)
    
    for i in range(len(arr)):
        print(f"Step {i + 1}: Checking index {i}, value = {arr[i]}")
        if arr[i] == target:
            print(f"  ✓ Found {target} at index {i}!")
            return i
        else:
            print(f"  ✗ {arr[i]} ≠ {target}, continue...")
    
    print(f"  ✗ {target} not found in array")
    return -1


def linear_search_all(arr, target):
    """
    Find ALL occurrences of target in arr.
    
    Returns:
        List of all indices where target is found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


# =============================================================================
# BINARY SEARCH
# =============================================================================

def binary_search(arr, target):
    """
    Search for target in SORTED arr using binary search.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Args:
        arr: SORTED list of elements
        target: Element to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
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


def binary_search_with_steps(arr, target):
    """
    Binary search that prints each step for educational purposes.
    """
    print(f"Binary searching for {target} in {arr}")
    print("-" * 50)
    
    left, right = 0, len(arr) - 1
    step = 1
    
    while left <= right:
        mid = (left + right) // 2
        
        print(f"Step {step}: left={left}, right={right}, mid={mid}")
        print(f"  Checking arr[{mid}] = {arr[mid]}")
        
        if arr[mid] == target:
            print(f"  ✓ Found {target} at index {mid}!")
            return mid
        elif arr[mid] < target:
            print(f"  {arr[mid]} < {target}, search right half")
            left = mid + 1
        else:
            print(f"  {arr[mid]} > {target}, search left half")
            right = mid - 1
        
        step += 1
    
    print(f"  ✗ {target} not found in array")
    return -1


def binary_search_recursive(arr, target, left=None, right=None):
    """
    Recursive implementation of binary search.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to call stack
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    # Base case: element not found
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Base case: element found
    if arr[mid] == target:
        return mid
    # Recursive case: search left or right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# =============================================================================
# BINARY SEARCH VARIATIONS
# =============================================================================

def find_first_occurrence(arr, target):
    """
    Find the FIRST occurrence of target in sorted array with duplicates.
    
    Example: [1, 2, 2, 2, 3, 4] with target=2 returns index 1
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid  # Found, but keep looking left for earlier occurrence
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def find_last_occurrence(arr, target):
    """
    Find the LAST occurrence of target in sorted array with duplicates.
    
    Example: [1, 2, 2, 2, 3, 4] with target=2 returns index 3
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid  # Found, but keep looking right for later occurrence
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def count_occurrences(arr, target):
    """
    Count how many times target appears in sorted array.
    Uses first/last occurrence to calculate count.
    
    Time Complexity: O(log n)
    """
    first = find_first_occurrence(arr, target)
    if first == -1:
        return 0
    last = find_last_occurrence(arr, target)
    return last - first + 1


def find_insert_position(arr, target):
    """
    Find the index where target should be inserted to maintain sorted order.
    Also known as 'bisect_left' in Python's bisect module.
    
    Example: [1, 3, 5, 7] with target=4 returns 2 (insert between 3 and 5)
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


def search_rotated_array(arr, target):
    """
    Search in a rotated sorted array.
    
    A rotated sorted array: [4, 5, 6, 7, 0, 1, 2] (original: [0, 1, 2, 4, 5, 6, 7])
    
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Determine which half is sorted
        if arr[left] <= arr[mid]:
            # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Target in left half
            else:
                left = mid + 1   # Target in right half
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Target in right half
            else:
                right = mid - 1  # Target in left half
    
    return -1


def find_peak_element(arr):
    """
    Find a peak element in array (element greater than its neighbors).
    
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[mid + 1]:
            # Peak is in left half (including mid)
            right = mid
        else:
            # Peak is in right half
            left = mid + 1
    
    return left


def find_minimum_rotated(arr):
    """
    Find the minimum element in a rotated sorted array.
    
    Example: [4, 5, 6, 7, 0, 1, 2] returns 0 (at index 4)
    
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[right]:
            # Minimum is in right half
            left = mid + 1
        else:
            # Minimum is in left half (including mid)
            right = mid
    
    return arr[left]


# =============================================================================
# SEARCHING IN DIFFERENT DATA STRUCTURES
# =============================================================================

def search_2d_matrix(matrix, target):
    """
    Search in a 2D matrix where each row is sorted and
    the first element of each row is greater than the last element of previous row.
    
    Time Complexity: O(log(m*n)) where m=rows, n=cols
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Convert 1D index to 2D coordinates
        row, col = mid // cols, mid % cols
        value = matrix[row][col]
        
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


def search_in_dict(data, key):
    """
    Search for a key in a dictionary.
    Dictionaries use hash-based lookup: O(1) average case.
    """
    return data.get(key, None)


def search_in_set(data_set, item):
    """
    Check if item exists in a set.
    Sets use hash-based lookup: O(1) average case.
    """
    return item in data_set


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_linear_search():
    """Demonstrate linear search with examples."""
    print("=" * 60)
    print("LINEAR SEARCH DEMONSTRATION")
    print("=" * 60)
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    # Basic linear search
    print("\n1. Basic Linear Search:")
    print(f"   Array: {arr}")
    
    target = 22
    result = linear_search(arr, target)
    print(f"   Searching for {target}: Found at index {result}")
    
    target = 99
    result = linear_search(arr, target)
    print(f"   Searching for {target}: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
    
    # Step-by-step linear search
    print("\n2. Step-by-step Linear Search:")
    linear_search_with_steps([4, 2, 7, 1, 9, 3], 7)
    
    # Find all occurrences
    print("\n3. Finding All Occurrences:")
    arr_with_dupes = [1, 3, 5, 3, 7, 3, 9]
    indices = linear_search_all(arr_with_dupes, 3)
    print(f"   Array: {arr_with_dupes}")
    print(f"   All indices of 3: {indices}")


def demo_binary_search():
    """Demonstrate binary search with examples."""
    print("\n" + "=" * 60)
    print("BINARY SEARCH DEMONSTRATION")
    print("=" * 60)
    
    sorted_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Basic binary search
    print("\n1. Basic Binary Search (requires sorted array):")
    print(f"   Sorted Array: {sorted_arr}")
    
    target = 11
    result = binary_search(sorted_arr, target)
    print(f"   Searching for {target}: Found at index {result}")
    
    target = 8
    result = binary_search(sorted_arr, target)
    print(f"   Searching for {target}: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
    
    # Step-by-step binary search
    print("\n2. Step-by-step Binary Search:")
    binary_search_with_steps([1, 2, 3, 4, 7, 9, 11, 15], 9)
    
    # Recursive binary search
    print("\n3. Recursive Binary Search:")
    result = binary_search_recursive(sorted_arr, 15)
    print(f"   Array: {sorted_arr}")
    print(f"   Searching for 15: Found at index {result}")


def demo_binary_search_variations():
    """Demonstrate binary search variations."""
    print("\n" + "=" * 60)
    print("BINARY SEARCH VARIATIONS")
    print("=" * 60)
    
    # First and last occurrence
    print("\n1. First and Last Occurrence:")
    arr_dupes = [1, 2, 2, 2, 2, 3, 4, 5]
    print(f"   Array: {arr_dupes}")
    print(f"   First occurrence of 2: index {find_first_occurrence(arr_dupes, 2)}")
    print(f"   Last occurrence of 2: index {find_last_occurrence(arr_dupes, 2)}")
    print(f"   Count of 2: {count_occurrences(arr_dupes, 2)}")
    
    # Insert position
    print("\n2. Find Insert Position:")
    arr = [1, 3, 5, 7, 9]
    print(f"   Array: {arr}")
    for target in [0, 4, 6, 10]:
        pos = find_insert_position(arr, target)
        print(f"   Insert position for {target}: index {pos}")
    
    # Rotated array search
    print("\n3. Search in Rotated Sorted Array:")
    rotated = [4, 5, 6, 7, 0, 1, 2]
    print(f"   Rotated Array: {rotated}")
    for target in [0, 5, 3]:
        result = search_rotated_array(rotated, target)
        status = f"Found at index {result}" if result != -1 else "Not found"
        print(f"   Searching for {target}: {status}")
    
    # Find minimum in rotated array
    print("\n4. Find Minimum in Rotated Array:")
    print(f"   Rotated Array: {rotated}")
    print(f"   Minimum element: {find_minimum_rotated(rotated)}")
    
    # Peak element
    print("\n5. Find Peak Element:")
    arr = [1, 3, 5, 4, 2]
    peak_idx = find_peak_element(arr)
    print(f"   Array: {arr}")
    print(f"   Peak element: {arr[peak_idx]} at index {peak_idx}")


def demo_2d_search():
    """Demonstrate 2D matrix search."""
    print("\n" + "=" * 60)
    print("2D MATRIX SEARCH")
    print("=" * 60)
    
    matrix = [
        [1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    
    print("\n   Matrix:")
    for row in matrix:
        print(f"   {row}")
    
    for target in [3, 16, 25]:
        result = search_2d_matrix(matrix, target)
        status = "Found" if result else "Not found"
        print(f"\n   Searching for {target}: {status}")


def demo_complexity_comparison():
    """Compare linear vs binary search performance."""
    print("\n" + "=" * 60)
    print("COMPLEXITY COMPARISON")
    print("=" * 60)
    
    import time
    
    # Create a large sorted array
    large_arr = list(range(1000000))
    target = 999999  # Worst case for linear search
    
    print(f"\n   Array size: {len(large_arr):,}")
    print(f"   Target: {target:,}")
    
    # Linear search
    start = time.perf_counter()
    linear_search(large_arr, target)
    linear_time = time.perf_counter() - start
    
    # Binary search
    start = time.perf_counter()
    binary_search(large_arr, target)
    binary_time = time.perf_counter() - start
    
    print(f"\n   Linear Search Time: {linear_time:.6f} seconds")
    print(f"   Binary Search Time: {binary_time:.6f} seconds")
    print(f"   Binary is ~{linear_time / binary_time:.0f}x faster!")
    
    import math
    print(f"\n   Theoretical comparisons:")
    print(f"   Linear (worst): {len(large_arr):,}")
    print(f"   Binary (worst): {int(math.log2(len(large_arr)))}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    demo_linear_search()
    demo_binary_search()
    demo_binary_search_variations()
    demo_2d_search()
    demo_complexity_comparison()
    
    print("\n" + "=" * 60)
    print("✓ All examples completed!")
    print("=" * 60)
