# 🧠 Dataclasses Quiz

## 1. Which methods does `@dataclass` generate by default?
- [ ] `__init__`, `__repr__`, and `__eq__`
- [ ] Only `__init__`
- [ ] `__init__`, `__repr__`, `__eq__`, `__lt__`, and `__gt__`
- [ ] `__init__`, `__hash__`, and `__del__`

## 2. How does a dataclass field get declared?
- [ ] By assigning inside `__init__` only
- [ ] By writing a type-annotated name in the class body (e.g. `title: str`)
- [ ] By calling `field()` with no arguments
- [ ] By listing names in the decorator: `@dataclass("title", "author")`

## 3. What happens when you write `tags: list = []` inside a `@dataclass`?
- [ ] Every instance silently shares the same list (like plain function defaults)
- [ ] The class is created, but `tags` is always `None`
- [ ] A `ValueError` is raised at class definition, suggesting `default_factory`
- [ ] The list is copied for each instance automatically

## 4. What is the correct way to give each instance its own empty list?
- [ ] `tags: list = list()`
- [ ] `tags: list = []`
- [ ] `tags = field([])`
- [ ] `tags: list = field(default_factory=list)`

## 5. What happens when you assign to a field of a `@dataclass(frozen=True)` instance?
- [ ] The assignment succeeds silently
- [ ] `FrozenInstanceError` is raised
- [ ] `TypeError: object doesn't support item assignment` is raised
- [ ] A new instance is returned

## 6. Why can a frozen dataclass be used as a dictionary key while a regular dataclass cannot?
- [ ] Frozen dataclasses are smaller in memory
- [ ] `frozen=True` plus the default `eq=True` generates a `__hash__`; mutable dataclasses get none
- [ ] Regular dataclasses cannot be created at module level
- [ ] Dictionary keys must be frozen by dictionary rules for any object type

## 7. When does `__post_init__` run?
- [ ] Before `__init__`, to prepare the fields
- [ ] Only when you call `obj.__post_init__()` manually
- [ ] Right after the generated `__init__`, with the fields already set
- [ ] When the object is deleted

## 8. Which `@dataclass` option requires Python 3.10+ (and so is avoided in this repo)?
- [ ] `frozen=True`
- [ ] `order=True`
- [ ] `field(default_factory=list)`
- [ ] `kw_only=True`

---

### Answers
1. `__init__`, `__repr__`, and `__eq__` (ordering methods and `__hash__` need extra flags)
2. By writing a type-annotated name in the class body (e.g. `title: str`) — the decorator reads the annotations
3. A `ValueError` is raised at class definition, suggesting `default_factory` — dataclasses refuses the shared-mutable bug instead of creating it
4. `tags: list = field(default_factory=list)` — the factory builds a fresh list per instance
5. `FrozenInstanceError` is raised
6. `frozen=True` plus the default `eq=True` generates a `__hash__`; mutable dataclasses get none (an object that can change must not be a key)
7. Right after the generated `__init__`, with the fields already set — ideal for validation and normalization
8. `kw_only=True` (and also `slots=True`) — both arrived in Python 3.10; this repo targets 3.8
