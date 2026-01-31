"""
Linked Lists - Examples
=======================
"""

print("=" * 50)
print("LINKED LISTS - Examples")
print("=" * 50)

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

print("\n--- Building Linked List ---\n")
ll = LinkedList()
for i in [1, 2, 3, 4, 5]:
    ll.append(i)
print(f"List: {ll.display()}")
print(f"Length: {ll.length()}")

print("\n--- Prepend ---")
ll.prepend(0)
print(f"After prepend(0): {ll.display()}")

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

print("\n" + "=" * 50)
print("Examples complete!")
print("=" * 50)
