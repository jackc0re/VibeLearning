"""
Divide and Conquer - Examples

This file demonstrates divide and conquer algorithms with
classic problems and detailed explanations.

Run this file to see the examples in action:
    python examples.py
"""

import math
import random


# =============================================================================
# MERGE SORT
# =============================================================================

def merge_sort(arr):
    """
    Sort array using Divide and Conquer (Merge Sort).
    
    1. Divide: Split array into two halves
    2. Conquer: Recursively sort each half
    3. Combine: Merge sorted halves
    
    Time: O(n log n)
    Space: O(n)
    """
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Combine
    return merge(left, right)


def merge(left, right):
    """Merge two sorted arrays into one sorted array."""
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


def merge_sort_visualized(arr, depth=0):
    """Merge sort with visualization."""
    indent = "  " * depth
    print(f"{indent}merge_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}  → base case: {arr}")
        return arr
    
    mid = len(arr) // 2
    print(f"{indent}  Divide: {arr[:mid]} | {arr[mid:]}")
    
    left = merge_sort_visualized(arr[:mid], depth + 1)
    right = merge_sort_visualized(arr[mid:], depth + 1)
    
    result = merge(left, right)
    print(f"{indent}  Combine: {left} + {right} → {result}")
    
    return result


# =============================================================================
# QUICK SORT
# =============================================================================

def quick_sort(arr):
    """
    Sort array using Divide and Conquer (Quick Sort).
    
    1. Divide: Partition array around pivot
    2. Conquer: Recursively sort partitions
    3. Combine: Concatenate (trivial)
    
    Time: O(n log n) average, O(n²) worst
    Space: O(log n)
    """
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (middle element)
    pivot = arr[len(arr) // 2]
    
    # Partition
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Conquer and combine
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_in_place(arr, low=0, high=None):
    """In-place Quick Sort."""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_idx - 1)
        quick_sort_in_place(arr, pivot_idx + 1, high)
    
    return arr


def partition(arr, low, high):
    """Partition array and return pivot index."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# =============================================================================
# BINARY SEARCH
# =============================================================================

def binary_search(arr, target, left=0, right=None):
    """
    Search for target using Divide and Conquer.
    
    1. Divide: Split at middle
    2. Conquer: Search appropriate half
    3. Combine: Return result (trivial)
    
    Time: O(log n)
    Space: O(log n) recursive
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: not found
    if left > right:
        return -1
    
    # Divide
    mid = (left + right) // 2
    
    # Conquer
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


# =============================================================================
# FAST EXPONENTIATION
# =============================================================================

def power(x, n):
    """
    Calculate x^n using Divide and Conquer.
    
    Key insight:
    - x^n = (x^(n/2))^2 for even n
    - x^n = x * (x^(n/2))^2 for odd n
    
    Time: O(log n)
    Space: O(log n)
    """
    # Base cases
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    
    # Divide and conquer
    half = power(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


def power_visualized(x, n, depth=0):
    """Fast exponentiation with visualization."""
    indent = "  " * depth
    print(f"{indent}power({x}, {n})")
    
    if n == 0:
        print(f"{indent}  → 1 (base case)")
        return 1
    if n < 0:
        result = 1 / power_visualized(x, -n, depth + 1)
        print(f"{indent}  → 1/{x}^{-n} = {result}")
        return result
    
    half = power_visualized(x, n // 2, depth + 1)
    
    if n % 2 == 0:
        result = half * half
        print(f"{indent}  → {half}² = {result}")
    else:
        result = x * half * half
        print(f"{indent}  → {x} × {half}² = {result}")
    
    return result


# =============================================================================
# MAXIMUM SUBARRAY (DIVIDE AND CONQUER)
# =============================================================================

def max_subarray_dc(arr):
    """
    Find maximum subarray sum using Divide and Conquer.
    
    1. Divide: Split at middle
    2. Conquer: Find max in left half and right half
    3. Combine: Find max crossing the middle
    
    Time: O(n log n)
    """
    def helper(arr, left, right):
        # Base case: single element
        if left == right:
            return arr[left]
        
        mid = (left + right) // 2
        
        # Conquer: max in left and right halves
        left_max = helper(arr, left, mid)
        right_max = helper(arr, mid + 1, right)
        
        # Combine: max crossing middle
        cross_max = max_crossing(arr, left, mid, right)
        
        return max(left_max, right_max, cross_max)
    
    if not arr:
        return 0
    return helper(arr, 0, len(arr) - 1)


def max_crossing(arr, left, mid, right):
    """Find maximum subarray sum crossing the middle."""
    # Max sum from mid going left
    left_sum = float('-inf')
    curr_sum = 0
    for i in range(mid, left - 1, -1):
        curr_sum += arr[i]
        left_sum = max(left_sum, curr_sum)
    
    # Max sum from mid+1 going right
    right_sum = float('-inf')
    curr_sum = 0
    for i in range(mid + 1, right + 1):
        curr_sum += arr[i]
        right_sum = max(right_sum, curr_sum)
    
    return left_sum + right_sum


# =============================================================================
# COUNT INVERSIONS
# =============================================================================

def count_inversions(arr):
    """
    Count pairs (i, j) where i < j but arr[i] > arr[j].
    
    Modified merge sort that counts split inversions during merge.
    
    Time: O(n log n)
    """
    def merge_count(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        
        # Divide and count
        left, left_inv = merge_count(arr[:mid])
        right, right_inv = merge_count(arr[mid:])
        
        # Merge and count split inversions
        merged, split_inv = merge_with_count(left, right)
        
        return merged, left_inv + right_inv + split_inv
    
    _, total = merge_count(arr)
    return total


def merge_with_count(left, right):
    """Merge and count split inversions."""
    result = []
    inversions = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            # All remaining elements in left are inversions with right[j]
            inversions += len(left) - i
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result, inversions


# =============================================================================
# CLOSEST PAIR OF POINTS
# =============================================================================

def closest_pair(points):
    """
    Find two closest points in 2D plane.
    
    1. Divide: Split by x-coordinate
    2. Conquer: Find closest in each half
    3. Combine: Check strip around middle
    
    Time: O(n log n)
    """
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def brute_force(pts):
        min_dist = float('inf')
        pair = None
        n = len(pts)
        for i in range(n):
            for j in range(i + 1, n):
                d = distance(pts[i], pts[j])
                if d < min_dist:
                    min_dist = d
                    pair = (pts[i], pts[j])
        return min_dist, pair
    
    def strip_closest(strip, d, best_pair):
        min_dist = d
        strip.sort(key=lambda p: p[1])  # Sort by y
        
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and strip[j][1] - strip[i][1] < min_dist:
                dist = distance(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist
                    best_pair = (strip[i], strip[j])
                j += 1
        
        return min_dist, best_pair
    
    def closest_util(pts_x):
        n = len(pts_x)
        
        # Base case: small input
        if n <= 3:
            return brute_force(pts_x)
        
        mid = n // 2
        mid_point = pts_x[mid]
        
        # Divide
        left = pts_x[:mid]
        right = pts_x[mid:]
        
        # Conquer
        dl, pair_l = closest_util(left)
        dr, pair_r = closest_util(right)
        
        if dl < dr:
            d, best_pair = dl, pair_l
        else:
            d, best_pair = dr, pair_r
        
        # Combine: check strip
        strip = [p for p in pts_x if abs(p[0] - mid_point[0]) < d]
        
        return strip_closest(strip, d, best_pair)
    
    if len(points) < 2:
        return float('inf'), None
    
    points_sorted = sorted(points, key=lambda p: p[0])
    return closest_util(points_sorted)


# =============================================================================
# KARATSUBA MULTIPLICATION
# =============================================================================

def karatsuba(x, y):
    """
    Multiply two numbers using Karatsuba algorithm.
    
    For n-digit numbers:
    - Normal multiplication: O(n²)
    - Karatsuba: O(n^1.585)
    
    Key insight: 3 multiplications instead of 4
    xy = 10^n * ac + 10^(n/2) * ((a+b)(c+d) - ac - bd) + bd
    
    where x = 10^(n/2) * a + b, y = 10^(n/2) * c + d
    """
    # Base case
    if x < 10 or y < 10:
        return x * y
    
    # Determine size
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Split numbers
    high_x = x // (10 ** m)
    low_x = x % (10 ** m)
    high_y = y // (10 ** m)
    low_y = y % (10 ** m)
    
    # Three recursive multiplications
    z0 = karatsuba(low_x, low_y)
    z2 = karatsuba(high_x, high_y)
    z1 = karatsuba(low_x + high_x, low_y + high_y) - z2 - z0
    
    # Combine
    return z2 * (10 ** (2 * m)) + z1 * (10 ** m) + z0


# =============================================================================
# FIND KTH SMALLEST (QUICKSELECT)
# =============================================================================

def quickselect(arr, k):
    """
    Find kth smallest element using Divide and Conquer.
    
    Like QuickSort but only recurse on one side.
    
    Time: O(n) average, O(n²) worst
    """
    if len(arr) == 1:
        return arr[0]
    
    # Choose pivot
    pivot = arr[len(arr) // 2]
    
    # Partition
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(middle):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(middle))


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_merge_sort():
    """Demonstrate Merge Sort."""
    print("=" * 60)
    print("MERGE SORT (Divide and Conquer)")
    print("=" * 60)
    
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"\nOriginal array: {arr}")
    
    print("\nVisualization:")
    print("-" * 40)
    result = merge_sort_visualized(arr)
    
    print(f"\nSorted array: {result}")


def demo_quick_sort():
    """Demonstrate Quick Sort."""
    print("\n" + "=" * 60)
    print("QUICK SORT (Divide and Conquer)")
    print("=" * 60)
    
    arr = [10, 7, 8, 9, 1, 5]
    print(f"\nOriginal: {arr}")
    print(f"Sorted:   {quick_sort(arr)}")
    
    # In-place version
    arr2 = [10, 7, 8, 9, 1, 5]
    quick_sort_in_place(arr2)
    print(f"In-place: {arr2}")


def demo_binary_search():
    """Demonstrate Binary Search."""
    print("\n" + "=" * 60)
    print("BINARY SEARCH (Divide and Conquer)")
    print("=" * 60)
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"\nSorted array: {arr}")
    
    for target in [7, 12, 1, 19]:
        result = binary_search(arr, target)
        if result != -1:
            print(f"Search for {target}: Found at index {result}")
        else:
            print(f"Search for {target}: Not found")


def demo_power():
    """Demonstrate Fast Exponentiation."""
    print("\n" + "=" * 60)
    print("FAST EXPONENTIATION (Divide and Conquer)")
    print("=" * 60)
    
    print("\nCalculating 2^10:")
    print("-" * 40)
    result = power_visualized(2, 10)
    print(f"\n2^10 = {result}")
    
    print("\nComparison with various exponents:")
    for base, exp in [(2, 16), (3, 5), (5, 3), (2, -3)]:
        result = power(base, exp)
        print(f"  {base}^{exp} = {result}")


def demo_max_subarray():
    """Demonstrate Maximum Subarray."""
    print("\n" + "=" * 60)
    print("MAXIMUM SUBARRAY (Divide and Conquer)")
    print("=" * 60)
    
    arrays = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
    ]
    
    for arr in arrays:
        max_sum = max_subarray_dc(arr)
        print(f"\nArray: {arr}")
        print(f"Maximum subarray sum: {max_sum}")


def demo_count_inversions():
    """Demonstrate Counting Inversions."""
    print("\n" + "=" * 60)
    print("COUNT INVERSIONS (Divide and Conquer)")
    print("=" * 60)
    
    arrays = [
        [2, 4, 1, 3, 5],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]
    
    for arr in arrays:
        count = count_inversions(arr)
        print(f"\nArray: {arr}")
        print(f"Inversions: {count}")
        
        # Verify with brute force for small arrays
        if len(arr) <= 10:
            bf_count = sum(1 for i in range(len(arr)) 
                         for j in range(i+1, len(arr)) if arr[i] > arr[j])
            print(f"Verified (brute force): {bf_count}")


def demo_closest_pair():
    """Demonstrate Closest Pair of Points."""
    print("\n" + "=" * 60)
    print("CLOSEST PAIR OF POINTS (Divide and Conquer)")
    print("=" * 60)
    
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(f"\nPoints: {points}")
    
    min_dist, closest = closest_pair(points)
    print(f"Closest pair: {closest}")
    print(f"Distance: {min_dist:.4f}")


def demo_karatsuba():
    """Demonstrate Karatsuba Multiplication."""
    print("\n" + "=" * 60)
    print("KARATSUBA MULTIPLICATION")
    print("=" * 60)
    
    pairs = [(1234, 5678), (12, 34), (1234567, 7654321)]
    
    for x, y in pairs:
        result = karatsuba(x, y)
        expected = x * y
        print(f"\n{x} × {y} = {result}")
        print(f"Verified: {expected} ({result == expected})")


def demo_quickselect():
    """Demonstrate Quickselect."""
    print("\n" + "=" * 60)
    print("QUICKSELECT (Find Kth Smallest)")
    print("=" * 60)
    
    arr = [3, 2, 1, 5, 6, 4]
    print(f"\nArray: {arr}")
    print(f"Sorted would be: {sorted(arr)}")
    
    for k in [1, 3, 6]:
        result = quickselect(arr.copy(), k)
        print(f"{k}th smallest: {result}")


def demo_complexity_comparison():
    """Compare D&C vs naive approaches."""
    print("\n" + "=" * 60)
    print("COMPLEXITY COMPARISON")
    print("=" * 60)
    
    import time
    
    sizes = [1000, 5000, 10000]
    
    print("\nSorting comparison (Merge Sort vs Python's sorted):")
    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        
        # Merge Sort
        start = time.perf_counter()
        merge_sort(arr.copy())
        merge_time = time.perf_counter() - start
        
        # Python's built-in (Timsort)
        start = time.perf_counter()
        sorted(arr)
        builtin_time = time.perf_counter() - start
        
        print(f"  n={size}: Merge Sort={merge_time:.4f}s, Built-in={builtin_time:.4f}s")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    demo_merge_sort()
    demo_quick_sort()
    demo_binary_search()
    demo_power()
    demo_max_subarray()
    demo_count_inversions()
    demo_closest_pair()
    demo_karatsuba()
    demo_quickselect()
    demo_complexity_comparison()
    
    print("\n" + "=" * 60)
    print("✓ All divide and conquer examples completed!")
    print("=" * 60)
