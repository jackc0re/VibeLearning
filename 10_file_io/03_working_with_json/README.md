# 🧩 Working with JSON

JSON (JavaScript Object Notation) is a **text-based** format for structured data.
In Python, you work with JSON via the built-in `json` module.

---

## ✅ JSON Basics

```python
import json

data = {"name": "Ada", "age": 30, "skills": ["python", "math"]}

text = json.dumps(data)      # Python -> JSON string
obj = json.loads(text)       # JSON string -> Python
```

---

## ✅ JSON + Files

```python
import json

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
```

---

## ⚠️ Common Mistakes

1. **Mixing up the four functions** - `dump`/`load` talk to **files**,
   `dumps`/`loads` talk to **strings** (the trailing `s` = string). Calling
   `json.dump(data)` with no file raises `TypeError`.
2. **Dumping non-JSON types** - `set`, `datetime`, and custom classes are not
   JSON, so `json.dumps({1, 2})` raises
   `TypeError: Object of type set is not JSON serializable`.
   (A `tuple` does serialize - it comes back as a list.) Convert exotic types
   before dumping.
3. **Forgetting `encoding="utf-8"`** - JSON is UTF-8 by spec. On Windows the
   default text encoding may not be, and non-ASCII data (`"naïve"`) can be
   written mojibake or crash on read.
4. **Assuming loaded numbers/keys keep their shape** - JSON object keys are
   always strings: `{1: "a"}` comes back as `{"1": "a"}`. Ints and floats
   survive, tuples become lists.

---

## 📝 Quick Reference

| Task | Call |
|---|---|
| Python -> JSON **string** | `json.dumps(obj)` |
| JSON **string** -> Python | `json.loads(s)` |
| Python -> JSON **file** | `json.dump(obj, f)` |
| JSON **file** -> Python | `json.load(f)` |
| Human-readable output | `json.dumps(obj, indent=2)` |
| Bad type (e.g. `set`) | raises `TypeError` |
| Malformed JSON text | raises `json.JSONDecodeError` |

---

## 🔍 Key Takeaways

- JSON is text, but it represents nested structures.
- Use `json.dump`/`json.load` for files (not `dumps`/`loads`).
- Consider `indent=2` for human-readable output.

---

[Back: Module 10 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
