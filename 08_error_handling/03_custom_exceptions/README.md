# 🧩 Custom Exceptions

Custom exceptions let you **describe errors in your own domain language**. Instead of raising generic errors, you can create meaningful types that make debugging and handling clearer.

---

## ✅ Why Create Custom Exceptions?

- **Clarity:** `InvalidEmailError` is more meaningful than `ValueError`.
- **Control:** Callers can catch specific error types.
- **Structure:** You can build an error hierarchy.

---

## ✅ Defining a Custom Exception

```python
class InvalidEmailError(ValueError):
    pass


def register(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain '@'")
```

---

## ✅ Exception Hierarchies

```python
class PaymentError(Exception):
    pass


class CardDeclinedError(PaymentError):
    pass


class InsufficientFundsError(PaymentError):
    pass


class InvalidAmountError(PaymentError):
    pass
```

Catch a whole category or a specific subtype:

```python
try:
    charge(card)
except CardDeclinedError:
    handle_decline()
except PaymentError:
    handle_generic_payment_error()
```

---

## ⚠️ Common Mistakes

1. **A custom exception with no meaningful message** - `raise CardDeclinedError()`
   tells the caller nothing. Carry the context: `raise CardDeclinedError("limit 100,
   attempted 150")`. The traceback is only useful if it says what the invalid state was.
2. **Catching the base class when you meant the subclass** - `except PaymentError`
   also catches `CardDeclinedError` and `InvalidAmountError`, so a "declined" branch can
   quietly handle an "invalid amount" failure. `except` clauses are matched top to
   bottom, so put the specific type first and the category after it.
3. **Inventing a type where a built-in already fits** - `class MyError(Exception): pass`
   for something that simply *is* a bad value forces callers to learn your type for no
   gain. Subclass `ValueError` (as `InvalidEmailError` does) unless callers genuinely
   need to tell it apart from every other error.

---

## 📝 Quick Reference

| Task | Code |
|---|---|
| Define an app-wide category | `class PaymentError(Exception): pass` |
| Define one specific failure | `class CardDeclinedError(PaymentError): pass` |
| Raise it with context | `raise CardDeclinedError("limit 100, attempted 150")` |
| Catch the specific type first | `except CardDeclinedError as exc:` |
| Catch the whole category after | `except PaymentError:` |
| Re-raise without changing it | `raise` (inside the `except` block) |
| Is it that type? | `isinstance(exc, PaymentError)` |

```python
try:
    charge(150)
except CardDeclinedError as exc:      # most specific first
    print("declined:", exc)
except PaymentError as exc:           # then the category
    print("payment error:", exc)
```

---

## 🔍 Key Takeaways

- Custom exceptions improve **readability and handling**.
- Inherit from a built-in exception when appropriate.
- Use hierarchies for related error types.

---

[Next: Defensive Programming →](../04_defensive_programming/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
