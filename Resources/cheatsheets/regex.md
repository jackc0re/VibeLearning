# Regex Cheatsheet

Quick reference for the `re` module: pattern syntax, matching functions, flags, and copy-paste recipes for everyday text processing.

---

## Pattern Syntax

### Character Classes

| Pattern | Matches | Equivalent |
|---------|---------|------------|
| `\d` | Any digit | `[0-9]` |
| `\D` | Any non-digit | `[^0-9]` |
| `\w` | Word character (letter, digit, underscore) | `[a-zA-Z0-9_]` |
| `\W` | Non-word character | `[^a-zA-Z0-9_]` |
| `\s` | Whitespace (space, tab, newline, ...) | `[ \t\n\r\f\v]` |
| `\S` | Non-whitespace | `[^ \t\n\r\f\v]` |
| `.` | Any character except newline | (use `re.S` to include newline) |
| `[abc]` | a, b, or c | |
| `[^abc]` | Anything except a, b, or c | |
| `[a-z0-9]` | Ranges inside a class | |

### Quantifiers

| Pattern | Matches | Example |
|---------|---------|---------|
| `*` | 0 or more | `ca*t` matches `ct`, `cat`, `caat` |
| `+` | 1 or more | `ca+t` matches `cat`, `caat` |
| `?` | 0 or 1 | `colou?r` matches `color`, `colour` |
| `{n}` | Exactly n | `a{3}` matches `aaa` |
| `{n,}` | n or more | `a{2,}` matches `aa`, `aaa`, ... |
| `{n,m}` | Between n and m | `a{2,4}` matches `aa`, `aaa`, `aaaa` |

Quantifiers are **greedy** by default — they grab as much as possible. Add `?` to make them lazy:

```python
import re

re.search(r'<.+>', '<a> and <b>').group()   # '<a> and <b>' (too much!)
re.search(r'<.+?>', '<a> and <b>').group()  # '<a>' (lazy stops early)
```

### Anchors

| Pattern | Matches |
|---------|---------|
| `^` | Start of string (start of each line with `re.M`) |
| `$` | End of string (end of each line with `re.M`) |
| `\b` | Word boundary — between `\w` and `\W` |

```python
re.findall(r'\bcat\b', 'cat catalog concat')  # ['cat'] — whole word only
```

### Groups, Alternation & Escapes

| Pattern | Meaning |
|---------|---------|
| `(...)` | Capturing group |
| `(?:...)` | Group without capturing |
| `(?P<name>...)` | Named group |
| `a\|b` | Alternation — a or b |
| `\.` `\*` `\\` | Escape a metacharacter to match it literally |

```python
import re

# Backslashes in patterns: use raw strings so Python keeps them intact
re.search(r'\d+\.\d+', 'pi is 3.14 here')  # matches '3.14'
```

---

## re Module Functions

| Function | Returns | Notes |
|----------|---------|-------|
| `re.match(p, s)` | Match or `None` | Only matches at the **start** of the string |
| `re.search(p, s)` | Match or `None` | First match **anywhere** in the string |
| `re.fullmatch(p, s)` | Match or `None` | The **whole** string must match |
| `re.findall(p, s)` | List of matches | Strings, or tuples if the pattern has groups |
| `re.finditer(p, s)` | Iterator of Match objects | Positions included; memory-friendly |
| `re.sub(p, repl, s)` | New string | Replace matches (`count=N` to limit) |
| `re.split(p, s)` | List of strings | Split on the pattern (`maxsplit=N` to limit) |
| `re.compile(p)` | Pattern object | Compile once, reuse for many strings |

### Match Objects

```python
import re

m = re.search(r'(\w+)@(\w+)', 'mail me at alice@example ok')
if m:                       # Always check — no match means None
    m.group()               # 'alice@example'  (whole match)
    m.group(1)              # 'alice'          (first group)
    m.group(1, 2)           # ('alice', 'example')
    m.start()               # 11  (index where match begins)
    m.end()                 # 24  (index just past the match)
    m.span()                # (11, 24)
```

### compile() for Reuse

```python
import re

number = re.compile(r'\b\d+\b')
number.findall('room 3, floor 12')   # ['3', '12']
number.search('gate 7').group()      # '7'
```

---

## Flags

| Flag | Short | Effect |
|------|-------|--------|
| `re.IGNORECASE` | `re.I` | Case-insensitive matching |
| `re.MULTILINE` | `re.M` | `^` and `$` match at each line break |
| `re.DOTALL` | `re.S` | `.` also matches newline |
| `re.VERBOSE` | `re.X` | Whitespace and `#` comments allowed in the pattern |

```python
import re

re.findall(r'python', 'Python and python', re.IGNORECASE)  # ['Python', 'python']

# VERBOSE makes complex patterns readable
pattern = re.compile(r"""
    \d{4}   # year
    -\d{2}  # month
    -\d{2}  # day
""", re.VERBOSE)
```

---

## Copy-Paste Recipes

### 1. Extract Dates (ISO format YYYY-MM-DD)

```python
import re

text = "Due 2025-01-15, revised 2025-03-02."
dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
print(dates)  # ['2025-01-15', '2025-03-02']
```

### 2. Split on Whitespace Runs

```python
import re

messy = "  hello   world\tfoo\nbar  "
words = re.split(r'\s+', messy.strip())
print(words)  # ['hello', 'world', 'foo', 'bar']
# .strip() first avoids a leading '' when the text starts with spaces
```

### 3. Strip Punctuation

```python
import re

text = "Well... that's all, folks!"
clean = re.sub(r'[^\w\s]', '', text)
print(clean)  # 'Well thats all folks'
```

### 4. Simple Email-ish Sanity Check

```python
import re

def looks_like_email(text):
    """Rough sanity check, NOT real validation."""
    return re.fullmatch(r'[\w.+-]+@[\w-]+\.[\w.-]+', text) is not None

print(looks_like_email("alice@example.com"))    # True
print(looks_like_email("not-an-email"))         # False
```

> ⚠️ **Honest caveat:** fully correct email validation by regex is famously
> hard, and this pattern happily accepts things that aren't real mailboxes
> (`a@b.co` exists, `no_body@nowhere` doesn't). Use it to catch obvious
> typos in a form; the only true test is sending a confirmation email.

### 5. Named Groups for Readable Access

```python
import re

pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
m = re.search(pattern, "Deadline: 2025-06-30!")
if m:
    print(m.group('year'))   # '2025'
    print(m.group('month'))  # '06'
    print(m['day'])          # '30'  (dict-style also works, 3.6+)
    print(m.groupdict())     # {'year': '2025', 'month': '06', 'day': '30'}

# Groups also work in re.sub replacements: \1, \2 ... or \g<name>
print(re.sub(pattern, r'\g<day>/\g<month>/\g<year>', "Deadline: 2025-06-30!"))
# Deadline: 30/06/2025!
```

---

## Quick Reference

| Task | Code |
|------|------|
| First match anywhere | `re.search(r'\d+', text)` |
| Match at start only | `re.match(r'\d+', text)` |
| All matches as list | `re.findall(r'\d+', text)` |
| All matches with positions | `re.finditer(r'\d+', text)` |
| Replace | `re.sub(r'\d+', 'N', text)` |
| Split | `re.split(r'\s+', text)` |
| Case-insensitive | `re.search(r'hi', text, re.I)` |
| Named group | `(?P<name>...)` → `m['name']` |
| Whole word | `r'\bword\b'` |
| Lazy quantifier | `*?`, `+?`, `??` |

---

**Full lesson:** [16_essential_libraries — Regular Expressions](../../16_essential_libraries/06_regular_expressions/README.md)

**Back to [Resources](../README.md)**
