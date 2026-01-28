# 🏁 Race Conditions

A **race condition** happens when the correctness of your program depends on timing.

Typical pattern:

1. Thread A reads shared state
2. Thread B changes it
3. Thread A writes back using stale information

Even with the GIL, many multi-step operations ("read-modify-write") are not atomic.

---

## ✅ Classic Example: Shared Counter

Two threads both run:

```python
counter = counter + 1
```

That statement is multiple bytecode operations: load, add, store. Another thread can interleave between those steps.

---

## ✅ Fixes

- Protect the critical section with `threading.Lock`
- Avoid shared mutable state (message passing, `queue.Queue`)
- Use higher-level primitives (thread-safe queues, executors)

---

## 🔍 Key Takeaways

- A race condition is a *correctness* bug, not just "weird behavior".
- If you share state, you need a strategy: lock, queue, or redesign.

---

[Back: Module 12 README](../README.md)
