# 🌳 Trees

A hierarchical data structure with nodes connected by edges, starting from a **root** node.

---

## Tree Terminology

```
       ┌───┐
       │ A │  ← Root
       └─┬─┘
    ┌────┴────┐
  ┌─┴─┐    ┌──┴──┐
  │ B │    │  C  │  ← Children of A
  └─┬─┘    └──┬──┘
 ┌──┴──┐   ┌──┴──┐
┌┴┐  ┌─┴┐ ┌┴─┐ ┌─┴┐
│D│  │ E│ │ F│ │ G│  ← Leaves
└─┘  └──┘ └──┘ └──┘
```

- **Root**: Top node (A)
- **Parent/Child**: A is parent of B, B is child of A
- **Leaf**: Node with no children (D, E, F, G)
- **Height**: Longest path from root to leaf
- **Depth**: Distance from root

---

## Binary Tree

Each node has at most **2 children** (left and right).

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

---

## Tree Traversals

```python
# Inorder (left, root, right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

# Preorder (root, left, right)
def preorder(node):
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)

# Postorder (left, right, root)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)
```

---

## Binary Search Tree (BST)

Left child < parent < right child

```
       5
      / \
     3   7
    / \ / \
   2  4 6  8
```

**Search, Insert, Delete**: O(log n) average, O(n) worst

---

## Common Operations

| Operation | Time (balanced) |
|-----------|-----------------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |
| Traversal | O(n) |

---

## Next Steps

Practice with [examples.py](examples.py)!
