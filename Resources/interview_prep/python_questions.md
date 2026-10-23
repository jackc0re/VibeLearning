# 🐍 Python Interview Questions

Forty questions interviewers actually ask, grouped by theme. Each answer is
hidden in a collapsible block — **say your answer out loud first**, then open
it and compare. Every answer links back to the topic page that teaches the
concept, so a miss turns into a five-minute review instead of a dead end.

Work through one theme per sitting. If you can explain 35 of 40 to a rubber
duck without hesitating, you are in good shape.

---

## Basics & Mutability

### 1. The mutable default argument trap

**What does this print, and why?**

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))
```

<details>
<summary>Click for answer</summary>

`[1]` then `[1, 2]`. A default value is evaluated **once**, when the `def`
statement runs — not on every call — so all calls share the *same* list. The
safe pattern is `def add_item(item, items=None)` followed by
`if items is None: items = []`.

📖 Deep dive: [Common Bugs](../../14_debugging/04_common_bugs/README.md)

</details>

---

### 2. `is` vs `==`

**What is the difference between `a == b` and `a is b`?**

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  - equal values
print(a is b)   # False - two separate list objects
```

<details>
<summary>Click for answer</summary>

`==` asks "do these have equal values?" and calls the objects' `__eq__`;
`is` asks "are these the *same object in memory*?" (same identity). Use `is`
only for singletons like `None` (`if x is None:`) and `True`/`False`. Note
that Python caches small ints and short strings, so `a is b` can *accidentally*
be `True` for them — that is an implementation detail, not a guarantee.

📖 Deep dive: [References vs Values](../../11_memory_performance/02_references_vs_values/README.md)

</details>

---

### 3. Shallow copy vs deep copy

**You copy a list of lists with `.copy()`, change an inner value, and the
original changes too. Why, and what is the fix?**

```python
import copy

grid = [[1, 2], [3, 4]]
shallow = grid.copy()      # outer list is new, inner lists are shared
shallow[0][0] = 99
print(grid)                # [[99, 2], [3, 4]]  - surprise!

deep = copy.deepcopy(grid) # every level is copied
```

<details>
<summary>Click for answer</summary>

`.copy()`, slicing, and `list(...)` make a **shallow** copy: a new outer
container whose elements still point at the *same* inner objects. `copy.deepcopy()`
recursively copies every level, so nested mutations stay independent. Deep
copies are slower, so use them only when shared nesting is actually a problem.

📖 Deep dive: [Immutability](../../05_functional_programming/02_immutability/README.md)

</details>

---

### 4. Hashability and dict keys

**Why can a tuple be a dict key but a list cannot?**

```python
d = {(1, 2): "point"}   # fine - tuples are immutable and hashable
d[[1, 2]] = "point"     # TypeError: unhashable type: 'list'
```

<details>
<summary>Click for answer</summary>

Dict keys must be **hashable**: their `hash()` value must never change over
their lifetime. A list is mutable — append one item and its hash would go
stale — so Python refuses. An immutable tuple is safe, *as long as everything
inside it is hashable too* (`(1, [2])` is not).

📖 Deep dive: [Hash Tables](../../02_data_structures/10_hash_tables/README.md)

</details>

---

### 5. List vs tuple

**When do you reach for a tuple instead of a list?**

```python
point = (3, 4)       # a record: fixed shape, fixed meaning
steps = []           # a collection: will grow and shrink
```

<details>
<summary>Click for answer</summary>

A tuple is an **immutable** sequence: use it for heterogeneous records with a
fixed shape (an x/y point, a database row), and as dict keys or set members
(see question 4). A list is for homogeneous items you will append, remove, or
sort. Tuples are also slightly smaller and faster since they never change.

📖 Deep dive: [Tuples](../../02_data_structures/05_tuples/README.md)

</details>

---

### 6. Assignment never copies

**After `b = a`, why does changing `b` change `a`?**

```python
a = [1, 2, 3]
b = a            # two names, ONE list
b.append(4)
print(a)         # [1, 2, 3, 4]
```

<details>
<summary>Click for answer</summary>

In Python, assignment binds a **name to an object** — it never copies the
object. `a` and `b` are two labels on the same list, so a change through
either name is visible through both. For an independent copy use `a.copy()`
(remember question 3: shallow!), or `copy.deepcopy()` for nested data.

📖 Deep dive: [References vs Values](../../11_memory_performance/02_references_vs_values/README.md)

</details>

---

## Data Structures

### 7. Why dict lookup is O(1)

**Why is `d[key]` fast no matter how big the dict is?**

<details>
<summary>Click for answer</summary>

A dict is a **hash table**: Python hashes the key, and the hash directly
picks a "bucket" in an internal array. Finding an item is one hash plus one
peek — constant time on average, regardless of size. The cost is memory and
the hashability requirement from question 4.

📖 Deep dive: [Hash Tables](../../02_data_structures/10_hash_tables/README.md)

</details>

---

### 8. List vs set for membership

**You need to check `x in items` in a loop over 100,000 items. What is wrong
with using a list?**

```python
items = [1, 2, 3, 4, 5]
2 in items            # O(n) - scans until it finds it

s = {1, 2, 3, 4, 5}
2 in s                # O(1) average - hash lookup
```

<details>
<summary>Click for answer</summary>

A list membership test scans element by element — O(n) — so a loop over
100,000 items does up to 100,000 × 100,000 comparisons. A set uses hash
lookups: O(1) on average. Convert once with `s = set(items)` and every later
check is cheap; just remember sets drop duplicates and lose order.

📖 Deep dive: [Sets](../../02_data_structures/04_sets/README.md)

</details>

---

### 9. Set operations

**What do `|`, `&`, `-`, and `^` do on sets?**

```python
a = {1, 2, 3}
b = {3, 4, 5}
a | b   # {1, 2, 3, 4, 5}  union          - in either
a & b   # {3}               intersection  - in both
a - b   # {1, 2}            difference    - in a only
a ^ b   # {1, 2, 4, 5}      symmetric difference - in exactly one
```

<details>
<summary>Click for answer</summary>

They are union, intersection, difference, and symmetric difference — the same
four operations as the methods `a.union(b)`, `a.intersection(b)`,
`a.difference(b)`, `a.symmetric_difference(b)`. Together they turn "compare
these two groups" questions into one-liners, which is why sets are an
interview favorite.

📖 Deep dive: [Sets](../../02_data_structures/04_sets/README.md)

</details>

---

### 10. Deduplicate while keeping order

**Remove duplicates from a list without scrambling the order.**

```python
items = [3, 1, 3, 2, 1]
unique = list(dict.fromkeys(items))
print(unique)            # [3, 1, 2]
```

<details>
<summary>Click for answer</summary>

`dict.fromkeys(items)` builds a dict whose keys are the items — dicts reject
duplicate keys **and preserve insertion order** (guaranteed since Python 3.7),
so wrapping it in `list()` gives de-duplicated, order-kept values. `list(set(items))`
is shorter but randomly ordered — mention that trade-off and you sound senior.

📖 Deep dive: [Dictionaries and Maps](../../02_data_structures/03_dictionaries_maps/README.md)

</details>

---

### 11. Stack or queue?

**Which built-in structures do you use for a stack and for a queue?**

```python
stack = []
stack.append(1)        # push
top = stack.pop()      # pop - LIFO, O(1)

from collections import deque
queue = deque()
queue.append(1)          # enqueue
first = queue.popleft()  # dequeue - O(1); list.pop(0) is O(n)!
```

<details>
<summary>Click for answer</summary>

A plain list is a fine **stack**: `append` and `pop` both work at the end in
O(1). For a **queue** use `collections.deque`, because `list.pop(0)` must shift
every remaining element — O(n). Saying "deque for queues, list for stacks" is
the expected answer.

📖 Deep dive: [Stacks and Queues](../../02_data_structures/06_stacks_queues/README.md)

</details>

---

## Functions & Scope

### 12. The LEGB rule

**Python looks up a name in four places. Name them, in order.**

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        return x
    return inner()

print(outer())     # local
```

<details>
<summary>Click for answer</summary>

**L**ocal (inside the current function) → **E**nclosing (the function that
wrapped it) → **B**uilt-in (things like `len` and `print`). Python stops at
the first match, which is why the inner `x` above wins. Shadowing a name at
an inner level is legal but confusing — pick distinct names.

📖 Deep dive: [Functions Basics](../../01_foundations/05_functions_basics/README.md)

</details>

---

### 13. `*args` and `**kwargs`

**What do `*args` and `**kwargs` actually collect?**

```python
def report(*args, **kwargs):
    print(args)      # tuple of extra positional values
    print(kwargs)    # dict of extra keyword values

report(1, 2, mode="fast")
# (1, 2)
# {'mode': 'fast'}
```

<details>
<summary>Click for answer</summary>

`*args` gathers leftover **positional** arguments into a tuple, and
`**kwargs` gathers leftover **keyword** arguments into a dict. The `*` is the
magic — the names are convention, not syntax. The same `*` also unpacks in a
call: `f(*my_list, **my_dict)` spreads a sequence and a mapping into
arguments, which is how decorators forward arguments.

📖 Deep dive: [Functions Basics](../../01_foundations/05_functions_basics/README.md)

</details>

---

### 14. Closures and late binding

**Why does the first greeter say "Bo" instead of "Ada"?**

```python
def make_greeters(names):
    funcs = []
    for n in names:
        funcs.append(lambda: f"Hi, {n}")
    return funcs

gs = make_greeters(["Ada", "Bo"])
print(gs[0]())    # Hi, Bo  - not Ada!
```

<details>
<summary>Click for answer</summary>

A closure captures the **variable itself, not its value at creation time**.
All three lambdas share the same `n`, which holds `"Bo"` once the loop ends —
this is called *late binding*. Capture a snapshot with a default argument:
`lambda n=n: f"Hi, {n}"`.

📖 Deep dive: [Closures](../../05_functional_programming/06_closures/README.md)

</details>

---

### 15. The UnboundLocalError trap

**This code reads a global, adds one — and crashes. Why?**

```python
count = 0

def bump():
    count = count + 1   # UnboundLocalError!

bump()
```

<details>
<summary>Click for answer</summary>

Because `bump` **assigns** to `count`, Python treats it as a local variable
for the whole function — so the right-hand `count + 1` reads a local that has
no value yet. You *can* patch it with `global count` (or `nonlocal` for
enclosing scopes), but the cleaner fix is to pass the value in and return the
new one.

📖 Deep dive: [Functions Basics](../../01_foundations/05_functions_basics/README.md)

</details>

---

### 16. Lambda limits

**When is a `lambda` the wrong tool?**

```python
pairs = [(1, "b"), (2, "a")]
pairs.sort(key=lambda pair: pair[1])   # one expression - fine
```

<details>
<summary>Click for answer</summary>

A lambda is restricted to a **single expression** — no statements, no
assignment, no `if:` blocks (only the ternary `x if c else y`). The moment
you need logic, comments, or a second look, write a named `def` instead;
readability beats cleverness. Lambdas shine as short inline `key=` and
`sort=` callbacks.

📖 Deep dive: [Lambda Expressions](../../05_functional_programming/04_lambda_expressions/README.md)

</details>

---

## OOP

### 17. Class vs instance attributes

**Where does each attribute live, and what does the shadowing do?**

```python
class Dog:
    legs = 4                  # class attribute - shared by all

    def __init__(self, name):
        self.name = name      # instance attribute - per object

a, b = Dog("Rex"), Dog("Fido")
a.legs = 3                    # creates an instance attr, shadows the class one
print(a.legs, b.legs)         # 3 4
```

<details>
<summary>Click for answer</summary>

Class attributes live on the **class object** and are shared by every
instance; instance attributes live in each object's own `__dict__`. Reading
`a.legs` falls back to the class if no instance attribute exists — but the
assignment above *creates* an instance attribute that shadows it, it never
edits the shared one. Great for constants; dangerous as mutable shared state.

📖 Deep dive: [Classes and Objects](../../04_oop_concepts/01_classes_and_objects/README.md)

</details>

---

### 18. The `@property` decorator

**What problem does `@property` solve?**

```python
class Temperature:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value
```

<details>
<summary>Click for answer</summary>

It lets a class expose a **method as if it were an attribute**, so callers
write `t.celsius = 25` while the class runs validation behind the scenes.
That means you can start with a plain attribute and add logic later without
breaking any caller — the classic Python answer to "getters and setters".

📖 Deep dive: [Encapsulation](../../04_oop_concepts/02_encapsulation/README.md)

</details>

---

### 19. `__repr__` vs `__str__`

**Which one runs in each print below?**

```python
class Point:
    def __repr__(self):
        return "Point(x=1, y=2)"
    def __str__(self):
        return "(1, 2)"

p = Point()
print(p)       # (1, 2)            -> __str__
print([p])     # [Point(x=1, y=2)] -> containers use __repr__
```

<details>
<summary>Click for answer</summary>

`__str__` is for **end users** — readable output via `print()` and `str()`.
`__repr__` is for **developers** — unambiguous, ideally something that could
recreate the object, and the fallback when `__str__` is missing. Containers
always use `__repr__` for their elements, which is why defining `__repr__`
first is the common advice.

📖 Deep dive: [Dunder Methods](../../04_oop_concepts/08_dunder_methods/README.md)

</details>

---

### 20. Dataclasses

**What does `@dataclass` write for you?**

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0

u = User("Ada")
print(u)                  # User(name='Ada', age=0)
print(u == User("Ada"))   # True
```

<details>
<summary>Click for answer</summary>

It generates the boilerplate: `__init__` from the annotated fields,
`__repr__`, and `__eq__` (field-by-field comparison) — roughly twenty lines
per class, gone. You can still add methods, defaults, and frozen
(immutability) options. Reach for one whenever a class mostly *holds data*.

📖 Deep dive: [Dataclasses](../../04_oop_concepts/09_dataclasses/README.md)

</details>

---

### 21. Method Resolution Order (MRO)

**In diamond inheritance, which parent's method wins?**

```python
class A:        pass
class B(A):     pass
class C(A):     pass
class D(B, C):  pass

print(D.__mro__)   # D -> B -> C -> A -> object
```

<details>
<summary>Click for answer</summary>

Python linearizes the family tree with the **C3 algorithm** and searches that
order — here `D`, then `B`, then `C`, then `A` — so `B` wins. Every class's
order is visible in its `__mro__` attribute, and `super()` follows exactly
this chain, not just "the parent". Mentioning C3 by name is a bonus point.

📖 Deep dive: [Inheritance](../../04_oop_concepts/03_inheritance/README.md)

</details>

---

### 22. Composition vs inheritance

**When should `Car` *have* an `Engine` instead of *being* one?**

```python
class Engine:
    def start(self):
        print("Vroom")

class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS an Engine

    def drive(self):
        self.engine.start()
```

<details>
<summary>Click for answer</summary>

Use inheritance only for a genuine **is-a** relationship (a `Dog` *is an*
`Animal`); use composition for **has-a** relationships (a `Car` *has an*
`Engine`). Composition keeps coupling low — you can swap the engine without
touching the car's family tree. The rule of thumb: prefer composition, and
reach for inheritance when the child truly behaves like the parent everywhere.

📖 Deep dive: [Composition vs Inheritance](../../04_oop_concepts/06_composition_vs_inheritance/README.md)

</details>

---

## Iterators & Generators

### 23. The iterator protocol

**What makes an object work in a `for` loop?**

```python
class CountDown:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration      # the "we're done" signal
        self.n -= 1
        return self.n + 1

for x in CountDown(3):
    print(x)          # 3, 2, 1
```

<details>
<summary>Click for answer</summary>

Two methods: `__iter__` returns an iterator (a `for` loop calls it first),
and `__next__` returns the next value or raises `StopIteration` to finish.
Anything with that pair *is* an iterator, which is how `for`, `zip`, `list()`
and friends all speak one protocol.

📖 Deep dive: [Generators and Iterators](../../05_functional_programming/08_generators_and_iterators/README.md)

</details>

---

### 24. Generators are one-shot

**What does the second `list(g)` print, and why?**

```python
def gen():
    yield 1
    yield 2

g = gen()
print(list(g))    # [1, 2]
print(list(g))    # [] - ?!
```

<details>
<summary>Click for answer</summary>

An empty list: a generator is an **iterator, and iterators are exhausted once
they finish** — there is no rewind. The first `list()` consumed both yields
and raised `StopIteration` internally; the second sees an already-spent
generator. Need the values twice? Store them in a list, or call the generator
function again for a fresh one.

📖 Deep dive: [Generators and Iterators](../../05_functional_programming/08_generators_and_iterators/README.md)

</details>

---

### 25. Why `yield` is lazy

**What does a generator function actually save you?**

```python
def squares(n):
    for i in range(n):
        yield i * i

total = sum(squares(10_000_000))   # one value in memory at a time
```

<details>
<summary>Click for answer</summary>

`yield` pauses the function and hands out **one value at a time**, on demand —
so memory holds a single number, not ten million. The computation also stops
early if you stop asking (`next(g)` or a `break` in the loop). That is why
processing a huge file line-by-line with a generator works on any machine.

📖 Deep dive: [Generators and Iterators](../../05_functional_programming/08_generators_and_iterators/README.md)

</details>

---

### 26. Generator expression vs list comprehension

**When does swapping `[]` for `()` matter?**

```python
import sys

lc = [x * x for x in range(1000)]   # list - built eagerly, in memory
ge = (x * x for x in range(1000))   # generator - built on demand
print(sys.getsizeof(lc) > sys.getsizeof(ge))   # True
```

<details>
<summary>Click for answer</summary>

The list comprehension builds **all** values immediately; the generator
expression produces them lazily and remembers only the recipe — a few hundred
bytes versus kilobytes, and megabytes versus gigabytes on big data. Use `()`
when you stream the values once (into `sum`, `any`, `max`...); use `[]` when
you need to reuse, index, or know the length.

📖 Deep dive: [Lists and Arrays](../../02_data_structures/01_lists_arrays/README.md)

</details>

---

## Exceptions & Context Managers

### 27. Exceptions vs returning `None`

**A lookup function can fail. Why raise instead of returning `None`?**

```python
# Returning None hides the failure until somewhere else blows up:
url = config.get("database_url")   # None now...
url.strip()                        # AttributeError: 'NoneType' object...

# Raising fails fast, at the actual mistake:
url = config["database_url"]       # KeyError: 'database_url'
```

<details>
<summary>Click for answer</summary>

`None` is a **silent failure**: it travels happily through the code and
crashes later, far from the real bug, with a confusing message. An exception
fails **loudly, immediately, and specifically** — and callers who genuinely
don't care can still catch it. Reserve `None` for a legitimate "absent" value
that the caller explicitly checks.

📖 Deep dive: [Defensive Programming](../../08_error_handling/04_defensive_programming/README.md)

</details>

---

### 28. What `with` really does

**What do `__enter__` and `__exit__` guarantee?**

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        return False          # False = don't swallow exceptions

with Timer() as t:
    sum(range(1_000_000))
print(t.elapsed)
```

<details>
<summary>Click for answer</summary>

`with` calls `__enter__`, runs the block, then **always** calls `__exit__` —
even if the block raises — which is why files close and locks release on
every path. Returning `True` from `__exit__` would suppress the exception
(rarely what you want); `False` lets it propagate. Saying "it's a guaranteed
cleanup, not a convenience" is the interview answer.

📖 Deep dive: [Context Managers](../../08_error_handling/06_context_managers/README.md)

</details>

---

### 29. Bare `except` vs `except Exception`

**Why is a bare `except:` frowned upon?**

```python
import json

def save(config):
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f)

try:
    save({"theme": "dark"})
except (TypeError, OSError) as exc:   # catch exactly what you can handle
    print(f"Could not save: {exc}")
```

<details>
<summary>Click for answer</summary>

A bare `except:` catches *everything*, including `KeyboardInterrupt` (Ctrl+C)
and `SystemExit`, so your program becomes impossible to stop and real bugs
vanish into a generic handler. `except Exception:` is the wide-but-sane net —
it skips those control-flow exceptions. Best practice: catch the **narrowest
set you can actually handle**.

📖 Deep dive: [Try / Except / Finally](../../08_error_handling/02_try_except_finally/README.md)

</details>

---

### 30. Custom exceptions

**When and why define your own exception class?**

```python
class InsufficientFunds(Exception):
    """Raised when a withdrawal exceeds the balance."""

    def __init__(self, needed, available):
        super().__init__(f"need {needed}, have {available}")
```

<details>
<summary>Click for answer</summary>

Custom exceptions turn "a `ValueError` happened somewhere" into **catchable,
meaningful vocabulary**: callers can write `except InsufficientFunds:` and
react to exactly that situation. Subclassing `Exception` (never the base
`BaseException`) keeps normal tooling working, and the class name plus message
carry domain information. One small hierarchy per module is usually plenty.

📖 Deep dive: [Custom Exceptions](../../08_error_handling/03_custom_exceptions/README.md)

</details>

---

## Concurrency

### 31. The GIL

**What is the Global Interpreter Lock, and when does it not matter?**

<details>
<summary>Click for answer</summary>

The GIL is CPython's rule that **only one thread executes Python bytecode at
a time**, so CPU-bound threads never run in parallel on multiple cores. It
does *not* matter for I/O-bound work: threads release the GIL while waiting
on the network or disk, so downloads and file reads overlap just fine. For
CPU-bound parallelism you need separate processes (beyond this course — see
[Further Reading](../further_reading.md)); Python 3.13's optional
"free-threaded" build is the experiment aimed at removing the GIL.

📖 Deep dive: [How Python Works](../../17_cs_fundamentals/05_how_python_works/README.md)

</details>

---

### 32. Threads vs asyncio

**Both handle 100 concurrent downloads. Which do you pick, and when?**

<details>
<summary>Click for answer</summary>

Threads **preemptively** juggle tasks — the OS switches them at any moment,
so shared data needs locks; asyncio is **cooperative** — tasks run until they
`await`, and switches happen only at await points. For I/O-bound work both
work: threads are the familiar default, asyncio scales to thousands of
connections with less overhead. The hard rule both share: never block the
event loop (or hold the GIL) with heavy computation.

📖 Deep dive: [Async Programming](../../12_concurrency/03_async_programming/README.md)

</details>

---

### 33. Race conditions and `Lock`

**Why can `counter += 1` lose updates across threads?**

```python
from threading import Lock

counter = 0
lock = Lock()

def bump():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1   # read-modify-write is three steps, not one
```

<details>
<summary>Click for answer</summary>

`counter += 1` is really **read, add, write back** — three steps a thread can
be interrupted between, so two threads can read the same old value and one
increment is lost. A `Lock` makes the whole read-modify-write atomic: only
one thread inside `with lock:` at a time. The classic symptom is a total
slightly *less* than expected — worth saying out loud.

📖 Deep dive: [Race Conditions](../../12_concurrency/04_race_conditions/README.md)

</details>

---

### 34. Deadlocks

**Two threads, two locks, permanent freeze. How does that happen, and what
is the standard fix?**

```python
# Thread 1: acquire lock_a, then lock_b
# Thread 2: acquire lock_b, then lock_a
# -> each holds one and waits forever for the other
#
# Fix: every thread acquires locks in the SAME order.
```

<details>
<summary>Click for answer</summary>

A deadlock needs circular waiting: each thread holds a lock the other one
needs, and neither will let go first. The standard fix is **lock ordering** —
agree on a global order and always acquire locks in it — plus keeping critical
sections small and never calling unknown code while holding a lock. Naming
the four conditions (mutual exclusion, hold-and-wait, no preemption, circular
wait) scores extra points.

📖 Deep dive: [Deadlocks](../../12_concurrency/05_deadlocks/README.md)

</details>

---

## Stdlib Gems

### 35. `collections.Counter`

**Count how often each word appears — in one line.**

```python
from collections import Counter

words = "the cat the dog the bird".split()
counts = Counter(words)
print(counts.most_common(2))   # [('the', 3), ('cat', 1)]
```

<details>
<summary>Click for answer</summary>

`Counter` is a dict subclass built for tallying: it initializes from any
iterable, returns `0` for missing keys instead of raising, and offers
`most_common(n)` for the top hits. It also supports arithmetic — `c1 + c2`
and `c1 - c2` combine counts — which makes it the answer to half of all
"count the things" interview warm-ups.

📖 Deep dive: [Collections Module](../../16_essential_libraries/01_collections_module/README.md)

</details>

---

### 36. `collections.defaultdict`

**Group names by department without checking "is the key there yet?".**

```python
from collections import defaultdict

groups = defaultdict(list)
for name, dept in [("Ada", "eng"), ("Bo", "ops"), ("Cy", "eng")]:
    groups[dept].append(name)

print(groups)   # {'eng': ['Ada', 'Cy'], 'ops': ['Bo']}
```

<details>
<summary>Click for answer</summary>

`defaultdict(list)` auto-creates a missing key with the **default factory's**
value — here an empty list — so `groups[dept].append(...)` just works, with
no `if dept not in groups:` dance. Any zero-argument callable works: `int`
for counters, `set` for unique members. One honest caveat for interviews: a
*read* of a missing key also creates it, which can surprise.

📖 Deep dive: [Collections Module](../../16_essential_libraries/01_collections_module/README.md)

</details>

---

### 37. `collections.deque`

**Keep only the last three moves, efficiently.**

```python
from collections import deque

history = deque(maxlen=3)
for move in ["up", "down", "left", "right"]:
    history.append(move)

print(history)   # deque(['down', 'left', 'right'], maxlen=3)
```

<details>
<summary>Click for answer</summary>

A deque (double-ended queue) appends and pops at **both ends in O(1)** — the
exact operation a list does in O(n) at its front. With `maxlen=` it becomes a
self-evicting ring buffer, perfect for last-N history, sliding windows, and
undo stacks. It's the structure behind "why is your queue not a list?"
(question 11 made the same point from the data-structure side).

📖 Deep dive: [Collections Module](../../16_essential_libraries/01_collections_module/README.md)

</details>

---

### 38. `itertools`

**Name three `itertools` tools and what they replace.**

```python
from itertools import chain, islice, product

list(chain([1, 2], [3, 4]))               # [1, 2, 3, 4] - loop-free concat
list(islice(range(10), 2, 5))             # [2, 3, 4] - slicing for iterables
list(product("AB", repeat=2))             # all pairs - nested loops in one call
```

<details>
<summary>Click for answer</summary>

`chain` glues iterables without building an intermediate list, `islice`
slices any iterable (even infinite ones), and `product` generates every
combination — replacing nested `for` loops. Everything in the module is
lazy and memory-friendly, in the spirit of question 25. Saying "I don't
memorize them all — I know the module exists and reach for it first" is a
perfectly good answer.

📖 Deep dive: [Itertools Module](../../16_essential_libraries/03_itertools/README.md)

</details>

---

### 39. `pathlib` vs `os.path`

**Why do modern codebases prefer `pathlib`?**

```python
from pathlib import Path

data_dir = Path("data")
for csv_path in data_dir.glob("*.csv"):
    text = csv_path.read_text(encoding="utf-8")

out = data_dir / "result.json"   # / joins paths - no os.path.join juggling
```

<details>
<summary>Click for answer</summary>

`Path` objects are **objects with behavior**, not strings: `/` joins paths
portably, `.glob()` finds files, and `.read_text()` / `.write_text()` do
one-step I/O — no `open()`/`close()` ceremony for small files. The same code
reads correctly on Windows and macOS/Linux, which `os.path.join` handled only
by convention. Under the hood it's the stdlib, so it fits the course's
no-installs promise.

📖 Deep dive: [Pathlib Module](../../16_essential_libraries/05_pathlib/README.md)

</details>

---

### 40. Type hints basics

**What do hints cost, and what do they buy?**

```python
from typing import List, Optional

def average(nums: List[float]) -> float:
    return sum(nums) / len(nums)

def find_user(user_id: int) -> Optional[str]:
    ...
```

<details>
<summary>Click for answer</summary>

Hints are **not enforced at runtime** — Python ignores them while executing;
they are documentation that editors, linters, and `mypy` can check. The payoff
is real: autocompletion, instant "you passed the wrong type" feedback, and
signatures that explain themselves. `Optional[str]` means "a `str` or `None`"
— a two-second answer that trips up plenty of candidates.

📖 Deep dive: [Type Hints](../../01_foundations/07_type_hints/README.md)

</details>

---

## How did you do?

- **32-40 explained cleanly:** Excellent — go run the mock interviews.
- **20-31:** Solid. Revisit the deep-dive links for every miss, then retry
  those in a few days.
- **Under 20:** Perfect timing to find out! Follow the links back to the
  modules — the [quizzes](../quizzes.md) make great warm-ups — and come back.
  This page is not going anywhere.
