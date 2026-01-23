# 🧯 Try / Except / Finally

The `try` statement lets you **separate normal logic from error handling**. You can catch errors, run cleanup code, or execute alternative paths safely.

---

## ✅ Basic Pattern

```python
try:
    value = int(user_input)
except ValueError:
    print("Please enter a number")
```

---

## ✅ `else` and `finally`

- **`else`** runs only if no exception happened.
- **`finally`** runs *always* (success or failure), perfect for cleanup.

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    data = ""
else:
    print("Read successful")
finally:
    file.close()
```

---

## ✅ Catching Multiple Exceptions

```python
try:
    result = data["count"] / total
except (KeyError, ZeroDivisionError) as exc:
    print("Problem:", exc)
```

---

## ⚠️ Don’t Catch Too Broadly

```python
try:
    risky()
except Exception:
    pass  # hides bugs and makes debugging hard
```

Prefer catching **specific** errors you expect.

---

## 🔍 Key Takeaways

- Use `try/except` to handle known failure cases.
- Use `else` for success-only logic.
- Use `finally` for cleanup and releasing resources.

---

[Next: Custom Exceptions →](../03_custom_exceptions/README.md)
