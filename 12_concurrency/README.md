# ⚡ Module 12: Concurrency

Concurrency is about doing **multiple things at once** (or at least *overlapping* their progress).

In Python, concurrency usually shows up in three practical forms:

- **Threads** (`threading`, `concurrent.futures.ThreadPoolExecutor`) for I/O-bound work
- **Async** (`asyncio`) for high-concurrency I/O without many OS threads
- **Processes** (`multiprocessing`, `ProcessPoolExecutor`) for CPU-bound parallelism (briefly mentioned)

> **Estimated Time:** 10-12 hours  \
> **Prerequisites:** Modules 01-05  \
> **Level:** ⭐⭐⭐⭐ Advanced

---

## 📚 Topics Covered

| # | Topic | Description | Key Concepts |
|---|-------|-------------|--------------|
| 01 | [Threads Basics](01_threads_basics/) | Starting and joining threads | `Thread`, `join()`, thread pools |
| 02 | [Synchronization](02_synchronization/) | Coordinating shared state safely | `Lock`, `Event`, `Semaphore`, `Queue` |
| 03 | [Async Programming](03_async_programming/) | Cooperative concurrency with `asyncio` | `async`/`await`, tasks, `gather()` |
| 04 | [Race Conditions](04_race_conditions/) | Understanding data races and fixes | atomicity, locks, message passing |
| 05 | [Deadlocks](05_deadlocks/) | Avoiding "stuck forever" situations | lock ordering, timeouts, design |

---

## 🎯 Learning Goals

By the end of this module, you should be able to:

- Choose between **threads** and **async** based on the problem.
- Protect shared state with the right **synchronization primitive**.
- Explain what a **race condition** is and how to prevent it.
- Recognize and avoid common **deadlock** patterns.
- Write concurrent code that is correct, testable, and maintainable.

---

## 📂 Module Structure

```
12_concurrency/
├── README.md
├── 01_threads_basics/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 02_synchronization/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 03_async_programming/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 04_race_conditions/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
└── 05_deadlocks/
    ├── README.md
    ├── examples.py
    ├── exercises.py
    └── quiz.md
```

---

**Start here:** [01_threads_basics](01_threads_basics/)
