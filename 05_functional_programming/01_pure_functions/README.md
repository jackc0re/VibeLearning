# 🧼 Pure Functions

Pure functions are the foundation of functional programming. A pure function:

1. **Always returns the same output** for the same inputs (deterministic).
2. **Has no side effects** (doesn't modify external state, print, or mutate inputs).

---

## ✅ Why Pure Functions Matter

- **Predictable:** Easy to test and reason about.
- **Reusable:** Safe to reuse across the codebase.
- **Composable:** Works well with other functions.
- **Cacheable:** Enables memoization because outputs only depend on inputs.

---

## ✅ Pure vs Impure

```python
# Pure
def add(a, b):
    return a + b

# Impure (prints = side effect)
def add_and_log(a, b):
    result = a + b
    print(result)
    return result
```

---

## ✅ Referential Transparency

If a function is pure, you can replace the function call with its result without changing the program’s behavior.

```python
def square(x):
    return x * x

square(3)  # always 9
```

---

## ✅ Avoiding Hidden State

```python
counter = 0

def next_id():
    global counter
    counter += 1
    return counter

# Impure because it depends on external state
```

Better:

```python
def next_id(current):
    return current + 1
```

---

## ✅ Guidelines for Pure Functions

- Don’t modify input arguments.
- Don’t read global state.
- Don’t write to files, databases, or the console.
- Return a new value instead of mutating existing data.

---

## 🔍 Key Takeaways

- Pure functions are deterministic and side-effect free.
- They improve testability and maintainability.
- They enable functional patterns like composition and memoization.

---

[Next: Immutability](../02_immutability/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
