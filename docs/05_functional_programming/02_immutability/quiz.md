# 🧠 Immutability Quiz

Check your understanding of immutable data and copy-on-write patterns!

---

## Question 1
Which Python type is **immutable**?

- A) list
- B) dict
- C) tuple
- D) set

<details>
<summary>Show Answer</summary>

**C)** Tuples are immutable.

</details>

---

## Question 2
What is a benefit of immutability?

- A) Faster printing
- B) Fewer unexpected side effects
- C) More global variables
- D) Automatic recursion

<details>
<summary>Show Answer</summary>

**B)** Immutability reduces unexpected changes in shared state.

</details>

---

## Question 3
Which creates a **new list** without mutating the original?

```python
nums = [1, 2, 3]
```

- A) nums.append(4)
- B) nums[0] = 99
- C) nums + [4]
- D) nums.sort()

<details>
<summary>Show Answer</summary>

**C)** `nums + [4]` returns a new list.

</details>

---

## Question 4
Why are immutable values safer with concurrency?

- A) They can’t be changed by other threads
- B) They always run faster
- C) They avoid loops
- D) They prevent exceptions

<details>
<summary>Show Answer</summary>

**A)** If data can’t change, threads cannot corrupt it.

</details>

---

## Question 5
Which expression creates a new dict with an updated key?

```python
data = {"a": 1}
```

- A) data["b"] = 2
- B) {**data, "b": 2}
- C) data.update({"b": 2})
- D) del data["a"]

<details>
<summary>Show Answer</summary>

**B)** `{**data, "b": 2}` creates a new dict.

</details>

---

[Back to Immutability README](README.md) | [Next: Higher-Order Functions →](../03_higher_order_functions/README.md)
