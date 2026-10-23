# 🪢 Deadlocks

A **deadlock** is when two or more threads wait forever because each is holding a resource the other needs.

Classic scenario:

- Thread A holds **Lock 1** and waits for **Lock 2**
- Thread B holds **Lock 2** and waits for **Lock 1**

No one can proceed.

---

## ✅ How Deadlocks Happen

Deadlocks usually appear when:

- you hold multiple locks at once
- different code paths acquire locks in different orders

---

## ✅ Prevention Strategies

- **Lock ordering:** always acquire multiple locks in a consistent order
- **Timeouts:** use `lock.acquire(timeout=...)` — on timeout it **returns `False`** instead of blocking forever, so you can back off and retry
- **Reduce shared state:** fewer locks, fewer problems
- **Use higher-level designs:** queues, actors, single owner of state

---

## 🔍 Key Takeaways

- Deadlocks are often caused by inconsistent lock ordering.
- The simplest fix is often a design fix (reduce lock sharing).

---

## ⚠️ Common Mistakes

- Acquiring a second lock while holding the first — with a different order somewhere else in the code
- Calling `lock.acquire()` with no timeout in code that takes multiple locks (a deadlock then hangs forever)
- Running callbacks or unknown code while holding a lock — it may grab more locks behind your back
- Forgetting that `with lock:` blocks too — two `with` blocks nested in crossed orders deadlock just the same

---

## 📝 Quick Reference

```python
# Back off instead of hanging forever:
got = lock.acquire(timeout=0.5)
if got:
    try:
        ...
    finally:
        lock.release()
# got is False when the timeout expired - treat that as "try later"

# Consistent global order for multiple locks:
first, second = sorted((lock_a, lock_b), key=id)
with first:
    with second:
        ...
```

`examples.py` for this topic shows the crossed-lock pattern rescued by a
timeout — including why you see `False` in its output.

---

[Back: Module 12 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
