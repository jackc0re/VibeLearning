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

## ⚠️ Forgetting `nonlocal`: the `UnboundLocalError` Trap

Here is the detail that surprises everyone: **reading** an outer variable works fine without any keyword, but **assigning** to it does not.

```python
def make_counter():
    count = 0

    def show():
        return count        # fine: only reading, so Python uses the outer count

    def inc():
        count += 1          # UnboundLocalError!
        return count

    return show, inc

show, inc = make_counter()
print(show())               # 0 - reading the outer variable just works

try:
    inc()
except UnboundLocalError as exc:
    print(f"UnboundLocalError: {exc}")
```

Why does `count += 1` fail? That line is really two operations: *read* `count`, then *write* `count`. The moment Python's compiler sees an assignment to `count` anywhere inside `inc`, it decides `count` must be a **local** variable of `inc`. So the read on the right-hand side looks for a *local* `count` — finds nothing yet — and raises `UnboundLocalError` (on older Python versions the message reads "local variable referenced before assignment").

`nonlocal` is the fix: it tells Python "assignments here target the enclosing variable, not a new local one."

```python
def make_counter():
    count = 0
    def inc():
        nonlocal count      # assignments now hit the outer count
        count += 1
        return count
    return inc

counter = make_counter()
counter()  # 1
counter()  # 2
```

The same rule explains `x = x + 1` failing on a module-level variable without `global` — `global` is the module-scope cousin of `nonlocal`.

---

## ⚠️ Gotcha: Closures Capture Variables, Not Values (Late Binding)

A closure remembers the **variable**, not a snapshot of its value. If the variable keeps changing after the closure is created, the closure sees the *latest* value. This bites most often inside loops:

```python
callbacks = []
for i in range(3):
    callbacks.append(lambda: i)     # three closures, one shared variable i

print([cb() for cb in callbacks])   # [2, 2, 2] - not [0, 1, 2]!
```

All three lambdas close over the *same* variable `i`. By the time any of them runs, the loop has finished and `i` is `2` — so every callback answers `2`. This is called **late binding**: the value is looked up when the function is *called*, not when it is *defined*.

The standard fix is a default argument, because defaults are evaluated **once, at definition time** — effectively taking a snapshot:

```python
callbacks = []
for i in range(3):
    callbacks.append(lambda i=i: i)  # default captures the current value

print([cb() for cb in callbacks])    # [0, 1, 2]
```

Reading `lambda i=i: i` as "give me a parameter `i` that defaults to today's `i`" makes it stick. The same trick works with `def` inside a loop, and for `functools.partial(fn, i)` as an alternative.

---

## ⚠️ Common Mistakes

1. **Expecting a snapshot of the value** - closures bind to variables, so a variable
   that changes later (a loop counter, a reassigned outer name) changes what the
   closure sees. Capture the current value with a default argument (`lambda i=i: i`).
2. **Assigning to an outer variable without `nonlocal`** - any assignment makes the
   name local, and then reading it raises `UnboundLocalError`. Add `nonlocal count`
   (nested function) or `global count` (module level) when you really want to update
   the outer variable.
3. **Looping over a factory that ignores its argument** - `for i in range(3): fs.append(make_adder())`
   creates three identical functions. Pass the loop variable in: `make_adder(i)` — then
   each call creates a fresh scope with its own `n`.
4. **Creating the inner function after using the captured name** - the name only needs
   to exist when the closure *runs*, but if it never existed in the enclosing scope at
   all, calling the closure raises `NameError`.

---

## 📝 Quick Reference

| Pattern | Code | Notes |
|---|---|---|
| Function factory | `def make_adder(n):` / `  def add(x): return x + n` / `  return add` | each call makes a new closure |
| Read outer variable | just use the name (`return count`) | no keyword needed for reads |
| Update outer variable | `nonlocal count` before assigning | `global` for module level |
| Snapshot a loop variable | `lambda i=i: i` | default evaluated at definition time |
| Inspect what was captured | `func.__closure__`, `func.__code__.co_freevars` | debugging aid |

```python
ticks = counter()    # one closure with its own hidden count
ticks()              # 1
other = counter()    # a second, independent closure
other()              # 1 - ticks is untouched (state lives in the closure)
```

---

## 🔍 Key Takeaways

- Closures capture variables from their enclosing scope (not a copy of the value).
- They are useful for customization and encapsulation.
- `nonlocal` lets you update captured variables; without it, assignment raises `UnboundLocalError`.
- Late binding means closures see the *current* value of captured variables — use default arguments to snapshot loop variables.

---

[Next: Decorators](../07_decorators/README.md)

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
