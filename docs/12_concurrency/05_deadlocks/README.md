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
- **Timeouts:** use `lock.acquire(timeout=...)` and back off
- **Reduce shared state:** fewer locks, fewer problems
- **Use higher-level designs:** queues, actors, single owner of state

---

## 🔍 Key Takeaways

- Deadlocks are often caused by inconsistent lock ordering.
- The simplest fix is often a design fix (reduce lock sharing).

---

[Back: Module 12 README](../README.md)
