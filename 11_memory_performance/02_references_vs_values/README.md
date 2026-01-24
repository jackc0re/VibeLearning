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

[Back: Module 11 README](../README.md)

