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

## Question 3
A coroutine calls `time.sleep(5)`. What happens to the event loop?

- A) Nothing, other tasks keep running
- B) The whole loop is blocked for 5 seconds — every task stalls
- C) The sleep is automatically converted to `asyncio.sleep`
- D) The coroutine raises `TypeError`

<details>
<summary>Show Answer</summary>

**B)** `time.sleep` blocks the single OS thread the loop runs on. Inside a
coroutine, use `await asyncio.sleep(...)` so control returns to the loop.

</details>

---

## Question 4
What does `asyncio.create_task(coro())` do?

- A) Runs `coro()` immediately to completion
- B) Schedules the coroutine on the event loop and returns a `Task` you can await later
- C) Creates an OS thread for the coroutine
- D) Cancels the coroutine

<details>
<summary>Show Answer</summary>

**B)** `create_task` starts the coroutine "in the background" of the loop;
await the returned `Task` (or `gather` it) to get the result.

</details>

---

## Question 5
You must make 1,000 web requests but never more than 5 at a time. What is the
idiomatic asyncio tool?

- A) `asyncio.Semaphore(5)` wrapped around each request's `await`
- B) 1,000 OS threads
- C) `time.sleep(0.001)` between requests
- D) `asyncio.gather()` alone

<details>
<summary>Show Answer</summary>

**A)** An `asyncio.Semaphore(5)` used with `async with` caps concurrent
requests while `gather` still drives all 1,000 tasks.

</details>

---

[Back to Async Programming README](README.md)
