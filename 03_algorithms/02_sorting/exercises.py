"""
Sorting Algorithms - Exercises

Practice implementing and using sorting algorithms.
Complete each exercise by filling in the function body.

Run tests with:
    python exercises.py
"""


# =============================================================================
# EXERCISE 1: Bubble Sort
# =============================================================================

def exercise_1_bubble_sort(arr):
    """
    Implement Bubble Sort.
    
    Repeatedly step through the list, compare adjacent elements,
    and swap them if they're in the wrong order.
    
    Hint: Use a nested loop. Outer loop for passes, inner for comparisons.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        List: Sorted array (ascending order)
        
    Example:
        >>> exercise_1_bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    arr = arr.copy()  # Don't modify original
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: Selection Sort
# =============================================================================

def exercise_2_selection_sort(arr):
    """
    Implement Selection Sort.
    
    Find the minimum element in the unsorted portion and
    swap it with the first unsorted element.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        List: Sorted array (ascending order)
        
    Example:
        >>> exercise_2_selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]
    """
    arr = arr.copy()
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Insertion Sort
# =============================================================================

def exercise_3_insertion_sort(arr):
    """
    Implement Insertion Sort.
    
    Build the sorted array one element at a time by inserting
    each element into its correct position.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        List: Sorted array (ascending order)
        
    Example:
        >>> exercise_3_insertion_sort([12, 11, 13, 5, 6])
        [5, 6, 11, 12, 13]
    """
    arr = arr.copy()
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Merge Sort
# =============================================================================

def exercise_4_merge_sort(arr):
    """
    Implement Merge Sort.
    
    Divide the array in half, recursively sort each half,
    then merge the sorted halves.
    
    Hint: You'll need a helper function to merge two sorted arrays.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        List: Sorted array (ascending order)
        
    Example:
        >>> exercise_4_merge_sort([38, 27, 43, 3, 9, 82, 10])
        [3, 9, 10, 27, 38, 43, 82]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Quick Sort
# =============================================================================

def exercise_5_quick_sort(arr):
    """
    Implement Quick Sort.
    
    Choose a pivot, partition the array around it,
    then recursively sort the partitions.
    
    Hint: You'll need a partition helper function.
    Use the last element as the pivot for simplicity.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        List: Sorted array (ascending order)
        
    Example:
        >>> exercise_5_quick_sort([10, 7, 8, 9, 1, 5])
        [1, 5, 7, 8, 9, 10]
    """
    arr = arr.copy()
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 6: Sort Colors (Dutch National Flag)
# =============================================================================

def exercise_6_sort_colors(nums):
    """
    Given an array with only 0s, 1s, and 2s, sort it in-place.
    
    This is known as the Dutch National Flag problem.
    Do it in one pass with O(1) extra space.
    
    Hint: Use three pointers - low, mid, high
    
    Args:
        nums: List containing only 0, 1, and 2
        
    Returns:
        List: Sorted array [0,0,0,...,1,1,1,...,2,2,2,...]
        
    Example:
        >>> exercise_6_sort_colors([2, 0, 2, 1, 1, 0])
        [0, 0, 1, 1, 2, 2]
    """
    nums = nums.copy()
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 7: Merge Two Sorted Arrays
# =============================================================================

def exercise_7_merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
        
    Returns:
        List: Merged sorted array
        
    Example:
        >>> exercise_7_merge_sorted_arrays([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 8: Sort by Frequency
# =============================================================================

def exercise_8_sort_by_frequency(arr):
    """
    Sort elements by their frequency (most frequent first).
    If frequency is the same, maintain original order.
    
    Args:
        arr: List of integers
        
    Returns:
        List: Sorted by frequency (descending)
        
    Example:
        >>> exercise_8_sort_by_frequency([1, 1, 2, 2, 2, 3])
        [2, 2, 2, 1, 1, 3]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 9: Kth Largest Element
# =============================================================================

def exercise_9_kth_largest(arr, k):
    """
    Find the kth largest element in an unsorted array.
    
    Note: kth largest, not kth distinct element.
    
    You can use any sorting algorithm or quickselect.
    
    Args:
        arr: List of integers
        k: Which largest element to find (1 = largest)
        
    Returns:
        int: The kth largest element
        
    Example:
        >>> exercise_9_kth_largest([3, 2, 1, 5, 6, 4], 2)
        5
        >>> exercise_9_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 10: Custom Sort - Sort by Absolute Value
# =============================================================================

def exercise_10_sort_by_abs(arr):
    """
    Sort array by absolute value (ascending).
    If absolute values are equal, negative numbers come first.
    
    Args:
        arr: List of integers (positive and negative)
        
    Returns:
        List: Sorted by absolute value
        
    Example:
        >>> exercise_10_sort_by_abs([1, -2, 3, -4, 5, -3])
        [1, -2, -3, 3, -4, 5]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 11: Counting Sort
# =============================================================================

def exercise_11_counting_sort(arr):
    """
    Implement Counting Sort for non-negative integers.
    
    Count occurrences of each element, then reconstruct sorted array.
    
    Time Complexity should be O(n + k) where k is the max value.
    
    Args:
        arr: List of non-negative integers
        
    Returns:
        List: Sorted array
        
    Example:
        >>> exercise_11_counting_sort([4, 2, 2, 8, 3, 3, 1])
        [1, 2, 2, 3, 3, 4, 8]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 12: Check if Array Can Be Sorted with At Most One Swap
# =============================================================================

def exercise_12_one_swap_sort(arr):
    """
    Check if the array can be sorted with at most one swap.
    
    Args:
        arr: List of integers
        
    Returns:
        bool: True if can be sorted with 0 or 1 swap, False otherwise
        
    Example:
        >>> exercise_12_one_swap_sort([1, 3, 2])
        True  # Swap 3 and 2
        >>> exercise_12_one_swap_sort([3, 2, 1])
        False  # Needs more than one swap
        >>> exercise_12_one_swap_sort([1, 2, 3])
        True  # Already sorted
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# BONUS: Implement Heap Sort
# =============================================================================

def bonus_heap_sort(arr):
    """
    BONUS: Implement Heap Sort.
    
    Build a max heap, then repeatedly extract the maximum element.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    
    Hint: You'll need a heapify helper function.
    
    Args:
        arr: List of comparable elements
        
    Returns:
        List: Sorted array
        
    Example:
        >>> bonus_heap_sort([12, 11, 13, 5, 6, 7])
        [5, 6, 7, 11, 12, 13]
    """
    arr = arr.copy()
    # YOUR CODE HERE
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def run_tests():
    """Run all test cases."""
    print("Running Sorting Algorithm Exercises Tests")
    print("=" * 50)
    
    all_passed = True
    
    # Test Exercise 1: Bubble Sort
    print("\nExercise 1: Bubble Sort")
    tests_1 = [
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
    ]
    for arr, expected in tests_1:
        result = exercise_1_bubble_sort(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} bubble_sort({arr}) = {result}")
    
    # Test Exercise 2: Selection Sort
    print("\nExercise 2: Selection Sort")
    tests_2 = [
        ([64, 25, 12, 22, 11], [11, 12, 22, 25, 64]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
    ]
    for arr, expected in tests_2:
        result = exercise_2_selection_sort(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} selection_sort({arr}) = {result}")
    
    # Test Exercise 3: Insertion Sort
    print("\nExercise 3: Insertion Sort")
    tests_3 = [
        ([12, 11, 13, 5, 6], [5, 6, 11, 12, 13]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1], [1]),
    ]
    for arr, expected in tests_3:
        result = exercise_3_insertion_sort(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} insertion_sort({arr}) = {result}")
    
    # Test Exercise 4: Merge Sort
    print("\nExercise 4: Merge Sort")
    tests_4 = [
        ([38, 27, 43, 3, 9, 82, 10], [3, 9, 10, 27, 38, 43, 82]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
    ]
    for arr, expected in tests_4:
        result = exercise_4_merge_sort(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} merge_sort({arr}) = {result}")
    
    # Test Exercise 5: Quick Sort
    print("\nExercise 5: Quick Sort")
    tests_5 = [
        ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
    ]
    for arr, expected in tests_5:
        result = exercise_5_quick_sort(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} quick_sort({arr}) = {result}")
    
    # Test Exercise 6: Sort Colors
    print("\nExercise 6: Sort Colors (Dutch Flag)")
    tests_6 = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1, 1, 1], [1, 1, 1]),
    ]
    for arr, expected in tests_6:
        result = exercise_6_sort_colors(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} sort_colors({arr}) = {result}")
    
    # Test Exercise 7: Merge Sorted Arrays
    print("\nExercise 7: Merge Two Sorted Arrays")
    tests_7 = [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1], [2], [1, 2]),
    ]
    for arr1, arr2, expected in tests_7:
        result = exercise_7_merge_sorted_arrays(arr1, arr2)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} merge({arr1}, {arr2}) = {result}")
    
    # Test Exercise 8: Sort by Frequency
    print("\nExercise 8: Sort by Frequency")
    tests_8 = [
        ([1, 1, 2, 2, 2, 3], [2, 2, 2, 1, 1, 3]),
        ([1, 1, 1, 2, 2, 3], [1, 1, 1, 2, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),  # All same frequency, maintain order
    ]
    for arr, expected in tests_8:
        result = exercise_8_sort_by_frequency(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} sort_by_frequency({arr}) = {result}")
    
    # Test Exercise 9: Kth Largest
    print("\nExercise 9: Kth Largest Element")
    tests_9 = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([7, 6, 5, 4, 3, 2, 1], 5, 3),
    ]
    for arr, k, expected in tests_9:
        result = exercise_9_kth_largest(arr, k)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} kth_largest({arr}, {k}) = {result} (expected {expected})")
    
    # Test Exercise 10: Sort by Absolute Value
    print("\nExercise 10: Sort by Absolute Value")
    tests_10 = [
        ([1, -2, 3, -4, 5, -3], [1, -2, -3, 3, -4, 5]),
        ([-1, 1], [-1, 1]),
        ([0, -1, 2], [0, -1, 2]),
    ]
    for arr, expected in tests_10:
        result = exercise_10_sort_by_abs(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} sort_by_abs({arr}) = {result}")
    
    # Test Exercise 11: Counting Sort
    print("\nExercise 11: Counting Sort")
    tests_11 = [
        ([4, 2, 2, 8, 3, 3, 1], [1, 2, 2, 3, 3, 4, 8]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ]
    for arr, expected in tests_11:
        result = exercise_11_counting_sort(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} counting_sort({arr}) = {result}")
    
    # Test Exercise 12: One Swap Sort
    print("\nExercise 12: One Swap Sort")
    tests_12 = [
        ([1, 3, 2], True),
        ([3, 2, 1], False),
        ([1, 2, 3], True),
        ([1, 5, 3, 4, 2], True),  # Swap 5 and 2
        ([5, 4, 3, 2, 1], False),
    ]
    for arr, expected in tests_12:
        result = exercise_12_one_swap_sort(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} one_swap_sort({arr}) = {result} (expected {expected})")
    
    # Test Bonus: Heap Sort
    print("\nBonus: Heap Sort")
    tests_bonus = [
        ([12, 11, 13, 5, 6, 7], [5, 6, 7, 11, 12, 13]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
    ]
    for arr, expected in tests_bonus:
        result = bonus_heap_sort(arr)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} heap_sort({arr}) = {result}")
    
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

# Exercise 1: Bubble Sort
def exercise_1_bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Exercise 2: Selection Sort
def exercise_2_selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Exercise 3: Insertion Sort
def exercise_3_insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Exercise 4: Merge Sort
def exercise_4_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = exercise_4_merge_sort(arr[:mid])
    right = exercise_4_merge_sort(arr[mid:])
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

# Exercise 5: Quick Sort
def exercise_5_quick_sort(arr):
    arr = arr.copy()
    def quick_sort_helper(arr, low, high):
        if low < high:
            pivot_idx = partition(arr, low, high)
            quick_sort_helper(arr, low, pivot_idx - 1)
            quick_sort_helper(arr, pivot_idx + 1, high)
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    if arr:
        quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

# Exercise 6: Sort Colors
def exercise_6_sort_colors(nums):
    nums = nums.copy()
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

# Exercise 7: Merge Sorted Arrays
def exercise_7_merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

# Exercise 8: Sort by Frequency
def exercise_8_sort_by_frequency(arr):
    from collections import Counter
    count = Counter(arr)
    # Sort by negative frequency (descending), then by first occurrence
    order = {v: i for i, v in enumerate(arr)}
    return sorted(arr, key=lambda x: (-count[x], order[x]))

# Exercise 9: Kth Largest
def exercise_9_kth_largest(arr, k):
    return sorted(arr, reverse=True)[k - 1]

# Exercise 10: Sort by Absolute Value
def exercise_10_sort_by_abs(arr):
    return sorted(arr, key=lambda x: (abs(x), x >= 0))

# Exercise 11: Counting Sort
def exercise_11_counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    return result

# Exercise 12: One Swap Sort
def exercise_12_one_swap_sort(arr):
    sorted_arr = sorted(arr)
    diff = []
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            diff.append(i)
    if len(diff) == 0:
        return True
    if len(diff) == 2:
        arr[diff[0]], arr[diff[1]] = arr[diff[1]], arr[diff[0]]
        return arr == sorted_arr
    return False

# Bonus: Heap Sort
def bonus_heap_sort(arr):
    arr = arr.copy()
    n = len(arr)
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr
"""


if __name__ == "__main__":
    run_tests()
