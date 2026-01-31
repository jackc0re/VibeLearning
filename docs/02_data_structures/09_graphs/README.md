# 🕸️ Graphs

A collection of **nodes (vertices)** connected by **edges**. Used to model relationships and networks.

---

## Graph Types

**Directed**: Edges have direction (one-way)
```
A → B → C
```

**Undirected**: Edges are bidirectional
```
A — B — C
```

**Weighted**: Edges have values (distances, costs)

---

## Graph Representation

### Adjacency List (Common)
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

### Adjacency Matrix
```python
#     A  B  C  D
# A [[0, 1, 1, 0],
# B  [1, 0, 0, 1],
# C  [1, 0, 0, 1],
# D  [0, 1, 1, 0]]
```

---

## Graph Traversals

### BFS (Breadth-First Search)
```python
from collections import deque

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
```

### DFS (Depth-First Search)
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result
```

---

## When to Use

- Social networks
- Maps/navigation
- Dependencies
- Recommendations

---

## Next Steps

Practice with [examples.py](examples.py)!
