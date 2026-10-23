# 📝 Linked Lists - Quiz

---

## Question 1
What does each node contain?

A) Only data  
B) Data and reference to next  
C) References only  
D) Array of data

<details>
<summary>Click for answer</summary>

**B) Data and reference to next**

Each node has data and a pointer/reference to the next node.

</details>

---

## Question 2
Time to insert at beginning?

A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)

<details>
<summary>Click for answer</summary>

**A) O(1)**

Just update head pointer. No shifting required.

</details>

---

## Question 3
Time to access nth element?

A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)

<details>
<summary>Click for answer</summary>

**B) O(n)**

Must traverse from head. No random access like arrays.

</details>

---

## Question 4
How to detect a cycle?

A) Check if last node is null  
B) Count nodes  
C) Use two pointers (slow/fast)  
D) Cannot be detected

<details>
<summary>Click for answer</summary>

**C) Use two pointers (slow/fast)**

Floyd's cycle detection: if they meet, there's a cycle.

</details>

---

## Question 5
When use linked list over array?

A) Need random access  
B) Frequent start insertions  
C) Memory efficiency  
D) Simple iteration

<details>
<summary>Click for answer</summary>

**B) Frequent start insertions**

Inserting at start is O(1) vs O(n) for arrays.

</details>

---

## Question 6
What does each node store in a **doubly** linked list?

A) Data only  
B) Data and a next pointer  
C) Data, a next pointer, and a prev pointer  
D) Data and its index

<details>
<summary>Click for answer</summary>

**C) Data, a next pointer, and a prev pointer**

Two pointers per node - which is why backward traversal works, and why the
memory cost is higher than a singly linked list.

</details>

---

## Question 7
You already hold a reference to a node in a doubly linked list. How long does deleting it take?

A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)

<details>
<summary>Click for answer</summary>

**A) O(1)**

The node's own `prev` pointer tells you the previous node, so no traversal
from the head is needed. In a singly list this would be O(n).

</details>

---

## Question 8
When traversing a circular linked list, when do you stop?

A) When `current` becomes None  
B) When you arrive back at the starting node  
C) After exactly n steps  
D) You cannot traverse it safely

<details>
<summary>Click for answer</summary>

**B) When you arrive back at the starting node**

There is no None to stop at. Checking `while current is not head` (after
processing head) is the safe pattern - `while current:` loops forever.

</details>

---

## Question 9
Which application is the classic fit for a circular linked list?

A) Binary search  
B) Round-robin scheduling  
C) Random access by index  
D) Sorting a large array

<details>
<summary>Click for answer</summary>

**B) Round-robin scheduling**

Players or processes take turns in a cycle - exactly what a circular list
models, since following `next` forever just walks the loop again.

</details>

---

## How did you do?

- **9 correct:** Excellent!
- **6-8 correct:** Good, review the ones you missed.
- **0-5 correct:** Re-read the README, then try again.
