# 🕸️ Graph Algorithms

> Traversing and analyzing connected data structures

---

## 📋 Table of Contents

1. [Graph Basics Recap](#graph-basics-recap)
2. [Graph Traversal](#graph-traversal)
3. [Shortest Path Algorithms](#shortest-path-algorithms)
4. [Minimum Spanning Tree](#minimum-spanning-tree)
5. [Topological Sort](#topological-sort)
6. [Cycle Detection](#cycle-detection)
7. [Algorithm Comparison](#algorithm-comparison)

---

## Graph Basics Recap

### Graph Representation

```python
# Adjacency List (most common)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Weighted Graph
weighted_graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('D', 3)],
    'C': [('A', 2), ('D', 1)],
    'D': [('B', 3), ('C', 1)]
}

# Adjacency Matrix
#     A  B  C  D
# A [[0, 4, 2, 0],
# B  [4, 0, 0, 3],
# C  [2, 0, 0, 1],
# D  [0, 3, 1, 0]]
```

### Graph Types

| Type | Description |
|------|-------------|
| Directed | Edges have direction (A → B) |
| Undirected | Edges go both ways (A — B) |
| Weighted | Edges have costs/distances |
| Unweighted | All edges equal |
| Cyclic | Contains cycles |
| Acyclic | No cycles (DAG if directed) |

---

## Graph Traversal

### Breadth-First Search (BFS)

Explores neighbors level by level. Uses a **queue**.

```
       A
      / \
     B   C
    / \   \
   D   E   F

BFS from A: A → B → C → D → E → F
(Level 0)  (Level 1)  (Level 2)
```

```python
from collections import deque

def bfs(graph, start):
    """
    Breadth-First Search traversal.
    
    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add unvisited neighbors to queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result
```

**Use BFS for:**
- Shortest path in unweighted graphs
- Level-order traversal
- Finding connected components
- Testing bipartiteness

### Depth-First Search (DFS)

Explores as deep as possible before backtracking. Uses a **stack** (or recursion).

```
       A
      / \
     B   C
    / \   \
   D   E   F

DFS from A: A → B → D → E → C → F
(Goes deep before wide)
```

```python
def dfs_recursive(graph, start, visited=None):
    """
    Depth-First Search (recursive).
    
    Time: O(V + E)
    Space: O(V) for recursion stack
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph, start):
    """
    Depth-First Search (iterative with stack).
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors to stack (reverse for consistent order)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result
```

**Use DFS for:**
- Detecting cycles
- Topological sorting
- Finding strongly connected components
- Solving mazes/puzzles
- Path finding (any path, not shortest)

### BFS vs DFS Comparison

| Aspect | BFS | DFS |
|--------|-----|-----|
| Data Structure | Queue | Stack/Recursion |
| Order | Level by level | Deep first |
| Shortest Path | Yes (unweighted) | No |
| Memory | O(width) | O(depth) |
| Complete | Yes | Yes |

---

## Shortest Path Algorithms

### Dijkstra's Algorithm

Finds shortest path from source to all vertices in **weighted graphs with non-negative edges**.

```python
import heapq

def dijkstra(graph, start):
    """
    Dijkstra's shortest path algorithm.
    
    Time: O((V + E) log V) with min-heap
    Space: O(V)
    
    Args:
        graph: Dict of {node: [(neighbor, weight), ...]}
        start: Starting node
        
    Returns:
        Dict of shortest distances from start
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        if curr_node in visited:
            continue
        visited.add(curr_node)
        
        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

**Example:**
```
Graph:
    A --4-- B
    |       |
    2       3
    |       |
    C --1-- D

Dijkstra from A:
- A: 0
- C: 2 (A→C)
- D: 3 (A→C→D)
- B: 4 (A→B) or (A→C→D→B = 6, so A→B is shorter)
```

### Bellman-Ford Algorithm

Handles **negative edge weights**. Detects negative cycles.

```python
def bellman_ford(graph, vertices, start):
    """
    Bellman-Ford shortest path algorithm.
    
    Time: O(V × E)
    Space: O(V)
    
    Args:
        graph: List of (u, v, weight) edges
        vertices: List of all vertices
        start: Starting vertex
        
    Returns:
        Dict of distances, or None if negative cycle exists
    """
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    
    # Relax all edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            return None  # Negative cycle detected
    
    return distances
```

### Floyd-Warshall Algorithm

Finds shortest paths between **all pairs** of vertices.

```python
def floyd_warshall(graph, n):
    """
    Floyd-Warshall all-pairs shortest path.
    
    Time: O(V³)
    Space: O(V²)
    
    Args:
        graph: Adjacency matrix (inf for no edge)
        n: Number of vertices
        
    Returns:
        Matrix of shortest distances
    """
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u in range(n):
        for v, weight in graph[u]:
            dist[u][v] = weight
    
    # Try each vertex as intermediate
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
```

### Shortest Path Algorithm Comparison

| Algorithm | Time | Space | Negative Edges | Use Case |
|-----------|------|-------|----------------|----------|
| BFS | O(V+E) | O(V) | N/A (unweighted) | Unweighted graphs |
| Dijkstra | O((V+E)logV) | O(V) | No | Non-negative weights |
| Bellman-Ford | O(VE) | O(V) | Yes | Negative weights |
| Floyd-Warshall | O(V³) | O(V²) | Yes | All pairs |

---

## Minimum Spanning Tree

A **Minimum Spanning Tree (MST)** connects all vertices with minimum total edge weight.

### Prim's Algorithm

Grows MST from a starting vertex.

```python
import heapq

def prim(graph, start):
    """
    Prim's MST algorithm.
    
    Time: O((V + E) log V)
    Space: O(V)
    """
    mst = []
    visited = set([start])
    
    # Edges from start: (weight, from, to)
    edges = [(weight, start, to) for to, weight in graph[start]]
    heapq.heapify(edges)
    
    while edges and len(visited) < len(graph):
        weight, frm, to = heapq.heappop(edges)
        
        if to in visited:
            continue
        
        visited.add(to)
        mst.append((frm, to, weight))
        
        for neighbor, w in graph[to]:
            if neighbor not in visited:
                heapq.heappush(edges, (w, to, neighbor))
    
    return mst
```

### Kruskal's Algorithm

Sorts all edges and adds them if they don't create a cycle.

```python
class UnionFind:
    """Union-Find data structure for Kruskal's."""
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


def kruskal(n, edges):
    """
    Kruskal's MST algorithm.
    
    Time: O(E log E)
    Space: O(V)
    
    Args:
        n: Number of vertices
        edges: List of (u, v, weight)
    """
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(n)
    mst = []
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == n - 1:
                break
    
    return mst
```

---

## Topological Sort

Orders vertices in a **Directed Acyclic Graph (DAG)** so that for every edge u→v, u comes before v.

```python
def topological_sort_dfs(graph):
    """
    Topological sort using DFS.
    
    Time: O(V + E)
    Space: O(V)
    """
    visited = set()
    result = []
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)  # Add after all descendants
    
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return result[::-1]  # Reverse for correct order


def topological_sort_kahn(graph, all_nodes):
    """
    Topological sort using Kahn's algorithm (BFS).
    
    Time: O(V + E)
    Space: O(V)
    """
    from collections import deque
    
    # Calculate in-degrees
    in_degree = {node: 0 for node in all_nodes}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Start with nodes having no incoming edges
    queue = deque([node for node in all_nodes if in_degree[node] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycle
    if len(result) != len(all_nodes):
        return None  # Cycle detected
    
    return result
```

**Use Cases:**
- Task scheduling
- Build systems (dependencies)
- Course prerequisites
- Package installation order

---

## Cycle Detection

### In Undirected Graphs

```python
def has_cycle_undirected(graph):
    """
    Detect cycle in undirected graph using DFS.
    """
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # Back edge found
        
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    
    return False
```

### In Directed Graphs

```python
def has_cycle_directed(graph):
    """
    Detect cycle in directed graph using colors.
    
    WHITE (0): Not visited
    GRAY (1): Being processed (in current path)
    BLACK (2): Completely processed
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    
    def dfs(node):
        color[node] = GRAY
        
        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:
                return True  # Back edge (cycle)
            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True
        
        color[node] = BLACK
        return False
    
    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True
    
    return False
```

---

## Algorithm Comparison

### When to Use Each Algorithm

| Problem | Algorithm | Time |
|---------|-----------|------|
| Traverse all nodes | BFS or DFS | O(V+E) |
| Shortest path (unweighted) | BFS | O(V+E) |
| Shortest path (weighted, non-negative) | Dijkstra | O((V+E)logV) |
| Shortest path (negative weights) | Bellman-Ford | O(VE) |
| All-pairs shortest path | Floyd-Warshall | O(V³) |
| Minimum spanning tree | Prim or Kruskal | O(ElogV) |
| Topological order | DFS or Kahn's | O(V+E) |
| Cycle detection | DFS | O(V+E) |
| Connected components | BFS or DFS | O(V+E) |

---

## 🔑 Key Takeaways

1. **BFS** = Queue, level-by-level, shortest path (unweighted)
2. **DFS** = Stack/recursion, deep-first, cycle detection
3. **Dijkstra** = Greedy, non-negative weights, priority queue
4. **Bellman-Ford** = Handles negative weights, detects negative cycles
5. **MST algorithms** = Prim (grow from vertex), Kruskal (sort edges)
6. **Topological sort** = DAG ordering, dependencies

---

## 🔗 Next Steps

- Practice with [`exercises.py`](exercises.py)
- Test your knowledge with [`quiz.md`](quiz.md)
- Return to [Module Overview](../README.md)
