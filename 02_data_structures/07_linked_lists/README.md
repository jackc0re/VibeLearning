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

## Doubly Linked List

A doubly linked list gives every node **two** pointers: `next` *and* `prev`. Think of a
train - each car is coupled to the car in front **and** the car behind, so you can walk
the train in either direction.

```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None          # keeping a tail makes append O(1)

    def append(self, data):       # O(1) - we always know the tail
        new_node = DoublyNode(data)
        if not self.tail:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):      # O(1) - new head
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete_node(self, node):  # O(1) - the headline advantage!
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next     # node was the head
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev     # node was the tail

    def traverse_forward(self):
        current, values = self.head, []
        while current:
            values.append(str(current.data))
            current = current.next
        return " <-> ".join(values)

    def traverse_backward(self):
        current, values = self.tail, []
        while current:
            values.append(str(current.data))
            current = current.prev
        return " <-> ".join(values)
```

The big win: **deleting a node you already hold is O(1)**. In a singly linked list you
must walk from the head to find the node *before* it first - O(n). Here the node carries
its own `prev` pointer, so no search is needed:

```python
dll = DoublyLinkedList()
for value in [1, 2, 3, 4]:
    dll.append(value)

node_2 = dll.head.next        # suppose someone handed you this node
dll.delete_node(node_2)       # no traversal - just rewire a few pointers
print(dll.traverse_forward())     # 1 <-> 3 <-> 4
print(dll.traverse_backward())    # 4 <-> 3 <-> 1
```

> 💡 **Memory honesty:** every node now carries *two* pointers instead of one. That is
> real overhead - roughly double the pointer memory per node. Pay it only when you
> actually need backward travel or O(1) delete-of-known-node (an LRU cache needs both).

---

## Circular Linked List

In a circular linked list the last node points back to the first, so the chain has **no
`None` at the end** - it is a loop. The usual convention: keep a `tail` reference, and
`tail.next` is the head.

```python
class CircularLinkedList:
    def __init__(self):
        self.tail = None              # tail.next is the head

    def append(self, data):           # O(1) - new node slots in right after tail
        new_node = Node(data)         # reuses the plain singly Node class!
        if not self.tail:
            new_node.next = new_node  # a lone node points at itself
        else:
            new_node.next = self.tail.next   # new node -> head
            self.tail.next = new_node        # old tail -> new node
        self.tail = new_node
```

### The safe traversal pattern

You cannot stop at `None` - there is none. Stop when you **arrive back where you
started**:

```python
def count_nodes(head):
    if head is None:
        return 0
    count = 1
    current = head.next
    while current is not head:    # looped all the way around -> done
        count += 1
        current = current.next
    return count
```

### The classic mistake

```python
current = head
while current:                    # runs FOREVER - current is never None
    print(current.data)
    current = current.next        # ...wraps back to head, keeps going
```

If you ever loop over a circular list, always test the "back at start" condition - or
guard the loop with a step counter while debugging.

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

## Which Variant Should I Pick?

| Variant | Shape | Typical use |
|---------|-------|-------------|
| Singly | one `next` pointer | Stack-ish behavior, simple forward-only chains |
| Doubly | `prev` + `next` | LRU caches, deques, text editors with a cursor |
| Circular (singly) | `tail.next` is head | Round-robin schedulers, turn-based games, circular buffers |

### Complexity by variant

| Operation | Singly | Doubly | Circular (singly) |
|-----------|--------|--------|-------------------|
| Insert at start | O(1) | O(1) | O(1) |
| Insert at end (with tail pointer) | O(1) | O(1) | O(1) |
| Delete a **known** node | O(n) - must find prev | **O(1)** | O(n) - must find prev |
| Delete the last node | O(n) | O(1) with tail | O(n) |
| Traverse backward | no | O(n) | no |
| Memory per node | 1 pointer | 2 pointers | 1 pointer |

Rule of thumb: stay **singly** until you need backward travel or O(1) known-node
deletion - then pay the extra pointer for **doubly**. Go **circular** when the data
genuinely repeats in a cycle: turns, time slices, buffers.

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
