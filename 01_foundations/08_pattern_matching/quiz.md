# 📝 Pattern Matching - Quiz

Test your match/case skills! (Remember: `match`/`case` needs Python 3.10+.)

---

## Question 1
Which Python version introduced `match`/`case`?

A) Python 3.6  
B) Python 3.8  
C) Python 3.10  
D) Python 3.12

---

## Question 2
What will this code print?
```python
code = 404
match code:
    case 200:
        print("OK")
    case 404:
        print("Missing")
    case _:
        print("Other")
```

A) OK  
B) Missing  
C) Other  
D) Missing and Other

---

## Question 3
What happens here?
```python
target = 7
value = 3
match value:
    case target:
        print("matched")
```

A) Prints "matched", and `target` becomes 3  
B) Prints nothing  
C) SyntaxError  
D) Prints "matched", and `target` stays 7

---

## Question 4
What does the wildcard pattern `case _:` do?

A) Compares the subject against a variable named `_`  
B) Matches anything but binds nothing  
C) Matches only `None`  
D) Raises an error if nothing above it matched

---

## Question 5
Which of these inputs match the pattern `case "n" | "no":`?

A) `"n"` only  
B) `"n"` and `"no"`  
C) `"n"`, `"no"`, and `"N"`  
D) `"n"`, `"no"`, and `"maybe"`

---

## Question 6
What does this print?
```python
for n in [0, 5, 50]:
    match n:
        case 0:
            print("zero")
        case n if n > 10:
            print("big")
        case _:
            print("small")
```

A) zero, small, big  
B) zero, big, small  
C) zero, small, small  
D) zero only

---

## Question 7
Which values match the pattern `case [x, y]:`?

A) Only the exact list `[x, y]` where `x` and `y` were defined earlier  
B) Only lists of length 2  
C) Any list or tuple with exactly two items  
D) Any list of two or more items

---

## Question 8
What happens when no case matches and there is no `case _:`?
```python
value = "banana"
match value:
    case "apple":
        print("fruit A")
    case "pear":
        print("fruit B")
print("done")
```

A) SyntaxError  
B) Nothing prints at all  
C) Prints "done" only — execution falls past the match  
D) RuntimeError

---

## Answers

**Question 1 — C) Python 3.10**  
Structural pattern matching landed in Python 3.10 (2021). Older interpreters
cannot even parse the syntax.

**Question 2 — B) Missing**  
Only the first matching case runs. `case 404:` matches, so `case _:` is never
reached — no fallthrough.

**Question 3 — A) Prints "matched", and `target` becomes 3**  
A bare name in a pattern is a *capture pattern*: it matches any value and binds
it to that name. It does NOT compare against the existing `target`. To compare,
use a guard: `case v if v == target:`.

**Question 4 — B) Matches anything but binds nothing**  
`_` is the catch-all: the "else" of pattern matching, useful for making
"none of the above" explicit.

**Question 5 — B) `"n"` and `"no"`**  
An or-pattern matches if the subject equals any one of its alternatives. `"N"`
does not match — pattern matching is case-sensitive (you would add
`.lower()` on the subject first).

**Question 6 — A) zero, small, big**  
For 0 the literal matches. For 5 the guard `n > 10` is False, so the case is
skipped and the wildcard catches it. For 50 the guard is True, so "big" runs.

**Question 7 — C) Any list or tuple with exactly two items**  
Sequence patterns match *structure*: exactly two items, bound to `x` and `y`.
They are not comparisons against earlier variables (that's Question 3's gotcha),
and a third item means the shape no longer fits.

**Question 8 — C) Prints "done" only — execution falls past the match**  
A non-matching value with no `case _:` is not an error: Python simply moves on
to the next statement. That silence is why a catch-all is usually a good idea.

---

## How did you do?

- **7-8 correct:** Pattern matching pro! 🏆
- **5-6 correct:** Great work! Review the ones you missed.
- **3-4 correct:** Good progress — re-run examples.py and re-read the README.
- **0-2 correct:** Re-read the README and try the exercises again.
