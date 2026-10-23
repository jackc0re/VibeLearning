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

## ⚠️ Common Mistakes

- Trusting the GIL to make `counter += 1` safe — it is a multi-step read-modify-write and can interleave
- "Fixing" a race by adding `sleep()` calls — it makes the bug rarer, not impossible
- Two locks guarding one invariant (each update must lock **both** — or the race survives half-protected)

---

## 📝 Quick Reference

```python
counter += 1          # NOT atomic: load, add, store (racy)

with lock:            # mutual exclusion makes it atomic
    counter += 1

q = queue.Queue()     # or avoid sharing: pass messages instead
q.put(item)
q.get()
```

---

[Back: Module 12 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
