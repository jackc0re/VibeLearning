# Algorithms Cheatsheet

Quick reference for algorithms: Big O notation, searching, sorting, recursion, and dynamic programming.

---

## Big O Notation

### Complexity Classes

| Notation | Name | Example | Description |
|-----------|------|---------|-------------|
| **O(1)** | Constant | Array access | Same time regardless of input |
| **O(log n)** | Logarithmic | Binary search | Cuts input in half each step |
| **O(n)** | Linear | Linear search | Directly proportional to input |
| **O(n log n)** | Linearithmic | Merge sort | Slightly slower than linear |
| **O(n²)** | Quadratic | Bubble sort | Nested loops |
| **O(2ⁿ)** | Exponential | Recursive Fibonacci | Doubles each step |
| **O(n!)** | Factorial | Permutations | Extremely slow |

### Visual Comparison

```
O(1)       →  ——————————— (constant)
O(log n)    →  ———————————— (very slow growth)
O(n)        →  ——————— (linear growth)
O(n log n)  →  ——————— (slightly steeper)
O(n²)       →  ——— (steep curve)
O(2ⁿ)       →  | (extremely steep)
O(n!)       →  / (almost vertical)
```

### Common Operations Complexity

| Operation | List | Dict | Set |
|----------|------|------|-----|
| **Access** | O(1) | O(1) | - |
| **Search** | O(n) | O(1) | O(1) |
| **Insert** | O(1)* | O(1) | O(1) |
| **Delete** | O(n)* | O(1) | O(1) |

*End of list, otherwise O(n)

---

## Searching Algorithms

### Linear Search
```python
def linear_search(arr, target):
    """Search array element by element. O(n)"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Usage
numbers = [1, 5, 3, 9, 7]
index = linear_search(numbers, 9)  # Returns 3
```

### Binary Search
```python
def binary_search(arr, target):
    """Search sorted array. O(log n)"""
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

# Usage (array must be sorted)
numbers = [1, 3, 5, 7, 9]
index = binary_search(numbers, 7)  # Returns 3
```

### Built-in Search
```python
numbers = [1, 3, 5, 7, 9]

# Check membership (linear search)
9 in numbers  # True

# Find index (linear search)
numbers.index(7)  # 3

# Sort then binary search (better for repeated searches)
numbers.sort()
index = bisect.bisect_left(numbers, 7)  # Requires import bisect
```

---

## Sorting Algorithms

### Bubble Sort
```python
def bubble_sort(arr):
    """Simple but slow. O(n²)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### Selection Sort
```python
def selection_sort(arr):
    """Find minimum repeatedly. O(n²)"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### Insertion Sort
```python
def insertion_sort(arr):
    """Build sorted portion. O(n²)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### Merge Sort
```python
def merge_sort(arr):
    """Divide and conquer. O(n log n)"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Quick Sort
```python
def quick_sort(arr):
    """Divide and conquer. O(n log n) average, O(n²) worst"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
```

### Built-in Sort (Python's Timsort)
```python
numbers = [5, 2, 8, 1, 9]

# Sort in place (modifies original)
numbers.sort()  # [1, 2, 5, 8, 9]

# Sort and return new list
sorted_numbers = sorted(numbers)

# Sort with custom key
names = ["Alice", "Bob", "Charlie"]
names.sort(key=len)  # ["Bob", "Alice", "Charlie"]

# Reverse sort
numbers.sort(reverse=True)  # [9, 8, 5, 2, 1]
```

### Sorting Comparison

| Algorithm | Best | Average | Worst | Space | When to Use |
|-----------|------|---------|-------|-------|-------------|
| **Bubble** | O(n) | O(n²) | O(n²) | O(1) | Never (educational) |
| **Selection** | O(n²) | O(n²) | O(n²) | O(1) | Small datasets |
| **Insertion** | O(n) | O(n²) | O(n²) | O(1) | Nearly sorted |
| **Merge** | O(n log n) | O(n log n) | O(n log n) | O(n) | Large datasets |
| **Quick** | O(n log n) | O(n log n) | O(n²) | O(log n) | General purpose |
| **Timsort** | O(n) | O(n log n) | O(n log n) | O(n) | Use Python's built-in |

---

## Recursion

### Basic Recursion
```python
def factorial(n):
    """Base case: n <= 1, Recursive case: n * factorial(n-1)"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### Fibonacci
```python
def fibonacci(n):
    """O(2ⁿ) - exponential (very slow)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Optimized with memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    """O(n) - linear (fast!)"""
    if n <= 1:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
```

### Binary Tree Traversal
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    """Left -> Root -> Right"""
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    """Root -> Left -> Right"""
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    """Left -> Right -> Root"""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
```

---

## Dynamic Programming

### Memoization (Top-Down)
```python
from functools import lru_cache

def fibonacci(n):
    """Store results to avoid redundant calculations."""
    @lru_cache(maxsize=None)
    def fib_helper(n):
        if n <= 1:
            return n
        return fib_helper(n - 1) + fib_helper(n - 2)
    return fib_helper(n)
```

### Tabulation (Bottom-Up)
```python
def fibonacci(n):
    """Build table iteratively."""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

### Climbing Stairs
```python
def climb_stairs(n):
    """Ways to reach top taking 1 or 2 steps at a time."""
    if n <= 2:
        return n

    prev1, prev2 = 2, 1
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
```

---

## Graph Algorithms

### Breadth-First Search (BFS)
```python
from collections import deque

def bfs(graph, start):
    """Visit nodes level by level. O(V + E)"""
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)  # Process node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Depth-First Search (DFS)
```python
def dfs(graph, start, visited=None):
    """Explore deep before wide. O(V + E)"""
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)  # Process node

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

---

## Utility Functions

### Built-in Algorithms

```python
# Maximum/Minimum
max([1, 5, 3])         # 5
min([1, 5, 3])         # 1

# Sum
sum([1, 2, 3, 4])      # 10

# Reversed
list(reversed([1, 2, 3])) # [3, 2, 1]

# Sorted
sorted([3, 1, 4, 2])   # [1, 2, 3, 4]

# Count
[1, 2, 2, 3].count(2)  # 2

# Find
[1, 2, 3].index(2)     # 1
```

### itertools Utilities
```python
from itertools import combinations, permutations, product

# Combinations (order doesn't matter)
list(combinations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 3)]

# Permutations (order matters)
list(permutations([1, 2, 3], 2))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Product (Cartesian product)
list(product([1, 2], [3, 4]))
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```

---

## Optimization Tips

### Use Built-ins
```python
# Bad (slow)
result = []
for x in range(1000):
    result.append(x * 2)

# Good (fast)
result = [x * 2 for x in range(1000)]

# Best (fastest for simple operations)
result = list(map(lambda x: x * 2, range(1000)))
```

### Choose Right Data Structure
```python
# Bad (O(n) lookup)
my_list = ["apple", "banana", "cherry"]
if "banana" in my_list:  # O(n)
    pass

# Good (O(1) lookup)
my_set = {"apple", "banana", "cherry"}
if "banana" in my_set:  # O(1)
    pass
```

### Avoid Nested Loops
```python
# Bad (O(n²))
result = []
for i in range(1000):
    for j in range(1000):
        result.append(i * j)

# Good (O(n))
result = [i * j for i in range(1000) for j in range(1000)]
```

---

## Quick Reference

| Algorithm | Complexity | Use Case |
|-----------|-------------|----------|
| **Linear Search** | O(n) | Unsorted array |
| **Binary Search** | O(log n) | Sorted array |
| **Bubble Sort** | O(n²) | Educational only |
| **Merge Sort** | O(n log n) | Large datasets |
| **Quick Sort** | O(n log n) avg | General purpose |
| **Python Sort** | O(n log n) | Always preferred |
| **BFS** | O(V + E) | Shortest path (unweighted) |
| **DFS** | O(V + E) | Path finding, topological |
| **Fibonacci** | O(2ⁿ) → O(n) | Recursive, add memoization |

---

**Back to [Resources](../README.md)**
