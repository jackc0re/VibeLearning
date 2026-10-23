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
Python 3.10+ says `expected ':'`; 3.8 and 3.9 say `invalid syntax`.

---

## ✅ Improving Tracebacks

These third-party packages make tracebacks easier to read, but they are **not**
part of the standard library - they need `pip install`:

```python
# Use rich library for colorful tracebacks
from rich import traceback
traceback.install()

# Use better_exceptions
import better_exceptions
better_exceptions.hook()
```

With nothing installed, the standard-library `traceback` module already gives
you the same information (`traceback.print_exc()` in `examples.py`).

---

## ⚠️ Common Mistakes

1. **Reading top-to-bottom** - the most recent call is at the **bottom**, and
   the exception line (the actual error) is the very last line. Start there,
   then find the last frame that is *your* code.
2. **Fixing only the symptom line** - the failing line tells you *where* the
   crash happened, not always *why*. A `KeyError` on `data['key']` may really
   be a misspelled key created ten lines earlier.
3. **Pasting traceback text instead of the exception type into a search** -
   search for `TypeError: cannot unpack non-iterable int object`, not the whole
   dump with your file paths in it.
4. **Ignoring chained exceptions** - when you see "During handling of the above
   exception, another exception occurred", the *first* traceback is usually the
   root cause; read both.

---

## 📝 Quick Reference

| Part of the traceback | What it tells you |
|---|---|
| Last line: `KeyError: 'key'` | the error type + message (read first) |
| Frame lines: `File "app.py", line 42` | the call chain, oldest at top |
| `^` under `SyntaxError` code | where parsing got confused |
| `The above exception was the direct cause...` | exception chaining (`raise ... from err`) |
| `ZeroDivisionError` | a denominator was 0 - find where it came from |

```python
import traceback
try:
    risky()
except Exception:
    traceback.print_exc()   # print the full traceback and keep going
```

---

## 🔍 Key Takeaways

- Read tracebacks **bottom to top**.
- The exception type tells you **what** happened.
- The line number tells you **where**.
- Follow the call chain to understand **how** you got there.
- Your fix is usually in the last frame showing your code.

---

[Back: Using Debuggers](../02_using_debuggers/README.md) | [Next: Common Bugs](../04_common_bugs/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
