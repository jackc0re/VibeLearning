# 📖 Reading Files

Reading files is a foundational I/O skill. The key idea is:

- Use `open()` with a **context manager** (`with`) so the file closes automatically.
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
If you need robust paths, consider `pathlib.Path`.

---

## ⚠️ Common Mistakes

1. **Opening without `with`** - a file you forget to close keeps a handle open,
   and buffered data may never reach the disk. `with open(...) as f:` closes it
   even if an exception fires mid-read.
2. **Guessing the encoding** - Windows may hand you `cp1252`, macOS `utf-8`,
   and a file saved as UTF-16 will look like gibberish (`ÿþ` at the start).
   Pass `encoding="utf-8"` explicitly so behavior is the same everywhere.
3. **`f.read()` on a huge file** - it loads every byte into memory at once.
   Iterate with `for line in f:` instead; the file object streams.
4. **Reading past the end** - `f.read()` on an exhausted file returns `""`
   (not an error), and `f.readline()` likewise returns `""` at EOF. Check for
   emptiness, not `None`.

---

## 📝 Quick Reference

| Task | Code |
|---|---|
| Read whole file | `with open(p, encoding="utf-8") as f: text = f.read()` |
| Read line-by-line (large files) | `with open(p, encoding="utf-8") as f:`<br>`    for line in f: ...` |
| All lines as a list | `lines = f.readlines()` |
| One line at a time | `line = f.readline()` |
| File missing? | `open()` raises `FileNotFoundError` |
| After the `with` block | file is closed; reading again raises `ValueError` |

---

## 🔍 Key Takeaways

- Prefer `with open(...):` to avoid leaking file handles.
- Text files need an encoding; use `encoding="utf-8"`.
- Iterate over the file object for large files.

---

[Back: Module 10 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
