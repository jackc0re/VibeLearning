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

## ✅ Logging vs `print`

`print` is fine while you are learning. Logging is what real programs use, for four reasons:

| Need | `print` | `logging` |
|---|---|---|
| Hide noisy detail | Delete or comment the line out | Filter by level: `logger.setLevel(...)` |
| Send output somewhere else | stdout only; redirect by hand | Handlers: console, file, syslog |
| Know *when* it happened | Stamp the time yourself | `%(asctime)s` adds it for you |
| Silence a noisy library | Impossible - it prints at you | Set that logger's level, leave yours alone |

The last row is the decisive one: a library cannot `print` at you, but it *can* log - and
whether those records are shown is your decision, not the library's.

---

## ✅ Formatting the Output

`basicConfig` configures the root logger once. The `format` string is a template that
logging fills in, so timestamps and level names come for free:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)

logging.info("App started")
# 14:03:07 | INFO     | root | App started
```

`name` shows which logger spoke - `root` here, because `logging.info(...)` is a
shortcut for the root logger.

---

## ✅ Handlers: Sending Logs to a File

A **logger** creates records; a **handler** delivers them somewhere. `FileHandler`
writes them to a file, so they outlive the terminal window:

```python
import logging
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    log_path = Path(tmp) / "app.log"

    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    logger.propagate = False            # do not also hand records to the root logger

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.name = "app-file"      # name it: real programs attach several handlers
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%H:%M:%S",
        )
    )
    logger.addHandler(file_handler)

    logger.info("Job started")
    logger.warning("Retrying request")

    file_handler.close()
    logger.removeHandler(file_handler)

    print(log_path.read_text(encoding="utf-8"))
    # 14:03:07 | INFO     | Job started
    # 14:03:07 | WARNING  | Retrying request
```

The demo in [examples.py](examples.py) writes to exactly this kind of temporary file,
reads it back, and lets `tempfile` delete it - no stray log files left in your repo.

---

## ✅ Named Loggers Beat the Root Logger

`logging.info(...)` logs through the **root** logger, which everything shares. Inside a
module, create your own logger instead:

```python
import logging

logger = logging.getLogger(__name__)   # "billing.invoice" when imported


def send_invoice(invoice):
    logger.info("Sending invoice %s", invoice.id)
```

Three reasons it is worth the extra line:

- The name lands in the output (`%(name)s`), so you can see *which module* spoke.
- You can turn one module up or down without touching the rest:
  `logging.getLogger("billing.invoice").setLevel(logging.DEBUG)`.
- Importing your module never reconfigures logging - deciding where output goes is the
  application's job, not a library's.

Run [examples.py](examples.py) as a script and `__name__` is `"__main__"`; import the
same file elsewhere and that same line logs under the module's name.

---

## ✅ Filtering by Level (`LOG_LEVEL`)

A logger's level is a **threshold**: a record is emitted only if its level is at or
above it. Same code, three settings:

```python
def report(logger):
    logger.debug("detail: row 42 parsed")
    logger.info("normal: import finished")
    logger.warning("unusual: 3 rows skipped")
```

| `logger.setLevel(...)` | What reaches the handler |
|---|---|
| `logging.DEBUG` | all three lines |
| `logging.INFO` | two lines (info and warning) |
| `logging.WARNING` | one line (warning only) |

Because the levels are plain integers (`DEBUG` 10, `INFO` 20, `WARNING` 30, `ERROR` 40,
`CRITICAL` 50), a level name from configuration converts with `getattr`:

```python
import logging
import os

level_name = os.environ.get("LOG_LEVEL", "INFO").upper()
logger.setLevel(getattr(logging, level_name, logging.INFO))   # unknown name -> INFO
```

That is why `LOG_LEVEL=DEBUG` is such a common switch: bigger window, no code change.

---

## ⚠️ Common Mistakes

1. **`print` debugging left in production** - nobody can switch it off, it has no level,
   and it lands in the middle of user-facing output. Replace it with `logger.debug(...)`.
2. **The wrong level for the event** - logging an expected, recoverable case at `ERROR`
   teaches everyone to ignore errors. Normal (`INFO`), unusual (`WARNING`), failed
   (`ERROR`), cannot continue (`CRITICAL`)?
3. **An f-string inside the logging call** - `logger.info(f"user {name} logged in")`
   builds the string even when the record is filtered out, and log tooling can no longer
   group messages. Use lazy formatting: `logger.info("user %s logged in", name)`.
4. **No handler configured, so the messages vanish** - `basicConfig()` only acts the
   *first* time it runs (later calls are silently ignored), and with no handler at all
   `DEBUG`/`INFO` records go nowhere - a last-resort handler shows only `WARNING` and
   above. Configure logging once, at startup, before the first log call.

---

## 📝 Quick Reference

| Task | Code |
|---|---|
| Configure once | `logging.basicConfig(level=logging.INFO, format=...)` |
| Get a module logger | `logger = logging.getLogger(__name__)` |
| Log a message | `logger.info("user %s logged in", name)` |
| Log an exception | `logger.exception("upload failed")` |
| Change one logger's level | `logger.setLevel(logging.DEBUG)` |
| Send records to a file | `logging.FileHandler("app.log", encoding="utf-8")` |
| Attach / detach a handler | `logger.addHandler(h)` / `logger.removeHandler(h)` |
| Format placeholders | `%(asctime)s %(levelname)s %(name)s %(message)s` |
| Numeric levels | DEBUG 10, INFO 20, WARNING 30, ERROR 40, CRITICAL 50 |

---

## 🔍 Key Takeaways

- Use logging instead of print for real applications.
- Choose the right log level for each message.
- Log exceptions with tracebacks for faster debugging.

---

[Back: Defensive Programming ←](../04_defensive_programming/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
