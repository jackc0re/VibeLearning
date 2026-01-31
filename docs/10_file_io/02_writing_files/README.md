# ✍️ Writing Files

Writing files lets your program **save results** and create logs, reports, exports, and more.

---

## ✅ File Modes

| Mode | Meaning | Notes |
|---|---|---|
| `"w"` | write (overwrite) | creates file if missing |
| `"a"` | append | writes at end, creates if missing |
| `"x"` | create exclusively | fails if file exists |
| `"r+"` | read/write | file must exist |

For binary data use `"wb"` / `"ab"`.

---

## ✅ Basic Pattern

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello!\n")
```

---

## ⚠️ Newlines on Windows

Python will translate `"\n"` to the platform newline automatically for text files.
For CSV, Python recommends `newline=''` when opening the file (covered in the CSV lesson).

---

## 🔍 Key Takeaways

- `"w"` overwrites; `"a"` appends.
- Use `with` so buffers flush and the file closes.
- Prefer explicit UTF-8 encoding for text.

---

[Back: Module 10 README](../README.md)

