# 🧠 Pure Functions Quiz

Test your understanding of pure functions!

---

## Question 1
Which statement best describes a **pure function**?

- A) It always prints its result
- B) It mutates at least one argument
- C) It always returns the same output for the same input and has no side effects
- D) It must use recursion

<details>
<summary>Show Answer</summary>

**C)** A pure function is deterministic and has no side effects.

</details>

---

## Question 2
Why are pure functions easier to test?

- A) They run faster
- B) They don't need inputs
- C) Their output depends only on their inputs
- D) They always return integers

<details>
<summary>Show Answer</summary>

**C)** You can test with fixed inputs and compare to expected outputs.

</details>

---

## Question 3
Which is **impure**?

```python
def f(x):
    return x * 2

def g(x):
    print(x)
    return x * 2
```

- A) f
- B) g
- C) Both are pure
- D) Neither is a function

<details>
<summary>Show Answer</summary>

**B)** `g` has a side effect (printing).

</details>

---

## Question 4
Referential transparency means:

- A) You can replace a function call with its result without changing behavior
- B) Functions must return references
- C) You can only use global variables
- D) Functions always mutate inputs

<details>
<summary>Show Answer</summary>

**A)** Pure functions are referentially transparent.

</details>

---

## Question 5
Which practice helps keep functions pure?

- A) Mutate input lists in place
- B) Read and write global variables
- C) Return new values without changing inputs
- D) Print inside every function

<details>
<summary>Show Answer</summary>

**C)** Return new values, avoid mutation and side effects.

</details>

---

[Back to Pure Functions README](README.md) | [Next: Immutability →](../02_immutability/README.md)
