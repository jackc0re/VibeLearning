# 🔧 Functools Module

> **Higher-order functions and operations on callable objects**

---

## 🎯 Learning Objectives

By the end of this section, you'll understand:
- How to use `partial` to create specialized functions
- How to cache function results with `lru_cache`
- How `reduce` combines elements of an iterable
- How `wraps` preserves function metadata

---

## 📦 Partial Functions

`partial` creates a new function with some arguments pre-filled.

### Real-World Analogy

Think of `partial` as a curry (the food) - you start with a base and add specific ingredients to create variations.

```python
from functools import partial

# Base function
def power(base, exponent):
    return base ** exponent

# Create specialized functions
square = partial(power, exponent=2)
cube = partial(power, exponent=3)
ten_to_the = partial(power, base=10)

print(square(5))        # 25
print(cube(3))          # 27
print(ten_to_the(3))    # 1000
```

### Common Use Cases

```python
from functools import partial

# Custom print with prefix
def log(prefix, message):
    print(f"[{prefix}] {message}")

info = partial(log, "INFO")
error = partial(log, "ERROR")

info("Application started")  # [INFO] Application started
error("Connection failed")   # [ERROR] Connection failed
```

---

## 🚀 Caching with lru_cache

`lru_cache` remembers function results to avoid redundant calculations.

### Real-World Analogy

Like keeping frequently used tools on your desk instead of fetching them from the garage each time.

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# First call calculates
print(fibonacci(30))  # Fast after caching

# Check cache info
print(fibonacci.cache_info())
# CacheInfo(hits=28, misses=31, maxsize=128, currsize=31)
```

### When to Use

- Expensive calculations
- Recursive functions
- API calls with same parameters
- Database queries

### Important Notes

- Arguments must be hashable (no lists/dicts)
- Use `maxsize=None` for unlimited cache
- Clear cache with `.cache_clear()`

---

## 🔁 The reduce Function

`reduce` applies a function cumulatively to items in an iterable.

```python
from functools import reduce

# Sum all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

# Multiply all numbers
product = reduce(lambda acc, x: acc * x, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(maximum)  # 5
```

### How reduce Works

```
reduce(f, [1, 2, 3, 4, 5])
→ f(f(f(f(1, 2), 3), 4), 5)
→ f(f(f(3, 3), 4), 5)
→ f(f(6, 4), 5)
→ f(10, 5)
→ 15
```

### With Initial Value

```python
# Start with initial value
result = reduce(lambda acc, x: acc + x, [1, 2, 3], 100)
print(result)  # 106 (100 + 1 + 2 + 3)
```

---

## 📝 Preserving Metadata with wraps

`wraps` is a decorator that preserves the original function's metadata.

### The Problem

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Say hello."""
    print("Hello!")

print(greet.__name__)  # 'wrapper' - lost original name!
print(greet.__doc__)   # None - lost docstring!
```

### The Solution

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Say hello."""
    print("Hello!")

print(greet.__name__)  # 'greet'
print(greet.__doc__)   # 'Say hello.'
```

---

## 📊 cmp_to_key

Convert a comparison function to a key function (useful for sorting).

```python
from functools import cmp_to_key

# Old-style comparison function
def compare_length(a, b):
    return len(a) - len(b)

words = ['apple', 'pie', 'banana', 'kiwi']
# Using comparison function
sorted_words = sorted(words, key=cmp_to_key(compare_length))
print(sorted_words)  # ['pie', 'kiwi', 'apple', 'banana']
```

---

## ⚠️ Common Mistakes

1. **Using unhashable arguments with lru_cache** - Lists and dicts can't be cached
2. **Forgetting to sort before reduce** - Order matters for some operations
3. **Not using wraps** - Decorators hide original function info
4. **Infinite recursion with lru_cache** - Ensure base case is reached

---

## 📝 Quick Reference

```python
from functools import partial, lru_cache, reduce, wraps

# Partial - pre-fill arguments
square = partial(pow, exp=2)

# Caching
@lru_cache(maxsize=128)
def expensive(n):
    pass

# Reduce - cumulative operations
total = reduce(lambda a, b: a + b, numbers)

# Wraps - preserve metadata
@wraps(original)
def wrapper(*args, **kwargs):
    pass
```

---

## 🎓 Next Steps

Run `examples.py` to see functools in action, then try `exercises.py`!
