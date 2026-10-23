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

## ⚠️ Common Mistakes

1. **Printing inside a "pure" function** - `print` is a side effect: the function now
   talks to the console, so it is not pure. Return the value; let the caller decide
   whether to display it.
2. **Reading or writing global state** - a function that depends on (or bumps) a
   module-level counter gives different answers on repeated calls with the same
   arguments. Pass the state in as a parameter instead.
3. **Mutating the input** - `items.sort()` or `items.append(x)` changes the caller's
   list. Return a new list (`sorted(items)`, `items + [x]`) to stay pure.
4. **Hidden impurity from the clock or randomness** - `datetime.now()` and
   `random.random()` are impure: the output depends on more than the arguments.
   Inject them as parameters (`def price_at(now, item)`) to keep the core pure.

---

## 📝 Quick Reference

| Call | Pure? | Why |
|---|---|---|
| `add(a, b)` returning `a + b` | Yes | output depends only on inputs |
| `len(items)` | Yes | no state touched |
| `print(result)` | No | writes to the console |
| `random.random()` | No | new answer on every call |
| `datetime.now()` | No | depends on the clock |
| `nums.sort()` on an argument | No | mutates the caller's list |

```python
def average(nums):                     # pure: same input, same output
    if not nums:
        return None
    return sum(nums) / len(nums)

result = average([1, 2, 3])            # compute
print(result)                          # display - side effect lives out here
```

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
