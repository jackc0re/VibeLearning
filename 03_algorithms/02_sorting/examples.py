"""
Sorting Algorithms - Examples

This file demonstrates various sorting algorithms with
clear explanations and visualizations.

Run this file to see the examples in action:
    python examples.py
"""

import random
import time


# =============================================================================
# BUBBLE SORT
# =============================================================================

def bubble_sort(arr):
    """
    Bubble Sort - repeatedly swap adjacent elements if in wrong order.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    """
    arr = arr.copy()  # Don't modify original
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


def bubble_sort_visualized(arr):
    """Bubble sort with step-by-step visualization."""
    arr = arr.copy()
    n = len(arr)
    
    print(f"Initial array: {arr}")
    print("-" * 40)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        sorted_part = arr[n - i - 1:]
        unsorted_part = arr[:n - i - 1]
        print(f"Pass {i + 1}: {unsorted_part} | {sorted_part}")
        
        if not swapped:
            print("No swaps - array is sorted!")
            break
    
    return arr


# =============================================================================
# SELECTION SORT
# =============================================================================

def selection_sort(arr):
    """
    Selection Sort - find minimum and place at beginning, repeat.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: No
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def selection_sort_visualized(arr):
    """Selection sort with step-by-step visualization."""
    arr = arr.copy()
    n = len(arr)
    
    print(f"Initial array: {arr}")
    print("-" * 40)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        print(f"Pass {i + 1}: Found minimum {arr[min_idx]} at index {min_idx}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        sorted_part = arr[:i + 1]
        unsorted_part = arr[i + 1:]
        print(f"         {sorted_part} | {unsorted_part}")
    
    return arr


# =============================================================================
# INSERTION SORT
# =============================================================================

def insertion_sort(arr):
    """
    Insertion Sort - build sorted array one element at a time.
    
    Time Complexity: O(n²), O(n) for nearly sorted
    Space Complexity: O(1)
    Stable: Yes
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr


def insertion_sort_visualized(arr):
    """Insertion sort with step-by-step visualization."""
    arr = arr.copy()
    
    print(f"Initial array: {arr}")
    print("-" * 40)
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        print(f"Pass {i}: Insert {key}")
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
        sorted_part = arr[:i + 1]
        unsorted_part = arr[i + 1:]
        print(f"         {sorted_part} | {unsorted_part}")
    
    return arr


# =============================================================================
# MERGE SORT
# =============================================================================

def merge_sort(arr):
    """
    Merge Sort - divide array in half, sort each half, merge.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Stable: Yes
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
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
    """Merge sort with visualization of divide and conquer."""
    indent = "  " * depth
    print(f"{indent}merge_sort({arr})")
    
    if len(arr) <= 1:
        print(f"{indent}  → base case, return {arr}")
        return arr
    
    mid = len(arr) // 2
    print(f"{indent}  Divide: {arr[:mid]} | {arr[mid:]}")
    
    left = merge_sort_visualized(arr[:mid], depth + 1)
    right = merge_sort_visualized(arr[mid:], depth + 1)
    
    result = merge(left, right)
    print(f"{indent}  Merge {left} + {right} → {result}")
    
    return result


# =============================================================================
# QUICK SORT
# =============================================================================

def quick_sort(arr):
    """
    Quick Sort - pick pivot, partition around it, recursively sort.
    
    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
    Stable: No
    """
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr, low, high):
    """Helper function for quick sort."""
    if low < high:
        pivot_idx = partition(arr, low, high)
        _quick_sort_helper(arr, low, pivot_idx - 1)
        _quick_sort_helper(arr, pivot_idx + 1, high)


def partition(arr, low, high):
    """Partition array around pivot (last element)."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_visualized(arr, depth=0, low=None, high=None):
    """Quick sort with visualization."""
    if low is None:
        arr = arr.copy()
        print(f"Initial array: {arr}")
        print("-" * 40)
        low = 0
        high = len(arr) - 1
    
    indent = "  " * depth
    
    if low < high:
        pivot = arr[high]
        print(f"{indent}Partitioning {arr[low:high+1]} with pivot={pivot}")
        
        pivot_idx = partition(arr, low, high)
        
        print(f"{indent}After partition: {arr[low:pivot_idx]} [{arr[pivot_idx]}] {arr[pivot_idx+1:high+1]}")
        
        quick_sort_visualized(arr, depth + 1, low, pivot_idx - 1)
        quick_sort_visualized(arr, depth + 1, pivot_idx + 1, high)
    
    return arr


# =============================================================================
# ADDITIONAL SORTING ALGORITHMS
# =============================================================================

def counting_sort(arr, max_val=None):
    """
    Counting Sort - count occurrences, reconstruct sorted array.
    
    Time Complexity: O(n + k) where k is range of values
    Space Complexity: O(k)
    Stable: Yes
    Works only for non-negative integers.
    """
    if not arr:
        return arr
    
    if max_val is None:
        max_val = max(arr)
    
    # Count occurrences
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    
    # Reconstruct sorted array
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    
    return result


def heap_sort(arr):
    """
    Heap Sort - build max heap, repeatedly extract maximum.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    Stable: No
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    """Heapify subtree rooted at index i."""
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


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_simple_sorts():
    """Demonstrate simple sorting algorithms."""
    print("=" * 60)
    print("SIMPLE SORTING ALGORITHMS (O(n²))")
    print("=" * 60)
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    # Bubble Sort
    print("\n1. BUBBLE SORT")
    print("   Idea: Repeatedly swap adjacent elements if in wrong order")
    bubble_sort_visualized(arr)
    
    # Selection Sort
    print("\n2. SELECTION SORT")
    print("   Idea: Find minimum, place at beginning, repeat")
    selection_sort_visualized(arr)
    
    # Insertion Sort
    print("\n3. INSERTION SORT")
    print("   Idea: Build sorted array one element at a time")
    insertion_sort_visualized(arr)


def demo_efficient_sorts():
    """Demonstrate efficient sorting algorithms."""
    print("\n" + "=" * 60)
    print("EFFICIENT SORTING ALGORITHMS (O(n log n))")
    print("=" * 60)
    
    arr = [38, 27, 43, 3, 9, 82, 10]
    
    # Merge Sort
    print("\n1. MERGE SORT")
    print("   Idea: Divide in half, sort each half, merge")
    print("-" * 40)
    merge_sort_visualized(arr)
    
    # Quick Sort
    print("\n2. QUICK SORT")
    print("   Idea: Pick pivot, partition around it, recurse")
    quick_sort_visualized(arr)


def demo_special_sorts():
    """Demonstrate special-purpose sorting algorithms."""
    print("\n" + "=" * 60)
    print("SPECIAL SORTING ALGORITHMS")
    print("=" * 60)
    
    # Counting Sort
    print("\n1. COUNTING SORT")
    print("   Idea: Count occurrences, reconstruct sorted array")
    print("   Time: O(n + k), but only works for integers")
    arr = [4, 2, 2, 8, 3, 3, 1]
    print(f"   Input:  {arr}")
    print(f"   Output: {counting_sort(arr)}")
    
    # Heap Sort
    print("\n2. HEAP SORT")
    print("   Idea: Build max heap, repeatedly extract maximum")
    print("   Time: O(n log n), in-place")
    arr = [12, 11, 13, 5, 6, 7]
    print(f"   Input:  {arr}")
    print(f"   Output: {heap_sort(arr)}")


def demo_stability():
    """Demonstrate stability in sorting."""
    print("\n" + "=" * 60)
    print("SORTING STABILITY DEMONSTRATION")
    print("=" * 60)
    
    # Create list of (name, score) tuples
    students = [
        ("Alice", 85),
        ("Bob", 90),
        ("Charlie", 85),
        ("Diana", 90),
        ("Eve", 85),
    ]
    
    print("\nOriginal order (note: Alice, Charlie, Eve all have 85):")
    for name, score in students:
        print(f"  {name}: {score}")
    
    # Stable sort (preserves original order for equal elements)
    stable_sorted = sorted(students, key=lambda x: x[1])
    print("\nStable sort by score (Python's built-in):")
    print("  Order of 85s preserved: Alice, Charlie, Eve")
    for name, score in stable_sorted:
        print(f"  {name}: {score}")
    
    # Demonstrate with insertion sort (stable)
    print("\nInsertion Sort is STABLE:")
    arr = [(3, 'a'), (1, 'b'), (2, 'c'), (1, 'd'), (3, 'e')]
    print(f"  Original: {arr}")
    
    # Sort by first element using insertion sort
    arr_copy = arr.copy()
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j][0] > key[0]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    
    print(f"  Sorted:   {arr_copy}")
    print("  Note: (1,'b') comes before (1,'d'), (3,'a') before (3,'e')")


def demo_performance_comparison():
    """Compare performance of different sorting algorithms."""
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    sizes = [100, 500, 1000]
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Python sorted()", sorted),
    ]
    
    for size in sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        print(f"\nArray size: {size}")
        print("-" * 40)
        
        for name, func in algorithms:
            # Skip slow algorithms for larger sizes
            if size > 500 and name in ["Bubble Sort", "Selection Sort"]:
                print(f"  {name}: Skipped (too slow)")
                continue
            
            arr_copy = arr.copy()
            start = time.perf_counter()
            func(arr_copy)
            elapsed = time.perf_counter() - start
            print(f"  {name}: {elapsed:.6f} seconds")


def demo_best_worst_cases():
    """Demonstrate best and worst cases for different algorithms."""
    print("\n" + "=" * 60)
    print("BEST AND WORST CASE SCENARIOS")
    print("=" * 60)
    
    size = 500
    
    # Already sorted array (best case for some, worst for others)
    sorted_arr = list(range(size))
    
    # Reverse sorted array (worst case for many)
    reverse_arr = list(range(size, 0, -1))
    
    # Random array (average case)
    random_arr = [random.randint(1, 1000) for _ in range(size)]
    
    scenarios = [
        ("Already Sorted", sorted_arr),
        ("Reverse Sorted", reverse_arr),
        ("Random", random_arr),
    ]
    
    algorithms = [
        ("Insertion Sort", insertion_sort),
        ("Quick Sort", quick_sort),
        ("Merge Sort", merge_sort),
    ]
    
    print(f"\nArray size: {size}")
    
    for scenario_name, arr in scenarios:
        print(f"\n{scenario_name} Array:")
        print("-" * 40)
        
        for alg_name, func in algorithms:
            arr_copy = arr.copy()
            start = time.perf_counter()
            func(arr_copy)
            elapsed = time.perf_counter() - start
            print(f"  {alg_name}: {elapsed:.6f} seconds")


def demo_sorting_objects():
    """Demonstrate sorting complex objects."""
    print("\n" + "=" * 60)
    print("SORTING COMPLEX OBJECTS")
    print("=" * 60)
    
    # List of dictionaries
    products = [
        {"name": "Laptop", "price": 999, "rating": 4.5},
        {"name": "Phone", "price": 699, "rating": 4.7},
        {"name": "Tablet", "price": 499, "rating": 4.3},
        {"name": "Watch", "price": 299, "rating": 4.8},
        {"name": "Earbuds", "price": 199, "rating": 4.4},
    ]
    
    print("\nOriginal products:")
    for p in products:
        print(f"  {p['name']}: ${p['price']}, Rating: {p['rating']}")
    
    # Sort by price (ascending)
    by_price = sorted(products, key=lambda x: x["price"])
    print("\nSorted by price (ascending):")
    for p in by_price:
        print(f"  {p['name']}: ${p['price']}")
    
    # Sort by rating (descending)
    by_rating = sorted(products, key=lambda x: x["rating"], reverse=True)
    print("\nSorted by rating (descending):")
    for p in by_rating:
        print(f"  {p['name']}: Rating {p['rating']}")
    
    # Sort by multiple criteria (price ascending, then rating descending)
    multi_sort = sorted(products, key=lambda x: (x["price"], -x["rating"]))
    print("\nSorted by price, then rating:")
    for p in multi_sort:
        print(f"  {p['name']}: ${p['price']}, Rating: {p['rating']}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    demo_simple_sorts()
    demo_efficient_sorts()
    demo_special_sorts()
    demo_stability()
    demo_performance_comparison()
    demo_best_worst_cases()
    demo_sorting_objects()
    
    print("\n" + "=" * 60)
    print("✓ All sorting examples completed!")
    print("=" * 60)
