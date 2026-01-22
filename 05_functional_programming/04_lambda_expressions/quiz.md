# 🧠 Lambda Expressions Quiz

Test your understanding of lambda expressions.

---

## Question 1
Which is a valid lambda expression?

- A) `lambda x: x * 2`
- B) `lambda (x): return x * 2`
- C) `def lambda x: x * 2`
- D) `lambda: x = 2`

<details>
<summary>Show Answer</summary>

**A)** `lambda x: x * 2` is valid.

</details>

---

## Question 2
What does this evaluate to?

```python
(lambda a, b: a + b)(2, 3)
```

- A) 2
- B) 3
- C) 5
- D) Error

<details>
<summary>Show Answer</summary>

**C)** It returns 5.

</details>

---

## Question 3
When should you avoid lambdas?

- A) When the logic is complex
- B) When you need a short callback
- C) When you need to pass a function
- D) When you want fewer lines of code

<details>
<summary>Show Answer</summary>

**A)** Use named functions for complex logic.

</details>

---

## Question 4
Which use of lambda is correct with `sorted`?

```python
names = ["bob", "Alice", "charlie"]
```

- A) `sorted(names, key=lambda n: n.lower())`
- B) `sorted(names, key=lambda(n) n.lower())`
- C) `sorted(names, key=lambda: n.lower())`
- D) `sorted(names, lambda n: n.lower())`

<details>
<summary>Show Answer</summary>

**A)** The key function must accept one argument.

</details>

---

## Question 5
Which statement is true about lambda expressions?

- A) They can contain multiple statements
- B) They are always faster than def
- C) They are anonymous, single-expression functions
- D) They can only be used with map/filter

<details>
<summary>Show Answer</summary>

**C)** Lambdas are anonymous single-expression functions.

</details>

---

[Back to Lambda README](README.md) | [Next: Map, Filter, Reduce →](../05_map_filter_reduce/README.md)
