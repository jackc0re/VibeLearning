# 📝 Strings Deep Dive - Quiz

Test your understanding! Try to answer without looking back.

---

## Question 1
What will this code print?
```python
text = "Python"
print(text[1:4])
```

A) "Pyt"  
B) "yth"  
C) "ytho"  
D) "tho"

<details>
<summary>Click for answer</summary>

**B) "yth"**

Slicing `[1:4]` gets characters at indices 1, 2, and 3 (end is exclusive).

</details>

---

## Question 2
What happens when you try to do this?
```python
s = "hello"
s[0] = "H"
```

A) s becomes "Hello"  
B) s becomes "HHello"  
C) TypeError  
D) No change, fails silently

<details>
<summary>Click for answer</summary>

**C) TypeError**

Strings are immutable. You cannot change individual characters. You'd need to create a new string: `s = "H" + s[1:]`

</details>

---

## Question 3
What does `"  hello  ".strip()` return?

A) "hello  "  
B) "  hello"  
C) "hello"  
D) "  hello  "

<details>
<summary>Click for answer</summary>

**C) "hello"**

`strip()` removes whitespace from both ends. Use `lstrip()` for left only or `rstrip()` for right only.

</details>

---

## Question 4
What is the result of `"apple,banana,cherry".split(",")`?

A) "apple banana cherry"  
B) ["apple", "banana", "cherry"]  
C) ("apple", "banana", "cherry")  
D) 3

<details>
<summary>Click for answer</summary>

**B) ["apple", "banana", "cherry"]**

`split()` returns a list of strings, not a single string or tuple.

</details>

---

## Question 5
What will this print?
```python
print(f"{42:05d}")
```

A) "42"  
B) "00042"  
C) "42000"  
D) "42.00"

<details>
<summary>Click for answer</summary>

**B) "00042"**

`:05d` means format as a 5-digit number, padding with leading zeros if necessary.

</details>

---

## Question 6
Which method finds a substring's position but returns -1 if not found?

A) `index()`  
B) `find()`  
C) `search()`  
D) `locate()`

<details>
<summary>Click for answer</summary>

**B) `find()`**

`find()` returns -1 if not found, while `index()` raises a ValueError.

</details>

---

## Question 7
What does `"hello".isalpha()` return?

A) True  
B) False  
C) "hello"  
D) 5

<details>
<summary>Click for answer</summary>

**A) True**

`isalpha()` returns True if all characters are letters and there's at least one character.

</details>

---

## Question 8
What is the output?
```python
words = ["Hello", "World"]
print("-".join(words))
```

A) "Hello World"  
B) "Hello-World"  
C) "-Hello-World-"  
D) ["Hello", "-", "World"]

<details>
<summary>Click for answer</summary>

**B) "Hello-World"**

`join()` puts the separator between each element of the list.

</details>

---

## Question 9
What does `"Hello World".title()` return?

A) "hello world"  
B) "HELLO WORLD"  
C) "Hello World"  
D) "Hello world"

<details>
<summary>Click for answer</summary>

**C) "Hello World"**

`title()` capitalizes the first letter of each word. Note: `capitalize()` only capitalizes the first letter of the string.

</details>

---

## Question 10
How do you create a raw string that preserves backslashes?

A) `"C:\path\file"`  
B) `r"C:\path\file"`  
C) `raw("C:\path\file")`  
D) `"C:\\path\\file"` only

<details>
<summary>Click for answer</summary>

**B) `r"C:\path\file"`**

The `r` prefix creates a raw string where backslashes are treated literally. Option D also works but requires doubling every backslash.

</details>

---

## How did you do?

- **9-10 correct:** Excellent! You've mastered strings.
- **7-8 correct:** Good job! Review the ones you missed.
- **5-6 correct:** Keep practicing with the examples.
- **0-4 correct:** Re-read the README and run the examples again.
