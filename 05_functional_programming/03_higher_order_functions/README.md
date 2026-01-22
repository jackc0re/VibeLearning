# 🔁 Higher-Order Functions

A **higher-order function** is a function that:

1. Takes another function as an argument, **and/or**
2. Returns a function as a result.

This is a core idea in functional programming that enables composition and reusable logic.

---

## ✅ Why It Matters

- **Reusability:** Write generic logic that works with many behaviors.
- **Composability:** Build complex behavior from simple functions.
- **Clarity:** Separate *what* you do from *how* you do it.

---

## ✅ Functions as Arguments

```python
def apply_twice(func, value):
    return func(func(value))

def double(x):
    return x * 2

apply_twice(double, 3)  # 12
```

---

## ✅ Functions that Return Functions

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

times3 = make_multiplier(3)
times3(5)  # 15
```

---

## ✅ Composition

```python
def compose(f, g):
    return lambda x: f(g(x))

def add1(x):
    return x + 1

def square(x):
    return x * x

add1_then_square = compose(square, add1)
add1_then_square(3)  # 16
```

---

## 🔍 Key Takeaways

- Functions can be treated like data.
- Higher-order functions make code flexible and reusable.
- They enable patterns like map/filter/reduce and decorators.

---

[Next: Lambda Expressions](../04_lambda_expressions/README.md)
