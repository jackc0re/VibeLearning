"""
Linked Lists - Examples
=======================
"""

print("=" * 50)
print("LINKED LISTS - Examples")
print("=" * 50)

# =============================================================================
# NODE AND LINKED LIST CLASSES
# =============================================================================

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
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
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# =============================================================================
# BUILD A LIST
# =============================================================================
print("\n--- Building Linked List ---\n")
ll = LinkedList()
for i in [1, 2, 3, 4, 5]:
    ll.append(i)
print(f"List: {ll.display()}")
print(f"Length: {ll.length()}")

# =============================================================================
# PREPEND
# =============================================================================
print("\n--- Prepend ---")
ll.prepend(0)
print(f"After prepend(0): {ll.display()}")

# =============================================================================
# REVERSE
# =============================================================================
print("\n--- Reverse ---")
def reverse(ll):
    prev = None
    current = ll.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    ll.head = prev

reverse(ll)
print(f"Reversed: {ll.display()}")

# =============================================================================
# DOUBLY LINKED LIST
# =============================================================================
print("\n--- Doubly Linked List ---")

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None      # keeping a tail makes append O(1)

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.tail:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete_node(self, node):
        # O(1): the node already knows its neighbours - no traversal needed.
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next    # node was the head
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev    # node was the tail

    def forward(self):
        values, current = [], self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " <-> ".join(values)

    def backward(self):
        values, current = [], self.tail
        while current:
            values.append(str(current.data))
            current = current.prev
        return " <-> ".join(values)

dll = DoublyLinkedList()
for value in [1, 2, 3, 4]:
    dll.append(value)
print(f"Append 1..4:  forward  = {dll.forward()}")
print(f"              backward = {dll.backward()}")
dll.prepend(0)
print(f"Prepend 0:    forward  = {dll.forward()}")

# The headline advantage: delete a node we already hold - O(1), no search.
node_2 = dll.head.next.next          # the node holding 2
dll.delete_node(node_2)
print(f"Deleted node 2 by reference: {dll.forward()}")

# =============================================================================
# CIRCULAR LINKED LIST
# =============================================================================
print("\n--- Circular Linked List ---")

class CircularLinkedList:
    def __init__(self):
        self.tail = None      # tail.next is the head

    def append(self, data):
        new_node = Node(data)     # reuses the plain singly Node class
        if not self.tail:
            new_node.next = new_node  # a lone node points at itself
        else:
            new_node.next = self.tail.next   # new node -> head
            self.tail.next = new_node        # old tail -> new node
        self.tail = new_node

cll = CircularLinkedList()
for value in [10, 20, 30]:
    cll.append(value)

# SAFE traversal: stop when we arrive back at the head - never at None.
head = cll.tail.next
values = []
current = head
while True:
    values.append(str(current.data))
    current = current.next
    if current is head:
        break
print(f"Circular list: {' -> '.join(values)} -> (back to head)")

# Round-robin flavor: keep cycling through the players (bounded - safe).
turns = []
current = head
for _ in range(5):
    turns.append(str(current.data))
    current = current.next
print(f"5 round-robin turns: {' -> '.join(turns)}")
print("Note: a plain 'while current:' loop would never stop here -")
print("no node has next = None, so the walk wraps around forever.")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
