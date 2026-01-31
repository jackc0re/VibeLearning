# 📁 Module 10: File & I/O

Files are how programs **persist data** and exchange information with the outside world.
In Python, most file operations revolve around the built-in [`open()`](10_file_io/README.md:1) function and using context managers (`with`) to ensure files are closed properly.

> **Estimated Time:** 4-6 hours  \
> **Prerequisites:** Module 01 (Foundations)  \
> **Level:** ⭐⭐ Beginner → Intermediate

---

## 📚 Topics Covered

| # | Topic | Description | Key Concepts |
|---|-------|-------------|--------------|
| 01 | [Reading Files](01_reading_files/) | Open and read text safely | encodings, iterating lines, `with open(...)` |
| 02 | [Writing Files](02_writing_files/) | Create, overwrite, append | modes (`w`, `a`), newline handling |
| 03 | [Working with JSON](03_working_with_json/) | Read/write structured data | `json.dumps`, `json.load`, validation |
| 04 | [Working with CSV](04_working_with_csv/) | Tabular data | `csv.reader`, `DictReader`, `DictWriter` |
| 05 | [Binary Files](05_binary_files/) | Read/write bytes | `rb`/`wb`, hashing, chunked IO |

---

## 🎯 Learning Goals

By the end of this module, you should be able to:

- Read and write text files using a context manager.
- Understand file modes (`r`, `w`, `a`, `rb`, `wb`) and when to use them.
- Serialize/deserialize data using JSON.
- Parse and generate CSV files in a platform-safe way (`newline=''`).
- Work with binary data and compute checksums/hashes efficiently.

---

## 📂 Module Structure

```
10_file_io/
├── README.md
├── 01_reading_files/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 02_writing_files/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 03_working_with_json/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
├── 04_working_with_csv/
│   ├── README.md
│   ├── examples.py
│   ├── exercises.py
│   └── quiz.md
└── 05_binary_files/
    ├── README.md
    ├── examples.py
    ├── exercises.py
    └── quiz.md
```

---

**Start here:** [01_reading_files](01_reading_files/)

