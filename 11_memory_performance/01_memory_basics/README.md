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
With `memoryview()`, you can create a **view** into the same underlying buffer.

---

## 🔍 Key Takeaways

- Variables hold references to objects.
- Mutability decides whether changes affect the same object.
- `memoryview` helps avoid copies for binary data.

---

## ⚠️ Common Mistakes

- Thinking `b = a` copies the list — it only copies the **reference**
- Assuming immutability goes all the way down: a tuple can still hold a **mutable list**
- Comparing values with `is` — use `==` for values, `is` for identity

---

## 📝 Quick Reference

```python
id(obj)          # identity: "which object is this?"
x is y           # same object?
x == y           # same value?
type(obj)        # the object's type

# mutable:   list, dict, set
# immutable: int, float, str, tuple, bytes

view = memoryview(data)   # view into a buffer, no copy
view[1:4].tobytes()       # now materialize just the piece you need
```

---

[Back: Module 11 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
