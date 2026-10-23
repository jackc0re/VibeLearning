# 📝 Trees - Quiz

---

## Question 1
What is the root of a tree?

A) Any node  
B) Bottom node  
C) Top node with no parent  
D) Node with most children

<details>
<summary>Click for answer</summary>

**C) Top node with no parent**

</details>

---

## Question 2
Binary tree max children per node?

A) 1  
B) 2  
C) 3  
D) Unlimited

<details>
<summary>Click for answer</summary>

**B) 2**

Binary means at most 2 children (left, right).

</details>

---

## Question 3
Inorder traversal order?

A) Root, Left, Right  
B) Left, Root, Right  
C) Left, Right, Root  
D) Right, Root, Left

<details>
<summary>Click for answer</summary>

**B) Left, Root, Right**

Inorder visits left subtree, then node, then right.

</details>

---

## Question 4
BST search time (balanced)?

A) O(1)  
B) O(log n)  
C) O(n)  
D) O(n²)

<details>
<summary>Click for answer</summary>

**B) O(log n)**

Each comparison eliminates half the tree.

</details>

---

## Question 5
BST property?

A) Left > Root > Right  
B) Left < Root < Right  
C) All values equal  
D) Random order

<details>
<summary>Click for answer</summary>

**B) Left < Root < Right**

All left descendants are smaller, all right are larger.

</details>

---

## Question 6
Which data structure does level-order (BFS) traversal use?

A) Stack  
B) Queue  
C) Dictionary  
D) Tuple

<details>
<summary>Click for answer</summary>

**B) Queue**

First in, first out: children wait in line behind the nodes already queued, so the
levels come out in order.

</details>

---

## Question 7
Deleting a node with **two children** from a BST replaces its value with...

A) Its parent's value  
B) The largest value in the whole tree  
C) The smallest value in its right subtree  
D) Zero

<details>
<summary>Click for answer</summary>

**C) The smallest value in its right subtree**

That is the in-order successor - the smallest value still larger than the whole left
subtree, so it keeps the BST rule intact. You then delete that successor from the right
subtree.

</details>

---

## Question 8
You delete a node that has exactly **one child**. What happens to the child?

A) It is deleted too  
B) It moves up into the deleted node's place  
C) It becomes the new root  
D) It stays where it is, detached

<details>
<summary>Click for answer</summary>

**B) It moves up into the deleted node's place**

The child's whole subtree is spliced upward as one block, which keeps the sorted order.

</details>

---

## Question 9
Where do you find the in-order successor of a node in a BST?

A) Walk right from the root  
B) Keep walking left, starting from the node's right child  
C) Keep walking right, starting from the node's left child  
D) Search the entire tree

<details>
<summary>Click for answer</summary>

**B) Keep walking left, starting from the node's right child**

Smallest value in the right subtree: go right once, then left as far as possible. That
node has no left child, so removing it is always a Case 1 or Case 2 delete.

</details>

---

## How did you do?

- **8-9 correct:** Excellent!
- **5-7 correct:** Good, review the ones you missed.
- **0-4 correct:** Re-read the README, then try again.
