"""
Graphs - Exercises
==================
"""

from collections import deque

print("=" * 50)
print("GRAPHS - Exercises")
print("=" * 50)

# EXERCISE 1: Find if path exists between two nodes
# EXERCISE 2: Count connected components

# SOLUTIONS
print("\n--- Solutions ---")

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

# Solution 1: Path exists
def path_exists(graph, start, end):
    if start == end:
        return True
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            queue.extend(graph.get(node, []))
    return False

print(f"Path A to D: {path_exists(graph, 'A', 'D')}")
print(f"Path A to X: {path_exists(graph, 'A', 'X')}")

print("\n" + "=" * 50)
print("Great job! Move on to 10_hash_tables next.")
print("=" * 50)
