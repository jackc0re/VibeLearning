# 📊 Sorting Algorithms

> Organizing data in a specific order

---

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [Simple Sorting Algorithms](#simple-sorting-algorithms)
   - [Bubble Sort](#bubble-sort)
   - [Selection Sort](#selection-sort)
   - [Insertion Sort](#insertion-sort)
3. [Efficient Sorting Algorithms](#efficient-sorting-algorithms)
   - [Merge Sort](#merge-sort)
   - [Quick Sort](#quick-sort)
4. [Comparison of Algorithms](#comparison-of-algorithms)
5. [Stability in Sorting](#stability-in-sorting)
6. [When to Use Each](#when-to-use-each)

---

## Introduction

Sorting is the process of arranging elements in a specific order (usually ascending or descending). It's one of the most studied problems in computer science because:

- Many algorithms require sorted data as input
- Sorting enables efficient searching (binary search)
- Understanding sorting teaches fundamental algorithm design techniques

### Key Metrics

When evaluating sorting algorithms, we consider:

| Metric | Description |
|--------|-------------|
| **Time Complexity** | How many operations needed |
| **Space Complexity** | Extra memory required |
| **Stability** | Preserves order of equal elements |
| **Adaptivity** | Faster on partially sorted data |

---

## Simple Sorting Algorithms

These algorithms are easy to understand but have O(n²) time complexity.

### Bubble Sort

**Idea:** Repeatedly swap adjacent elements if they're in the wrong order.

```
Array: [5, 2, 8, 1, 9]

Pass 1: [2, 5, 1, 8, 9] — Largest (9) bubbles to the end
Pass 2: [2, 1, 5, 8, 9] — Second largest (8) in place
Pass 3: [1, 2, 5, 8, 9] — Third largest (5) in place
Pass 4: [1, 2, 5, 8, 9] — Array is sorted!
```

#### Implementation

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize: stop if no swaps occur
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

#### Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst | O(n²) | O(1) |

**Stable:** Yes  
**Best used:** Educational purposes, detecting if array is sorted

---

### Selection Sort

**Idea:** Find the minimum element and place it at the beginning. Repeat for remaining elements.

```
Array: [64, 25, 12, 22, 11]

Pass 1: Find min (11), swap with first → [11, 25, 12, 22, 64]
Pass 2: Find min in rest (12), swap → [11, 12, 25, 22, 64]
Pass 3: Find min in rest (22), swap → [11, 12, 22, 25, 64]
Pass 4: Find min in rest (25), swap → [11, 12, 22, 25, 64]
```

#### Implementation

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find minimum element in remaining array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap minimum with first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

#### Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n²) | O(1) |
| Average | O(n²) | O(1) |
| Worst | O(n²) | O(1) |

**Stable:** No (can be made stable with modification)  
**Best used:** When memory writes are expensive (always n swaps)

---

### Insertion Sort

**Idea:** Build sorted array one element at a time, inserting each element into its correct position.

```
Array: [5, 2, 8, 1, 9]

Start: [5] | 2, 8, 1, 9
Insert 2: [2, 5] | 8, 1, 9
Insert 8: [2, 5, 8] | 1, 9
Insert 1: [1, 2, 5, 8] | 9
Insert 9: [1, 2, 5, 8, 9]
```

#### Implementation

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

#### Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst | O(n²) | O(1) |

**Stable:** Yes  
**Best used:** Small arrays, nearly sorted data, online sorting (streaming data)

---

## Efficient Sorting Algorithms

These algorithms achieve O(n log n) time complexity.

### Merge Sort

**Idea:** Divide the array in half, sort each half, then merge them.

```
Array: [38, 27, 43, 3, 9, 82, 10]

Divide: [38, 27, 43, 3] | [9, 82, 10]
        [38, 27] [43, 3] | [9, 82] [10]
        [38] [27] [43] [3] | [9] [82] [10]

Merge:  [27, 38] [3, 43] | [9, 82] [10]
        [3, 27, 38, 43] | [9, 10, 82]
        [3, 9, 10, 27, 38, 43, 82]
```

#### Implementation

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge
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
```

#### Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n log n) | O(n) |
| Average | O(n log n) | O(n) |
| Worst | O(n log n) | O(n) |

**Stable:** Yes  
**Best used:** Linked lists, external sorting (large files), when stability matters

---

### Quick Sort

**Idea:** Pick a pivot, partition array around it, recursively sort partitions.

```
Array: [10, 7, 8, 9, 1, 5]
Pivot: 5

Partition: [1, 5, 8, 9, 7, 10]  (elements < 5 on left, > 5 on right)
           ^pivot at correct position

Recursively sort [1] and [8, 9, 7, 10]
```

#### Implementation

```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition and get pivot index
        pivot_idx = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

#### Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n log n) | O(log n) |
| Average | O(n log n) | O(log n) |
| Worst | O(n²) | O(n) |

**Stable:** No  
**Best used:** General purpose, in-memory sorting, when average case matters

---

## Comparison of Algorithms

### Time Complexity

| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

### Space Complexity

| Algorithm | Space |
|-----------|-------|
| Bubble Sort | O(1) |
| Selection Sort | O(1) |
| Insertion Sort | O(1) |
| Merge Sort | O(n) |
| Quick Sort | O(log n) average, O(n) worst |

### Visual Comparison

```
Speed for n=1000 random elements:

Bubble Sort:    ████████████████████████████████████████ (slow)
Selection Sort: ████████████████████████████████████████ (slow)
Insertion Sort: ████████████████████████████ (medium, depends on data)
Merge Sort:     ████ (fast)
Quick Sort:     ███ (fast, usually fastest)
```

---

## Stability in Sorting

A sorting algorithm is **stable** if it preserves the relative order of equal elements.

### Example

Original: `[(A, 3), (B, 1), (C, 3), (D, 2)]`  
Sort by number:

**Stable result:** `[(B, 1), (D, 2), (A, 3), (C, 3)]`  
(A comes before C because it was first originally)

**Unstable result:** `[(B, 1), (D, 2), (C, 3), (A, 3)]`  
(C might come before A)

### Why Stability Matters

- Sorting by multiple keys (sort by name, then by age)
- Preserving original order when values are equal
- Database operations

### Stability Summary

| Algorithm | Stable? |
|-----------|---------|
| Bubble Sort | ✅ Yes |
| Selection Sort | ❌ No |
| Insertion Sort | ✅ Yes |
| Merge Sort | ✅ Yes |
| Quick Sort | ❌ No |

---

## When to Use Each

### Bubble Sort
- ❌ Almost never in production
- ✅ Educational purposes
- ✅ Detecting if array is already sorted

### Selection Sort
- ✅ When memory writes are costly
- ✅ Small arrays
- ❌ Large datasets

### Insertion Sort
- ✅ Small arrays (n < 50)
- ✅ Nearly sorted data
- ✅ Online sorting (streaming data)
- ✅ As a subroutine in hybrid algorithms

### Merge Sort
- ✅ Linked lists (no random access needed)
- ✅ External sorting (data too large for memory)
- ✅ When stable sorting is required
- ✅ When guaranteed O(n log n) is needed

### Quick Sort
- ✅ General purpose in-memory sorting
- ✅ When average case performance matters
- ✅ When space is limited (in-place)
- ❌ When worst case must be avoided (use merge sort)

---

## Python's Built-in Sorting

Python uses **Timsort**, a hybrid of merge sort and insertion sort:

```python
# Sort in place
arr.sort()

# Return new sorted list
sorted_arr = sorted(arr)

# Custom key function
arr.sort(key=lambda x: x[1])

# Reverse order
arr.sort(reverse=True)
```

Timsort is:
- O(n log n) worst case
- O(n) best case (nearly sorted data)
- Stable
- Adaptive (takes advantage of existing order)

---

## 🔑 Key Takeaways

1. **Simple sorts (O(n²))**: Bubble, Selection, Insertion — use for small data
2. **Efficient sorts (O(n log n))**: Merge, Quick — use for large data
3. **Stability matters** when order of equals is important
4. **Quick Sort** is usually fastest in practice
5. **Merge Sort** has guaranteed O(n log n) and is stable
6. **Use Python's built-in** `sort()` for production code

---

## 🔗 Next Steps

- Practice with [`exercises.py`](exercises.py)
- Test your knowledge with [`quiz.md`](quiz.md)
- Move on to [03_recursion](../03_recursion/)
