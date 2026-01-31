# 🧠 Sorting Algorithms Quiz

Test your understanding of sorting algorithms!

---

## Question 1: Time Complexity

What is the **average-case** time complexity of Quick Sort?

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary>Show Answer</summary>

**B) O(n log n)**

Quick Sort achieves O(n log n) on average by partitioning the array into roughly equal halves at each level.

</details>

---

## Question 2: Worst Case

Which sorting algorithm has O(n²) as its **best case** time complexity?

- A) Bubble Sort
- B) Insertion Sort
- C) Selection Sort
- D) Merge Sort

<details>
<summary>Show Answer</summary>

**C) Selection Sort**

Selection Sort always scans the entire unsorted portion to find the minimum, regardless of input order. It performs O(n²) comparisons even on sorted data.

Bubble Sort and Insertion Sort can be O(n) on already sorted arrays.

</details>

---

## Question 3: Stability

Which of these sorting algorithms is **NOT stable**?

- A) Bubble Sort
- B) Insertion Sort
- C) Merge Sort
- D) Quick Sort

<details>
<summary>Show Answer</summary>

**D) Quick Sort**

Quick Sort is not stable because the partitioning process can change the relative order of equal elements.

Bubble Sort, Insertion Sort, and Merge Sort are all stable algorithms.

</details>

---

## Question 4: Space Complexity

Which sorting algorithm requires O(n) extra space?

- A) Bubble Sort
- B) Selection Sort
- C) Merge Sort
- D) Quick Sort

<details>
<summary>Show Answer</summary>

**C) Merge Sort**

Merge Sort requires O(n) extra space to store the temporary arrays during merging.

Bubble Sort, Selection Sort, and Quick Sort (average case) are in-place algorithms with O(1) or O(log n) space.

</details>

---

## Question 5: Best Case

Which algorithm performs best on **already sorted** arrays?

- A) Quick Sort (with last element as pivot)
- B) Merge Sort
- C) Insertion Sort
- D) Selection Sort

<details>
<summary>Show Answer</summary>

**C) Insertion Sort**

Insertion Sort achieves O(n) time on sorted arrays because each element is already in its correct position (no shifts needed).

- Quick Sort with last-element pivot: O(n²) on sorted data
- Merge Sort: Always O(n log n)
- Selection Sort: Always O(n²)

</details>

---

## Question 6: Algorithm Identification

```
Pass 1: [5, 3, 8, 4, 2] → [3, 5, 4, 2, 8]
Pass 2: [3, 5, 4, 2, 8] → [3, 4, 2, 5, 8]
Pass 3: [3, 4, 2, 5, 8] → [3, 2, 4, 5, 8]
Pass 4: [3, 2, 4, 5, 8] → [2, 3, 4, 5, 8]
```

Which sorting algorithm is this?

- A) Selection Sort
- B) Bubble Sort
- C) Insertion Sort
- D) Quick Sort

<details>
<summary>Show Answer</summary>

**B) Bubble Sort**

The pattern shows:
1. Largest elements "bubbling up" to the right
2. After each pass, one more element is in its final position
3. Adjacent element swaps within each pass

</details>

---

## Question 7: Merge Sort

How many times will the `merge()` function be called when sorting an array of 8 elements using Merge Sort?

- A) 3
- B) 7
- C) 8
- D) 15

<details>
<summary>Show Answer</summary>

**B) 7**

For n elements, merge is called n-1 times (7 for 8 elements).

Visualization for 8 elements:
```
Level 3: 4 merges (pairs → 4 sorted pairs)
Level 2: 2 merges (4 pairs → 2 sorted arrays)
Level 1: 1 merge (2 arrays → 1 sorted array)
Total: 4 + 2 + 1 = 7 merges
```

</details>

---

## Question 8: Quick Sort Pivot

If you always choose the first element as the pivot in Quick Sort, what input causes worst-case O(n²) behavior?

- A) Random array
- B) Array with all same elements
- C) Already sorted array
- D) Both B and C

<details>
<summary>Show Answer</summary>

**D) Both B and C**

With first element as pivot:
- **Sorted array**: Pivot is always smallest/largest, creating unbalanced partitions
- **All same elements**: Every partition is unbalanced (all elements go to one side)

Both result in n partitions with ~n elements each = O(n²)

</details>

---

## Question 9: In-Place Sorting

Which statement about in-place sorting is TRUE?

- A) In-place algorithms cannot use any extra memory
- B) Merge Sort is typically implemented in-place
- C) In-place algorithms use O(1) or O(log n) extra space
- D) Quick Sort is never in-place

<details>
<summary>Show Answer</summary>

**C) In-place algorithms use O(1) or O(log n) extra space**

In-place sorting means the algorithm doesn't require extra space proportional to input size:
- Bubble/Selection/Insertion Sort: O(1) extra space
- Quick Sort: O(log n) for recursion stack (average)
- Merge Sort: Typically O(n) - NOT in-place

</details>

---

## Question 10: Counting Sort

When is Counting Sort the best choice?

- A) Sorting floating-point numbers
- B) Sorting strings alphabetically
- C) Sorting integers with a small range (0 to k where k is small)
- D) Sorting a linked list

<details>
<summary>Show Answer</summary>

**C) Sorting integers with a small range (0 to k where k is small)**

Counting Sort is O(n + k) where k is the range of values. It's efficient when:
- Elements are non-negative integers
- The range k is similar to or smaller than n
- k is not extremely large

It doesn't work for floats, strings (directly), or non-integer data.

</details>

---

## Question 11: Practical Choice

You need to sort 50 elements that are mostly already sorted - only 2-3 elements are out of place. Which algorithm is best?

- A) Merge Sort
- B) Quick Sort
- C) Insertion Sort
- D) Selection Sort

<details>
<summary>Show Answer</summary>

**C) Insertion Sort**

For small, nearly-sorted arrays, Insertion Sort is optimal because:
- O(n) time on nearly sorted data (minimal shifts needed)
- Simple with low overhead
- In-place with O(1) extra space

Many hybrid algorithms (like Timsort) switch to insertion sort for small subarrays.

</details>

---

## Question 12: Sorting Objects

You're sorting a list of students by grade. Two students (Alice and Bob) both have grade 85. In the original list, Alice comes before Bob. After sorting, Alice should still come before Bob. Which algorithm property ensures this?

- A) Time efficiency
- B) Space efficiency
- C) Stability
- D) Adaptivity

<details>
<summary>Show Answer</summary>

**C) Stability**

A stable sorting algorithm preserves the relative order of equal elements. If Alice appears before Bob in the input and they have equal grades, a stable sort guarantees Alice still appears before Bob in the output.

</details>

---

## Question 13: Code Output

```python
def mystery_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(mystery_sort([3, 1, 4, 1, 5]))
```

After the FIRST iteration of the outer loop, what is the array?

- A) [1, 3, 4, 1, 5]
- B) [1, 1, 4, 3, 5]
- C) [1, 1, 3, 4, 5]
- D) [3, 1, 1, 4, 5]

<details>
<summary>Show Answer</summary>

**A) [1, 3, 4, 1, 5]**

This is Selection Sort:
1. Find minimum in [3, 1, 4, 1, 5] → 1 at index 1
2. Swap with element at index 0
3. Result: [1, 3, 4, 1, 5]

Note: It finds the first occurrence of the minimum (index 1, not index 3).

</details>

---

## Question 14: Divide and Conquer

Both Merge Sort and Quick Sort use divide and conquer. What's the key difference?

- A) Quick Sort divides, Merge Sort conquers
- B) Merge Sort does work during merge (combine), Quick Sort during partition (divide)
- C) Quick Sort is always faster
- D) They use the same approach

<details>
<summary>Show Answer</summary>

**B) Merge Sort does work during merge (combine), Quick Sort during partition (divide)**

- **Merge Sort**: Dividing is trivial (split in half). The work happens during merging sorted halves.
- **Quick Sort**: The work happens during partitioning (placing pivot in correct position). Combining is trivial (subproblems are already in place).

</details>

---

## Question 15: Hybrid Algorithms

Python's built-in `sort()` uses Timsort. What is Timsort?

- A) A variant of Quick Sort
- B) A pure Merge Sort implementation
- C) A hybrid of Merge Sort and Insertion Sort
- D) A hybrid of Quick Sort and Heap Sort

<details>
<summary>Show Answer</summary>

**C) A hybrid of Merge Sort and Insertion Sort**

Timsort:
- Identifies "runs" of already sorted data
- Uses insertion sort for small runs
- Merges runs using merge sort technique
- O(n log n) worst case, O(n) best case
- Stable
- Optimized for real-world data that often has some existing order

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

1. **Know the complexities**: Best, average, and worst case
2. **Stability matters** when sorting objects with multiple fields
3. **Choose based on context**: Data size, existing order, memory constraints
4. **Simple sorts** (O(n²)): Good for small n or educational purposes
5. **Efficient sorts** (O(n log n)): Use for larger datasets
6. **Python's sort()** is highly optimized — use it in production!

---

[Back to Sorting README](README.md) | [Next: Recursion →](../03_recursion/)
