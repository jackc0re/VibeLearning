# 🔄 Generators and Iterators

Generators are **functions that produce values one at a time, pausing between each
one**. Iterators are the **objects that quietly power every `for` loop** you have ever
written. The analogy: a list is a book with every page already printed; a generator is
a storyteller who invents the next episode only when you ask "what happens next?".

---

## ✅ What `for` Really Does

```python
numbers = [10, 20, 30]

for n in numbers:
    print(n)
```

Under the hood, that loop is roughly this:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)         # 1. ask the list for an iterator
while True:
    try:
        n = next(iterator)       # 2. pull the next value
    except StopIteration:        # 3. the "empty" flag -> leave the loop
        break
    print(n)
```

So `for` is a robot pressing a "next" button: `iter()` gets hold of the button,
`next()` presses it, and `StopIteration` is the machine raising its "no more" flag.
Every loop you write runs this exact protocol.

---

## ✅ The Iterator Protocol

Two small methods make the whole system work:

- An **iterable** is anything you can call `iter()` on - it defines `__iter__`.
  Lists, strings, dicts, and `range` are all iterables.
- An **iterator** is the object that actually walks through the values - it defines
  `__iter__` *and* `__next__`, and it remembers where it is.

Every iterator is iterable (its `__iter__` returns itself), but not every iterable is
an iterator (a list has `__iter__` but no `__next__`).

Driving one by hand:

```python
it = iter(["a", "b"])

print(next(it))   # 'a'
print(next(it))   # 'b'
# one more next(it) would raise StopIteration
```

`next()` takes an optional default, so you never have to see the exception:

```python
it = iter([1])

print(next(it, "empty"))   # 1
print(next(it, "empty"))   # 'empty'  - the default instead of StopIteration
```

---

## ✅ A Class-Based Iterator: Countdown

Before generators existed, every iterator was a class. Writing one makes the protocol
explicit - this class is exactly what `for` needs:

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self              # an iterator's __iter__ returns itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # the "no more" flag
        value = self.current
        self.current -= 1
        return value

for n in Countdown(3):
    print(n)                     # 3, then 2, then 1
```

Notice the shape: `__next__` computes one value, keeps state on `self`, and raises
`StopIteration` when done. Generators let Python write all that bookkeeping for you.

---

## ✅ Generator Functions: `yield` Pauses the Function

A function containing `yield` is a **generator function**. Calling it does not run the
body - it hands you a generator object. Each `next()` runs the body *until the next
`yield`*, hands out that value, and freezes the function exactly where it stopped.
All local variables stay alive until the next `next()`.

```python
def simple_gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

gen = simple_gen()      # prints NOTHING - the body has not started yet
print(next(gen))        # start  -> 1
print(next(gen))        # middle -> 2
try:
    next(gen)           # end    -> the function finishes...
except StopIteration:
    print("all done")   # ...and that raises StopIteration
```

Watch the function's prints and yours interleave - `start` and `middle` appear
*between* the values, because the body runs in slices, one `yield` at a time.

---

## ✅ Generator Expressions: Lazy by Default

Swap a list comprehension's brackets for parentheses and you get a **generator
expression** - a one-line generator:

```python
squares_list = [x * x for x in range(5)]   # list: all 5 values built right now
squares_gen  = (x * x for x in range(5))   # generator: a recipe, nothing cooked yet

print(squares_list)   # [0, 1, 4, 9, 16]
print(squares_gen)    # <generator object <genexpr> at 0x...>

print(sum(squares_gen))               # 30 - values produced one at a time
print(max(x * x for x in range(10)))  # 81 - sum/max take any iterable
```

`sum()`, `max()`, `min()`, and `any()` happily eat generators, so the parentheses
often blend right into the call: `sum(x * x for x in range(10))`.

---

## ✅ Generators Are One-Shot

A generator is like a ticket that gets punched once: after the last value it is empty,
and it does **not** restart. This is the single biggest surprise for beginners:

```python
gen = (x * x for x in range(4))

print(sum(gen))    # 14  (0 + 1 + 4 + 9)
print(sum(gen))    # 0   - already exhausted, nothing left to give

for value in gen:  # prints nothing at all
    print(value)
```

If you need to walk the values twice, build a list instead (or recreate the
generator) - `list(x * x for x in range(4))` can be summed as many times as you like.

---

## ✅ Delegating with `yield from`

`yield from` hands control to another iterable and yields everything in it - a shorter
way to write the inner loop:

```python
def flatten_once(nested):
    for sublist in nested:
        yield from sublist     # same as: for item in sublist: yield item

print(list(flatten_once([[1, 2], [3], [4, 5]])))   # [1, 2, 3, 4, 5]
```

---

## ✅ Infinite Generators

Because a generator only computes on demand, it can be *infinite*. The classic
example is Fibonacci:

```python
def fibonacci():
    a, b = 0, 1
    while True:          # never ends on its own - and that is fine!
        yield a
        a, b = b, a + b
```

The danger: `list(fibonacci())` would run forever. **You** must bound the consumption:

```python
from itertools import islice

gen = fibonacci()
first_six = []
for _ in range(6):                       # bound it with a manual counter...
    first_six.append(next(gen))

print(first_six)                         # [0, 1, 1, 2, 3, 5]
print(list(islice(fibonacci(), 8)))      # ...or islice: [0, 1, 1, 2, 3, 5, 8, 13]
```

The `itertools` module is full of helpers for taming infinite generators - see
[itertools](../../16_essential_libraries/03_itertools/README.md) for `islice`,
`takewhile`, and friends.

---

## ✅ Lazy Pipelines Save Memory

Generators shine when you chain them: each stage pulls from the previous one, and only
one value is "in flight" at a time.

```python
def evens(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def doubled(numbers):
    for n in numbers:
        yield n * 2

pipeline = doubled(evens(range(10)))
print(list(pipeline))    # [0, 4, 8, 12, 16]
```

And the payoff at scale - a finished list stores every element, while a generator
stores only its recipe:

```python
import sys

n = 1_000_000
as_list = [x * 2 for x in range(n)]   # all million values in memory right now
as_gen  = (x * 2 for x in range(n))   # a recipe; computes one value on demand

print(sys.getsizeof(as_list))   # about 8,000,000 bytes (~8 MB)
print(sys.getsizeof(as_gen))    # about 200 bytes - it holds no values at all
```

Exact byte counts vary by Python version, but the *ratio* does not: the list costs
megabytes no matter what, and the generator costs about as much as a short string,
no matter how many values it will eventually produce.

---

## ⚠️ Common Mistakes

1. **Calling `len()` on a generator** - a generator does not know how many values it
   will produce, so `len()` raises `TypeError`. Count with `sum(1 for _ in gen)`.

   ```python
   gen = (x for x in range(3))
   try:
       len(gen)
   except TypeError:
       print("Generators have no length")
   ```

2. **Using a generator twice** - the second loop, `sum()`, or `list()` sees nothing.
   Recreate the generator, or store the values in a list first.

3. **A membership test consumes the generator** - `x in gen` *walks* the generator
   looking for `x`, and everything it walked past is gone:

   ```python
   gen = (x for x in range(10))
   print(5 in gen)     # True - but the generator is now part-consumed
   print(list(gen))    # [6, 7, 8, 9] - values 0..5 were used up by the check
   ```

4. **Expecting a value back from a generator expression** - `(x * 2 for x in data)`
   gives you a generator *object*, not the values; you still have to iterate it with
   `sum(...)`, `list(...)`, or a `for`. Likewise, a `return` inside a generator
   function does not hand a value to your loop - it just stops the generator.

---

## 📝 Quick Reference

| Term | What it is | Example |
|---|---|---|
| Iterable | anything `iter()` accepts; defines `__iter__` | `list`, `str`, `range` |
| Iterator | defines `__iter__` + `__next__`; remembers its position | `iter([1, 2])` |
| Generator | an iterator built from a `yield` function or `(x for x ...)` | `def g(): yield 1` |
| `next(it)` | pull the next value, or raise `StopIteration` | `next(it, "done")` |
| `yield` | pause the function and hand out one value | `yield a` |
| `yield from` | delegate to another iterable | `yield from sublist` |
| `StopIteration` | the "no more values" signal that ends `for` | raised by `__next__` |

```python
def countdown_gen(start):
    while start > 0:
        yield start
        start -= 1

print(list(countdown_gen(3)))   # [3, 2, 1] - the generator version of Countdown
```

---

## 🔍 Key Takeaways

- `for` calls `iter()` once, then `next()` repeatedly until `StopIteration`.
- An iterator defines `__iter__` and `__next__`; a class-based iterator makes the
  protocol explicit.
- A generator function (`yield`) delivers the same protocol with far less code.
- Generator expressions are lazy one-line generators; feed them to `sum()`, `max()`,
  and friends.
- Generators are one-shot: once exhausted, a second pass yields nothing.
- `yield from` delegates to another iterable.
- Infinite generators are fine - as long as something else bounds the consumption.
- Lazy pipelines process data one value at a time, using almost no extra memory.

---

[Back to Decorators](../07_decorators/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
