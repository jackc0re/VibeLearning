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

## 🔍 Key Takeaways

- Text uses encodings; binary is raw bytes.
- Use chunked IO for large files.
- Hashing (like SHA-256) is a common binary-file operation.

---

[Back: Module 10 README](../README.md)

