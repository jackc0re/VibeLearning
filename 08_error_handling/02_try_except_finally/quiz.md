# 🧠 Try/Except/Finally Quiz

Check your understanding of safe error handling flow.

---

## Question 1
What does the `finally` block do?

- A) Runs only if no error happens
- B) Runs only if an error happens
- C) Always runs, success or error
- D) Stops exceptions from propagating

<details>
<summary>Show Answer</summary>

**C)** `finally` executes regardless of success or failure.

</details>

---

## Question 2
When does the `else` block run?

- A) Only when an exception is raised
- B) Only when no exception is raised
- C) Always
- D) Never

<details>
<summary>Show Answer</summary>

**B)** `else` runs when the `try` block succeeds.

</details>

---

## Question 3
Which is the best practice for `except` blocks?

- A) Catch all exceptions with `except Exception`
- B) Catch the most specific exception you expect
- C) Always ignore exceptions
- D) Use `pass` to hide errors

<details>
<summary>Show Answer</summary>

**B)** Specific exceptions prevent hiding unrelated bugs.

</details>

---

## Question 4
What happens if you catch an exception and do nothing?

- A) The program still crashes
- B) The error is hidden and execution continues
- C) Python restarts automatically
- D) The exception becomes a warning

<details>
<summary>Show Answer</summary>

**B)** Catching and ignoring hides the error.

</details>

---

## Question 5
Why is `finally` useful for files?

- A) It speeds up file IO
- B) It ensures files are closed even on errors
- C) It prevents exceptions altogether
- D) It changes file permissions

<details>
<summary>Show Answer</summary>

**B)** `finally` guarantees cleanup.

</details>

---

[Back to Try/Except/Finally README](README.md) | [Next: Custom Exceptions →](../03_custom_exceptions/README.md)
