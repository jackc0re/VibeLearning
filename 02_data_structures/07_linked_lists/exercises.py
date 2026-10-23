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
# EXERCISE 4: Doubly linked list - delete a known node in O(1)
# EXERCISE 5: Count nodes in a circular linked list (safely!)
# EXERCISE 6: Convert a singly linked list to a doubly linked one

# =============================================================================
# EXERCISES 4-6: STUBS AND SELF-TESTS
# =============================================================================
# The functions below are TODO stubs: running this file unattempted prints
# FAIL for each check but still exits 0. Worked solutions are at the bottom;
# paste one over its stub and re-run to see PASS.

print("\n--- Exercises 4-6: self-tests (stubs -> FAIL until solved) ---")

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

def dll_values(dll):
    values, current = [], dll.head
    while current:
        values.append(current.data)
        current = current.next
    return values

def check(name, condition):
    print(f"{'PASS' if condition else 'FAIL'}: {name}")

def run_new_tests():
    # --- Exercise 4: delete a node we already hold ---
    dll = DoublyLinkedList()
    for value in [1, 2, 3, 4]:
        dll.append(value)
    delete_node(dll, dll.head.next)       # remove the middle node (2)
    check("ex4: deletes a middle node", dll_values(dll) == [1, 3, 4])
    delete_node(dll, dll.head)            # remove the head
    check("ex4: deletes the head", dll_values(dll) == [3, 4])
    delete_node(dll, dll.tail)            # remove the tail
    check("ex4: deletes the tail", dll_values(dll) == [3])

    # --- Exercise 5: count nodes in a singly CIRCULAR list ---
    one = Node(7)
    one.next = one                        # a lonely one-node circle
    three = [Node(v) for v in [1, 2, 3]]
    for a, b in zip(three, three[1:] + three[:1]):
        a.next = b                        # ...and the last one points back
    check("ex5: counts a 1-node circle", count_circular(one) == 1)
    check("ex5: counts a 3-node circle", count_circular(three[0]) == 3)
    check("ex5: empty list counts 0", count_circular(None) == 0)

    # --- Exercise 6: convert singly to doubly ---
    sll = LinkedList()
    for value in [4, 5, 6]:
        sll.append(value)
    dhead = to_doubly(sll)
    ok = dhead is not None and dhead.prev is None
    if ok:
        forward, last = [], None
        current = dhead
        while current:
            forward.append(current.data)
            if current.next is not None and current.next.prev is not current:
                ok = False                # a broken prev link
            last = current
            current = current.next
        ok = ok and forward == [4, 5, 6]
        backward = []
        current = last
        while current:
            backward.append(current.data)
            current = current.prev
        ok = ok and backward == [6, 5, 4]
    check("ex6: converts with working prev links", ok)

# EXERCISE 4: unlink `node` in O(1) - no traversal from the head.
def delete_node(dll, node):
    # TODO: rewire node.prev.next and node.next.prev, and remember to
    # update dll.head when node.prev is None, dll.tail when node.next is None.
    return None  # replace with your implementation

# EXERCISE 5: the last node points back to `head`, so there is no None
# to stop at - stop when you ARRIVE BACK AT THE START.
def count_circular(head):
    # TODO: an empty list (head is None) has 0 nodes; otherwise walk until
    # the next step lands on head again.
    return None  # replace with your implementation

# EXERCISE 6: build an equivalent DoublyNode chain from a singly LinkedList
# and return its head; every node's prev must point at the one before it.
def to_doubly(sll):
    # TODO: walk sll.head..., build a DoublyNode per value, wire prev/next.
    return None  # replace with your implementation

run_new_tests()

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

# Solution 3: Remove duplicates
print()
print("--- Solution 3: Remove duplicates ---")
def to_list(ll):
    values = []
    current = ll.head
    while current:
        values.append(current.data)
        current = current.next
    return values

def remove_duplicates(ll):
    seen = set()
    previous = None
    current = ll.head
    while current:
        if current.data in seen:
            previous.next = current.next      # skip this node
        else:
            seen.add(current.data)
            previous = current
        current = current.next
    return ll

dup = LinkedList()
for value in [1, 2, 3, 2, 4, 1]:
    dup.append(value)
print(f"Before: {to_list(dup)}")
remove_duplicates(dup)
print(f"After:  {to_list(dup)}")

# Solution 4: Doubly delete known node
print("\n--- Solution 4: Doubly delete known node ---")
def delete_node(dll, node):
    if node.prev:
        node.prev.next = node.next
    else:
        dll.head = node.next     # node was the head
    if node.next:
        node.next.prev = node.prev
    else:
        dll.tail = node.prev     # node was the tail

dll = DoublyLinkedList()
for value in [1, 2, 3, 4]:
    dll.append(value)
print(f"Before delete: {dll_values(dll)}")
delete_node(dll, dll.head.next)      # remove 2 - no traversal needed
print(f"After delete:  {dll_values(dll)}")

# Solution 5: Count circular nodes safely
print("\n--- Solution 5: Count circular nodes safely ---")
def count_circular(head):
    if head is None:
        return 0
    count = 1
    current = head.next
    while current is not head:   # looped all the way around -> done
        count += 1
        current = current.next
    return count

nodes = [Node(v) for v in [1, 2, 3]]
for a, b in zip(nodes, nodes[1:] + nodes[:1]):
    a.next = b                   # ...and the last one points back to the first
print(f"Nodes in the 3-node circle: {count_circular(nodes[0])}")

# Solution 6: Convert singly to doubly
print("\n--- Solution 6: Singly to doubly ---")
def to_doubly(sll):
    dhead = dtail = None
    current = sll.head
    while current:
        new_node = DoublyNode(current.data)
        if dtail is None:
            dhead = dtail = new_node
        else:
            new_node.prev = dtail
            dtail.next = new_node
            dtail = new_node
        current = current.next
    return dhead

sll6 = LinkedList()
for value in [4, 5, 6]:
    sll6.append(value)
dhead = to_doubly(sll6)
forward, backward = [], []
current = dhead
while current:
    forward.append(current.data)
    current = current.next
current = dhead
while current.next:
    current = current.next       # walk to the tail
while current:
    backward.append(current.data)
    current = current.prev
print(f"Doubly forward:  {forward}")
print(f"Doubly backward: {backward}")

print("\n--- Re-running the self-tests with the solutions in place ---")
run_new_tests()

print("\n" + "=" * 50)
print("Great job! Move on to 08_trees next.")
print("=" * 50)
