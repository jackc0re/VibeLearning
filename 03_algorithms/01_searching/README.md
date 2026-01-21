# 🔍 Searching Algorithms

> Finding elements in collections efficiently

---

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Linear Search](#linear-search)
3. [Binary Search](#binary-search)
4. [Comparison](#comparison)
5. [When to Use Each](#when-to-use-each)
6. [Common Variations](#common-variations)

---

## Introduction

Searching is one of the most fundamental operations in programming. Given a collection of items, we need to find whether a specific item exists and where it's located.

**The Two Main Approaches:**
- **Linear Search** — Check every element one by one
- **Binary Search** — Divide and conquer on sorted data

---

## Linear Search

### How It Works

Linear search (or sequential search) examines each element from start to finish until it finds the target or reaches the end.

```
Array: [4, 2, 7, 1, 9, 3]
Target: 7

Step 1: Check index 0 → 4 ≠ 7, continue
Step 2: Check index 1 → 2 ≠ 7, continue
Step 3: Check index 2 → 7 = 7, FOUND at index 2!
```

### Implementation

```python
def linear_search(arr, target):
    """
    Search for target in arr using linear search.
    
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
```

### Complexity Analysis

| Case | Time Complexity | When |
|------|-----------------|------|
| Best | O(1) | Target is first element |
| Average | O(n/2) → O(n) | Target is in the middle |
| Worst | O(n) | Target is last or not present |

**Space Complexity:** O(1) — only uses a few variables

### Pros and Cons

✅ **Advantages:**
- Works on unsorted data
- Simple to implement
- No preprocessing required
- Works on any data structure (arrays, linked lists)

❌ **Disadvantages:**
- Slow for large datasets
- Checks every element in worst case

---

## Binary Search

### How It Works

Binary search works on **sorted arrays** by repeatedly dividing the search space in half.

```
Sorted Array: [1, 2, 3, 4, 7, 9, 11, 15]
Target: 9

Step 1: mid = 4 (value 7) → 9 > 7, search right half
        [-, -, -, -, -, 9, 11, 15]
        
Step 2: mid = 6 (value 11) → 9 < 11, search left half
        [-, -, -, -, -, 9, -, -]
        
Step 3: mid = 5 (value 9) → 9 = 9, FOUND at index 5!
```

### Implementation (Iterative)

```python
def binary_search(arr, target):
    """
    Search for target in sorted arr using binary search.
    
    Args:
        arr: Sorted list of elements
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
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
            
    return -1
```

### Implementation (Recursive)

```python
def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive binary search implementation.
    """
    if right is None:
        right = len(arr) - 1
        
    if left > right:
        return -1
        
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

### Complexity Analysis

| Case | Time Complexity | When |
|------|-----------------|------|
| Best | O(1) | Target is at middle |
| Average | O(log n) | General case |
| Worst | O(log n) | Target at end or not present |

**Space Complexity:**
- Iterative: O(1)
- Recursive: O(log n) due to call stack

### Why O(log n)?

Each step cuts the search space in half:
- n → n/2 → n/4 → n/8 → ... → 1

The number of steps: `log₂(n)`

For n = 1,000,000:
- Linear: up to 1,000,000 comparisons
- Binary: up to 20 comparisons (log₂(1,000,000) ≈ 20)

### Pros and Cons

✅ **Advantages:**
- Very fast for large datasets
- Efficient O(log n) time

❌ **Disadvantages:**
- Requires sorted data
- Only works with random access (arrays, not linked lists)
- Sorting cost if data isn't already sorted

---

## Comparison

| Feature | Linear Search | Binary Search |
|---------|---------------|---------------|
| Time Complexity | O(n) | O(log n) |
| Space Complexity | O(1) | O(1) iterative, O(log n) recursive |
| Requires Sorted Data | No | Yes |
| Works on Linked Lists | Yes | Inefficient |
| Implementation | Simple | Moderate |

### Visual Comparison

```
Array size: 1,000,000 elements

Linear Search (worst case):
[████████████████████████████████] 1,000,000 comparisons

Binary Search (worst case):
[█] 20 comparisons
```

---

## When to Use Each

### Use Linear Search When:

1. **Data is unsorted** and sorting would be expensive
2. **Small dataset** (< ~100 elements)
3. **Searching only once** (one-time search)
4. **Data structure doesn't support random access** (linked list)
5. **Looking for multiple occurrences**

### Use Binary Search When:

1. **Data is already sorted**
2. **Large dataset** where O(log n) matters
3. **Searching many times** (sorting cost amortized)
4. **Data is in an array** or supports random access
5. **Memory is limited** (iterative version)

---

## Common Variations

### 1. Find First Occurrence

```python
def find_first(arr, target):
    """Find the first occurrence of target in sorted array."""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid  # Found, but keep looking left
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result
```

### 2. Find Last Occurrence

```python
def find_last(arr, target):
    """Find the last occurrence of target in sorted array."""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid  # Found, but keep looking right
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result
```

### 3. Find Insert Position

```python
def find_insert_position(arr, target):
    """Find where target should be inserted to maintain sorted order."""
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left
```

### 4. Search in Rotated Sorted Array

```python
def search_rotated(arr, target):
    """Search in a rotated sorted array like [4,5,6,7,0,1,2]."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
            
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1
```

---

## 🔑 Key Takeaways

1. **Linear search** is simple but slow — O(n)
2. **Binary search** is fast but requires sorted data — O(log n)
3. **Choose based on context**: data size, whether sorted, search frequency
4. **Binary search variations** solve many related problems
5. **Off-by-one errors** are common in binary search — test edge cases!

---

## 📚 Python Built-in Tools

Python provides built-in searching capabilities:

```python
# Using 'in' operator (linear search)
if target in my_list:
    print("Found!")

# Using list.index() (linear search)
index = my_list.index(target)  # Raises ValueError if not found

# Using bisect module (binary search)
import bisect
index = bisect.bisect_left(sorted_list, target)
```

---

## 🔗 Next Steps

- Practice with [`exercises.py`](exercises.py)
- Test your knowledge with [`quiz.md`](quiz.md)
- Move on to [02_sorting](../02_sorting/)
