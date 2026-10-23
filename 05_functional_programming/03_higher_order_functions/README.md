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

## ⚠️ Common Mistakes

1. **Calling instead of passing** - `apply_twice(double(), 3)` raises `TypeError`:
   `double()` is already a *number*. Pass the function itself: `apply_twice(double, 3)`.
2. **Forgetting to return the inner function** - a factory that ends with
   `return multiply()` *calls* the function and hands back a number. Drop the
   parentheses: `return multiply`.
3. **Order confusion in composition** - `compose(f, g)` returning `f(g(x))` runs `g`
   first, then `f`. If it reads backwards, rename the parameters or write
   `def compose(outer, inner)`.
4. **Building functions in a loop that share one variable** - `[lambda: i for i in range(3)]`
   gives three functions that all see the final `i` (late binding). Capture each value
   with a default argument: `lambda i=i: i`. See the [Closures gotcha](../06_closures/README.md).

---

## 📝 Quick Reference

| Tool | Takes | Returns | Example |
|---|---|---|---|
| `map` | function + iterable | lazy iterator | `map(double, nums)` |
| `filter` | predicate + iterable | lazy iterator | `filter(lambda n: n > 0, nums)` |
| `sorted` | iterable + `key` function | list | `sorted(words, key=len)` |
| Factory | configuration arguments | a new function | `make_multiplier(3)` |
| Composition | two functions | one function | `compose(square, add1)` |

```python
def apply_twice(func, value):
    return func(func(value))     # pass the name, call it inside

def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply              # return the function, not multiply()
```

---

## 🔍 Key Takeaways

- Functions can be treated like data.
- Higher-order functions make code flexible and reusable.
- They enable patterns like map/filter/reduce and decorators.

---

[Next: Lambda Expressions](../04_lambda_expressions/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
