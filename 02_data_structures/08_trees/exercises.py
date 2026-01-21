"""
Trees - Exercises
=================
"""

print("=" * 50)
print("TREES - Exercises")
print("=" * 50)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# EXERCISE 1: Count nodes
# EXERCISE 2: Find max value
# EXERCISE 3: Check if BST

# SOLUTIONS
print("\n--- Solutions ---")

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

# Solution 1
def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
print(f"Node count: {count_nodes(root)}")

# Solution 2
def max_value(node):
    if not node:
        return float('-inf')
    return max(node.val, max_value(node.left), max_value(node.right))
print(f"Max value: {max_value(root)}")

print("\n" + "=" * 50)
print("Great job! Move on to 09_graphs next.")
print("=" * 50)
