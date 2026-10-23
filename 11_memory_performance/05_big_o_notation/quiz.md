# 🧠 Big-O Notation Quiz

---

## Question 1
What is the Big-O time complexity of binary search on a sorted list?

- A) `O(1)`
- B) `O(log n)`
- C) `O(n)`
- D) `O(n^2)`

<details>
<summary>Show Answer</summary>

**B)** Binary search halves the search space each step.

</details>

---

## Question 2
Which Big-O class grows fastest as `n` becomes very large?

- A) `O(n)`
- B) `O(log n)`
- C) `O(n log n)`
- D) `O(n^2)`

<details>
<summary>Show Answer</summary>

**D)** Quadratic growth dominates linear and linearithmic growth for large `n`.

</details>

---

## Question 3
How should `O(2n)` be written in proper simplified form?

- A) `O(2n)` — keep every constant
- B) `O(n)` — constant factors are dropped
- C) `O(n^2)`
- D) `O(log n)`

<details>
<summary>Show Answer</summary>

**B)** Big-O ignores constant factors: what matters is the growth shape, and
doubling everything changes only the constant.

</details>

---

## Question 4
A function does a linear scan (`O(n)`) and then a nested-loop step (`O(n^2)`).
What is its overall complexity?

- A) `O(n)`
- B) `O(n^3)`
- C) `O(n^2)` — the dominant term wins
- D) `O(n + n^2)`, which cannot be simplified

<details>
<summary>Show Answer</summary>

**C)** Sequential steps add, and the sum keeps only the dominant term:
`O(n) + O(n^2)` simplifies to `O(n^2)`.

</details>

---

## Question 5
Which operation is `O(1)` on average?

- A) `x in some_list`
- B) `x in some_dict`
- C) Finding the maximum by scanning all items
- D) Sorting a list

<details>
<summary>Show Answer</summary>

**B)** Dicts (and sets) use hashing for `O(1)` average lookups. The others
scan or sort, costing at least `O(n)`.

</details>

---

[Back to Big-O Notation README](README.md)
