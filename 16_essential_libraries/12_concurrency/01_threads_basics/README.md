# 🧵 Threads Basics

A **thread** is an OS-level unit of execution inside a process. Multiple threads share the same memory, which makes communication easy—but also makes bugs (like races) easy.

Python threads are most useful for **I/O-bound work**:

- waiting for network responses
- reading/writing files
- calling slow APIs

> For CPU-bound work, Python’s **GIL** (Global Interpreter Lock) often prevents threads from running Python bytecode in parallel. In those cases, prefer processes.

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

## 🔍 Key Takeaways

- Threads overlap work, especially when waiting on I/O.
- Always `join()` (or use a pool) when you need results.
- Be careful with shared state—synchronization comes next.

---

[Back: Module 12 README](../README.md)
