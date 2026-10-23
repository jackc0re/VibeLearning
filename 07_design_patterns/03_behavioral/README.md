# 🧠 Behavioral Design Patterns

Behavioral patterns focus on **how objects communicate and share responsibilities**. They help you design interactions that are flexible, testable, and easy to change.

---

## ✅ Why Behavioral Patterns Matter

- **Reduce tight coupling** between objects that need to collaborate.
- **Encapsulate behavior** so it can change independently.
- **Make systems extensible** by plugging in new behaviors.

---

## ✅ Common Behavioral Patterns

### 1) Observer
One object (subject) notifies multiple observers when its state changes.

✅ Use when: you need event-style updates (UI updates, notifications).

### 2) Strategy
Encapsulates interchangeable algorithms behind a common interface.

✅ Use when: you want to swap logic without changing the caller.

### 3) Command
Encapsulates an action as an object, enabling queues, history, or undo.

✅ Use when: you need to log, delay, or undo operations.

---

## ✅ Example: Strategy

```python
class StandardShipping:
    def cost(self, total):
        return 5 if total < 50 else 0


class ExpressShipping:
    def cost(self, total):
        return 15


def checkout(total, shipping_strategy):
    return total + shipping_strategy.cost(total)


total = checkout(40, ExpressShipping())
```

---

## 🔍 Key Takeaways

- Behavioral patterns structure collaboration between objects.
- Observers react to events without direct coupling.
- Strategies and commands make behavior swappable and reusable.

---

[Back: Structural Patterns](../02_structural/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
