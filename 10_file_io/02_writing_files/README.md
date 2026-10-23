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

## ⚠️ Common Mistakes

1. **Overwriting by accident** - `"w"` truncates the file to zero **immediately**
   on open, before you write a single character. If the old content matters,
   use `"a"` or read it first.
2. **No `with`, no flush** - writes go to an in-memory buffer. If you never
   close the file (or your program crashes), the tail of your data can be lost.
   The `with` block flushes and closes for you.
3. **`write` vs `writelines` confusion** - neither adds newlines.
   `f.writelines(["a", "b"])` produces `"ab"`. Add `"\n"` yourself.
4. **Mode typos** - opening for writing with `"r"` raises
   `io.UnsupportedOperation: not writable` the moment you call `f.write(...)`.
   Check the mode letter first.

---

## 📝 Quick Reference

| Mode | Behavior | File must exist? |
|---|---|---|
| `"w"` | overwrite from a blank file | no - creates it |
| `"a"` | append at the end | no - creates it |
| `"x"` | create only | fails with `FileExistsError` if it exists |
| `"r+"` | read and overwrite in place | yes |

```python
with open("log.txt", "a", encoding="utf-8") as f:   # append, never clobbers
    f.write("new entry\n")
```

---

## 🔍 Key Takeaways

- `"w"` overwrites; `"a"` appends.
- Use `with` so buffers flush and the file closes.
- Prefer explicit UTF-8 encoding for text.

---

[Back: Module 10 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
