"""
Linked Lists - Exercises
========================
"""

print("=" * 50)
print("LINKED LISTS - Exercises")
print("=" * 50)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

# EXERCISE 1: Find middle element
# EXERCISE 2: Detect cycle
# EXERCISE 3: Remove duplicates

# =============================================================================
# SOLUTIONS
# =============================================================================
print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# Solution 1: Middle element
print("\n--- Solution 1: Middle ---")
def find_middle(ll):
    slow = fast = ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None

ll = LinkedList()
for i in [1, 2, 3, 4, 5]:
    ll.append(i)
print(f"Middle of [1,2,3,4,5]: {find_middle(ll)}")

# Solution 2: Detect cycle
print("\n--- Solution 2: Cycle ---")
def has_cycle(ll):
    slow = fast = ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
print(f"Has cycle: {has_cycle(ll)}")

print("\n" + "=" * 50)
print("Great job! Move on to 08_trees next.")
print("=" * 50)
