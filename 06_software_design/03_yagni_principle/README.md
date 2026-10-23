# 🚫 YAGNI Principle (You Aren't Gonna Need It)

**YAGNI** means: don’t build features, abstractions, or flexibility until you actually need them. It’s a guardrail against speculative design.

---

## ✅ What YAGNI Prevents

Common “future-proofing” traps:

- Building a plugin system for a script with one use case
- Adding configuration options nobody asked for
- Writing generalized frameworks instead of finishing the task

---

## ✅ Why YAGNI Matters

- **Less code:** Fewer bugs and less maintenance.
- **Faster delivery:** Ship working value sooner.
- **Better designs:** Real requirements create better abstractions than guesses.

---

## ⚠️ YAGNI Doesn’t Mean “No Planning”

You can still design with:

- Clear boundaries
- Good naming
- Modest, reversible choices

YAGNI only says: don’t pay the cost of complexity **before** the value exists.

---

## ✅ Example: Avoid Premature Generalization

Before (generalized too soon):

```python
class StorageBackend:
    def save(self, key, value):
        raise NotImplementedError
```

If you only need a dictionary today, start simple:

```python
def save(store, key, value):
    store[key] = value
```

When requirements change (e.g., DB storage), *then* introduce an interface.

---

## 🔍 Key Takeaways

- Build for current requirements, not imagined ones.
- Prefer small, reversible steps.
- Let abstractions emerge from real repetition and constraints.

---

[Back: KISS Principle](../02_kiss_principle/README.md) | [Next: Separation of Concerns](../04_separation_of_concerns/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
