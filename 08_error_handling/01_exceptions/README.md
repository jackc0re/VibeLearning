# ⚠️ Exceptions

Exceptions are **runtime signals** that something went wrong. Instead of silently failing, Python raises an exception and unwinds the call stack until it’s handled.

---

## ✅ What Is an Exception?

- A **type** that represents an error (e.g., `ValueError`, `KeyError`).
- A **message** that describes the problem.
- A **stack trace** showing where the error happened.

Exceptions can be **raised** by Python or by your own code.

---

## ✅ Why Exceptions Matter

- They **stop incorrect execution** early.
- They let you **separate normal logic** from error handling.
- They help you **find bugs faster** with tracebacks.

---

## ✅ Common Built-in Exceptions

| Exception | Typical Cause | Example |
|---|---|---|
| `ValueError` | Wrong value type/format | `int("abc")` |
| `TypeError` | Wrong operation for type | `"3" + 4` |
| `KeyError` | Missing dict key | `data["missing"]` |
| `IndexError` | Invalid list index | `items[10]` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |

---

## ✅ Raising Exceptions

You can raise your own exceptions to enforce rules:

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

---

## 🔍 Key Takeaways

- Exceptions are **signals of failure** with context.
- Built-in exceptions cover most common errors.
- Raising errors early prevents silent bugs.

---

[Next: Try/Except/Finally →](../02_try_except_finally/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
