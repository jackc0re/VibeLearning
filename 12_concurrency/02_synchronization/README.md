# 🔒 Synchronization

Threads share memory, which means two threads can read/write the **same data** at the same time.

Synchronization primitives help you coordinate access and avoid corruption.

---

## ✅ Locks

A `Lock` protects a critical section:

```python
import threading

lock = threading.Lock()

with lock:
    # only one thread at a time here
    shared_counter += 1
```

Use the smallest critical section possible.

---

## ✅ Events

An `Event` is a simple signal:

- one thread waits: `event.wait()`
- another thread signals: `event.set()`

---

## ✅ Semaphores

A `Semaphore` limits how many threads may enter a section concurrently.

---

## ✅ Prefer Message Passing

Often the cleanest approach is to avoid sharing state:

- use `queue.Queue` to pass work/results between threads
- let each thread own its local state

---

## 🔍 Key Takeaways

- Use `Lock` when you must share state.
- Use `Event` for one-way signaling.
- Use `Queue` to reduce shared-state complexity.

---

[Back: Module 12 README](../README.md)
