# 🧠 Custom Exceptions Quiz

Test your understanding of defining and using your own exceptions.

---

## Question 1
Why create custom exceptions?

- A) To avoid writing tests
- B) To make errors more meaningful and catchable
- C) To speed up execution
- D) To remove try/except blocks

<details>
<summary>Show Answer</summary>

**B)** Custom exceptions improve clarity and handling.

</details>

---

## Question 2
Which is a good base class for a custom error about invalid input?

- A) StopIteration
- B) ValueError
- C) ImportError
- D) SystemExit

<details>
<summary>Show Answer</summary>

**B)** Input validation errors typically subclass `ValueError`.

</details>

---

## Question 3
What is the advantage of an exception hierarchy?

- A) It prevents exceptions from being raised
- B) It lets you catch a group of related errors
- C) It makes all errors identical
- D) It removes the need for messages

<details>
<summary>Show Answer</summary>

**B)** A hierarchy allows catching a whole category or a specific subtype.

</details>

---

## Question 4
Which code raises a custom exception?

- A) `raise InvalidEmailError("Missing @")`
- B) `throw InvalidEmailError()`
- C) `error InvalidEmailError()`
- D) `InvalidEmailError.raise()`

<details>
<summary>Show Answer</summary>

**A)** Use `raise` to throw exceptions in Python.

</details>

---

## Question 5
Why should errors include clear messages?

- A) To hide the real problem
- B) To reduce logging
- C) To make debugging faster
- D) To avoid stack traces

<details>
<summary>Show Answer</summary>

**C)** Clear messages speed up diagnosis and fixes.

</details>

---

[Back to Custom Exceptions README](README.md) | [Next: Defensive Programming →](../04_defensive_programming/README.md)
