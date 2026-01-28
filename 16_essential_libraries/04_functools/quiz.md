# 🔧 Functools Module - Quiz

Test your knowledge of functools!

---

## Question 1
**What does `functools.partial` do?**

A) Makes a function partial (incomplete)
B) Creates a new function with some arguments pre-filled
C) Partially executes a function
D) Splits a function into parts

<details>
<summary>Click for answer</summary>

**B) Creates a new function with some arguments pre-filled**

`partial(func, arg=value)` creates a new function where `arg` is already set to `value`.
</details>

---

## Question 2
**What is the main benefit of `@lru_cache`?**

A) Makes code shorter
B) Reduces memory usage
C) Avoids redundant calculations by caching results
D) Makes functions thread-safe

<details>
<summary>Click for answer</summary>

**C) Avoids redundant calculations by caching results**

LRU (Least Recently Used) cache stores function results to avoid recalculating for the same inputs.
</details>

---

## Question 3
**What is the output of `reduce(lambda a, b: a + b, [1, 2, 3, 4])`?**

A) 4
B) 10
C) [1, 2, 3, 4]
D) Error

<details>
<summary>Click for answer</summary>

**B) 10**

`reduce` cumulatively applies the function: ((1+2)+3)+4 = 10.
</details>

---

## Question 4
**Why should you use `@wraps` when writing decorators?**

A) It makes the decorator run faster
B) It preserves the original function's metadata (name, docstring)
C) It wraps the function in a try-except block
D) It's required for all decorators

<details>
<summary>Click for answer</summary>

**B) It preserves the original function's metadata (name, docstring)**

Without `@wraps`, decorated functions lose their `__name__`, `__doc__`, etc.
</details>

---

## Question 5
**What happens if you call a cached function with an unhashable argument?**

A) It works normally
B) It raises TypeError
C) It ignores the cache
D) It converts the argument to a hashable type

<details>
<summary>Click for answer</summary>

**B) It raises TypeError**

`@lru_cache` requires all arguments to be hashable (e.g., no lists or dicts).
</details>

---

## Question 6
**What does `partial(pow, exp=2)` create?**

A) A function that raises any number to power 2 (square)
B) A function that raises 2 to any power
C) A function that calculates 2^2
D) An error

<details>
<summary>Click for answer</summary>

**A) A function that raises any number to power 2 (square)**

`partial(pow, exp=2)` pre-fills `exp=2`, so you only need to provide the base.
</details>

---

## Question 7
**What does `lru_cache(maxsize=None)` mean?**

A) No caching
B) Cache up to None items
C) Unlimited cache size
D) Cache is disabled

<details>
<summary>Click for answer</summary>

**C) Unlimited cache size**

`maxsize=None` means the cache can grow without bounds (use with caution).
</details>

---

## Question 8
**Which of these is equivalent to `reduce(f, [a, b, c])`?**

A) f(f(a, b), c)
B) f(a, f(b, c))
C) a + b + c
D) f(a, b, c)

<details>
<summary>Click for answer</summary>

**A) f(f(a, b), c)**

`reduce` applies the function cumulatively from left to right.
</details>

---

## Question 9
**What is `cmp_to_key` used for?**

A) Comparing two keys
B) Converting a comparison function to a key function for sorting
C) Comparing dictionaries by keys
D) Creating sorted keys

<details>
<summary>Click for answer</summary>

**B) Converting a comparison function to a key function for sorting**

In Python 3, `sorted()` uses key functions. `cmp_to_key` converts old-style comparison functions.
</details>

---

## Question 10
**How do you clear an LRU cache?**

A) `del cache`
B) `cache.clear()`
C) `func.cache_clear()`
D) Restart Python

<details>
<summary>Click for answer</summary>

**C) `func.cache_clear()`**

The decorated function gets a `.cache_clear()` method to clear its cache.
</details>

---

**How did you do?** Check `examples.py` for more practice!
