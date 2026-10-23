# 🧵 Threads Basics

A **thread** is an OS-level unit of execution inside a process. Multiple threads share the same memory, which makes communication easy—but also makes bugs (like races) easy.

Python threads are most useful for **I/O-bound work**:

- waiting for network responses
- reading/writing files
- calling slow APIs

> For CPU-bound work, Python's **GIL** (Global Interpreter Lock) often prevents threads from running Python bytecode in parallel. In those cases, prefer processes.

---

## ✅ Creating and Joining Threads

```python
import threading

def worker():
    print("Hello from a thread")

t = threading.Thread(target=worker)
t.start()
t.join()
```

- `start()` begins running the thread.
- `join()` waits for it to finish.

---

## ✅ Thread Pools

For many small tasks, use a **thread pool**:

- `concurrent.futures.ThreadPoolExecutor`
- `executor.submit(...)` / `executor.map(...)`

Thread pools manage thread creation and reuse for you.

---

## ✅ When Threads Are Not Enough: `multiprocessing`

The **GIL** lets only one thread execute Python bytecode at a time. For
**CPU-bound** work (heavy math, image processing, parsing gigabytes), threads
do not add speed — the threads take turns, not run side by side.

Processes sidestep the GIL: each process gets its own interpreter with its own
GIL, and the OS runs processes truly in parallel on multiple cores.

```python
import multiprocessing

def cpu_sum(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":      # required on Windows and macOS (spawn)
    p = multiprocessing.Process(target=cpu_sum, args=(2_000_000,))
    p.start()
    p.join()
    print("exit code:", p.exitcode)
```

The `if __name__ == "__main__":` guard is **not optional** on Windows: there,
new processes start by re-importing your module, and without the guard each
child would try to start children of its own, forever.

Rules of thumb:

- **I/O-bound** -> threads (or `asyncio`)
- **CPU-bound** -> processes (`multiprocessing`, `ProcessPoolExecutor`)

A runnable version of this demo is in this topic's `examples.py`.

---

## 🔍 Key Takeaways

- Threads overlap work, especially when waiting on I/O.
- Always `join()` (or use a pool) when you need results.
- Be careful with shared state—synchronization comes next.

---

## ⚠️ Common Mistakes

- Using threads for CPU-bound work and wondering why nothing got faster (the GIL)
- Forgetting `join()` and reading results before the thread produced them
- Sharing a plain list/dict across threads and mutating it without a lock (see [Race Conditions](../04_race_conditions/README.md))
- Writing `multiprocessing` code without the `if __name__ == "__main__":` guard — it breaks on Windows

---

## 📝 Quick Reference

```python
import threading
t = threading.Thread(target=f, args=(1,))
t.start()      # begin running
t.join()       # wait until done

from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(f, items))

import multiprocessing
p = multiprocessing.Process(target=f, args=(1,))
p.start()
p.join(timeout=10)     # wait, but never forever
```

Threads for I/O-bound work, processes for CPU-bound work.

---

[Back: Module 12 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
