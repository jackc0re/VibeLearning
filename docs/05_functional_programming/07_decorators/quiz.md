# 🧠 Decorators Quiz

Test your understanding of decorators.

---

## Question 1
What does `@decorator` syntax do?

- A) Calls the function immediately
- B) Replaces the function with `decorator(function)`
- C) Creates a class
- D) Imports a module

<details>
<summary>Show Answer</summary>

**B)** `@decorator` is syntax sugar for `func = decorator(func)`.

</details>

---

## Question 2
Why use `functools.wraps` inside decorators?

- A) To speed up functions
- B) To preserve the wrapped function's metadata
- C) To create recursion
- D) To avoid arguments

<details>
<summary>Show Answer</summary>

**B)** `wraps` preserves `__name__`, docstring, etc.

</details>

---

## Question 3
Which decorator adds behavior without changing the original function body?

- A) A closure
- B) A class method
- C) A wrapper function
- D) A global variable

<details>
<summary>Show Answer</summary>

**C)** Decorators wrap functions with a wrapper.

</details>

---

## Question 4
What is a decorator factory?

- A) A function that returns a decorator
- B) A decorator that returns a class
- C) A function that returns None
- D) A module for testing

<details>
<summary>Show Answer</summary>

**A)** A decorator factory lets you pass arguments to decorators.

</details>

---

## Question 5
Which use case fits decorators best?

- A) Sorting lists
- B) Logging and timing function calls
- C) Reading files
- D) Creating tuples

<details>
<summary>Show Answer</summary>

**B)** Decorators are commonly used for logging, timing, caching, etc.

</details>

---

[Back to Decorators README](README.md)
