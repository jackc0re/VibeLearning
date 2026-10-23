# 🛡️ Defensive Programming

Defensive programming is about **preventing errors before they happen**. You validate inputs, check assumptions, and create clear guardrails so code fails fast and predictably.

---

## ✅ Common Defensive Techniques

- **Input validation:** check types, ranges, and formats.
- **Guard clauses:** return early for invalid states.
- **Assertions:** verify internal assumptions.
- **Defaults:** provide safe fallbacks.

---

## ✅ Example: Guard Clauses

```python
def transfer(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

---

## ✅ Assertions (Internal Checks)

```python
def average(values):
    assert values, "values must not be empty"
    return sum(values) / len(values)
```

Use assertions for **programmer errors**, not user input.

---

## 🔍 Key Takeaways

- Validate inputs early and clearly.
- Guard clauses keep code readable.
- Assertions document internal assumptions.

---

[Next: Logging →](../05_logging/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
