# 🔍 Regular Expressions - Quiz

Test your knowledge of regular expressions!

---

## Question 1
**What does `.` match in a regex?**

A) A literal period
B) Any character except newline
C) Only whitespace
D) Only digits

<details>
<summary>Click for answer</summary>

**B) Any character except newline**

The dot matches any single character except newline (by default).
</details>

---

## Question 2
**What is the difference between `*` and `+`?**

A) `*` matches more characters
B) `*` matches 0 or more, `+` matches 1 or more
C) `*` is faster than `+`
D) There is no difference

<details>
<summary>Click for answer</summary>

**B) `*` matches 0 or more, `+` matches 1 or more**

`a*` matches "", "a", "aa", "aaa"...
`a+` matches "a", "aa", "aaa"... (at least one)
</details>

---

## Question 3
**What does `\d` match?**

A) Any letter
B) Any digit (0-9)
C) Any whitespace
D) Any word character

<details>
<summary>Click for answer</summary>

**B) Any digit (0-9)**

`\d` is equivalent to `[0-9]`.
</details>

---

## Question 4
**What does `^` do in a regex?**

A) Inverts a character class when inside `[]`
B) Matches start of string when at beginning
C) Both A and B
D) Escapes special characters

<details>
<summary>Click for answer</summary>

**C) Both A and B**

`^abc` matches string starting with "abc"
`[^abc]` matches any character except a, b, or c
</details>

---

## Question 5
**What does `re.findall()` return when there are groups in the pattern?**

A) All matches as strings
B) Only the first match
C) Only the grouped parts
D) A list of tuples containing groups

<details>
<summary>Click for answer</summary>

**D) A list of tuples containing groups**

If pattern has one group: returns list of strings
If pattern has multiple groups: returns list of tuples
</details>

---

## Question 6
**What is a non-capturing group?**

A) A group that doesn't capture anything
B) `(?:...)` - groups without creating a backreference
C) A group with no name
D) Both B and C

<details>
<summary>Click for answer</summary>

**B) `(?:...)` - groups without creating a backreference**

Use `(?:...)` when you need grouping but don't need to capture.
</details>

---

## Question 7
**What does `re.sub(r'\d+', 'X', 'Room 101')` return?**

A) "Room 101"
B) "Room X"
C) "X"
D) Error

<details>
<summary>Click for answer</summary>

**B) "Room X"**

Replaces one or more digits with "X".
</details>

---

## Question 8
**What does `$` match?**

A) Dollar sign
B) End of string
C) Empty string
D) Newline

<details>
<summary>Click for answer</summary>

**B) End of string**

`world$` matches "hello world" but not "world hello".
</details>

---

## Question 9
**What is the output of `re.split(r'\s+', 'a  b    c')`?**

A) `['a', 'b', 'c']`
B) `['a', '', 'b', '', '', '', 'c']`
C) `['a  b    c']`
D) `['a', '  ', 'b', '    ', 'c']`

<details>
<summary>Click for answer</summary>

**A) `['a', 'b', 'c']`**

`\s+` matches one or more whitespace characters as delimiter.
</details>

---

## Question 10
**What does `?` after a quantifier do?**

A) Makes it optional
B) Makes it non-greedy (lazy)
C) Matches exactly one
D) Nothing

<details>
<summary>Click for answer</summary>

**B) Makes it non-greedy (lazy)**

`.*?` matches as few characters as possible vs `.*` (greedy).
</details>

---

**How did you do?** Check `examples.py` for more practice!
