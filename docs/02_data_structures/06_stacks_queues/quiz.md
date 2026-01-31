# 📝 Stacks and Queues - Quiz

---

## Question 1
What is the order of a Stack?

A) FIFO  
B) LIFO  
C) Random  
D) Sorted

<details>
<summary>Click for answer</summary>

**B) LIFO**

Last-In-First-Out. The most recently added item is removed first.

</details>

---

## Question 2
What is the order of a Queue?

A) FIFO  
B) LIFO  
C) Random  
D) Sorted

<details>
<summary>Click for answer</summary>

**A) FIFO**

First-In-First-Out. Items are removed in the order they were added.

</details>

---

## Question 3
Why use `deque` instead of `list` for queues?

A) Deque has more features  
B) `list.pop(0)` is O(n), `deque.popleft()` is O(1)  
C) Lists can't be used as queues  
D) Deque uses less memory

<details>
<summary>Click for answer</summary>

**B) `list.pop(0)` is O(n), `deque.popleft()` is O(1)**

Removing from the front of a list shifts all elements. Deque is optimized for both ends.

</details>

---

## Question 4
What does `stack.pop()` return when the stack is `[1, 2, 3]`?

A) 1  
B) 2  
C) 3  
D) [1, 2]

<details>
<summary>Click for answer</summary>

**C) 3**

Pop removes and returns the top (last) element.

</details>

---

## Question 5
Stacks are useful for:

A) Print queues  
B) Undo functionality  
C) Task scheduling  
D) All of the above

<details>
<summary>Click for answer</summary>

**B) Undo functionality**

Undo uses LIFO: the last action is undone first. Print queues use FIFO.

</details>

---

## Question 6
What is "peek" in a stack?

A) Remove the top element  
B) View the top element without removing  
C) Add to the top  
D) Check if empty

<details>
<summary>Click for answer</summary>

**B) View the top element without removing**

Peek lets you see the top without modifying the stack.

</details>

---

## How did you do?

- **5-6 correct:** Excellent!
- **3-4 correct:** Good, review missed ones.
- **0-2 correct:** Re-read README.
