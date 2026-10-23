# 🪄 Dunder Methods Quiz

## 1. How should you normally get an object's debug representation?
- [ ] `obj.__repr__()`
- [ ] `repr(obj)`
- [ ] `print(obj.__str__)`
- [ ] `debug(obj)`

## 2. Which method does `print(playlist)` use first?
- [ ] `__repr__`
- [ ] `__print__`
- [ ] `__str__`
- [ ] `__format__`

## 3. You define `__eq__` on your class but NOT `__hash__`. What happens when you use an instance as a dict key?
- [ ] It works, but slowly
- [ ] `TypeError: unhashable type` — defining `__eq__` sets `__hash__` to `None`
- [ ] The dict silently drops the entry
- [ ] Python auto-generates a hash from the attributes

## 4. Which rule must `__hash__` follow to keep dicts and sets correct?
- [ ] It must return a unique number for every object
- [ ] It must return a string
- [ ] If `a == b`, then `hash(a) == hash(b)`
- [ ] It must be larger than `len(a)`

## 5. `len(playlist)` triggers `__len__`. What must `__len__` return?
- [ ] Any number, including floats like `3.0`
- [ ] A non-negative int
- [ ] A string like `"3"`
- [ ] `True` or `False`

## 6. You define only `__getitem__` on a class. What do you get for free?
- [ ] Pickling support
- [ ] `for item in obj:` iteration (Python indexes until `IndexError`)
- [ ] Comparison with `<` and `>`
- [ ] Nothing — iteration needs `__iter__`

## 7. `"Bohemian Rhapsody" in playlist` triggers which method?
- [ ] `__in__`
- [ ] `__query__`
- [ ] `__contains__`
- [ ] `__getitem__`

## 8. `favorites + workout` calls `favorites.__add__(workout)`. If that returns `NotImplemented` (or is missing), what does Python try next?
- [ ] Raises `TypeError` immediately — no fallback
- [ ] Calls `favorites.__concat__(workout)`
- [ ] Mutates `favorites` in place
- [ ] Calls `workout.__radd__(favorites)` — the right operand's reflected method

---

### Answers
1. `repr(obj)` — call the friendly builtin; the dunder is the wiring behind the wall.
2. `__str__` — `print()` and `str()` prefer it and fall back to `__repr__` if missing.
3. `TypeError: unhashable type` — defining `__eq__` without `__hash__` makes instances unhashable; define both together.
4. If `a == b`, then `hash(a) == hash(b)` — equal objects must land in the same hash bucket.
5. A non-negative int — returning `"3"` or `3.0` raises `TypeError`.
6. `for item in obj:` iteration — the legacy protocol indexes `obj[0]`, `obj[1]`, ... until `IndexError` (though `__iter__` is the modern way).
7. `__contains__`
8. `workout.__radd__(favorites)` — the reflected method; that is how `3 + my_object` can work even though ints know nothing about your class.
