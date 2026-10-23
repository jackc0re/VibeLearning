# 🏷️ Type Hints - Quiz

Test your type hint knowledge!

---

## Question 1
What does Python do with type hints when it runs your code?

A) Raises a TypeError for wrong types  
B) Converts wrong types for you automatically  
C) Ignores them - hints are not enforced at runtime  
D) Prints a warning for every mismatch

---

## Question 2
What does the `-> str` part of `def greet(name: str) -> str:` describe?

A) The type of the first parameter  
B) The type of the value the function returns  
C) That the function prints a string  
D) That the function converts its result to a string

---

## Question 3
`find_score` returns the score for a name, or `None` when the name is
missing. Which return hint is honest?

A) `-> int`  
B) `-> None`  
C) `-> Optional[int]`  
D) `-> str`

---

## Question 4
Why does `def total(scores: list[int]) -> int:` run on Python 3.8 in this
repo's lesson files?

A) `list[int]` has worked since Python 3.0  
B) The files start with `from __future__ import annotations`, so hints are stored as text and never evaluated at runtime  
C) Python 3.8 skips any function that has hints  
D) It does not work - lesson files require Python 3.9+

---

## Question 5
What does `Callable[[int], int]` describe?

A) Any built-in function  
B) A function that takes one int and returns an int  
C) A function that takes two ints  
D) A class with one int attribute

---

## Question 6
In `def first_item(items: List[T]) -> T:`, what is `T`?

A) A specific type, short for tuple  
B) A placeholder (TypeVar) linking the list's element type to the return type  
C) A built-in type you must import from `builtins`  
D) The number of parameters the function takes

---

## Question 7
What does `typing.get_type_hints(some_function)` give you?

A) A list of bugs in the function  
B) A dict of the annotations Python recorded for the function's parameters and return  
C) The types of the values that were passed in on a call  
D) A warning for every wrong type the function receives

---

## Question 8
Which spelling is the legacy form (works on every Python 3.x) of
`dict[str, int]`?

A) `dictionary[str, int]`  
B) `Dict[str, int]` from the `typing` module  
C) `dict{str: int}`  
D) `Map[str, int]`

---

## Answers

1. **C** - Hints are labels for humans and tools (like mypy). The interpreter
   never checks them: `add("Hello, ", "world")` with `int` hints runs fine.
2. **B** - The part after the `->` arrow always describes the return value.
   `name: str` (before the arrow) describes the parameter.
3. **C** - `Optional[int]` means "an int, or None" - exactly what the function
   can return. Plain `-> int` would be a lie, and `-> None` would too.
4. **B** - The future import stores every annotation as plain text and never
   evaluates it at runtime, so the modern `list[int]` spelling is safe even
   where it is not a real object (Python 3.8).
5. **B** - The inner list `[int]` is the argument types; the item after it is
   the return type. So: one int in, one int out.
6. **B** - `T = TypeVar("T")` is a placeholder. Calling with a list of ints
   makes T mean int; calling with strings makes T mean str. The link between
   the parameter and the return is the whole point.
7. **B** - `get_type_hints` reads back what Python recorded on the function,
   as a dict like `{'a': <class 'int'>, 'return': <class 'int'>}`. It knows
   nothing about the actual values passed at call time.
8. **B** - `List`, `Dict`, `Tuple`, `Optional`, `Union` and friends live in
   `typing` and work on every Python 3.x. `dict[str, int]` as a real object
   needs Python 3.9+.

---

## How did you do?

- **7-8 correct:** Type hint pro! 🏷️
- **5-6 correct:** Solid - review the ones you missed.
- **3-4 correct:** Re-run [examples.py](examples.py) and try again.
- **0-2 correct:** Start with the [README](README.md) once more - you will get there.
