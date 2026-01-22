# 🧠 Higher-Order Functions Quiz

Test your knowledge of higher-order functions!

---

## Question 1
Which best defines a higher-order function?

- A) A function that only uses loops
- B) A function that takes or returns another function
- C) A function that always returns a list
- D) A function with no parameters

<details>
<summary>Show Answer</summary>

**B)** Higher-order functions take and/or return functions.

</details>

---

## Question 2
What does this return?

```python
def apply_twice(f, x):
    return f(f(x))

def add1(x):
    return x + 1

apply_twice(add1, 3)
```

- A) 3
- B) 4
- C) 5
- D) 6

<details>
<summary>Show Answer</summary>

**C)** add1(add1(3)) = 5.

</details>

---

## Question 3
Which example shows a function returning a function?

- A)
```python
def f(x):
    return x * 2
```
- B)
```python
def make_adder(n):
    def add(x):
        return x + n
    return add
```
- C)
```python
def g(x):
    print(x)
```
- D)
```python
def h():
    return 42
```

<details>
<summary>Show Answer</summary>

**B)** `make_adder` returns the inner `add` function.

</details>

---

## Question 4
Function composition `compose(f, g)` typically computes:

- A) f + g
- B) f(g(x))
- C) g(f(x)) and f(g(x))
- D) f(x) + g(x)

<details>
<summary>Show Answer</summary>

**B)** Composition applies `g` first, then `f`.

</details>

---

## Question 5
Why are higher-order functions useful?

- A) They replace all loops
- B) They make functions run faster
- C) They enable reusable, composable behavior
- D) They avoid using variables

<details>
<summary>Show Answer</summary>

**C)** They let you reuse and combine behavior cleanly.

</details>

---

[Back to Higher-Order Functions README](README.md) | [Next: Lambda Expressions →](../04_lambda_expressions/README.md)
