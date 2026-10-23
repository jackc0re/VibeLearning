# 🧠 Deadlocks Quiz

---

## Question 1
What is a deadlock?

- A) A thread that runs too quickly
- B) Two threads waiting forever due to circular resource dependency
- C) A syntax error in multithreaded code
- D) A missing import

<details>
<summary>Show Answer</summary>

**B)** Deadlocks commonly happen when locks are acquired in inconsistent order.

</details>

---

## Question 2
A common deadlock prevention strategy is:

- A) Acquiring locks in a consistent global order
- B) Using more threads
- C) Calling `join()` less often
- D) Converting lists to tuples

<details>
<summary>Show Answer</summary>

**A)** Lock ordering prevents circular wait.

</details>

---

## Question 3
`got = lock.acquire(timeout=1.0)` times out. What is `got`?

- A) `True`
- B) `False` — the lock was not acquired, and the thread can back off
- C) `None`
- D) The call raises `DeadlockError`

<details>
<summary>Show Answer</summary>

**B)** A timed acquire returns `False` when it gave up waiting. That lets the
thread back off instead of hanging forever — the escape hatch used in this
topic's `examples.py`.

</details>

---

## Question 4
Which situation is the classic deadlock setup?

- A) Thread 1 holds lock A and waits for lock B, while Thread 2 holds lock B and waits for lock A
- B) Two threads use the same lock one after the other
- C) A thread calls `join()` on itself
- D) A thread sleeps for one second

<details>
<summary>Show Answer</summary>

**A)** Each holds what the other needs, so neither can ever proceed — a
circular wait.

</details>

---

## Question 5
Why does consistent lock ordering prevent deadlock?

- A) It makes locks faster
- B) A circular wait can never form if every thread acquires the same locks in the same order
- C) It hides locks from the operating system
- D) Ordered locks release automatically

<details>
<summary>Show Answer</summary>

**B)** Deadlock needs a cycle: someone holding X while waiting for Y, while
someone else holds Y and waits for X. With one global order, the "later"
lock is only ever taken after the "earlier" one, so no cycle can close.

</details>

---

[Back to Deadlocks README](README.md)
