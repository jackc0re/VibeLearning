# 🔗 Linked Lists

A linear data structure where elements are stored in **nodes** connected by pointers/references.

---

## What is a Linked List?

Unlike arrays, linked list elements aren't stored contiguously. Each **node** contains data and a reference to the next node.

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ data: 1      │    │ data: 2      │    │ data: 3      │
│ next: ───────┼───▶│ next: ───────┼───▶│ next: None   │
└──────────────┘    └──────────────┘    └──────────────┘
      head                                    tail
```

---

## Node Class

> 💡 **First time seeing `class`?** Start with the [10-line primer in Stacks and Queues](../06_stacks_queues/README.md#stack-class-implementation) - a class is a blueprint, `__init__` sets it up, `self` is the instance. Full treatment in [Module 04](../../04_oop_concepts/01_classes_and_objects/README.md).

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

## Singly Linked List

```python
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
```

---

## Linked List vs Array

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Access by index | O(1) | O(n) |
| Insert at start | O(n) | O(1) |
| Insert at end | O(1)† | O(n)‡ |
| Delete at start | O(n) | O(1) |
| Search | O(n) | O(n) |

† Amortized: O(1) on average, but occasionally the list has to grow.

‡ Without a tail pointer. With a tail pointer, adding at the end is also O(1).

---

## Common Operations

```python
# Traverse (inside the class)
def traverse(self):
    current = self.head
    while current:
        print(current.data)
        current = current.next

# Find length
def length(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count

# Reverse
def reverse(self):
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
```

---

## When to Use

**Use Linked Lists when:**
- Frequent insertions/deletions at beginning
- Unknown size (dynamic)
- No random access needed

**Use Arrays when:**
- Random access needed
- Memory efficiency matters
- Cache performance important

---

## Common Mistakes

### 1. Rebinding a local name instead of rewiring the link
```python
# Delete the node holding 2 from: 1 -> 2 -> 3
current = ll.head                  # node 1
while current and current.next and current.next.data != 2:
    current = current.next         # lands on the node BEFORE the one to delete
current = current.next             # ❌ rebinds the local name only - 1 still points at 2

# ✅ Rewire the previous node's next pointer
current = ll.head
while current and current.next:
    if current.next.data == 2:
        current.next = current.next.next   # 1 -> 3, node 2 is skipped
        break
    current = current.next
```
`del node` does not unlink anything either - only the `next` pointer decides who is in the list.

### 2. Walking past the end
```python
current = ll.head
while current.next:          # ❌ AttributeError if the list is empty (head is None)
    current = current.next

# ✅ Check the node itself before following it
current = ll.head
while current:
    current = current.next
```

### 3. Forgetting that the head can be the node to delete
```python
# Delete the first node
ll.head = ll.head.next       # ✅ the list now starts one node later

# ❌ `while current.next` skips the check for head itself,
#    so a match on the first node is never found
```

---

## Quick Reference

```python
# Build
node = Node(1)          # data, next=None
ll = LinkedList()
ll.prepend(0)           # O(1) - new head
ll.append(5)            # O(n) - walk to the end, then link

# Walk the chain
current = ll.head
while current:
    print(current.data)
    current = current.next

# Delete by value: rewire the previous node
#   current.next = current.next.next

# Peek
ll.head.data            # first value      O(1)
ll.head.next            # second node      (None if it was the only one)
ll.length()             # count the nodes  O(n)
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
