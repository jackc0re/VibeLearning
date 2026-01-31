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
