# 📖 Reading Files

Reading files is a foundational I/O skill. The key idea is:

- Use [`open()`](10_file_io/01_reading_files/README.md:1) with a **context manager** (`with`) so the file closes automatically.
- Specify an **encoding** for text files (UTF-8 is the modern default).

---

## ✅ Basic Pattern

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

---

## ✅ Common Reading Methods

| Method | Returns | When to use |
|---|---|---|
| `f.read()` | full file as a single string | small/medium files |
| `f.readline()` | next line | streaming line-by-line |
| `f.readlines()` | list of lines | small files, quick processing |
| `for line in f:` | lines iterator | large files, memory-safe |

---

## ⚠️ Paths and Working Directory

Relative paths are resolved from the **current working directory** (where you run `python`).
If you need robust paths, consider [`pathlib.Path`](10_file_io/01_reading_files/README.md:1).

---

## 🔍 Key Takeaways

- Prefer `with open(...):` to avoid leaking file handles.
- Text files need an encoding; use `encoding="utf-8"`.
- Iterate over the file object for large files.

---

[Back: Module 10 README](../README.md)

