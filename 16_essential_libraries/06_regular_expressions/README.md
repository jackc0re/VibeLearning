# 🔍 Regular Expressions (re module)

> **Pattern matching for text processing**

---

## 🎯 Learning Objectives

By the end of this section, you'll understand:
- How to write basic regex patterns
- Common metacharacters and their meanings
- How to use `re` module functions
- When to use (and not use) regular expressions

---

## 💡 What Are Regular Expressions?

Regular expressions (regex) are patterns used to match character combinations in strings.

### Real-World Analogy

Think of regex like a search with wildcards on steroids:
- Normal search: Find exact word "cat"
- Regex search: Find "c.t" (cat, cut, cot), "ca+" (ca, cat, caat), "\d+" (any number)

---

## 🔤 Basic Patterns

### Literal Characters

```python
import re

re.search(r'cat', 'the cat sat')      # Matches 'cat'
re.search(r'hello', 'hello world')    # Matches 'hello'
```

### Metacharacters

| Character | Meaning | Example |
|-----------|---------|---------|
| `.` | Any character except newline | `c.t` matches cat, cut |
| `^` | Start of string | `^hello` matches "hello world" |
| `$` | End of string | `world$` matches "hello world" |
| `*` | 0 or more | `ca*t` matches ct, cat, caat |
| `+` | 1 or more | `ca+t` matches cat, caat |
| `?` | 0 or 1 | `colou?r` matches color, colour |
| `{n}` | Exactly n | `a{3}` matches aaa |
| `{n,m}` | Between n and m | `a{2,4}` matches aa, aaa, aaaa |

---

## 🔢 Character Classes

### Predefined Classes

| Pattern | Matches | Equivalent |
|---------|---------|------------|
| `\d` | Any digit | `[0-9]` |
| `\D` | Any non-digit | `[^0-9]` |
| `\w` | Word character | `[a-zA-Z0-9_]` |
| `\W` | Non-word character | `[^a-zA-Z0-9_]` |
| `\s` | Whitespace | `[ \t\n\r\f\v]` |
| `\S` | Non-whitespace | `[^ \t\n\r\f\v]` |

### Custom Classes

```python
import re

# Match vowels
re.findall(r'[aeiou]', 'hello')  # ['e', 'o']

# Match lowercase letters
re.findall(r'[a-z]', 'Hello')    # ['e', 'l', 'l', 'o']

# Match anything except vowels
re.findall(r'[^aeiou]', 'hello') # ['h', 'l', 'l']

# Match specific characters
re.findall(r'[xyz]', 'xylophone') # ['x', 'o'] wait, o is not...
# Actually returns ['x']
```

---

## 🔗 Groups and Alternation

### Groups with Parentheses

```python
import re

# Capture groups
text = "John Smith, 30 years old"
match = re.search(r'(\w+) (\w+), (\d+)', text)
if match:
    print(match.group(0))  # Full match: "John Smith, 30"
    print(match.group(1))  # First group: "John"
    print(match.group(2))  # Second group: "Smith"
    print(match.groups())  # All groups: ("John", "Smith", "30")
```

### Named Groups

```python
import re

pattern = r'(?P<first>\w+) (?P<last>\w+)'
match = re.search(pattern, 'John Smith')
if match:
    print(match.group('first'))  # John
    print(match.group('last'))   # Smith
```

### Alternation (OR)

```python
import re

# Match cat OR dog
re.findall(r'cat|dog', 'I have a cat and a dog')  # ['cat', 'dog']

# Match color variations
re.findall(r'colou?r', 'color and colour')  # ['color', 'colour']
```

---

## 🛠️ re Module Functions

### search() - Find first match

```python
import re

match = re.search(r'\d+', 'Age: 25 years')
if match:
    print(match.group())  # 25
    print(match.start())  # 5 (starting index)
    print(match.end())    # 7 (ending index)
```

### match() - Match at beginning

```python
import re

re.match(r'Hello', 'Hello World')   # Matches
re.match(r'World', 'Hello World')   # No match (not at start)
```

### findall() - Find all matches

```python
import re

re.findall(r'\d+', 'Room 101, Floor 3, Building 5')
# ['101', '3', '5']
```

### finditer() - Iterator of matches

```python
import re

for match in re.finditer(r'\d+', 'Room 101, Floor 3'):
    print(f"Found {match.group()} at position {match.start()}")
```

### sub() - Replace matches

```python
import re

# Replace digits with X
text = "Room 101, Floor 3"
result = re.sub(r'\d+', 'XXX', text)
print(result)  # Room XXX, Floor XXX

# Replace with groups
text = "2024-03-15"
result = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', text)
print(result)  # 15/03/2024
```

### split() - Split by pattern

```python
import re

# Split by any whitespace
text = "hello   world\tfoo\nbar"
words = re.split(r'\s+', text)
print(words)  # ['hello', 'world', 'foo', 'bar']
```

---

## ⚠️ Common Mistakes

1. **Forgetting raw strings** - Use `r'pattern'` to avoid escaping backslashes
2. **Greedy matching** - `.*` matches too much; use `.*?` for non-greedy
3. **Not escaping special characters** - Use `\` to match literal `.`, `*`, etc.
4. **Overusing regex** - For simple tasks, string methods are clearer

---

## 📝 Quick Reference

```python
import re

# Basic matching
re.search(r'pattern', text)       # First match anywhere
re.match(r'pattern', text)        # Match at start
re.findall(r'pattern', text)      # All matches as list
re.finditer(r'pattern', text)     # All matches as iterator

# Modification
re.sub(r'pattern', 'replace', text)  # Replace matches
re.split(r'pattern', text)           # Split by pattern

# Patterns
.  ^  $  *  +  ?  {n}  {n,m}         # Metacharacters
\d  \D  \w  \W  \s  \S                 # Character classes
[abc]  [^abc]  [a-z]                  # Custom classes
(a|b)  (?:...)  (?P<name>...)         # Groups
```

---

## 🎓 Next Steps

Run `examples.py` to see regex in action, then try `exercises.py`!

**Remember:** "Some people, when confronted with a problem, think 'I know, I'll use regular expressions.' Now they have two problems." — Use them wisely!
