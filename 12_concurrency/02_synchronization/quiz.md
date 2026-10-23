# 🧠 Synchronization Quiz

---

## Question 1
What problem does a `Lock` primarily solve?

- A) It makes code run faster
- B) It prevents two threads from entering a critical section at the same time
- C) It automatically retries failed network calls
- D) It creates new threads

<details>
<summary>Show Answer</summary>

**B)** A lock provides mutual exclusion for shared state.

</details>

---

## Question 2
Which primitive is best for simple one-way signaling between threads?

- A) `threading.Event`
- B) `threading.RLock`
- C) `threading.Barrier`
- D) `threading.local`

<details>
<summary>Show Answer</summary>

**A)** An `Event` is designed for signaling.

</details>

---

## Question 3
A method acquires a lock, then calls a helper method **on the same object**
that acquires the same lock again. Which lock lets this work without freezing?

- A) `threading.Lock`
- B) `threading.RLock` — it allows the owning thread to re-enter
- C) `threading.Semaphore(0)`
- D) No lock can do this

<details>
<summary>Show Answer</summary>

**B)** An `RLock` is reentrant: the same thread may acquire it again, and it
only frees up after a matching `release()` for every `acquire()`. A plain
`Lock` would deadlock the thread against itself.

</details>

---

## Question 4
What does `threading.Semaphore(3)` enforce?

- A) Only 3 threads may exist in the program
- B) At most 3 threads can hold the semaphore (enter the section) at once
- C) Threads wait exactly 3 seconds
- D) The section runs 3 times

<details>
<summary>Show Answer</summary>

**B)** A `Semaphore(n)` is a counter: `acquire` decrements, `release`
increments, and acquire blocks when the counter is zero.

</details>

---

## Question 5
`got = lock.acquire(timeout=1.0)` — what does `got == False` mean?

- A) The lock is broken
- B) The lock was acquired but is unusable
- C) The lock was NOT acquired within 1 second — back off instead of hanging forever
- D) Another thread released the lock

<details>
<summary>Show Answer</summary>

**C)** A timed acquire returns `False` when the wait expired. That is the
standard escape hatch from a potential deadlock: give up, then retry or take
another path.

</details>

---

[Back to Synchronization README](README.md)
