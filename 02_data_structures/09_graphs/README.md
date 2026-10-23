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

```python
# Weighted adjacency list: graph[node][neighbor] = weight
weighted = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

print(weighted['A']['C'])     # 2 - the cost of travelling A -> C
print(list(weighted['A']))    # ['B', 'C'] - the neighbours of A
```

Use the weighted shape whenever the number on the edge matters: minutes between train stops,
the price of a flight, the length of a road. Finding the cheapest path through those numbers
needs Dijkstra's algorithm - see
[03_algorithms/07_graph_algorithms](../../03_algorithms/07_graph_algorithms/README.md).

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
# Rows and columns are A, B, C, D. 1 = edge, 0 = no edge.
#       A  B  C  D
matrix = [
    [0, 1, 1, 0],   # A
    [1, 0, 0, 1],   # B
    [1, 0, 0, 1],   # C
    [0, 1, 1, 0],   # D
]

matrix[0][1]   # 1 -> A is connected to B
matrix[0][3]   # 0 -> A is not connected to D
```
A matrix costs O(V squared) memory even when the graph has few edges, which is why the
adjacency list is the usual choice. It pays off for dense graphs, or when you want
"is there an edge?" answered in one step.

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

> 🔁 **Recursion again?** `dfs` calls itself - the [recursion aside in Trees](../08_trees/README.md#tree-traversals) explains the pattern.

---

## When to Use

- Social networks
- Maps/navigation
- Dependencies
- Recommendations

---

## Common Mistakes

### 1. Forgetting `visited` (endless traversal)
```python
def dfs(graph, node):              # ❌ A - B - A - B ... runs forever
    for neighbor in graph[node]:
        dfs(graph, neighbor)

# ✅ Record what you have already seen
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

### 2. Changing a neighbour list while looping over it
```python
for neighbor in graph['A']:
    if neighbor == 'B':
        graph['A'].remove(neighbor)   # ❌ the loop skips the element after it

# ✅ Loop over a copy
for neighbor in list(graph['A']):
    if neighbor == 'B':
        graph['A'].remove(neighbor)
```

### 3. A one-way edge in an undirected graph
```python
graph = {'A': ['B'], 'B': []}     # ❌ B has no way back to A

# ✅ Add both directions
graph = {'A': ['B'], 'B': ['A']}
```

---

## Quick Reference

```python
# Adjacency list (the usual choice)
graph = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}

# Weighted adjacency list
weighted = {'A': {'B': 4}, 'B': {'A': 4}}

# Neighbours of a node
graph['A']
graph.get('Z', [])      # [] instead of KeyError for an unknown node

# Traverse - BFS uses a queue, DFS uses a stack (or recursion)
from collections import deque
queue = deque([start])
stack = [start]

# Always track what you have seen
visited = set()
```

| Structure | Memory | "Is there an edge?" |
|-----------|--------|---------------------|
| Adjacency list | O(V + E) | O(degree) |
| Adjacency matrix | O(V squared) | O(1) |

---

## Next Steps

Practice with [examples.py](examples.py), then try [exercises.py](exercises.py)!

---

## 🧠 Test Yourself

Ready to check what stuck? Take the **[quiz for this topic](quiz.md)** — answers and
explanations are included.
