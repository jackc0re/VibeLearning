# 🧩 Working with JSON

JSON (JavaScript Object Notation) is a **text-based** format for structured data.
In Python, you work with JSON via the built-in [`json`](10_file_io/03_working_with_json/README.md:1) module.

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

## 🔍 Key Takeaways

- JSON is text, but it represents nested structures.
- Use `json.dump`/`json.load` for files (not `dumps`/`loads`).
- Consider `indent=2` for human-readable output.

---

[Back: Module 10 README](../README.md)

