# 📝 Loops - Quiz

Test your loop knowledge!

---

## Question 1
What will `range(3)` produce?

A) 1, 2, 3  
B) 0, 1, 2  
C) 0, 1, 2, 3  
D) 1, 2

<details>
<summary>Click for answer</summary>

**B) 0, 1, 2**

`range(n)` produces numbers from 0 to n-1.

</details>

---

## Question 2
What does this print?
```python
for i in range(5, 2, -1):
    print(i, end=" ")
```

A) 5 4 3 2  
B) 5 4 3  
C) 2 3 4 5  
D) 3 4 5

<details>
<summary>Click for answer</summary>

**B) 5 4 3**

Starts at 5, stops before 2, steps by -1. So: 5, 4, 3.

</details>

---

## Question 3
What does `break` do?

A) Pauses the loop  
B) Exits the loop immediately  
C) Skips to the next iteration  
D) Restarts the loop

<details>
<summary>Click for answer</summary>

**B) Exits the loop immediately**

`break` completely stops the loop execution.

</details>

---

## Question 4
What will this print?
```python
for i in range(3):
    pass
else:
    print("done")
```

A) done  
B) Nothing  
C) Error  
D) 0 1 2 done

<details>
<summary>Click for answer</summary>

**A) done**

The `else` clause runs when the loop completes normally (no `break`).

</details>

---

## Question 5
What does `continue` do?

A) Exits the loop  
B) Restarts the loop from the beginning  
C) Skips to the next iteration  
D) Continues after the loop

<details>
<summary>Click for answer</summary>

**C) Skips to the next iteration**

`continue` jumps to the next loop iteration, skipping remaining code in the current iteration.

</details>

---

## Question 6
What will this print?
```python
i = 0
while i < 3:
    print(i)
```

A) 0 1 2  
B) 0 0 0...  (infinite)  
C) Nothing  
D) Error

<details>
<summary>Click for answer</summary>

**B) 0 0 0... (infinite)**

`i` is never incremented, so `i < 3` is always True. This is an infinite loop.

</details>

---

## Question 7
What is the output?
```python
nums = [1, 2, 3]
for i, n in enumerate(nums, start=1):
    print(i, end=" ")
```

A) 0 1 2  
B) 1 2 3  
C) 1 2 3 4  
D) 0 1 2 3

<details>
<summary>Click for answer</summary>

**B) 1 2 3**

`enumerate(nums, start=1)` produces indices starting at 1.

</details>

---

## Question 8
Which creates `[0, 1, 4, 9, 16]`?

A) `[i ** 2 for i in range(5)]`  
B) `[i ** 2 for i in range(1, 5)]`  
C) `[i ** 2 for i in (0, 1, 2, 3, 4, 5)]`  
D) `[i * 2 for i in range(5)]`

<details>
<summary>Click for answer</summary>

**A) `[i ** 2 for i in range(5)]`**

0², 1², 2², 3², 4² = 0, 1, 4, 9, 16

</details>

---

## Question 9
What happens when `break` is inside a nested loop?

A) Both loops exit  
B) Only the innermost loop exits  
C) Only the outermost loop exits  
D) Error

<details>
<summary>Click for answer</summary>

**B) Only the innermost loop exits**

`break` only affects the loop it's directly inside.

</details>

---

## Question 10
How many times does this loop run?
```python
for i in range(10, 10):
    print("Hello")
```

A) 10 times  
B) 1 time  
C) 0 times  
D) Infinite

<details>
<summary>Click for answer</summary>

**C) 0 times**

`range(10, 10)` is empty because start equals stop.

</details>

---

## How did you do?

- **9-10 correct:** Loop master! 🏆
- **7-8 correct:** Great looping skills!
- **5-6 correct:** Good, keep practicing.
- **0-4 correct:** Review the examples again.
