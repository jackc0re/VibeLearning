# 📝 Control Flow - Quiz

Test your decision-making skills!

---

## Question 1
What will this code print?
```python
x = 5
if x > 10:
    print("A")
elif x > 3:
    print("B")
elif x > 1:
    print("C")
else:
    print("D")
```

A) A  
B) B  
C) C  
D) B and C

<details>
<summary>Click for answer</summary>

**B) B**

Only the first matching condition (`x > 3`) executes. Even though `x > 1` is also true, `elif` stops after the first match.

</details>

---

## Question 2
What does `if not False:` evaluate to?

A) True  
B) False  
C) Error  
D) None

<details>
<summary>Click for answer</summary>

**A) True**

`not False` equals `True`, so the condition is met.

</details>

---

## Question 3
What will this print?
```python
value = ""
if value:
    print("truthy")
else:
    print("falsy")
```

A) truthy  
B) falsy  
C) ""  
D) Error

<details>
<summary>Click for answer</summary>

**B) falsy**

An empty string is a falsy value in Python.

</details>

---

## Question 4
What is the output?
```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
```

A) adult  
B) minor  
C) True  
D) Error

<details>
<summary>Click for answer</summary>

**A) adult**

This is a conditional expression (ternary). Since `20 >= 18` is True, "adult" is assigned.

</details>

---

## Question 5
What will this print?
```python
x = 0
if x:
    print("yes")
```

A) yes  
B) no  
C) 0  
D) Nothing (no output)

<details>
<summary>Click for answer</summary>

**D) Nothing (no output)**

`0` is falsy, so the condition is False and the block doesn't execute.

</details>

---

## Question 6
Which is a valid way to check if `x` is between 5 and 10 (inclusive)?

A) `if x >= 5 and <= 10:`  
B) `if 5 <= x <= 10:`  
C) `if x in range(5, 10):`  
D) `if 5 < x < 10:`

<details>
<summary>Click for answer</summary>

**B) `if 5 <= x <= 10:`**

A) is invalid syntax. C) excludes 10. D) excludes both 5 and 10.

</details>

---

## Question 7
What does this code print?
```python
a = True
b = False
if a and b:
    print("both")
elif a or b:
    print("at least one")
else:
    print("neither")
```

A) both  
B) at least one  
C) neither  
D) Error

<details>
<summary>Click for answer</summary>

**B) at least one**

`a and b` is False (both must be True). `a or b` is True (at least one is True).

</details>

---

## Question 8
What is printed?
```python
x = None
result = x or "default"
print(result)
```

A) None  
B) default  
C) True  
D) Error

<details>
<summary>Click for answer</summary>

**B) default**

`None` is falsy, so `or` returns the second value "default".

</details>

---

## Question 9
What happens here?
```python
if True:
print("hello")
```

A) Prints "hello"  
B) Prints nothing  
C) IndentationError  
D) SyntaxError

<details>
<summary>Click for answer</summary>

**C) IndentationError**

The code block under `if` must be indented.

</details>

---

## Question 10
What will this print?
```python
num = 15
if num % 3 == 0:
    print("Fizz", end="")
if num % 5 == 0:
    print("Buzz", end="")
print()
```

A) Fizz  
B) Buzz  
C) FizzBuzz  
D) 15

<details>
<summary>Click for answer</summary>

**C) FizzBuzz**

These are two separate `if` statements (not elif), so both conditions are checked independently.

</details>

---

## How did you do?

- **9-10 correct:** Control flow master! 🏆
- **7-8 correct:** Great work! Review the ones you missed.
- **5-6 correct:** Good progress, keep practicing.
- **0-4 correct:** Re-read the README and run examples.
