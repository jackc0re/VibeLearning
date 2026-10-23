"""
Intermediate Exercise 3: Algorithms
===================================
Practice binary search, merge sort, quick sort, recursion,
and a first taste of dynamic programming.
"""

print("=" * 50)
print("EXERCISE 3: Algorithms")
print("=" * 50)


# =============================================================================
# EXERCISE 3.1: Binary Search
# =============================================================================
print("\n--- Exercise 3.1: Binary Search ---")
"""
Write binary_search(sorted_items, target) that:
- Assumes sorted_items is already sorted ascending
- Returns the index of target, or -1 if it is not present
- Runs in O(log n) by halving the search range each step
"""


# Your code below:
def binary_search(sorted_items, target):
    """Return the index of target, or -1 if not found."""
    pass


# Test (uncomment after implementing)
# data = [1, 3, 5, 7, 9, 11]
# print(binary_search(data, 7))   # 3
# print(binary_search(data, 4))   # -1


# =============================================================================
# EXERCISE 3.2: Merge Sort
# =============================================================================
print("\n--- Exercise 3.2: Merge Sort ---")
"""
Implement merge_sort(items) that:
- Returns a NEW sorted list (does not modify the input)
- Splits the list in half, sorts each half, then merges them
- Uses a helper _merge(left, right) that combines two sorted lists
"""


# Your code below:
def merge_sort(items):
    """Return a new sorted list using merge sort."""
    pass


# Test (uncomment after implementing)
# print(merge_sort([38, 27, 43, 3, 9, 82, 10]))


# =============================================================================
# EXERCISE 3.3: Quick Sort
# =============================================================================
print("\n--- Exercise 3.3: Quick Sort ---")
"""
Implement quick_sort(items) that:
- Picks a pivot, partitions the rest into smaller / equal / larger
- Recursively sorts the partitions and concatenates them
- Returns a NEW sorted list
"""


# Your code below:
def quick_sort(items):
    """Return a new sorted list using quicksort."""
    pass


# Test (uncomment after implementing)
# print(quick_sort([38, 27, 43, 3, 9, 82, 10]))


# =============================================================================
# EXERCISE 3.4: Recursion
# =============================================================================
print("\n--- Exercise 3.4: Recursion ---")
"""
Write flatten(nested) that takes a list which may contain numbers
or further nested lists (to any depth) and returns one flat list.

Example: [1, [2, [3, [4]], 5], [[6]]] -> [1, 2, 3, 4, 5, 6]
"""


# Your code below:
def flatten(nested):
    """Return a flat list from arbitrarily nested lists."""
    pass


# Test (uncomment after implementing)
# print(flatten([1, [2, [3, [4]], 5], [[6]]]))


# =============================================================================
# EXERCISE 3.5: Dynamic Programming (Intro)
# =============================================================================
print("\n--- Exercise 3.5: Dynamic Programming (Intro) ---")
"""
Write min_coins(amount, coins) that:
- Returns the fewest number of coins (values in coins) summing to amount
- Returns -1 when the amount cannot be made
- Builds a bottom-up table: best[v] = fewest coins for value v
- Hint: a greedy approach fails for coins [1, 5, 6, 9] and amount 11!
"""


# Your code below:
def min_coins(amount, coins):
    """Return the fewest coins that sum to amount, or -1."""
    pass


# Test (uncomment after implementing)
# print(min_coins(11, [1, 5, 6, 9]))  # 2  (5 + 6, greedy needs 3)
# print(min_coins(7, [2, 4]))         # -1


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 3.1
print("\n--- Solution 3.1 ---")


def binary_search(sorted_items, target):
    """Return the index of target, or -1 if not found."""
    low, high = 0, len(sorted_items) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        if sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


data = [1, 3, 5, 7, 9, 11]
print(f"Search 7  -> index {binary_search(data, 7)}")
print(f"Search 11 -> index {binary_search(data, 11)}")
print(f"Search 4  -> index {binary_search(data, 4)} (not found)")

# SOLUTION 3.2
print("\n--- Solution 3.2 ---")


def merge_sort(items):
    """Return a new sorted list using merge sort."""
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return _merge(left, right)


def _merge(left, right):
    """Merge two sorted lists into one sorted list."""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


messy = [38, 27, 43, 3, 9, 82, 10]
print(f"merge_sort({messy}) = {merge_sort(messy)}")

# SOLUTION 3.3
print("\n--- Solution 3.3 ---")


def quick_sort(items):
    """Return a new sorted list using quicksort."""
    if len(items) <= 1:
        return list(items)
    pivot = items[len(items) // 2]
    smaller = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    larger = [x for x in items if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(larger)


print(f"quick_sort({messy}) = {quick_sort(messy)}")
print(f"Both agree with sorted(): {merge_sort(messy) == sorted(messy) == quick_sort(messy)}")

# SOLUTION 3.4
print("\n--- Solution 3.4 ---")


def flatten(nested):
    """Return a flat list from arbitrarily nested lists."""
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


deep = [1, [2, [3, [4]], 5], [[6]]]
print(f"flatten({deep}) = {flatten(deep)}")

# SOLUTION 3.5
print("\n--- Solution 3.5 ---")


def min_coins(amount, coins):
    """Return the fewest coins that sum to amount, or -1."""
    infinity = float("inf")
    best = [0] + [infinity] * amount
    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and best[value - coin] + 1 < best[value]:
                best[value] = best[value - coin] + 1
    return best[amount] if best[amount] != infinity else -1


print(f"min_coins(11, [1, 5, 6, 9]) = {min_coins(11, [1, 5, 6, 9])} (greedy would say 3)")
print(f"min_coins(7, [2, 4]) = {min_coins(7, [2, 4])} (impossible)")

print("\n" + "=" * 50)
print("Great job! Move on to 04_data_structures.py")
print("=" * 50)
