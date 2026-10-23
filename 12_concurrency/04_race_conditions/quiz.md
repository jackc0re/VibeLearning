# 🧠 Race Conditions Quiz

---

## Question 1
What is a race condition?

- A) A program that runs too fast
- B) A bug where correctness depends on timing/interleaving
- C) A type of syntax error
- D) A thread that never starts

<details>
<summary>Show Answer</summary>

**B)** Races depend on timing and interleaving.

</details>

---

## Question 2
Which is a common way to prevent races on shared state?

- A) Use a `Lock` around the critical section
- B) Add more `print()` statements
- C) Use `break` in loops
- D) Turn the code into a class

<details>
<summary>Show Answer</summary>

**A)** Locks provide mutual exclusion.

</details>

---

## Question 3
Why is `counter += 1` not atomic, even with the GIL?

- A) Integers are too large for one CPU instruction
- B) It is several steps (read, add, write) and a thread can be switched out between them
- C) The GIL only protects dicts
- D) It is atomic, but only on Windows

<details>
<summary>Show Answer</summary>

**B)** Two threads can both read the old value, both add one, and both write
back — one increment is lost. The GIL does not make multi-step operations
atomic.

</details>

---

## Question 4
Two threads each run `counter += 1` once, starting from 0, with no lock.
Which final value is **possible**?

- A) Only 2
- B) 1 — one update was lost when both read the same starting value
- C) Only 0
- D) -1

<details>
<summary>Show Answer</summary>

**B)** If both read 0 before either writes, the last write wins and the
result is 1 instead of 2. That is a lost update.

</details>

---

## Question 5
Which design avoids shared mutable state altogether?

- A) A global dict protected by a very big lock
- B) Passing messages between threads with `queue.Queue`
- C) Adding `time.sleep(0)` inside loops
- D) Using more threads than CPU cores

<details>
<summary>Show Answer</summary>

**B)** With a queue, each thread owns its own state and communicates by
passing data — there is nothing shared to race over.

</details>

---

[Back to Race Conditions README](README.md)
