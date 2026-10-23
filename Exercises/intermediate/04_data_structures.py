"""
Intermediate Exercise 4: Data Structures
========================================
Build a stack, a queue, a linked list, a binary search tree,
and a hash table from scratch.
"""

print("=" * 50)
print("EXERCISE 4: Data Structures")
print("=" * 50)


# =============================================================================
# EXERCISE 4.1: Stack
# =============================================================================
print("\n--- Exercise 4.1: Stack ---")
"""
Implement a Stack class (last-in, first-out) with push, pop,
peek, is_empty and __len__.

Then write is_balanced(text) that uses your stack to check whether
every (, [ and { is closed by the matching bracket, in the right order.
"""


# Your code below:
class Stack:
    """A last-in, first-out stack."""

    pass


def is_balanced(text):
    """Return True if all brackets in text are balanced."""
    pass


# Test (uncomment after implementing)
# print(is_balanced("{[()]}"))   # True
# print(is_balanced("{[(])}"))   # False
# print(is_balanced("((("))      # False


# =============================================================================
# EXERCISE 4.2: Queue
# =============================================================================
print("\n--- Exercise 4.2: Queue ---")
"""
Implement a Queue class (first-in, first-out) backed by
collections.deque, with enqueue, dequeue, is_empty and __len__.

Simulate three print jobs being served in arrival order.
"""

from collections import deque


# Your code below:
class Queue:
    """A first-in, first-out queue backed by a deque."""

    pass


# Test (uncomment after implementing)
# jobs = Queue()
# jobs.enqueue("print_report.pdf")
# jobs.enqueue("photo.png")
# while not jobs.is_empty():
#     print(f"printing {jobs.dequeue()}")


# =============================================================================
# EXERCISE 4.3: Linked List
# =============================================================================
print("\n--- Exercise 4.3: Linked List ---")
"""
Implement a singly linked list:
- Node: has value and next
- LinkedList: append(value), to_list() and reverse()

reverse() should flip the list in place by re-wiring the next
pointers (no new nodes, no to_list/append trickery).
"""


# Your code below:
class Node:
    """One link in a singly linked list."""

    pass


class LinkedList:
    """A singly linked list with append, to_list and reverse."""

    pass


# Test (uncomment after implementing)
# chain = LinkedList()
# for value in [1, 2, 3, 4]:
#     chain.append(value)
# chain.reverse()
# print(chain.to_list())  # [4, 3, 2, 1]


# =============================================================================
# EXERCISE 4.4: Binary Search Tree
# =============================================================================
print("\n--- Exercise 4.4: Binary Search Tree ---")
"""
Implement a binary search tree:
- TreeNode: value, left, right
- BinarySearchTree: insert(value), contains(value), in_order()

in_order() visits left subtree, node, right subtree - which yields
the values in sorted order.
"""


# Your code below:
class TreeNode:
    """One node in a binary search tree."""

    pass


class BinarySearchTree:
    """A binary search tree: left < node < right."""

    pass


# Test (uncomment after implementing)
# tree = BinarySearchTree()
# for value in [50, 30, 70, 20, 40, 60, 80]:
#     tree.insert(value)
# print(tree.in_order())       # sorted
# print(tree.contains(60))     # True
# print(tree.contains(65))     # False


# =============================================================================
# EXERCISE 4.5: Hash Table
# =============================================================================
print("\n--- Exercise 4.5: Hash Table ---")
"""
Build a tiny hash map from scratch (no dict storage!):

- HashTable(size): fixed number of buckets
- set(key, value): hash the key with hash(key) % size, handle
  collisions with a list per bucket ("separate chaining"),
  update the value if the key already exists
- get(key, default=None), delete(key) -> bool, __len__, __contains__
"""


# Your code below:
class HashTable:
    """A tiny hash map built from scratch (separate chaining)."""

    pass


# Test (uncomment after implementing)
# table = HashTable()
# table.set("python", 1991)
# table.set("rust", 2010)
# table.set("python", 2026)  # overwrite
# print(table.get("python"), table.get("rust"), table.get("go", "missing"))


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 4.1
print("\n--- Solution 4.1 ---")


class Stack:
    """A last-in, first-out stack."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


BRACKET_PAIRS = {")": "(", "]": "[", "}": "{"}


def is_balanced(text):
    """Return True if all brackets in text are balanced."""
    stack = Stack()
    for char in text:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != BRACKET_PAIRS[char]:
                return False
    return stack.is_empty()


for sample in ["{[()]}", "{[(])}", "(((", "no brackets at all"]:
    print(f"is_balanced({sample!r}) = {is_balanced(sample)}")

# SOLUTION 4.2
print("\n--- Solution 4.2 ---")


class Queue:
    """A first-in, first-out queue backed by a deque."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.popleft()

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


jobs = Queue()
for name in ["print_report.pdf", "photo.png", "invoice.docx"]:
    jobs.enqueue(name)
print(f"Jobs waiting: {len(jobs)}")
while not jobs.is_empty():
    print(f"  printing {jobs.dequeue()}")

# SOLUTION 4.3
print("\n--- Solution 4.3 ---")


class Node:
    """One link in a singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A singly linked list with append, to_list and reverse."""

    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def to_list(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    def reverse(self):
        """Reverse the list in place by re-wiring next pointers."""
        previous = None
        current = self.head
        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        self.head = previous


chain = LinkedList()
for value in [1, 2, 3, 4]:
    chain.append(value)
print(f"Linked list: {chain.to_list()}")
chain.reverse()
print(f"Reversed   : {chain.to_list()}")

# SOLUTION 4.4
print("\n--- Solution 4.4 ---")


class TreeNode:
    """One node in a binary search tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """A binary search tree: left < node < right."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def contains(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def in_order(self):
        values = []

        def visit(node):
            if node is None:
                return
            visit(node.left)
            values.append(node.value)
            visit(node.right)

        visit(self.root)
        return values


tree = BinarySearchTree()
for value in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(value)
print(f"In-order (sorted): {tree.in_order()}")
print(f"Contains 60: {tree.contains(60)}")
print(f"Contains 65: {tree.contains(65)}")

# SOLUTION 4.5
print("\n--- Solution 4.5 ---")


class HashTable:
    """A tiny hash map built from scratch (separate chaining)."""

    def __init__(self, size=8):
        self.size = size
        self._buckets = [[] for _ in range(size)]
        self._count = 0

    def _index(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        bucket = self._buckets[self._index(key)]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._count += 1

    def get(self, key, default=None):
        bucket = self._buckets[self._index(key)]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return default

    def delete(self, key):
        bucket = self._buckets[self._index(key)]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(i)
                self._count -= 1
                return True
        return False

    def __len__(self):
        return self._count

    def __contains__(self, key):
        sentinel = object()
        return self.get(key, sentinel) is not sentinel


table = HashTable()
table.set("python", 1991)
table.set("java", 1995)
table.set("rust", 2010)
table.set("python", 2026)  # overwrite, same bucket logic
print(f"python -> {table.get('python')} (updated)")
print(f"java   -> {table.get('java')}")
print(f"go     -> {table.get('go', 'missing')}")
print(f"Items stored: {len(table)}")
first_delete = table.delete("java")
second_delete = table.delete("java")
print(f"Delete 'java': {first_delete}, delete again: {second_delete}")

print("\n" + "=" * 50)
print("Great job! Move on to 05_error_handling.py")
print("=" * 50)
