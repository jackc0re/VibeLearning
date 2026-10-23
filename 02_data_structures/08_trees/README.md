# 🌳 Trees

A hierarchical data structure with nodes connected by edges, starting from a **root** node.

---

## Tree Terminology

```
         ┌───┐
         │ A │  ← Root
         └─┬─┘
     ┌─────┴─────┐
     │           │
   ┌───┐       ┌───┐
   │ B │       │ C │  ← Children of A
   └─┬─┘       └─┬─┘
  ┌──┴──┐     ┌──┴──┐
  │     │     │     │
┌───┐ ┌───┐ ┌───┐ ┌───┐
│ D │ │ E │ │ F │ │ G │  ← Leaves
└───┘ └───┘ └───┘ └───┘
```

- **Root**: Top node (A)
- **Parent/Child**: A is parent of B, B is child of A
- **Leaf**: Node with no children (D, E, F, G)
- **Height**: Number of levels from the root down to the deepest leaf (a single node has height 1)
- **Depth**: Distance from root

---

## Binary Tree

> 💡 **First time seeing `class`?** Start with the [10-line primer in Stacks and Queues](../06_stacks_queues/README.md#stack-class-implementation) - a class is a blueprint, `__init__` sets it up, `self` is the instance. Full treatment in [Module 04](../../04_oop_concepts/01_classes_and_objects/README.md).

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

> 💡 **This function calls itself?!** The traversals below are *recursive* - `inorder` calls `inorder`. Read it like this:
>
> - A recursive function needs a **base case**: the input where it returns without calling
>   itself. Here it is `if node:` - an empty branch (`None`, the bottom of the tree) does
>   nothing, and that is what stops the chain.
> - Otherwise it does a little work (`print(node.val)`) and hands a *smaller* problem - the
>   left subtree, then the right subtree - to another run of itself.
> - The trick to reading recursion: assume the smaller call already works, and check only
>   what this step adds.
>
> Full treatment in [03_algorithms/03_recursion](../../03_algorithms/03_recursion/README.md).

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

Both operations below walk a single path from the root downwards, so each comparison throws
away half of the remaining tree:

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(node, val):
    """Add val to the tree, return the root of the tree."""
    if node is None:                    # found the empty spot - base case
        return TreeNode(val)
    if val < node.val:
        node.left = insert(node.left, val)
    elif val > node.val:
        node.right = insert(node.right, val)
    return node                         # val == node.val: already there


def search(node, val):
    """Return the node holding val, or None if the value is not in the tree."""
    while node is not None:
        if val == node.val:
            return node
        node = node.left if val < node.val else node.right
    return None
```

**Trace.** Starting from the 7-node tree above, insert `1`:

1. `1 < 5`, so go left to `3`.
2. `1 < 3`, so go left to `2`.
3. `1 < 2`, so go left - that spot is empty, so `1` becomes the left child of `2`.

Now search `9`: `9 > 5` goes right to `7`, `9 > 7` goes right to `8`, `9 > 8` goes right,
which is empty, so `search` returns `None` - the value is not in the tree.

**Delete** is the awkward one, so it is left as a challenge: a leaf just disappears, a node
with one child is replaced by that child, and a node with two children is usually replaced
by its in-order successor (the smallest value in its right subtree).

---

## Common Operations

| Operation | Time (balanced) |
|-----------|-----------------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |
| Traversal | O(n) |

---

## Common Mistakes

### 1. Two different definitions of "height"
```python
# Count edges on the longest path: empty tree = -1, single node = 0
def height_edges(node):
    if node is None:
        return -1
    return 1 + max(height_edges(node.left), height_edges(node.right))

# Count levels: empty tree = 0, single node = 1 (this README and examples.py)
def height_levels(node):
    if node is None:
        return 0
    return 1 + max(height_levels(node.left), height_levels(node.right))
```
Both are used in the wild, so always say which one you mean - they differ by exactly 1.

### 2. A missing base case
```python
def count(node):            # ❌ never stops: runs past the bottom of the tree
    return 1 + count(node.left) + count(node.right)

# ✅ Stop at the empty branch
def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)
```

### 3. Creating a node but not linking it
```python
root = TreeNode(5)
TreeNode(3)                 # ❌ built and thrown away - not attached to anything

# ✅ Assign it into a slot
root.left = TreeNode(3)
```

### 4. Thinking a BST only compares parent and child
```python
#        5
#       / \
#      3   7
#       \
#        6      ❌ 6 sits in the left subtree of 5, so the BST property is broken
```
The rule is about **whole subtrees**: every value in the left subtree is smaller than the
root, every value in the right subtree is larger.

---

## Quick Reference

```python
# Build a tree by hand
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

# Traverse (all recursive)
#   inorder    left, node, right   - sorted order for a BST
#   preorder   node, left, right
#   postorder  left, right, node

# Measure
height(root)        # levels: 0 for None, 1 for a single node
count(root)         # 1 + count(left) + count(right)

# BST
insert(root, 4)     # returns the root, O(log n) when balanced
search(root, 4)     # returns the node or None, O(log n) when balanced
```

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
