# 📊 Working with CSV

CSV (Comma-Separated Values) is a simple format for **tabular data**.
Python's built-in [`csv`](10_file_io/04_working_with_csv/README.md:1) module handles quoting and parsing correctly.

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

## 🔍 Key Takeaways

- Use `csv.reader` for plain lists.
- Use `csv.DictReader`/`DictWriter` for headers + dict rows.
- Open CSV files with `newline=""`.

---

[Back: Module 10 README](../README.md)

