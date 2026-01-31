"""
Stacks and Queues - Examples
============================
Run this file to see stacks and queues in action!
"""

from collections import deque

print("=" * 50)
print("STACKS AND QUEUES - Examples")
print("=" * 50)

# =============================================================================
# STACK WITH LIST
# =============================================================================
print("\n--- Stack with List ---\n")

stack = []
print(f"Empty stack: {stack}")

# Push operations
print("\nPush 1, 2, 3:")
stack.append(1)
stack.append(2)
stack.append(3)
print(f"Stack: {stack}")

# Pop operations
print("\nPop operations:")
while stack:
    top = stack.pop()
    print(f"  Popped: {top}, Stack: {stack}")

# =============================================================================
# QUEUE WITH DEQUE
# =============================================================================
print("\n--- Queue with deque ---\n")

queue = deque()
print(f"Empty queue: {queue}")

# Enqueue operations
print("\nEnqueue A, B, C:")
queue.append("A")
queue.append("B")
queue.append("C")
print(f"Queue: {queue}")

# Dequeue operations
print("\nDequeue operations:")
while queue:
    front = queue.popleft()
    print(f"  Dequeued: {front}, Queue: {queue}")

# =============================================================================
# BALANCED PARENTHESES
# =============================================================================
print("\n--- Balanced Parentheses ---\n")

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

test_cases = ["()", "()[]{}", "([)]", "{[]}", "((()))", "((("]
for tc in test_cases:
    print(f"  '{tc}': {is_balanced(tc)}")

# =============================================================================
# REVERSE STRING WITH STACK
# =============================================================================
print("\n--- Reverse String with Stack ---\n")

def reverse_string(s):
    stack = list(s)
    result = ""
    while stack:
        result += stack.pop()
    return result

text = "Hello World"
print(f"Original: '{text}'")
print(f"Reversed: '{reverse_string(text)}'")

# =============================================================================
# BFS WITH QUEUE
# =============================================================================
print("\n--- Simple BFS Example ---\n")

# Simple tree as adjacency list
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

def bfs(start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(tree[node])
    return visited

print(f"BFS from 'A': {bfs('A')}")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
