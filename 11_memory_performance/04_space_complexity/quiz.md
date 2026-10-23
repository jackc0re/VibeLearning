# 🧠 Space Complexity Quiz

---

## Question 1
What is a typical memory advantage of using a generator instead of building a list?

- A) It makes the CPU faster by default
- B) It stores fewer results in memory at once
- C) It changes `O(n)` time to `O(1)` time
- D) It automatically parallelizes computation

<details>
<summary>Show Answer</summary>

**B)** Generators yield items one at a time instead of storing all items.

</details>

---

## Question 2
What extra space does an in-place algorithm often aim for?

- A) `O(n)`
- B) `O(n^2)`
- C) `O(1)`
- D) `O(log n)`

<details>
<summary>Show Answer</summary>

**C)** In-place usually targets constant auxiliary space.

</details>

---

## Question 3
What is the auxiliary space of `(x * x for x in range(1_000_000))`?

- A) `O(1)` — the generator holds only its current item and state
- B) `O(n)` — it secretly builds the full list first
- C) `O(n^2)`
- D) `O(log n)`

<details>
<summary>Show Answer</summary>

**A)** A generator computes each value on demand, so it does not store all
million results at once.

</details>

---

## Question 4
A recursive function that calls itself `d` levels deep typically uses how much
extra memory for the call stack?

- A) `O(1)`
- B) `O(log d)`
- C) `O(d)`
- D) `O(d^2)`

<details>
<summary>Show Answer</summary>

**C)** Each pending call adds a stack frame, so depth `d` costs `O(d)` stack
space. Very deep recursion can exhaust the stack.

</details>

---

## Question 5
Which call allocates a **new list** instead of sorting in place?

- A) `nums.sort()`
- B) `sorted(nums)`
- C) `nums.reverse()`
- D) `nums.append(x)`

<details>
<summary>Show Answer</summary>

**B)** `sorted(nums)` returns a new list (`O(n)` extra space); `sort()`,
`reverse()`, and `append()` work in place.

</details>

---

[Back to Space Complexity README](README.md)
