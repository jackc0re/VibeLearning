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

## ⚠️ Common Mistakes

1. **Assuming `sort()`, `append()`, `reverse()` give something back** - they mutate
   in place and return `None`, so `result = nums.sort()` quietly gives you `None`.
   Use `sorted(nums)`, `nums + [x]`, or `nums[::-1]` for new objects.
2. **Mutating a tuple or string by index** - `point[0] = 9` raises `TypeError`.
   Build a new tuple (`point[:0] + (9,) + point[1:]`) or switch to a list.
3. **Trusting a shallow copy for nested data** - `data.copy()` and `list(nums)` copy
   only the outer object; nested lists or dicts are still shared. Use
   `copy.deepcopy(data)` when you need a fully independent copy.
4. **"Updating" a dict with `data[key] = value`** - that mutates the caller's dict.
   `{**data, key: value}` builds a new one and leaves the original alone.

---

## 📝 Quick Reference

| Goal | Mutating (avoid) | Non-mutating (prefer) |
|---|---|---|
| Add to a list | `nums.append(4)` | `nums + [4]` or `[*nums, 4]` |
| Sort a list | `nums.sort()` | `sorted(nums)` |
| Remove a value | `nums.remove(x)` | `[n for n in nums if n != x]` |
| Update a dict | `data[k] = v` | `{**data, k: v}` |
| Change a tuple | not allowed | `t[:i] + (new,) + t[i+1:]` |

```python
original = {"name": "Alice", "age": 30}
updated = {**original, "age": 31}   # new dict; original still 30
```

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
