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

## ✅ Reentrant Locks (`RLock`)

A regular `Lock` has a surprising rule: it blocks **even if the same thread
acquires it twice**. A thread that owns a `Lock` and asks for it again waits
forever — waiting for itself.

An `RLock` ("reentrant lock") removes that trap: **the thread that owns it may
acquire it again**, and the lock is only released when every `acquire()` has a
matching `release()` (it *counts*).

Think of it as **a key the owner may reuse while still inside**: re-entering
your own room is fine, but other people still have to knock and wait — and the
lock only frees up once you have left exactly as many times as you entered.

```python
import threading

lock = threading.RLock()

class Basket:
    def __init__(self) -> None:
        self.items: list[str] = []
        self._lock = threading.RLock()

    def add(self, item: str) -> None:
        with self._lock:      # acquire 1
            self._audit()     # ...which calls a method that acquires again
            self.items.append(item)

    def _audit(self) -> None:
        with self._lock:      # acquire 2 - same thread, OK with RLock
            print(f"audit: {len(self.items)} item(s) so far")
```

With a plain `Lock`, `add()` would deadlock on the second acquire. Use `RLock`
only for genuinely re-entrant call paths like this; prefer a plain `Lock`
otherwise (it is simpler and slightly faster).

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

## ⚠️ Common Mistakes

- Acquiring a plain `Lock` twice from the same thread (deadlock) — that case needs an `RLock`
- Holding a lock while doing slow work (I/O, sleeps) — keep critical sections small
- Locking in different places in different orders — that is the road to [deadlocks](../05_deadlocks/README.md)
- Reaching for shared state when a `queue.Queue` would remove the need for a lock

---

## 📝 Quick Reference

| Primitive | Use it for |
|-----------|------------|
| `Lock` | mutual exclusion around a critical section |
| `RLock` | critical sections that re-enter (same thread acquires again) |
| `Event` | one-way signal: "something happened" |
| `Semaphore(n)` | allow at most `n` threads inside |
| `queue.Queue` | pass messages instead of sharing state |

```python
with lock:            # acquire/release pair (also for RLock, Semaphore)
    ...

event.wait()          # block until event.set()
q = queue.Queue()
q.put(item) / q.get() # thread-safe message passing
```

---

[Back: Module 12 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
