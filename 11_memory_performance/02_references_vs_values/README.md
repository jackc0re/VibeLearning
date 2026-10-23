# 🔗 References vs Values

In Python, **assignment does not copy**. It binds a name to an object.

This can be surprising with mutable objects:

```python
a = [1, 2]
b = a
b.append(3)

print(a)  # [1, 2, 3]
```

---

## ✅ Shallow vs Deep Copy

- **Shallow copy** copies the container, but keeps references to the same inner objects.
- **Deep copy** recursively copies inner objects too.

```python
import copy

nested = [[1], [2]]
shallow = copy.copy(nested)
deep = copy.deepcopy(nested)
```

---

## ✅ When to Copy

Copy when:

- you want to prevent accidental mutation via aliases
- you need an independent version to modify

Avoid copying when:

- the object is large and you only need read access
- you can use an immutable type (tuple, `frozenset`, etc.)

---

## 🔍 Key Takeaways

- Python variables hold references.
- Mutations affect all references to the same object.
- Use shallow/deep copies intentionally.

---

## ⚠️ Common Mistakes

- Expecting `copy.copy()` to duplicate **nested** objects (it doesn't — that's `deepcopy`)
- Copying "just in case" — wasted memory and time when read access would do
- Using `is` to compare values: `a == b` compares content, `a is b` compares identity

---

## 📝 Quick Reference

```python
b = a                # alias: same object, no copy
copy.copy(a)         # shallow: new outer container, shared inner objects
copy.deepcopy(a)     # deep: nested objects copied too
a == b               # equal values?
a is b               # same object?
```

---

[Back: Module 11 README](../README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
