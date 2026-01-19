# 📝 Input and Output - Quiz

Test your I/O knowledge!

---

## Question 1
What's the difference between `print(a, b)` and `print(a + b)` when a="Hello" and b="World"?

A) No difference  
B) First prints "Hello World", second prints "HelloWorld"  
C) First prints "HelloWorld", second prints "Hello World"  
D) Second causes an error

<details>
<summary>Click for answer</summary>

**B) First prints "Hello World", second prints "HelloWorld"**

`print(a, b)` adds a space between arguments. `print(a + b)` concatenates directly.

</details>

---

## Question 2
What does `input()` always return?

A) An integer  
B) The type of what user entered  
C) A string  
D) None

<details>
<summary>Click for answer</summary>

**C) A string**

`input()` always returns a string, even if the user types a number.

</details>

---

## Question 3
What does `f"{3.14159:.2f}"` produce?

A) 3.14159  
B) 3.14  
C) 3.1  
D) "3.14f"

<details>
<summary>Click for answer</summary>

**B) 3.14**

`.2f` formats the number as a float with 2 decimal places.

</details>

---

## Question 4
What does `print("Hello", end="")` do differently?

A) Prints nothing  
B) Doesn't print a newline at the end  
C) Prints "end" after "Hello"  
D) Causes an error

<details>
<summary>Click for answer</summary>

**B) Doesn't print a newline at the end**

`end=""` replaces the default newline with nothing.

</details>

---

## Question 5
What does `f"{5:03}"` produce?

A) 53  
B) 005  
C) 500  
D) 5

<details>
<summary>Click for answer</summary>

**B) 005**

`:03` zero-pads the number to 3 digits.

</details>

---

## Question 6
What does `\n` represent in a string?

A) The letter n  
B) Nothing  
C) A newline  
D) A tab

<details>
<summary>Click for answer</summary>

**C) A newline**

`\n` is an escape sequence for newline (line break).

</details>

---

## Question 7
How do you get multiple values from one input line?
```python
# User types: "10 20"
```

A) `x, y = input()`  
B) `x, y = input().split()`  
C) `x y = input()`  
D) `[x, y] = input()`

<details>
<summary>Click for answer</summary>

**B) `x, y = input().split()`**

`split()` breaks the string at spaces, and we unpack into x and y.

</details>

---

## Question 8
What does `f"{text:>10}"` do?

A) Left aligns in 10 characters  
B) Right aligns in 10 characters  
C) Centers in 10 characters  
D) Repeats text 10 times

<details>
<summary>Click for answer</summary>

**B) Right aligns in 10 characters**

`>` means right align, `<` is left, `^` is center.

</details>

---

## Question 9
What does `r"C:\new"` print?

A) C:\new  
B) C:  
ew  
C) C:\new (literally)  
D) Error

<details>
<summary>Click for answer</summary>

**A) C:\new**

The `r` prefix makes it a raw string, so `\n` is not interpreted as newline.

</details>

---

## Question 10
What's the output of `print(1, 2, 3, sep="-")`?

A) 1 2 3  
B) 1-2-3  
C) 1-2-3-  
D) -1-2-3

<details>
<summary>Click for answer</summary>

**B) 1-2-3**

`sep="-"` changes the separator between printed values from space to hyphen.

</details>

---

## How did you do?

- **9-10 correct:** I/O expert! 🏆
- **7-8 correct:** Great output skills!
- **5-6 correct:** Keep practicing.
- **0-4 correct:** Review the README and examples.

---

## 🎉 Module 01 Complete!

You've mastered the foundations! Move on to **02_data_structures**.
