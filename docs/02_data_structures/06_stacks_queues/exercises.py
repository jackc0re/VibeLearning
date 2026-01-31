"""
Stacks and Queues - Exercises
=============================
Solutions at the bottom.
"""

from collections import deque

print("=" * 50)
print("STACKS AND QUEUES - Exercises")
print("=" * 50)

# EXERCISE 1: Implement a Stack class with push, pop, peek, is_empty
print("\n--- Exercise 1: Stack Class ---\n")

# EXERCISE 2: Reverse a list using a stack
print("\n--- Exercise 2: Reverse List ---\n")
"""
def reverse_list(lst): ...
reverse_list([1, 2, 3, 4]) -> [4, 3, 2, 1]
"""

# EXERCISE 3: Implement a Queue class
print("\n--- Exercise 3: Queue Class ---\n")

# EXERCISE 4: Check if brackets are balanced
print("\n--- Exercise 4: Balanced Brackets ---\n")

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# Solution 1
print("\n--- Solution 1: Stack ---")
class Stack:
    def __init__(self):
        self._items = []
    def push(self, item):
        self._items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty stack")
        return self._items.pop()
    def peek(self):
        return self._items[-1] if self._items else None
    def is_empty(self):
        return len(self._items) == 0

s = Stack()
s.push(1); s.push(2); s.push(3)
print(f"Peek: {s.peek()}, Pop: {s.pop()}, Pop: {s.pop()}")

# Solution 2
print("\n--- Solution 2: Reverse ---")
def reverse_list(lst):
    stack = list(lst)
    return [stack.pop() for _ in range(len(stack))]
print(f"reverse_list([1,2,3,4]): {reverse_list([1,2,3,4])}")

# Solution 3
print("\n--- Solution 3: Queue ---")
class Queue:
    def __init__(self):
        self._items = deque()
    def enqueue(self, item):
        self._items.append(item)
    def dequeue(self):
        return self._items.popleft()
    def is_empty(self):
        return len(self._items) == 0

q = Queue()
q.enqueue("A"); q.enqueue("B")
print(f"Dequeue: {q.dequeue()}, Dequeue: {q.dequeue()}")

# Solution 4
print("\n--- Solution 4: Balanced ---")
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{': stack.append(c)
        elif c in ')]}':
            if not stack or stack.pop() != pairs[c]:
                return False
    return len(stack) == 0

print(f"'([])': {is_balanced('([])')}, '([)]': {is_balanced('([)]')}")

print("\n" + "=" * 50)
print("Great job! Move on to 07_linked_lists next.")
print("=" * 50)
