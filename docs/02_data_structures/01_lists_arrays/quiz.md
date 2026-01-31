# 📝 Lists and Arrays - Quiz

Test your understanding! Try to answer without looking back.

---

## Question 1
What will this code print?
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[-2])
```

A) "apple"  
B) "banana"  
C) "cherry"  
D) IndexError

<details>
<summary>Click for answer</summary>

**B) "banana"**

Negative indexing counts from the end. `-1` is the last item ("cherry"), so `-2` is the second to last ("banana").

</details>

---

## Question 2
What is the result of this slice?
```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])
```

A) [0, 1, 2, 3]  
B) [1, 2, 3, 4]  
C) [1, 2, 3]  
D) [1, 2, 3, 4, 5]

<details>
<summary>Click for answer</summary>

**C) [1, 2, 3]**

Slicing is `[start:end]` where end is **exclusive**. So `[1:4]` gets indices 1, 2, and 3.

</details>

---

## Question 3
What's the difference between `append()` and `extend()`?
```python
a = [1, 2]
a.append([3, 4])

b = [1, 2]
b.extend([3, 4])
```

A) Both result in [1, 2, 3, 4]  
B) a = [1, 2, [3, 4]], b = [1, 2, 3, 4]  
C) a = [1, 2, 3, 4], b = [1, 2, [3, 4]]  
D) Error in one or both

<details>
<summary>Click for answer</summary>

**B) a = [1, 2, [3, 4]], b = [1, 2, 3, 4]**

`append()` adds the entire object as a single element. `extend()` adds each item from the iterable individually.

</details>

---

## Question 4
What does `pop()` return when called on an empty list?

A) None  
B) 0  
C) An empty list  
D) IndexError

<details>
<summary>Click for answer</summary>

**D) IndexError**

Calling `pop()` on an empty list raises `IndexError: pop from empty list`.

</details>

---

## Question 5
What will this list comprehension produce?
```python
result = [x * 2 for x in range(4)]
```

A) [0, 2, 4, 6]  
B) [2, 4, 6, 8]  
C) [0, 1, 2, 3]  
D) [1, 2, 3, 4]

<details>
<summary>Click for answer</summary>

**A) [0, 2, 4, 6]**

`range(4)` produces 0, 1, 2, 3. Each is multiplied by 2.

</details>

---

## Question 6
After this code, what is `a`?
```python
a = [1, 2, 3]
b = a
b.append(4)
```

A) [1, 2, 3]  
B) [1, 2, 3, 4]  
C) [4, 1, 2, 3]  
D) Error

<details>
<summary>Click for answer</summary>

**B) [1, 2, 3, 4]**

`b = a` doesn't create a copy — it creates another reference to the same list. Modifying through `b` also affects `a`.

</details>

---

## Question 7
What will `sorted([3, 1, 2])` return?

A) None  
B) [3, 1, 2]  
C) [1, 2, 3]  
D) [3, 2, 1]

<details>
<summary>Click for answer</summary>

**C) [1, 2, 3]**

`sorted()` returns a **new** sorted list. This is different from `.sort()` which sorts in place and returns None.

</details>

---

## Question 8
How do you access element 5 in this matrix?
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

A) matrix[1][1]  
B) matrix[2][2]  
C) matrix[4]  
D) matrix[1, 1]

<details>
<summary>Click for answer</summary>

**A) matrix[1][1]**

5 is in row index 1 (second row), column index 1 (second column). Python uses `[row][col]`, not `[row, col]`.

</details>

---

## Question 9
What's the output?
```python
letters = ['a', 'b', 'c']
letters.insert(1, 'x')
print(letters)
```

A) ['x', 'a', 'b', 'c']  
B) ['a', 'x', 'b', 'c']  
C) ['a', 'b', 'x', 'c']  
D) ['a', 'b', 'c', 'x']

<details>
<summary>Click for answer</summary>

**B) ['a', 'x', 'b', 'c']**

`insert(1, 'x')` inserts 'x' at index 1, shifting other elements right.

</details>

---

## Question 10
What does `[1, 2, 3][::-1]` produce?

A) [1, 2, 3]  
B) [3, 2, 1]  
C) [3]  
D) Error

<details>
<summary>Click for answer</summary>

**B) [3, 2, 1]**

The slice `[::-1]` creates a reversed copy of the list. The `-1` step means go backwards.

</details>

---

## How did you do?

- **9-10 correct:** Excellent! You've mastered lists.
- **7-8 correct:** Good job! Review the ones you missed.
- **5-6 correct:** Keep practicing with the examples.
- **0-4 correct:** Re-read the README and run the examples again.
