# 🔗 Linked Lists

A linear data structure where elements are stored in **nodes** connected by pointers/references.

---

## What is a Linked List?

Unlike arrays, linked list elements aren't stored contiguously. Each **node** contains data and a reference to the next node.

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ data: 1      │    │ data: 2      │    │ data: 3      │
│ next: ────────────│ next: ────────────│ next: None   │
└──────────────┘    └──────────────┘    └──────────────┘
      head                                    tail
```

---

## Node Class

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
| Insert at end | O(1)* | O(n)** |
| Delete at start | O(n) | O(1) |
| Search | O(n) | O(n) |

*If space available **Without tail pointer

---

## Common Operations

```python
# Traverse
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

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!
