# 🧠 Divide and Conquer Quiz

Test your understanding of divide and conquer algorithms!

---

## Question 1

**What are the three main steps of the Divide and Conquer paradigm?**

- A) Plan, Execute, Review
- B) Divide, Conquer, Combine
- C) Split, Sort, Merge
- D) Partition, Recurse, Return

<details>
<summary>Show Answer</summary>

**B) Divide, Conquer, Combine**

The three steps are:
1. **Divide**: Break the problem into smaller subproblems
2. **Conquer**: Solve subproblems recursively
3. **Combine**: Merge solutions to solve the original problem

</details>

---

## Question 2

**What is the time complexity of Merge Sort?**

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary>Show Answer</summary>

**B) O(n log n)**

Merge Sort divides the array in half (log n levels) and merges at each level (O(n) work per level), giving O(n log n) total.

</details>

---

## Question 3

**What is the key difference between Divide and Conquer and Dynamic Programming?**

- A) D&C is faster than DP
- B) D&C subproblems are independent; DP subproblems overlap
- C) DP uses recursion; D&C doesn't
- D) D&C only works on arrays

<details>
<summary>Show Answer</summary>

**B) D&C subproblems are independent; DP subproblems overlap**

In D&C, subproblems don't share work (e.g., merge sort halves are independent). In DP, subproblems overlap and results are cached to avoid redundant computation.

</details>

---

## Question 4

**In Quick Sort, what is the worst-case time complexity?**

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary>Show Answer</summary>

**C) O(n²)**

Worst case occurs when the pivot is always the smallest or largest element, creating unbalanced partitions. This happens with already sorted arrays and poor pivot selection.

</details>

---

## Question 5

**What is the space complexity of Merge Sort?**

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n log n)

<details>
<summary>Show Answer</summary>

**C) O(n)**

Merge Sort requires O(n) auxiliary space for the temporary arrays used during merging. The recursion stack adds O(log n), but O(n) dominates.

</details>

---

## Question 6

**The Master Theorem applies to recurrences of what form?**

- A) T(n) = T(n-1) + f(n)
- B) T(n) = aT(n/b) + f(n)
- C) T(n) = T(n/2) + T(n/2)
- D) T(n) = 2^n

<details>
<summary>Show Answer</summary>

**B) T(n) = aT(n/b) + f(n)**

Where:
- `a` = number of subproblems
- `b` = factor by which input size shrinks
- `f(n)` = cost of dividing and combining

</details>

---

## Question 7

**For Binary Search, T(n) = T(n/2) + O(1). Using the Master Theorem, what is the complexity?**

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n log n)

<details>
<summary>Show Answer</summary>

**B) O(log n)**

With a=1, b=2, f(n)=1:
- n^(log_b(a)) = n^0 = 1
- f(n) = 1 = n^(log_b(a))
- This is Case 2: T(n) = O(n^(log_b(a)) × log n) = O(log n)

</details>

---

## Question 8

**What is the time complexity of the D&C approach to finding the maximum subarray sum?**

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary>Show Answer</summary>

**B) O(n log n)**

The recurrence is T(n) = 2T(n/2) + O(n), which gives O(n log n). Note: Kadane's algorithm solves this in O(n), but the D&C approach is O(n log n).

</details>

---

## Question 9

**In the Closest Pair of Points problem, why do we only need to check a limited number of points in the strip?**

- A) The strip is always empty
- B) Points in the strip are sorted by x-coordinate
- C) At most 6 points can be within distance d of any point in the strip
- D) We use binary search in the strip

<details>
<summary>Show Answer</summary>

**C) At most 6 points can be within distance d of any point in the strip**

Due to geometric constraints, at most 6 points can fit in a d×2d rectangle. This keeps the strip checking at O(n) per level, maintaining O(n log n) overall.

</details>

---

## Question 10

**What is the key insight behind fast exponentiation (power function)?**

- A) Use logarithms instead of multiplication
- B) x^n = (x^(n/2))² for even n
- C) Always use floating-point arithmetic
- D) Cache all intermediate results

<details>
<summary>Show Answer</summary>

**B) x^n = (x^(n/2))² for even n**

By squaring the half-power, we reduce the number of multiplications from n to log n. For odd n: x^n = x × (x^(n/2))².

</details>

---

## Question 11

**Counting inversions uses a modified version of which algorithm?**

- A) Quick Sort
- B) Merge Sort
- C) Binary Search
- D) Heap Sort

<details>
<summary>Show Answer</summary>

**B) Merge Sort**

During the merge step, when an element from the right half is placed before elements from the left half, we count those as inversions. This gives O(n log n) complexity.

</details>

---

## Question 12

**What is the Karatsuba algorithm used for?**

- A) Sorting large arrays
- B) Multiplying large numbers
- C) Finding shortest paths
- D) Matrix inversion

<details>
<summary>Show Answer</summary>

**B) Multiplying large numbers**

Karatsuba reduces multiplication from O(n²) to O(n^1.585) by using 3 multiplications instead of 4 for n-digit numbers.

</details>

---

## Question 13

**In Quickselect (finding kth smallest), what is the average time complexity?**

- A) O(log n)
- B) O(n)
- C) O(n log n)
- D) O(n²)

<details>
<summary>Show Answer</summary>

**B) O(n)**

Unlike QuickSort, Quickselect only recurses on one partition. On average, this gives T(n) = T(n/2) + O(n) = O(n). Worst case is still O(n²).

</details>

---

## Question 14

**Which of these is NOT a characteristic of Divide and Conquer algorithms?**

- A) Recursive structure
- B) Independent subproblems
- C) Memoization of results
- D) Combining step

<details>
<summary>Show Answer</summary>

**C) Memoization of results**

Memoization is a characteristic of Dynamic Programming, not D&C. D&C subproblems are independent and don't need caching because they don't overlap.

</details>

---

## Question 15

**What is the recurrence relation for Merge Sort?**

- A) T(n) = T(n-1) + O(1)
- B) T(n) = T(n/2) + O(n)
- C) T(n) = 2T(n/2) + O(n)
- D) T(n) = 2T(n/2) + O(1)

<details>
<summary>Show Answer</summary>

**C) T(n) = 2T(n/2) + O(n)**

- **2T(n/2)**: Two recursive calls on halves
- **O(n)**: Linear time to merge the sorted halves

Using Master Theorem: a=2, b=2, f(n)=n → O(n log n)

</details>

---

## 🏆 Score Guide

| Score | Rating |
|-------|--------|
| 13-15 | ⭐⭐⭐⭐⭐ D&C Master! |
| 10-12 | ⭐⭐⭐⭐ Great understanding! |
| 7-9 | ⭐⭐⭐ Good progress! |
| 4-6 | ⭐⭐ Review the concepts |
| 0-3 | ⭐ Start with the basics |

---

## 📚 Review Topics

If you struggled with certain questions, review these topics:

- **Questions 1-3**: Basic D&C concepts and comparison with DP
- **Questions 4-5**: Sorting algorithm analysis
- **Questions 6-7**: Master Theorem application
- **Questions 8-9**: Classic D&C problems
- **Questions 10-12**: Advanced D&C applications
- **Questions 13-15**: Algorithm analysis and recurrences
