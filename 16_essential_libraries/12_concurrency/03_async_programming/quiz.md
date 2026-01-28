# 🧠 Async Programming Quiz

---

## Question 1
In asyncio, when can other tasks run?

- A) Only when you call `print()`
- B) At `await` points
- C) Only when the program exits
- D) When you create a new thread

<details>
<summary>Show Answer</summary>

**B)** Tasks switch at `await` points.

</details>

---

## Question 2
What does `asyncio.gather()` return?

- A) A list of results from awaited coroutines
- B) A new OS thread
- C) A file handle
- D) A lock

<details>
<summary>Show Answer</summary>

**A)** It waits for all provided awaitables and returns their results.

</details>

---

[Back to Async Programming README](README.md)
