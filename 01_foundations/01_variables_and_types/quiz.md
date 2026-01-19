# 📝 Variables and Types - Quiz

Test your understanding! Try to answer without looking back.

---

## Question 1
What type is the variable `x` after this code runs?
```python
x = "42"
```

A) int  
B) float  
C) str  
D) bool

<details>
<summary>Click for answer</summary>

**C) str**

Even though it looks like a number, the quotes make it a string.

</details>

---

## Question 2
What will this code print?
```python
x = 10
y = 3
print(x / y)
```

A) 3  
B) 3.0  
C) 3.333...  
D) Error

<details>
<summary>Click for answer</summary>

**C) 3.333...**

Regular division (`/`) always returns a float. For integer division, use `//`.

</details>

---

## Question 3
Which variable name is INVALID?

A) `my_variable`  
B) `_count`  
C) `2nd_place`  
D) `firstName`

<details>
<summary>Click for answer</summary>

**C) 2nd_place**

Variable names cannot start with a number.

</details>

---

## Question 4
What will `int(3.9)` return?

A) 3  
B) 4  
C) 3.9  
D) Error

<details>
<summary>Click for answer</summary>

**A) 3**

`int()` truncates (cuts off) the decimal part. It does NOT round.

</details>

---

## Question 5
What is printed?
```python
a = "Hello"
b = a
a = "World"
print(b)
```

A) Hello  
B) World  
C) HelloWorld  
D) Error

<details>
<summary>Click for answer</summary>

**A) Hello**

When we assign `a = "World"`, we're changing what `a` points to. `b` still points to the original string "Hello".

</details>

---

## Question 6
What does this code print?
```python
x = None
if x:
    print("True")
else:
    print("False")
```

A) True  
B) False  
C) None  
D) Error

<details>
<summary>Click for answer</summary>

**B) False**

`None` is "falsy" in Python, so it evaluates to `False` in a boolean context.

</details>

---

## Question 7
What is the result of `"Ha" * 3`?

A) "Ha3"  
B) "HaHaHa"  
C) Error  
D) 6

<details>
<summary>Click for answer</summary>

**B) "HaHaHa"**

Multiplying a string by an integer repeats the string.

</details>

---

## Question 8
What does `type(True)` return?

A) `<class 'int'>`  
B) `<class 'str'>`  
C) `<class 'bool'>`  
D) `<class 'true'>`

<details>
<summary>Click for answer</summary>

**C) `<class 'bool'>`**

`True` and `False` are boolean values.

</details>

---

## Bonus Question
What will this print?
```python
a, b = 1, 2
a, b = b, a + b
print(a, b)
```

A) 2, 3  
B) 1, 2  
C) 2, 1  
D) 3, 2

<details>
<summary>Click for answer</summary>

**A) 2, 3**

Python evaluates the right side first: `b` is 2, `a + b` is 3. Then assigns: `a = 2`, `b = 3`.

</details>

---

## How did you do?

- **8-9 correct:** Excellent! You've mastered this topic.
- **6-7 correct:** Good job! Review the ones you missed.
- **4-5 correct:** Keep practicing with the examples.
- **0-3 correct:** Re-read the README and run the examples again.
