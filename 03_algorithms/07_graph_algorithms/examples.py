"""
Graph Algorithms - Examples

This file demonstrates graph algorithms with
visualizations and detailed explanations.

Run this file to see the examples in action:
    python examples.py
"""

from collections import deque, defaultdict
import heapq


# =============================================================================
# GRAPH REPRESENTATIONS
# =============================================================================

def create_sample_graphs():
    """Create sample graphs for demonstrations."""
    
    # Unweighted undirected graph
    #     A --- B
    #     |     |
    #     C --- D --- E
    #           |
    #           F
    unweighted = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['D'],
        'F': ['D']
    }
    
    # Weighted undirected graph
    #     A --4-- B
    #     |       |
    #     2       3
    #     |       |
    #     C --1-- D --5-- E
    weighted = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('D', 3)],
        'C': [('A', 2), ('D', 1)],
        'D': [('B', 3), ('C', 1), ('E', 5)],
        'E': [('D', 5)]
    }
    
    # Directed acyclic graph (DAG)
    #     A --> B --> D
    #     |     |
    #     v     v
    #     C --> E --> F
    dag = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['E'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    return unweighted, weighted, dag


# =============================================================================
# BREADTH-FIRST SEARCH (BFS)
# =============================================================================

def bfs(graph, start):
    """
    Breadth-First Search traversal.
    
    Explores all neighbors at current depth before moving deeper.
    Uses a queue (FIFO).
    
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
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result


def bfs_with_levels(graph, start):
    """BFS that tracks the level/distance of each node."""
    visited = {start: 0}
    queue = deque([start])
    levels = {start: 0}
    
    while queue:
        vertex = queue.popleft()
        current_level = levels[vertex]
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited[neighbor] = current_level + 1
                levels[neighbor] = current_level + 1
                queue.append(neighbor)
    
    return levels


def bfs_shortest_path(graph, start, end):
    """Find shortest path in unweighted graph using BFS."""
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        vertex, path = queue.popleft()
        
        for neighbor in graph[vertex]:
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No path found


# =============================================================================
# DEPTH-FIRST SEARCH (DFS)
# =============================================================================

def dfs_recursive(graph, start, visited=None):
    """
    Depth-First Search (recursive).
    
    Explores as deep as possible before backtracking.
    Uses recursion (implicit stack).
    
    Time: O(V + E)
    Space: O(V)
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
    Depth-First Search (iterative with explicit stack).
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors in reverse order for consistent traversal
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


def dfs_all_paths(graph, start, end, path=None):
    """Find all paths from start to end using DFS."""
    if path is None:
        path = []
    
    path = path + [start]
    
    if start == end:
        return [path]
    
    if start not in graph:
        return []
    
    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:  # Avoid cycles
            new_paths = dfs_all_paths(graph, neighbor, end, path)
            paths.extend(new_paths)
    
    return paths


# =============================================================================
# DIJKSTRA'S ALGORITHM
# =============================================================================

def dijkstra(graph, start):
    """
    Dijkstra's shortest path algorithm.
    
    Finds shortest path from start to all other vertices.
    Works with non-negative edge weights.
    
    Time: O((V + E) log V) with min-heap
    Space: O(V)
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        if curr_node in visited:
            continue
        visited.add(curr_node)
        
        for neighbor, weight in graph[curr_node]:
            if neighbor in visited:
                continue
                
            distance = curr_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = curr_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous


def dijkstra_path(graph, start, end):
    """Get shortest path and distance using Dijkstra."""
    distances, previous = dijkstra(graph, start)
    
    if distances[end] == float('inf'):
        return None, float('inf')
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    
    return path[::-1], distances[end]


# =============================================================================
# BELLMAN-FORD ALGORITHM
# =============================================================================

def bellman_ford(vertices, edges, start):
    """
    Bellman-Ford shortest path algorithm.
    
    Handles negative edge weights.
    Detects negative cycles.
    
    Time: O(V × E)
    Space: O(V)
    
    Args:
        vertices: List of all vertices
        edges: List of (u, v, weight) tuples
        start: Starting vertex
    """
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    previous = {v: None for v in vertices}
    
    # Relax all edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                previous[v] = u
    
    # Check for negative cycles
    for u, v, weight in edges:
        if distances[u] + weight < distances[v]:
            return None, None  # Negative cycle detected
    
    return distances, previous


# =============================================================================
# FLOYD-WARSHALL ALGORITHM
# =============================================================================

def floyd_warshall(vertices, edges):
    """
    Floyd-Warshall all-pairs shortest path.
    
    Time: O(V³)
    Space: O(V²)
    """
    n = len(vertices)
    vertex_to_idx = {v: i for i, v in enumerate(vertices)}
    
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u, v, weight in edges:
        i, j = vertex_to_idx[u], vertex_to_idx[v]
        dist[i][j] = weight
    
    # Try each vertex as intermediate
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist, vertices


# =============================================================================
# MINIMUM SPANNING TREE - PRIM'S ALGORITHM
# =============================================================================

def prim(graph, start):
    """
    Prim's Minimum Spanning Tree algorithm.
    
    Grows MST from starting vertex by always adding
    the minimum weight edge to an unvisited vertex.
    
    Time: O((V + E) log V)
    Space: O(V)
    """
    mst = []
    total_weight = 0
    visited = set([start])
    
    # Edges: (weight, from_vertex, to_vertex)
    edges = [(weight, start, to) for to, weight in graph[start]]
    heapq.heapify(edges)
    
    while edges and len(visited) < len(graph):
        weight, frm, to = heapq.heappop(edges)
        
        if to in visited:
            continue
        
        visited.add(to)
        mst.append((frm, to, weight))
        total_weight += weight
        
        for neighbor, w in graph[to]:
            if neighbor not in visited:
                heapq.heappush(edges, (w, to, neighbor))
    
    return mst, total_weight


# =============================================================================
# MINIMUM SPANNING TREE - KRUSKAL'S ALGORITHM
# =============================================================================

class UnionFind:
    """Union-Find (Disjoint Set Union) data structure."""
    
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in same set
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True


def kruskal(vertices, edges):
    """
    Kruskal's Minimum Spanning Tree algorithm.
    
    Sorts edges by weight and adds them if they
    don't create a cycle.
    
    Time: O(E log E)
    Space: O(V)
    """
    edges = sorted(edges, key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(vertices)
    mst = []
    total_weight = 0
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            
            if len(mst) == len(vertices) - 1:
                break
    
    return mst, total_weight


# =============================================================================
# TOPOLOGICAL SORT
# =============================================================================

def topological_sort_dfs(graph):
    """
    Topological sort using DFS.
    
    Orders vertices so that for every edge u→v,
    u comes before v.
    
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
        result.append(node)
    
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return result[::-1]


def topological_sort_kahn(graph):
    """
    Topological sort using Kahn's algorithm (BFS-based).
    
    Returns None if graph has a cycle.
    """
    # Get all nodes
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
    
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
    
    if len(result) != len(all_nodes):
        return None  # Cycle detected
    
    return result


# =============================================================================
# CYCLE DETECTION
# =============================================================================

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


def has_cycle_directed(graph):
    """
    Detect cycle in directed graph using colors.
    
    WHITE (0): Not visited
    GRAY (1): Being processed
    BLACK (2): Completely processed
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    
    # Get all nodes
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
    
    color = {node: WHITE for node in all_nodes}
    
    def dfs(node):
        color[node] = GRAY
        
        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:
                return True  # Back edge
            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True
        
        color[node] = BLACK
        return False
    
    for node in all_nodes:
        if color[node] == WHITE:
            if dfs(node):
                return True
    
    return False


# =============================================================================
# CONNECTED COMPONENTS
# =============================================================================

def connected_components(graph):
    """Find all connected components in undirected graph."""
    visited = set()
    components = []
    
    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)
    
    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)
    
    return components


# =============================================================================
# DEMONSTRATIONS
# =============================================================================

def demo_bfs():
    """Demonstrate BFS traversal."""
    print("=" * 60)
    print("BREADTH-FIRST SEARCH (BFS)")
    print("=" * 60)
    
    graph, _, _ = create_sample_graphs()
    
    print("\nGraph:")
    print("    A --- B")
    print("    |     |")
    print("    C --- D --- E")
    print("          |")
    print("          F")
    
    print(f"\nBFS from 'A': {bfs(graph, 'A')}")
    
    levels = bfs_with_levels(graph, 'A')
    print(f"\nLevels from 'A': {levels}")
    
    path = bfs_shortest_path(graph, 'A', 'E')
    print(f"\nShortest path A → E: {' → '.join(path)}")


def demo_dfs():
    """Demonstrate DFS traversal."""
    print("\n" + "=" * 60)
    print("DEPTH-FIRST SEARCH (DFS)")
    print("=" * 60)
    
    graph, _, _ = create_sample_graphs()
    
    print(f"\nDFS (recursive) from 'A': {dfs_recursive(graph, 'A')}")
    print(f"DFS (iterative) from 'A': {dfs_iterative(graph, 'A')}")
    
    all_paths = dfs_all_paths(graph, 'A', 'E')
    print(f"\nAll paths A → E:")
    for path in all_paths:
        print(f"  {' → '.join(path)}")


def demo_dijkstra():
    """Demonstrate Dijkstra's algorithm."""
    print("\n" + "=" * 60)
    print("DIJKSTRA'S ALGORITHM")
    print("=" * 60)
    
    _, weighted, _ = create_sample_graphs()
    
    print("\nWeighted Graph:")
    print("    A --4-- B")
    print("    |       |")
    print("    2       3")
    print("    |       |")
    print("    C --1-- D --5-- E")
    
    distances, _ = dijkstra(weighted, 'A')
    print(f"\nShortest distances from 'A':")
    for node, dist in sorted(distances.items()):
        print(f"  A → {node}: {dist}")
    
    path, dist = dijkstra_path(weighted, 'A', 'E')
    print(f"\nShortest path A → E: {' → '.join(path)} (distance: {dist})")


def demo_bellman_ford():
    """Demonstrate Bellman-Ford algorithm."""
    print("\n" + "=" * 60)
    print("BELLMAN-FORD ALGORITHM")
    print("=" * 60)
    
    vertices = ['A', 'B', 'C', 'D']
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'D', 3),
        ('C', 'B', -1),  # Negative edge
        ('C', 'D', 5),
    ]
    
    print("\nGraph with negative edge (C→B = -1):")
    print("    A --4--> B")
    print("    |        |")
    print("    2       3")
    print("    v   -1   v")
    print("    C -----> D")
    print("    \\--5---/")
    
    distances, _ = bellman_ford(vertices, edges, 'A')
    
    if distances:
        print(f"\nShortest distances from 'A':")
        for node, dist in sorted(distances.items()):
            print(f"  A → {node}: {dist}")
    else:
        print("\nNegative cycle detected!")


def demo_mst():
    """Demonstrate MST algorithms."""
    print("\n" + "=" * 60)
    print("MINIMUM SPANNING TREE")
    print("=" * 60)
    
    _, weighted, _ = create_sample_graphs()
    
    print("\nWeighted Graph:")
    print("    A --4-- B")
    print("    |       |")
    print("    2       3")
    print("    |       |")
    print("    C --1-- D --5-- E")
    
    # Prim's
    mst_prim, weight_prim = prim(weighted, 'A')
    print(f"\nPrim's MST (starting from A):")
    for u, v, w in mst_prim:
        print(f"  {u} -- {v} (weight: {w})")
    print(f"Total weight: {weight_prim}")
    
    # Kruskal's
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'D', 3), ('C', 'D', 1), ('D', 'E', 5)
    ]
    mst_kruskal, weight_kruskal = kruskal(vertices, edges)
    print(f"\nKruskal's MST:")
    for u, v, w in mst_kruskal:
        print(f"  {u} -- {v} (weight: {w})")
    print(f"Total weight: {weight_kruskal}")


def demo_topological_sort():
    """Demonstrate topological sort."""
    print("\n" + "=" * 60)
    print("TOPOLOGICAL SORT")
    print("=" * 60)
    
    _, _, dag = create_sample_graphs()
    
    print("\nDAG (Directed Acyclic Graph):")
    print("    A --> B --> D")
    print("    |     |")
    print("    v     v")
    print("    C --> E --> F")
    
    topo_dfs = topological_sort_dfs(dag)
    print(f"\nTopological order (DFS): {' → '.join(topo_dfs)}")
    
    topo_kahn = topological_sort_kahn(dag)
    print(f"Topological order (Kahn): {' → '.join(topo_kahn)}")


def demo_cycle_detection():
    """Demonstrate cycle detection."""
    print("\n" + "=" * 60)
    print("CYCLE DETECTION")
    print("=" * 60)
    
    # Undirected graph with cycle
    graph_with_cycle = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],  # A-B-C-A forms a cycle
        'C': ['A', 'B']
    }
    
    # Undirected graph without cycle (tree)
    tree = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['A']
    }
    
    print("\nUndirected graphs:")
    print(f"  Triangle (A-B-C-A): has cycle = {has_cycle_undirected(graph_with_cycle)}")
    print(f"  Tree: has cycle = {has_cycle_undirected(tree)}")
    
    # Directed graph with cycle
    directed_cycle = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']  # Cycle: A→B→C→A
    }
    
    # DAG (no cycle)
    _, _, dag = create_sample_graphs()
    
    print("\nDirected graphs:")
    print(f"  A→B→C→A: has cycle = {has_cycle_directed(directed_cycle)}")
    print(f"  DAG: has cycle = {has_cycle_directed(dag)}")


def demo_connected_components():
    """Demonstrate finding connected components."""
    print("\n" + "=" * 60)
    print("CONNECTED COMPONENTS")
    print("=" * 60)
    
    # Graph with 3 components
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D', 'E'],
        'D': ['C', 'E'],
        'E': ['C', 'D'],
        'F': []
    }
    
    print("\nGraph with 3 components:")
    print("  Component 1: A -- B")
    print("  Component 2: C -- D -- E (triangle)")
    print("  Component 3: F (isolated)")
    
    components = connected_components(graph)
    print(f"\nFound {len(components)} components:")
    for i, comp in enumerate(components, 1):
        print(f"  Component {i}: {comp}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    demo_bfs()
    demo_dfs()
    demo_dijkstra()
    demo_bellman_ford()
    demo_mst()
    demo_topological_sort()
    demo_cycle_detection()
    demo_connected_components()
    
    print("\n" + "=" * 60)
    print("✓ All graph algorithm examples completed!")
    print("=" * 60)
