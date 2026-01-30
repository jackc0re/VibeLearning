"""
Graphs - Examples
=================
"""

from collections import deque

print("=" * 50)
print("GRAPHS - Examples")
print("=" * 50)

# Graph as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("\n--- Graph Representation ---")
print("Adjacency List:")
for node, neighbors in graph.items():
    print(f"  {node}: {neighbors}")

print("\n--- BFS ---")
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    return result

print(f"BFS from A: {bfs(graph, 'A')}")

print("\n--- DFS ---")
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

print(f"DFS from A: {dfs(graph, 'A')}")

print("\n" + "=" * 50)
print("Examples complete!")
print("=" * 50)
