# 📜 Reading Tracebacks

A **traceback** is Python's error message showing where and why your code failed. Learning to read tracebacks quickly is essential for debugging.

---

## ✅ Traceback Structure

```
Traceback (most recent call last):
  File "script.py", line 10, in main
    result = process(data)
  File "script.py", line 5, in process
    return data['key']
KeyError: 'key'
```

Read from **bottom to top**:
1. **Exception type and message**: `KeyError: 'key'` - What went wrong
2. **Immediate cause**: Line 5 tried to access `data['key']`
3. **Call chain**: How we got there (main called process)

---

## ✅ Common Exception Types

| Exception | Meaning | Common Cause |
|-----------|---------|--------------|
| `SyntaxError` | Invalid Python syntax | Missing colon, bracket, quote |
| `NameError` | Name not defined | Typo, forgot to define/import |
| `TypeError` | Wrong type for operation | Passing wrong argument type |
| `ValueError` | Right type, wrong value | Invalid conversion |
| `KeyError` | Dict key not found | Missing or misspelled key |
| `IndexError` | List index out of range | Off-by-one error |
| `AttributeError` | Object has no attribute | Wrong method name, None value |
| `ImportError` | Can't import module | Module not installed or typo |
| `FileNotFoundError` | File doesn't exist | Wrong path |

---

## ✅ Reading Tips

**Start from the bottom:**
```
KeyError: 'username'
```
This tells you the key `'username'` wasn't in the dictionary.

**Look at the last file/line that's YOUR code:**
```
  File "myapp/views.py", line 42, in get_user
    return data['username']
```
This is probably where you need to fix something.

**Trace the call chain:**
See how execution reached the error point.

---

## ✅ Chained Exceptions

Python 3 shows exception chains:

```
Traceback (most recent call last):
  File "app.py", line 5, in load_config
    data = json.load(f)
json.JSONDecodeError: Expecting property name: line 2

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "app.py", line 10, in main
    config = load_config()
  File "app.py", line 8, in load_config
    raise ConfigError("Invalid config file")
ConfigError: Invalid config file
```

Read both parts to understand the full story.

---

## ✅ SyntaxError Tracebacks

Syntax errors look different:

```
  File "script.py", line 5
    if x == 1
           ^
SyntaxError: expected ':'
```

The `^` points to where Python got confused (often the error is just before).

---

## ✅ Improving Tracebacks

```python
# Use rich library for colorful tracebacks
from rich import traceback
traceback.install()

# Use better_exceptions
import better_exceptions
better_exceptions.hook()
```

---

## 🔍 Key Takeaways

- Read tracebacks **bottom to top**.
- The exception type tells you **what** happened.
- The line number tells you **where**.
- Follow the call chain to understand **how** you got there.
- Your fix is usually in the last frame showing your code.

---

[Back: Using Debuggers](../02_using_debuggers/) | [Next: Common Bugs](../04_common_bugs/)
