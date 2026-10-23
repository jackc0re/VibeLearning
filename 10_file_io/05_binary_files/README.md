# 🧱 Binary Files

Binary files store **raw bytes** instead of text characters.
Use binary modes `"rb"` and `"wb"` when working with images, PDFs, compressed data, or custom protocols.

---

## ✅ Reading/Writing Bytes

```python
data = b"\x00\x01\x02"

with open("blob.bin", "wb") as f:
    f.write(data)

with open("blob.bin", "rb") as f:
    back = f.read()
```

---

## ✅ Chunked Reading (Large Files)

```python
chunk_size = 8192
with open("big.bin", "rb") as f:
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        # process chunk
```

---

## ⚠️ Common Mistakes

1. **Mixing bytes and str** - in `"rb"` mode you get `bytes`, and in `"wb"`
   mode you must write `bytes`. `f.write("hello")` in binary mode raises
   `TypeError`; use `f.write(b"hello")` or `s.encode("utf-8")`.
2. **Decoding binary data as text** - opening a PNG with `open(p, "r")`
   produces mojibake or `UnicodeDecodeError`. If the content is not text,
   don't open it in text mode.
3. **Reading whole huge files** - `f.read()` slurps every byte into RAM.
   For big files, read fixed-size chunks in a loop until you get back `b""`.
4. **Confusing `b""` with `None`** - at end-of-file, `f.read(n)` returns the
   empty bytes object `b""`; that is your EOF signal, not an error.

---

## 📝 Quick Reference

| Task | Code |
|---|---|
| Write bytes | `open(p, "wb")`, `f.write(b"...")` |
| Read bytes | `open(p, "rb")`, `data = f.read()` |
| str -> bytes | `s.encode("utf-8")` |
| bytes -> str | `b.decode("utf-8")` |
| EOF signal in chunk loop | `f.read(n)` returns `b""` |
| Typical uses | images, PDFs, hashing (`hashlib.sha256`) |

---

## 🔍 Key Takeaways

- Text uses encodings; binary is raw bytes.
- Use chunked IO for large files.
- Hashing (like SHA-256) is a common binary-file operation.

---

[Back: Module 10 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
