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

## ⚠️ Common Mistakes

1. **Over-defensive code that hides bugs** - re-validating the same value in five
   functions, or wrapping everything in `try/except Exception: pass`, turns a clear
   crash into a silent `None` that breaks somewhere far away. Validate once, at the
   boundary, and let real bugs fail loudly.
2. **Validating in the wrong layer** - checks belong where the data enters (user input,
   file reader, API handler). Type and range checks buried deep in business logic fire
   too late to say which input was bad, and every internal caller pays for them.
   Internal invariants are what `assert` is for.
3. **Using `assert` for user input** - assertions are for programmer errors and vanish
   under `python -O`, so the guard you relied on silently disappears. Raise `ValueError`
   for data that comes from outside your program, and keep `assert` for "this can never
   happen" checks.

---

## 📝 Quick Reference

| Technique | Use it for | Example |
|---|---|---|
| Guard clause | reject bad input first thing | `if amount <= 0: raise ValueError("amount must be positive")` |
| Type check | data from outside the program | `if not isinstance(price, (int, float)): raise TypeError("price must be a number")` |
| Range check | known valid bounds | `if not (0 <= percent <= 100): raise ValueError("percent must be 0-100")` |
| `assert` | internal invariants only | `assert values, "values must not be empty"` |
| Default | optional configuration | `retries = retries if retries is not None else 3` |

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
