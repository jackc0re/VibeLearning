# 🧠 Closures Quiz

Test your understanding of closures.

---

## Question 1
What is a closure?

- A) A function with no parameters
- B) A function that remembers variables from its enclosing scope
- C) A function that always returns None
- D) A function that only uses global variables

<details>
<summary>Show Answer</summary>

**B)** Closures capture variables from their enclosing scope.

</details>

---

## Question 2
What does this return?

```python
def make_adder(n):
    def add(x):
        return x + n
    return add

add3 = make_adder(3)
add3(4)
```

- A) 3
- B) 4
- C) 7
- D) Error

<details>
<summary>Show Answer</summary>

**C)** 4 + 3 = 7.

</details>

---

## Question 3
Why use `nonlocal`?

- A) To import a module
- B) To create a new local variable
- C) To modify a variable from an enclosing scope
- D) To access global variables

<details>
<summary>Show Answer</summary>

**C)** `nonlocal` lets you update the outer variable.

</details>

---

## Question 4
Closures are useful because they:

- A) Replace classes entirely
- B) Allow functions to keep internal state
- C) Always run faster
- D) Prevent all bugs

<details>
<summary>Show Answer</summary>

**B)** Closures can store state without classes.

</details>

---

## Question 5
Which pattern uses closures often?

- A) Decorators
- B) List slicing
- C) File I/O
- D) Exception handling

<details>
<summary>Show Answer</summary>

**A)** Decorators commonly use closures.

</details>

---

[Back to Closures README](README.md) | [Next: Decorators →](../07_decorators/README.md)
