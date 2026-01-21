# ⚔️ Divide and Conquer

> Breaking big problems into smaller, independent subproblems

---

## 📋 Table of Contents

1. [What is Divide and Conquer?](#what-is-divide-and-conquer)
2. [The Three Steps](#the-three-steps)
3. [Classic Examples](#classic-examples)
4. [Master Theorem](#master-theorem)
5. [Comparison with DP](#comparison-with-dp)
6. [When to Use](#when-to-use)

---

## What is Divide and Conquer?

Divide and Conquer (D&C) is an algorithm design paradigm that:

1. **Divides** the problem into smaller subproblems
2. **Conquers** each subproblem recursively
3. **Combines** the solutions to solve the original problem

> "The whole is equal to the sum of its parts." — But we solve the parts first!

### Visual Example: Merge Sort

```
Original:    [38, 27, 43, 3, 9, 82, 10]
                        |
              ┌─────────┴─────────┐
         DIVIDE                DIVIDE
              |                    |
         [38, 27, 43, 3]    [9, 82, 10]
              |                    |
        ┌─────┴─────┐        ┌─────┴─────┐
    [38, 27]    [43, 3]   [9, 82]    [10]
        |          |          |         |
      ┌─┴─┐      ┌─┴─┐      ┌─┴─┐       |
    [38] [27]  [43] [3]   [9] [82]    [10]
      |          |          |         |
    CONQUER & COMBINE (merge)
      |          |          |         |
    [27, 38]  [3, 43]   [9, 82]    [10]
        |          |          |         |
        └────┬─────┘          └────┬────┘
        [3, 27, 38, 43]      [9, 10, 82]
              |                    |
              └────────┬───────────┘
                       |
          [3, 9, 10, 27, 38, 43, 82]
```

---

## The Three Steps

### 1. Divide

Split the problem into smaller subproblems of the same type.

```python
# Divide array into two halves
mid = len(arr) // 2
left = arr[:mid]
right = arr[mid:]
```

### 2. Conquer

Solve each subproblem recursively. Base case: solve directly when small enough.

```python
# Conquer: recursively sort each half
left_sorted = merge_sort(left)
right_sorted = merge_sort(right)
```

### 3. Combine

Merge the solutions of subproblems to solve the original problem.

```python
# Combine: merge sorted halves
return merge(left_sorted, right_sorted)
```

---

## Classic Examples

### 1. Merge Sort

```python
def merge_sort(arr):
    """
    Sort array using Divide and Conquer.
    
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
    
    # Combine (merge)
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays."""
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

### 2. Quick Sort

```python
def quick_sort(arr):
    """
    Sort array using Divide and Conquer with partitioning.
    
    Time: O(n log n) average, O(n²) worst
    Space: O(log n)
    """
    if len(arr) <= 1:
        return arr
    
    # Divide: partition around pivot
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Conquer & Combine
    return quick_sort(left) + middle + quick_sort(right)
```

### 3. Binary Search

```python
def binary_search(arr, target, left=0, right=None):
    """
    Search using Divide and Conquer.
    
    Time: O(log n)
    Space: O(log n) recursive, O(1) iterative
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: not found
    if left > right:
        return -1
    
    # Divide: find middle
    mid = (left + right) // 2
    
    # Conquer: search appropriate half
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
```

### 4. Maximum Subarray (D&C Approach)

```python
def max_subarray_dc(arr):
    """
    Find maximum subarray sum using Divide and Conquer.
    
    Time: O(n log n)
    """
    def helper(arr, left, right):
        # Base case
        if left == right:
            return arr[left]
        
        mid = (left + right) // 2
        
        # Conquer: max in left half, right half
        left_max = helper(arr, left, mid)
        right_max = helper(arr, mid + 1, right)
        
        # Combine: max crossing middle
        cross_max = max_crossing_sum(arr, left, mid, right)
        
        return max(left_max, right_max, cross_max)
    
    def max_crossing_sum(arr, left, mid, right):
        # Find max sum ending at mid
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += arr[i]
            left_sum = max(left_sum, curr_sum)
        
        # Find max sum starting at mid+1
        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += arr[i]
            right_sum = max(right_sum, curr_sum)
        
        return left_sum + right_sum
    
    return helper(arr, 0, len(arr) - 1)
```

### 5. Counting Inversions

```python
def count_inversions(arr):
    """
    Count pairs (i, j) where i < j but arr[i] > arr[j].
    
    Modified merge sort: count splits during merge.
    
    Time: O(n log n)
    """
    def merge_count(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, left_inv = merge_count(arr[:mid])
        right, right_inv = merge_count(arr[mid:])
        
        merged, split_inv = merge_and_count(left, right)
        
        return merged, left_inv + right_inv + split_inv
    
    def merge_and_count(left, right):
        result = []
        inversions = 0
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                # All remaining elements in left are greater than right[j]
                inversions += len(left) - i
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inversions
    
    _, total = merge_count(arr)
    return total
```

### 6. Power Function (Fast Exponentiation)

```python
def power(x, n):
    """
    Calculate x^n using Divide and Conquer.
    
    Time: O(log n)
    
    Key insight: x^n = (x^(n/2))^2 for even n
                 x^n = x * (x^(n/2))^2 for odd n
    """
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    
    half = power(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half
```

### 7. Closest Pair of Points

```python
import math

def closest_pair(points):
    """
    Find two closest points in 2D plane.
    
    Time: O(n log n)
    
    Better than brute force O(n²).
    """
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def brute_force(pts):
        min_dist = float('inf')
        n = len(pts)
        for i in range(n):
            for j in range(i + 1, n):
                min_dist = min(min_dist, distance(pts[i], pts[j]))
        return min_dist
    
    def strip_closest(strip, d):
        min_dist = d
        strip.sort(key=lambda p: p[1])  # Sort by y
        
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and strip[j][1] - strip[i][1] < min_dist:
                min_dist = min(min_dist, distance(strip[i], strip[j]))
                j += 1
        
        return min_dist
    
    def closest_util(pts_x):
        n = len(pts_x)
        
        # Base case: brute force for small inputs
        if n <= 3:
            return brute_force(pts_x)
        
        mid = n // 2
        mid_point = pts_x[mid]
        
        # Divide
        left = pts_x[:mid]
        right = pts_x[mid:]
        
        # Conquer
        dl = closest_util(left)
        dr = closest_util(right)
        d = min(dl, dr)
        
        # Combine: check strip around middle
        strip = [p for p in pts_x if abs(p[0] - mid_point[0]) < d]
        
        return min(d, strip_closest(strip, d))
    
    # Sort by x-coordinate
    points_sorted = sorted(points, key=lambda p: p[0])
    return closest_util(points_sorted)
```

---

## Master Theorem

The Master Theorem helps analyze D&C recurrences of the form:

```
T(n) = aT(n/b) + f(n)
```

Where:
- `a` = number of subproblems
- `b` = factor by which input size shrinks
- `f(n)` = cost of dividing and combining

### Three Cases

| Case | Condition | Complexity |
|------|-----------|------------|
| 1 | f(n) < n^(log_b(a)) | O(n^(log_b(a))) |
| 2 | f(n) = n^(log_b(a)) | O(n^(log_b(a)) × log n) |
| 3 | f(n) > n^(log_b(a)) | O(f(n)) |

### Examples

**Merge Sort:** T(n) = 2T(n/2) + O(n)
- a=2, b=2, f(n)=n
- n^(log₂2) = n¹ = n
- f(n) = n = n^(log_b(a)) → Case 2
- T(n) = **O(n log n)**

**Binary Search:** T(n) = T(n/2) + O(1)
- a=1, b=2, f(n)=1
- n^(log₂1) = n⁰ = 1
- f(n) = 1 = n^(log_b(a)) → Case 2
- T(n) = **O(log n)**

---

## Comparison with DP

| Aspect | Divide & Conquer | Dynamic Programming |
|--------|------------------|---------------------|
| Subproblems | Independent | Overlapping |
| Approach | Top-down, divide first | Bottom-up or memoized |
| Redundancy | No repeated work | Avoids repeated work |
| Examples | Merge sort, Quick sort, Binary search | Fibonacci, Knapsack, LCS |

### When Subproblems Overlap

If subproblems overlap, D&C becomes inefficient:

```
Fibonacci (D&C without memo):
fib(5) splits into fib(4) and fib(3)
fib(4) splits into fib(3) and fib(2)  ← fib(3) calculated twice!
```

In such cases, use DP with memoization.

---

## When to Use

### ✅ Use Divide and Conquer When:

1. **Problem naturally divides** into independent parts
2. **Subproblems don't overlap** (or you'll use DP)
3. **Combining is efficient** (not too expensive)
4. **Recursive structure** is clear
5. Problem follows: **T(n) = aT(n/b) + f(n)**

### Common D&C Problems

- Sorting (Merge Sort, Quick Sort)
- Searching (Binary Search)
- Matrix multiplication (Strassen's)
- Closest pair of points
- Fast Fourier Transform
- Counting inversions
- Finding median

---

## 🔑 Key Takeaways

1. **Three steps**: Divide → Conquer → Combine
2. **Independent subproblems** — no overlap (unlike DP)
3. **Typically O(n log n)** complexity
4. **Master Theorem** for complexity analysis
5. **Classic examples**: Merge Sort, Quick Sort, Binary Search
6. **Base case** must be simple to solve directly

---

## 🔗 Next Steps

- Practice with [`exercises.py`](exercises.py)
- Test your knowledge with [`quiz.md`](quiz.md)
- Move on to [07_graph_algorithms](../07_graph_algorithms/)
