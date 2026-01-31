# 🪟 Closures

A **closure** is a function that remembers the variables from its outer (enclosing) scope, even after that outer function has finished executing.

---

## ✅ Why Closures Matter

- Let you create **customized functions** (function factories)
- Hide internal state without classes
- Enable patterns like decorators

---

## ✅ Example: Function Factory

```python
def make_adder(n):
    def add(x):
        return x + n
    return add

add5 = make_adder(5)
add5(10)  # 15
```

Here, `add` remembers the value of `n` even after `make_adder` returns.

---

## ✅ Using `nonlocal`

To update an outer variable, use `nonlocal`.

```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

next_count = counter()
next_count()  # 1
next_count()  # 2
```

---

## 🔍 Key Takeaways

- Closures capture values from enclosing scopes.
- They are useful for customization and encapsulation.
- `nonlocal` lets you update captured variables.

---

[Next: Decorators](../07_decorators/README.md)
