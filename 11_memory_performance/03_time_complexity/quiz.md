# 🧠 Time Complexity Quiz

---

## Question 1
What is the typical time complexity of checking `x in some_list`?

- A) `O(1)`
- B) `O(log n)`
- C) `O(n)`
- D) `O(n^2)`

<details>
<summary>Show Answer</summary>

**C)** Lists use a linear scan for membership.

</details>

---

## Question 2
What is the typical average time complexity of checking `x in some_set`?

- A) `O(1)`
- B) `O(n)`
- C) `O(n log n)`
- D) `O(n^2)`

<details>
<summary>Show Answer</summary>

**A)** Sets use hashing, giving `O(1)` average membership checks.

</details>

---

## Question 3
A loop over `n` items that contains another full loop over the same `n` items is:

- A) `O(n)`
- B) `O(n log n)`
- C) `O(n^2)`
- D) `O(2n)`, which simplifies to `O(n)`

<details>
<summary>Show Answer</summary>

**C)** Nested loops multiply: `n` work inside `n` work gives `n * n = n^2`.

</details>

---

## Question 4
Two loops over `n` items, one **after** the other (not nested), cost:

- A) `O(n^2)` — any two loops are quadratic
- B) `O(n)` — sequential loops add, and constants are dropped
- C) `O(log n)`
- D) `O(1)`

<details>
<summary>Show Answer</summary>

**B)** `O(n) + O(n) = O(2n)`, which simplifies to `O(n)`. Only *nesting*
multiplies.

</details>

---

## Question 5
Your program is slow because `names.remove(x)` runs inside a loop over 100,000
items. What is the most likely first fix?

- A) Add more comments so the code is easier to read
- B) Replace the list with a set or dict where the operation is faster
- C) Rename the variable `names` to something shorter
- D) Wrap the loop in a function

<details>
<summary>Show Answer</summary>

**B)** Removing from the middle of a list is `O(n)`; sets and dicts support
fast membership operations. This is the "use the right data structure" fix.

</details>

---

[Back to Time Complexity README](README.md)
