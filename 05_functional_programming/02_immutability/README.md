# 🧊 Immutability

Immutability means **data does not change after it's created**. Instead of mutating existing values, you create new ones. This reduces bugs caused by shared state and makes code easier to reason about.

---

## ✅ Why Immutability?

- **Predictable behavior** — values don't change unexpectedly.
- **Safer concurrency** — no race conditions on shared data.
- **Easier debugging** — state changes are explicit.

---

## ✅ Immutable vs Mutable in Python

| Type | Mutable? | Examples |
|------|----------|----------|
| `int`, `float`, `str`, `tuple` | ❌ No | numbers, strings, tuples |
| `list`, `dict`, `set` | ✅ Yes | collections |

---

## ✅ Non-Mutating Patterns

### Strings (Immutable)
```python
name = "alice"
upper = name.upper()  # creates a new string
```

### Tuples (Immutable)
```python
point = (1, 2)
new_point = (point[0] + 1, point[1])
```

### Lists (Use Copies)
```python
nums = [1, 2, 3]
new_nums = nums + [4]   # new list
```

---

## ✅ Copy-on-Write

Instead of mutating an object, create a modified copy.

```python
original = {"name": "Alice", "age": 30}
updated = {**original, "age": 31}
```

---

## ✅ Immutability Tips

- Prefer `tuple` over `list` when you don’t need mutation.
- Return new objects instead of mutating inputs.
- Use `dataclasses` with `frozen=True` for immutable models.

---

## 🔍 Key Takeaways

- Immutability reduces side effects.
- You can emulate immutability with copies.
- Immutable data works great with pure functions.

---

[Next: Higher-Order Functions](../03_higher_order_functions/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
