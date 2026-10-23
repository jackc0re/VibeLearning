# 📊 Working with CSV

CSV (Comma-Separated Values) is a simple format for **tabular data**.
Python's built-in `csv` module handles quoting and parsing correctly.

---

## ✅ Reading CSV

```python
import csv

with open("people.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
```

---

## ✅ Writing CSV

```python
import csv

rows = [{"name": "Ada", "age": "30"}]

with open("people.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(rows)
```

---

## ⚠️ Why `newline=""`?

On Windows, not using `newline=""` can lead to extra blank lines in CSV output.

---

## ⚠️ Common Mistakes

1. **Parsing with `line.split(",")`** - a quoted field like `"Smith, Ada"`
   contains a comma, so naive splitting produces extra columns. The `csv`
   module implements the quoting rules; let it do the work.
2. **Forgetting `newline=""`** - on Windows, rows can come out with a blank
   line between them. Open both when reading and writing with
   `open(path, ..., newline="")`.
3. **Treating cells as numbers** - the `csv` module returns **strings**.
   `"30" + 1` raises `TypeError`; convert with `int()` / `float()` yourself.
4. **`DictWriter` without `fieldnames`** - it is a required argument, and the
   header only appears if you call `writer.writeheader()` yourself.
5. **Manual line breaks in cells** - writing a value containing `\n` without
   quoting spreads one record over two rows; `csv.writer` quotes it correctly
   if you route the value through the writer rather than concatenating text.

---

## 📝 Quick Reference

| Task | Code |
|---|---|
| Read rows as lists | `csv.reader(f)` |
| Read rows as dicts (header row) | `csv.DictReader(f)` |
| Write rows as lists | `csv.writer(f)`, then `writer.writerow(row)` / `writer.writerows(rows)` |
| Write rows as dicts | `csv.DictWriter(f, fieldnames=[...])`, then `writeheader()` |
| Open for CSV | `open(path, "w", encoding="utf-8", newline="")` |
| Cell types when reading | always `str` - convert numbers yourself |

---

## 🔍 Key Takeaways

- Use `csv.reader` for plain lists.
- Use `csv.DictReader`/`DictWriter` for headers + dict rows.
- Open CSV files with `newline=""`.

---

[Back: Module 10 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
