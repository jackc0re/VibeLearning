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

# Solution 3
print()
print("--- Solution 3: Check if BST ---")
def is_bst(node, low=float("-inf"), high=float("inf")):
    if node is None:
        return True
    if not low < node.val < high:
        return False
    return (is_bst(node.left, low, node.val)
            and is_bst(node.right, node.val, high))

print(f"Is BST: {is_bst(root)}")

# A broken tree: 6 sits in the left subtree of 5, so the BST rule fails
broken = TreeNode(5)
broken.left = TreeNode(3)
broken.right = TreeNode(7)
broken.left.right = TreeNode(6)
print(f"Broken tree is BST: {is_bst(broken)}")

# =============================================================================
# EXERCISES 4-7: STUBS - YOUR TURN
# =============================================================================
print("\n--- Exercises 4-7: stubs + self-tests (FAIL is expected at first) ---")

from collections import deque

# -----------------------------------------------------------------------------
# EXERCISE 4: Level-order traversal
# -----------------------------------------------------------------------------
# TODO: implement level_order(node).
#   Return a list of lists - one list of values per level, top to bottom,
#   left to right. An empty tree gives [].
#   Hint: keep a deque of nodes; the "for _ in range(len(queue))" trick
#   processes exactly one level per inner loop.
def level_order(node):
    # YOUR CODE HERE (replace the stub return)
    return []

# -----------------------------------------------------------------------------
# EXERCISE 5: BST delete - one case at a time
# -----------------------------------------------------------------------------
# TODO: implement bst_delete(node, val) so it removes val and returns the
#   (possibly new) root. Build it up in this order:
#   Case 1 - leaf: return None.
#   Case 2 - one child: return the child, splicing it into place.
#   Case 3 - two children: copy the inorder successor's value (the smallest
#     value in the right subtree) into the node, then delete that successor
#     from the right subtree (it has no left child, so Case 1 or 2 applies).
def bst_delete(node, val):
    # YOUR CODE HERE (replace the stub return)
    return node

# -----------------------------------------------------------------------------
# EXERCISE 6: Count leaves
# -----------------------------------------------------------------------------
# TODO: implement count_leaves(node) - how many nodes have no children.
#   An empty tree gives 0, a single node gives 1.
def count_leaves(node):
    # YOUR CODE HERE (replace the stub return)
    return 0

# -----------------------------------------------------------------------------
# EXERCISE 7: Tree height, iteratively
# -----------------------------------------------------------------------------
# TODO: implement height_iterative(node) WITHOUT recursion.
#   Count levels exactly like examples.py does: empty tree -> 0,
#   a single node -> 1.
#   Hint: peel one level off a queue per round - the number of rounds
#   is the height.
def height_iterative(node):
    # YOUR CODE HERE (replace the stub return)
    return 0

# -----------------------------------------------------------------------------
# SELF-TESTS (PASS/FAIL) - they run against whichever functions you pass in
# -----------------------------------------------------------------------------
def make_tree():
    """Build the exercise tree fresh:
          5
         / \\
        3   7
       / \\
      2   4
    """
    t = TreeNode(5)
    t.left = TreeNode(3)
    t.right = TreeNode(7)
    t.left.left = TreeNode(2)
    t.left.right = TreeNode(4)
    return t

def inorder_vals(node, out=None):
    """Collect values in sorted order - handy for checking BST deletes."""
    if out is None:
        out = []
    if node:
        inorder_vals(node.left, out)
        out.append(node.val)
        inorder_vals(node.right, out)
    return out

def run_self_tests(label, level_order_fn, bst_delete_fn, count_leaves_fn, height_fn):
    """Run every exercise 4-7 check; print PASS/FAIL; return the failure count."""
    failures = 0

    def check(name, got, expected):
        nonlocal failures
        ok = got == expected
        if not ok:
            failures += 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        if not ok:
            print(f"        got:      {got}")
            print(f"        expected: {expected}")

    print(f"\n{label} - Exercise 4: level_order")
    check("level_order(make_tree())",
          level_order_fn(make_tree()), [[5], [3, 7], [2, 4]])
    check("level_order(None)", level_order_fn(None), [])

    print(f"\n{label} - Exercise 5: bst_delete")
    t = make_tree()
    check("delete leaf 2", inorder_vals(bst_delete_fn(t, 2)), [3, 4, 5, 7])
    t = make_tree()
    bst_delete_fn(t, 2)             # leave 3 with a single child
    check("delete one-child 3", inorder_vals(bst_delete_fn(t, 3)), [4, 5, 7])
    t = make_tree()
    check("delete two-children root 5",
          inorder_vals(bst_delete_fn(t, 5)), [2, 3, 4, 7])
    t = make_tree()
    check("delete missing 99 leaves the tree unchanged",
          inorder_vals(bst_delete_fn(t, 99)), [2, 3, 4, 5, 7])

    print(f"\n{label} - Exercise 6: count_leaves")
    check("count_leaves(None)", count_leaves_fn(None), 0)
    check("count_leaves(single node)", count_leaves_fn(TreeNode(1)), 1)
    check("count_leaves(make_tree())", count_leaves_fn(make_tree()), 3)

    print(f"\n{label} - Exercise 7: height_iterative")
    check("height_iterative(None)", height_fn(None), 0)
    check("height_iterative(single node)", height_fn(TreeNode(1)), 1)
    check("height_iterative(make_tree())", height_fn(make_tree()), 3)

    return failures

stub_failures = run_self_tests("Your stubs",
                               level_order, bst_delete,
                               count_leaves, height_iterative)
print(f"\n{stub_failures} failing check(s) in the stubs - that is normal while"
      " the TODOs are unfilled. Worked solutions below.")

# =============================================================================
# SOLUTIONS 4-7
# =============================================================================
print("\n--- Solutions 4-7 ---")

def find_min(node):
    """Smallest value in a subtree: keep walking left."""
    while node.left:
        node = node.left
    return node

# Solution 4
def level_order_solution(node):
    if node is None:
        return []
    result = []
    queue = deque([node])
    while queue:
        level = []
        for _ in range(len(queue)):
            current = queue.popleft()
            level.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(level)
    return result

# Solution 5
def bst_delete_solution(node, val):
    if node is None:
        return None
    if val < node.val:
        node.left = bst_delete_solution(node.left, val)
    elif val > node.val:
        node.right = bst_delete_solution(node.right, val)
    else:
        # Cases 1 and 2 collapse into one move:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        # Case 3: replace with the inorder successor, then delete it.
        node.val = find_min(node.right).val
        node.right = bst_delete_solution(node.right, node.val)
    return node

# Solution 6
def count_leaves_solution(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves_solution(node.left) + count_leaves_solution(node.right)

# Solution 7
def height_iterative_solution(node):
    if node is None:
        return 0
    levels = 0
    queue = deque([node])
    while queue:
        levels += 1
        for _ in range(len(queue)):
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return levels

solution_failures = run_self_tests("Reference solutions",
                                   level_order_solution, bst_delete_solution,
                                   count_leaves_solution, height_iterative_solution)
print(f"\nReference solutions: {12 - solution_failures}/12 checks passed.")

print("\n" + "=" * 50)
print("Great job! Move on to 09_graphs next.")
print("=" * 50)
