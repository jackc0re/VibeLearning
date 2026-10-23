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
# LEVEL-ORDER TRAVERSAL (BFS)
# =============================================================================
print("\n--- Level-Order Traversal (BFS) ---")

from collections import deque

def level_order(node):
    """Return a list of lists - one list of values per level, top to bottom."""
    if node is None:
        return []
    result = []
    queue = deque([node])                # the line starts with just the root
    while queue:
        level = []
        for _ in range(len(queue)):      # everyone in line RIGHT NOW = one level
            current = queue.popleft()
            level.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(level)
    return result

for depth, level in enumerate(level_order(root), start=1):
    print(f"Level {depth}: {level}")

print(f"Empty tree: {level_order(None)}")

# =============================================================================
# TREE HEIGHT
# =============================================================================
print("\n--- Tree Height ---")
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

print(f"Height: {height(root)}")

# =============================================================================
# BST DELETE - ALL THREE CASES
# =============================================================================
print("\n--- BST Delete: All Three Cases ---")

def bst_insert(node, val):
    """Add val to the BST, return the root (same insert as the README)."""
    if node is None:
        return TreeNode(val)
    if val < node.val:
        node.left = bst_insert(node.left, val)
    elif val > node.val:
        node.right = bst_insert(node.right, val)
    return node

def find_min(node):
    """Smallest value in a subtree: keep walking left."""
    while node.left:
        node = node.left
    return node

def bst_delete(node, val):
    """Remove val from the BST, return the root of the tree."""
    if node is None:
        return None
    if val < node.val:
        node.left = bst_delete(node.left, val)
    elif val > node.val:
        node.right = bst_delete(node.right, val)
    else:
        # Found the node to remove.
        if node.left is None:
            return node.right   # Case 1 (leaf) or Case 2 (right child only)
        if node.right is None:
            return node.left    # Case 2: left child only
        # Case 3: two children - copy the inorder successor's value here,
        # then delete the successor from the right subtree.
        successor = find_min(node.right)
        node.val = successor.val
        node.right = bst_delete(node.right, successor.val)
    return node

def build_bst(skip=None):
    """Build the tree below; skip one value to leave a one-child node.

           50
          /  \\
        30    70
       /  \\   /  \\
     20   40 60   80
    """
    tree = None
    for value in [50, 30, 70, 20, 40, 60, 80]:
        if value != skip:
            tree = bst_insert(tree, value)
    return tree

print(f"Fresh tree inorder:             {inorder(build_bst())}")

# Case 1: delete a leaf - just remove it
tree = build_bst()
tree = bst_delete(tree, 20)
print(f"Case 1 - delete 20 (leaf):      {inorder(tree)}")

# Case 2: delete a node with one child (30, whose only child is 40)
tree = build_bst(skip=20)
tree = bst_delete(tree, 30)
print(f"Case 2 - delete 30 (one child): {inorder(tree)}")

# Case 3: delete a node with two children (the root, 50)
tree = build_bst()
successor = find_min(tree.right)
tree = bst_delete(tree, 50)
print(f"Case 3 - delete 50 (two children): successor was {successor.val}")
print(f"                                   {inorder(tree)}")

print("\n" + "=" * 50)
print("Examples complete! Try exercises.py next.")
print("=" * 50)
