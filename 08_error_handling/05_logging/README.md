# 🪵 Logging

Logging records **what happened and when** so you can debug failures and understand system behavior. Unlike `print`, logs are structured, configurable, and can be stored in files or external systems.

---

## ✅ Why Logging Matters

- **Debugging:** See context around failures.
- **Monitoring:** Track errors in production.
- **Auditing:** Keep a record of important events.

---

## ✅ Basic Logging Example

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("App started")
logging.warning("Low disk space")
logging.error("Failed to connect to database")
```

---

## ✅ Logging Levels

| Level | Use Case |
|---|---|
| DEBUG | Detailed diagnostic info |
| INFO | Normal events |
| WARNING | Unexpected, but not fatal |
| ERROR | Something failed |
| CRITICAL | App cannot continue |

---

## ✅ Logging Exceptions

```python
try:
    risky_operation()
except Exception:
    logging.exception("Something went wrong")
```

`logging.exception` records the traceback automatically.

---

## 🔍 Key Takeaways

- Use logging instead of print for real applications.
- Choose the right log level for each message.
- Log exceptions with tracebacks for faster debugging.

---

[Back: Defensive Programming ←](../04_defensive_programming/README.md)
