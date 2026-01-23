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

## 🔍 Key Takeaways

- Custom exceptions improve **readability and handling**.
- Inherit from a built-in exception when appropriate.
- Use hierarchies for related error types.

---

[Next: Defensive Programming →](../04_defensive_programming/README.md)
