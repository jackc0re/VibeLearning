"""
Trees - Examples
================
"""

print("=" * 50)
print("TREES - Examples")
print("=" * 50)

# =============================================================================
# TREE NODE AND SAMPLE TREE
# =============================================================================

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build a tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# =============================================================================
# TRAVERSALS
# =============================================================================
print("\n--- Tree Traversals ---")

def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)
    return result

def preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.val)
        preorder(node.left, result)
        preorder(node.right, result)
    return result

def postorder(node, result=None):
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.val)
    return result

print(f"Inorder:   {inorder(root)}")
print(f"Preorder:  {preorder(root)}")
print(f"Postorder: {postorder(root)}")

# =============================================================================
# TREE HEIGHT
# =============================================================================
print("\n--- Tree Height ---")
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

print(f"Height: {height(root)}")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
