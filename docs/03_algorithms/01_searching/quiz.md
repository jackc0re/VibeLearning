# 🧠 Searching Algorithms Quiz

Test your understanding of searching algorithms!

---

## Question 1: Time Complexity

What is the **worst-case** time complexity of linear search on an array of n elements?

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

<details>
<summary>Show Answer</summary>

**C) O(n)**

In the worst case, linear search must check every element in the array (when the target is at the end or not present).

</details>

---

## Question 2: Binary Search Requirement

What is the main requirement for binary search to work correctly?

- A) The array must be in descending order
- B) The array must be sorted
- C) The array must have unique elements
- D) The array must have an even number of elements

<details>
<summary>Show Answer</summary>

**B) The array must be sorted**

Binary search relies on comparing the middle element to determine which half contains the target. This only works if elements are in sorted order.

</details>

---

## Question 3: Binary Search Time Complexity

What is the time complexity of binary search?

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n log n)

<details>
<summary>Show Answer</summary>

**B) O(log n)**

Each comparison eliminates half of the remaining elements, so the number of comparisons is log₂(n).

</details>

---

## Question 4: Searching Methods

Given an **unsorted** array of 10,000 elements, which search method should you use?

- A) Binary search
- B) Linear search
- C) Binary search after sorting
- D) Both B and C are correct

<details>
<summary>Show Answer</summary>

**D) Both B and C are correct**

- **Linear search** works directly on unsorted data: O(n) = 10,000 operations
- **Sort + Binary search**: O(n log n) + O(log n) ≈ 130,000 + 14 operations

For a single search, linear search is faster. But if you need to search multiple times, sorting first becomes worthwhile.

</details>

---

## Question 5: Binary Search Implementation

In binary search, if `arr[mid] < target`, what should happen next?

- A) Search the left half: `right = mid - 1`
- B) Search the right half: `left = mid + 1`
- C) Return mid
- D) Return -1

<details>
<summary>Show Answer</summary>

**B) Search the right half: `left = mid + 1`**

If `arr[mid] < target`, the target must be in the right half (larger values), so we update `left = mid + 1`.

</details>

---

## Question 6: Comparisons in Binary Search

In an array of 1,024 elements, what is the **maximum** number of comparisons binary search will make?

- A) 8
- B) 10
- C) 11
- D) 1,024

<details>
<summary>Show Answer</summary>

**B) 10**

Maximum comparisons = ⌊log₂(1024)⌋ + 1 = 10 + 1 = 11

Wait, let me recalculate:
- log₂(1024) = 10
- Maximum comparisons = 10 (since 2¹⁰ = 1024)

Actually **B) 10** is correct. In binary search of 1024 elements:
- After 1 comparison: 512 elements remain
- After 2 comparisons: 256 elements remain
- ...
- After 10 comparisons: 1 element remains

</details>

---

## Question 7: Space Complexity

What is the space complexity of **iterative** binary search?

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n log n)

<details>
<summary>Show Answer</summary>

**A) O(1)**

Iterative binary search only uses a constant number of variables (left, right, mid) regardless of input size.

Note: Recursive binary search uses O(log n) space due to the call stack.

</details>

---

## Question 8: Code Output

```python
def search(arr, target):
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

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(search(arr, 23))
```

What is the output?

- A) 4
- B) 5
- C) 6
- D) -1

<details>
<summary>Show Answer</summary>

**B) 5**

Tracing through:
1. left=0, right=9, mid=4, arr[4]=16 < 23, left=5
2. left=5, right=9, mid=7, arr[7]=56 > 23, right=6
3. left=5, right=6, mid=5, arr[5]=23 == 23, return 5

</details>

---

## Question 9: First Occurrence

In an array `[1, 2, 2, 2, 2, 3, 4]`, how do you find the **first** occurrence of 2 using binary search?

- A) Standard binary search returns the first occurrence
- B) When you find target, continue searching in the left half
- C) When you find target, continue searching in the right half
- D) Use linear search instead

<details>
<summary>Show Answer</summary>

**B) When you find target, continue searching in the left half**

To find the first occurrence:
1. When `arr[mid] == target`, save this index as a candidate
2. Continue searching in the left half (`right = mid - 1`)
3. Return the leftmost match found

</details>

---

## Question 10: Rotated Array

Given a rotated sorted array `[4, 5, 6, 7, 0, 1, 2]`, can binary search still achieve O(log n)?

- A) No, you must use linear search
- B) Yes, with a modified binary search algorithm
- C) Yes, but only after "unrotating" the array first
- D) No, rotated arrays cannot be searched efficiently

<details>
<summary>Show Answer</summary>

**B) Yes, with a modified binary search algorithm**

Modified binary search can handle rotated arrays by:
1. Find the middle element
2. Determine which half is sorted
3. Check if target is in the sorted half
4. Eliminate the appropriate half

This maintains O(log n) complexity.

</details>

---

## Question 11: Practical Application

You have a phone book with 1 million entries sorted by name. How many comparisons does binary search need (worst case)?

- A) About 10
- B) About 20
- C) About 100
- D) About 1000

<details>
<summary>Show Answer</summary>

**B) About 20**

log₂(1,000,000) ≈ 19.93

So approximately 20 comparisons in the worst case.

This is why phone books and dictionaries are so efficient to search!

</details>

---

## Question 12: When to Use What

Which scenario is best suited for **linear search**?

- A) Searching in a sorted array of 1 million elements
- B) Searching in an unsorted linked list
- C) Searching multiple times in the same sorted array
- D) Searching in a balanced binary search tree

<details>
<summary>Show Answer</summary>

**B) Searching in an unsorted linked list**

Linear search is the best choice when:
- Data is unsorted
- Data structure doesn't support random access (like linked lists)
- Data set is small

Binary search cannot be efficiently applied to linked lists because they don't support O(1) random access.

</details>

---

## Question 13: Off-by-One Errors

In binary search, why is the condition `left <= right` used instead of `left < right`?

- A) It's just a coding style preference
- B) To handle the case when target is at the last remaining position
- C) To prevent infinite loops
- D) To make the code run faster

<details>
<summary>Show Answer</summary>

**B) To handle the case when target is at the last remaining position**

When `left == right`, there's still one element to check. Using `left < right` would skip this element.

Example: Array `[5]`, searching for 5
- left=0, right=0
- With `left < right`: Loop doesn't execute, returns -1 (wrong!)
- With `left <= right`: Checks arr[0], finds 5, returns 0 (correct!)

</details>

---

## Question 14: Python Built-ins

What does Python's `bisect.bisect_left([1, 3, 5, 7], 4)` return?

- A) 1
- B) 2
- C) 3
- D) -1

<details>
<summary>Show Answer</summary>

**B) 2**

`bisect_left` returns the leftmost position where the target should be inserted to maintain sorted order.

Array: [1, 3, 5, 7]
Target 4 should go between 3 and 5, at index 2.

Result: [1, 3, **4**, 5, 7]

</details>

---

## Question 15: Complexity Analysis

If you need to search the same sorted array 1000 times, which approach is more efficient overall?

- A) Use linear search 1000 times: 1000 × O(n) = O(1000n)
- B) Use binary search 1000 times: 1000 × O(log n) = O(1000 log n)
- C) They're the same
- D) Depends on the array size

<details>
<summary>Show Answer</summary>

**B) Use binary search 1000 times: 1000 × O(log n) = O(1000 log n)**

For repeated searches on sorted data, binary search is vastly superior.

Example with n = 1,000,000:
- Linear: 1000 × 1,000,000 = 1 billion operations
- Binary: 1000 × 20 = 20,000 operations

That's 50,000x faster!

</details>

---

## Scoring

| Score | Level |
|-------|-------|
| 13-15 | ⭐⭐⭐ Expert |
| 10-12 | ⭐⭐ Proficient |
| 7-9 | ⭐ Intermediate |
| 0-6 | Keep studying! |

---

## Key Takeaways

1. **Linear Search**: O(n) time, works on any data
2. **Binary Search**: O(log n) time, requires sorted data
3. **Choose wisely** based on data characteristics
4. **Watch for edge cases** in implementation
5. **Binary search has many variations** for different problems

---

[Back to Searching README](README.md) | [Next: Sorting →](../02_sorting/)
