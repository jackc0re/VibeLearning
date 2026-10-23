# 📚 Stacks and Queues

Two fundamental data structures with opposite access patterns: **Last-In-First-Out (LIFO)** and **First-In-First-Out (FIFO)**.

---

## Stack (LIFO)

Think of a **stack of plates**: you add to the top and remove from the top.

```
     ┌─────┐
     │  3  │  ← Top (push/pop here)
     ├─────┤
     │  2  │
     ├─────┤
     │  1  │  ← Bottom
     └─────┘
```

### Stack Operations
- **push** - Add to top: O(1)
- **pop** - Remove from top: O(1)
- **peek/top** - View top element: O(1)
- **isEmpty** - Check if empty: O(1)

---

## Stack with Python List

```python
stack = []

# Push (add to top)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

# Pop (remove from top)
top = stack.pop()
print(top)    # 3
print(stack)  # [1, 2]

# Peek (view top without removing)
if stack:
    top = stack[-1]
    print(top)  # 2
```

---

## Queue (FIFO)

Think of a **line at a store**: first person in line is first served.

```
     ┌─────┬─────┬─────┐
     │  1  │  2  │  3  │
     └─────┴─────┴─────┘
       ↑               ↑
     Front           Back
   (dequeue)       (enqueue)
```

### Queue Operations
- **enqueue** - Add to back: O(1)
- **dequeue** - Remove from front: O(1)
- **front** - View front element: O(1)
- **isEmpty** - Check if empty: O(1)

---

## Queue with collections.deque

```python
from collections import deque

queue = deque()

# Enqueue (add to back)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # deque([1, 2, 3])

# Dequeue (remove from front)
front = queue.popleft()
print(front)  # 1
print(queue)  # deque([2, 3])

# Peek front
if queue:
    front = queue[0]
```

> ⚠️ **Why not use list?** `list.pop(0)` is O(n) because all elements shift. `deque.popleft()` is O(1).

---

## Use Cases

### Stack Uses
- **Undo/Redo** - Each action pushed, undo pops
- **Browser history** - Back button pops pages
- **Function calls** - Call stack
- **Expression evaluation** - Matching parentheses
- **DFS** - Depth-first search

### Queue Uses
- **Print queue** - First document prints first
- **Task scheduling** - Process in order
- **BFS** - Breadth-first search
- **Message queues** - Handle requests in order
- **Buffering** - Streaming data

---

## Stack Class Implementation

> 💡 **First time seeing `class`?** A class is a blueprint for making objects. Read
> it like this:
>
> - `class Stack:` defines a new type; `Stack()` builds one instance of it.
> - `__init__(self)` is the setup code that runs automatically when an instance is built.
> - `self` means "this particular instance" - `self._items` is a box that belongs to this
>   stack, not to every stack.
> - A leading underscore (`_items`) is a convention: "internal, please use `push`/`pop`".
>   Nothing enforces it - it is a hint to other programmers.
>
> That is all you need to follow the code below. Full treatment in
> [Module 04](../../04_oop_concepts/01_classes_and_objects/README.md).

```python
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
```

---

## Queue Class Implementation

```python
from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item):
        self._items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()
    
    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self._items[0]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
```

---

## Common Patterns

### Balanced Parentheses
```python
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0

print(is_balanced("([])"))   # True
print(is_balanced("([)]"))   # False
```

### Reverse with Stack
```python
def reverse_string(s):
    stack = list(s)
    result = ""
    while stack:
        result += stack.pop()
    return result
```

---

## Common Mistakes

### 1. Popping an empty stack
```python
stack = []
top = stack.pop()   # ❌ IndexError: pop from empty list

# ✅ Guard first - the same applies to stack[-1]
if stack:
    top = stack.pop()
```

### 2. Using `list.pop(0)` as a queue
```python
queue = [1, 2, 3]
first = queue.pop(0)   # Works, but O(n): every remaining element shifts left

# ✅ deque.popleft() is O(1)
from collections import deque
queue = deque([1, 2, 3])
first = queue.popleft()
```

### 3. Mixing up stack and queue methods
```python
stack.append(4); stack.pop()       # ✅ Last in, first out
queue.append(4); queue.popleft()   # ✅ First in, first out
queue.append(4); queue.pop()       # ❌ That removes the newest - a stack, not a queue
```

---

## Quick Reference

```python
# Stack (using list)
stack = []
stack.append(x)    # Push
stack.pop()        # Pop
stack[-1]          # Peek

# Queue (using deque)
from collections import deque
queue = deque()
queue.append(x)    # Enqueue
queue.popleft()    # Dequeue
queue[0]           # Front
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
