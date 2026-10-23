# 🧠 Threads Basics Quiz

---

## Question 1
What does `thread.join()` do?

- A) Starts a thread
- B) Stops a thread immediately
- C) Waits for a thread to finish
- D) Makes a thread run faster

<details>
<summary>Show Answer</summary>

**C)** `join()` blocks until the thread completes.

</details>

---

## Question 2
When are Python threads usually most beneficial?

- A) CPU-heavy math and image processing
- B) I/O-bound work (waiting on network/files)
- C) Replacing all for-loops
- D) Increasing recursion depth

<details>
<summary>Show Answer</summary>

**B)** Threads help overlap waiting on I/O.

</details>

---

## Question 3
What does `ThreadPoolExecutor.map(func, items)` do?

- A) Creates a dict from `items`
- B) Runs `func` on every item across pool threads and gives the results back in order
- C) Runs `func` on one item only
- D) Maps memory for a new thread

<details>
<summary>Show Answer</summary>

**B)** The pool distributes the work over its threads; results come back in
the input order.

</details>

---

## Question 4
Why don't threads speed up pure-Python **CPU-bound** work?

- A) Threads cannot call functions
- B) The GIL lets only one thread execute Python bytecode at a time, so they take turns
- C) Threads are slower than processes for all work
- D) The OS refuses to schedule more than one thread

<details>
<summary>Show Answer</summary>

**B)** The Global Interpreter Lock serializes bytecode execution. For
CPU-bound work, use `multiprocessing` instead — each process has its own GIL.

</details>

---

## Question 5
Which multiprocessing detail is **required** on Windows?

- A) Using `ProcessPoolExecutor` instead of `Process`
- B) Putting the launching code under `if __name__ == "__main__":`
- C) Calling `join()` before `start()`
- D) Passing all arguments as strings

<details>
<summary>Show Answer</summary>

**B)** Windows starts child processes by re-importing your module; without
the guard, each child would try to launch children of its own, forever.

</details>

---

[Back to Threads Basics README](README.md)
