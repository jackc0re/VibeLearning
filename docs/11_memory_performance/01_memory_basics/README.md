# 🧩 Memory Basics

Python programs manipulate **objects**. Variables don’t “contain” the object — they **refer** to it.

This topic focuses on:

- object identity: `id()`
- mutability vs immutability
- avoiding unnecessary copies using `memoryview`

---

## ✅ Object Identity & References

```python
a = [1, 2, 3]
b = a

print(id(a) == id(b))  # True (same object)
```

`a` and `b` are two names pointing to the **same** list.

---

## ✅ Mutability

- **Mutable** objects can change “in place” (list, dict, set).
- **Immutable** objects can’t (int, float, str, tuple). “Changing” them creates a new object.

---

## ✅ Views with `memoryview`

If you slice bytes, you often create a **copy**.
With [`memoryview()`](11_memory_performance/01_memory_basics/README.md:1), you can create a **view** into the same underlying buffer.

---

## 🔍 Key Takeaways

- Variables hold references to objects.
- Mutability decides whether changes affect the same object.
- `memoryview` helps avoid copies for binary data.

---

[Back: Module 11 README](../README.md)

