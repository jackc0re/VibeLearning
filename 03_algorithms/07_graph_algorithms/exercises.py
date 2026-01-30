"""
Graph Algorithms - Exercises

Practice implementing graph algorithms.
Each exercise includes test cases to verify your solution.

Run this file to test your implementations:
    python exercises.py
"""

from collections import deque


# =============================================================================
# EXERCISE 1: BFS Traversal
# =============================================================================

def bfs(graph, start):
    """
    Implement Breadth-First Search traversal.
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        start: Starting node
        
    Returns:
        List of nodes in BFS order
        
    Example:
        >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        >>> bfs(graph, 'A')
        ['A', 'B', 'C', 'D']
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 2: DFS Traversal
# =============================================================================

def dfs(graph, start):
    """
    Implement Depth-First Search traversal (iterative or recursive).
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        start: Starting node
        
    Returns:
        List of nodes in DFS order
        
    Example:
        >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        >>> dfs(graph, 'A')
        ['A', 'B', 'D', 'C']  # or similar valid DFS order
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 3: Shortest Path (Unweighted)
# =============================================================================

def shortest_path_unweighted(graph, start, end):
    """
    Find shortest path in unweighted graph using BFS.
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        start: Starting node
        end: Target node
        
    Returns:
        List representing the path, or None if no path exists
        
    Example:
        >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []}
        >>> shortest_path_unweighted(graph, 'A', 'E')
        ['A', 'B', 'D', 'E']  # or ['A', 'C', 'D', 'E']
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 4: Dijkstra's Algorithm
# =============================================================================

def dijkstra(graph, start):
    """
    Implement Dijkstra's shortest path algorithm.
    
    Args:
        graph: Weighted adjacency list {node: [(neighbor, weight), ...]}
        start: Starting node
        
    Returns:
        Dict of shortest distances from start to each node
        
    Example:
        >>> graph = {
        ...     'A': [('B', 4), ('C', 2)],
        ...     'B': [('D', 3)],
        ...     'C': [('B', 1), ('D', 5)],
        ...     'D': []
        ... }
        >>> dijkstra(graph, 'A')
        {'A': 0, 'B': 3, 'C': 2, 'D': 6}
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 5: Detect Cycle (Undirected)
# =============================================================================

def has_cycle_undirected(graph):
    """
    Detect if an undirected graph has a cycle.
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        
    Returns:
        True if cycle exists, False otherwise
        
    Example:
        >>> graph = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}
        >>> has_cycle_undirected(graph)
        False
        >>> graph = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
        >>> has_cycle_undirected(graph)
        True
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 6: Detect Cycle (Directed)
# =============================================================================

def has_cycle_directed(graph):
    """
    Detect if a directed graph has a cycle.
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        
    Returns:
        True if cycle exists, False otherwise
        
    Example:
        >>> graph = {'A': ['B'], 'B': ['C'], 'C': []}
        >>> has_cycle_directed(graph)
        False
        >>> graph = {'A': ['B'], 'B': ['C'], 'C': ['A']}
        >>> has_cycle_directed(graph)
        True
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 7: Topological Sort
# =============================================================================

def topological_sort(graph):
    """
    Perform topological sort on a DAG.
    
    Args:
        graph: Adjacency list {node: [neighbors]} (directed)
        
    Returns:
        List of nodes in topological order, or None if cycle exists
        
    Example:
        >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        >>> topological_sort(graph)
        ['A', 'B', 'C', 'D']  # or ['A', 'C', 'B', 'D']
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 8: Connected Components
# =============================================================================

def count_connected_components(graph):
    """
    Count the number of connected components in an undirected graph.
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        
    Returns:
        Number of connected components
        
    Example:
        >>> graph = {
        ...     'A': ['B'], 'B': ['A'],
        ...     'C': ['D'], 'D': ['C'],
        ...     'E': []
        ... }
        >>> count_connected_components(graph)
        3
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 9: Is Bipartite
# =============================================================================

def is_bipartite(graph):
    """
    Check if a graph is bipartite (2-colorable).
    
    A graph is bipartite if nodes can be divided into two sets
    such that no two nodes in the same set are adjacent.
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        
    Returns:
        True if bipartite, False otherwise
        
    Example:
        >>> graph = {'A': ['B', 'D'], 'B': ['A', 'C'], 'C': ['B', 'D'], 'D': ['A', 'C']}
        >>> is_bipartite(graph)
        True  # Square graph is bipartite
        >>> graph = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
        >>> is_bipartite(graph)
        False  # Triangle is not bipartite
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# EXERCISE 10: Find All Paths
# =============================================================================

def find_all_paths(graph, start, end):
    """
    Find all paths from start to end in a directed graph.
    
    Args:
        graph: Adjacency list {node: [neighbors]}
        start: Starting node
        end: Target node
        
    Returns:
        List of all paths (each path is a list of nodes)
        
    Example:
        >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        >>> find_all_paths(graph, 'A', 'D')
        [['A', 'B', 'D'], ['A', 'C', 'D']]
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# TEST CASES
# =============================================================================

def test_bfs():
    """Test BFS implementation."""
    print("Testing bfs...")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    result = bfs(graph, 'A')
    assert result[0] == 'A', "BFS should start with start node"
    assert set(result) == set(graph.keys()), "BFS should visit all nodes"
    
    # Check level ordering
    a_idx = result.index('A')
    b_idx = result.index('B')
    c_idx = result.index('C')
    d_idx = result.index('D')
    
    assert a_idx < b_idx and a_idx < c_idx, "Level 0 before level 1"
    assert b_idx < d_idx and c_idx < d_idx, "Level 1 before level 2"
    
    print("✓ All bfs tests passed!")


def test_dfs():
    """Test DFS implementation."""
    print("\nTesting dfs...")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    
    result = dfs(graph, 'A')
    assert result[0] == 'A', "DFS should start with start node"
    assert set(result) == set(graph.keys()), "DFS should visit all nodes"
    
    print("✓ All dfs tests passed!")


def test_shortest_path_unweighted():
    """Test shortest path in unweighted graph."""
    print("\nTesting shortest_path_unweighted...")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    
    path = shortest_path_unweighted(graph, 'A', 'E')
    assert path is not None, "Path should exist"
    assert path[0] == 'A' and path[-1] == 'E', "Path should start at A and end at E"
    assert len(path) == 3, f"Shortest path should have 3 nodes, got {len(path)}"
    
    # Test no path
    graph2 = {'A': ['B'], 'B': ['A'], 'C': []}
    assert shortest_path_unweighted(graph2, 'A', 'C') is None, "No path should return None"
    
    print("✓ All shortest_path_unweighted tests passed!")


def test_dijkstra():
    """Test Dijkstra's algorithm."""
    print("\nTesting dijkstra...")
    
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('D', 3)],
        'C': [('A', 2), ('B', 1), ('D', 5)],
        'D': [('B', 3), ('C', 5)]
    }
    
    distances = dijkstra(graph, 'A')
    
    assert distances['A'] == 0, "Distance to self should be 0"
    assert distances['C'] == 2, "Distance to C should be 2"
    assert distances['B'] == 3, "Distance to B should be 3 (via C)"
    assert distances['D'] == 6, "Distance to D should be 6"
    
    print("✓ All dijkstra tests passed!")


def test_has_cycle_undirected():
    """Test cycle detection in undirected graph."""
    print("\nTesting has_cycle_undirected...")
    
    # No cycle (tree)
    tree = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['A']
    }
    assert has_cycle_undirected(tree) == False, "Tree should have no cycle"
    
    # Has cycle (triangle)
    triangle = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    assert has_cycle_undirected(triangle) == True, "Triangle should have cycle"
    
    print("✓ All has_cycle_undirected tests passed!")


def test_has_cycle_directed():
    """Test cycle detection in directed graph."""
    print("\nTesting has_cycle_directed...")
    
    # No cycle (DAG)
    dag = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    assert has_cycle_directed(dag) == False, "DAG should have no cycle"
    
    # Has cycle
    cyclic = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    assert has_cycle_directed(cyclic) == True, "A->B->C->A should have cycle"
    
    print("✓ All has_cycle_directed tests passed!")


def test_topological_sort():
    """Test topological sort."""
    print("\nTesting topological_sort...")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    
    result = topological_sort(graph)
    assert result is not None, "DAG should have valid topological order"
    
    # Verify order: for each edge u->v, u comes before v
    indices = {node: i for i, node in enumerate(result)}
    for node in graph:
        for neighbor in graph[node]:
            assert indices[node] < indices[neighbor], f"{node} should come before {neighbor}"
    
    print("✓ All topological_sort tests passed!")


def test_count_connected_components():
    """Test connected components counting."""
    print("\nTesting count_connected_components...")
    
    # 3 components
    graph = {
        'A': ['B'], 'B': ['A'],
        'C': ['D'], 'D': ['C'],
        'E': []
    }
    assert count_connected_components(graph) == 3, "Should have 3 components"
    
    # 1 component
    connected = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    assert count_connected_components(connected) == 1, "Should have 1 component"
    
    print("✓ All count_connected_components tests passed!")


def test_is_bipartite():
    """Test bipartite check."""
    print("\nTesting is_bipartite...")
    
    # Bipartite (square)
    square = {
        'A': ['B', 'D'],
        'B': ['A', 'C'],
        'C': ['B', 'D'],
        'D': ['A', 'C']
    }
    assert is_bipartite(square) == True, "Square should be bipartite"
    
    # Not bipartite (triangle)
    triangle = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    assert is_bipartite(triangle) == False, "Triangle should not be bipartite"
    
    print("✓ All is_bipartite tests passed!")


def test_find_all_paths():
    """Test finding all paths."""
    print("\nTesting find_all_paths...")
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    
    paths = find_all_paths(graph, 'A', 'D')
    assert len(paths) == 2, "Should find 2 paths"
    
    expected_paths = [['A', 'B', 'D'], ['A', 'C', 'D']]
    for path in expected_paths:
        assert path in paths, f"Path {path} should be found"
    
    print("✓ All find_all_paths tests passed!")


# =============================================================================
# SOLUTIONS (Hidden - Try to solve without looking!)
# =============================================================================

def _show_solutions():
    """Display solutions for all exercises."""
    solutions = '''
# =============================================================================
# SOLUTIONS
# =============================================================================

from collections import deque
import heapq

# Exercise 1: BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result


# Exercise 2: DFS
def dfs(graph, start):
    visited = set()
    result = []
    
    def helper(node):
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                helper(neighbor)
    
    helper(start)
    return result


# Exercise 3: Shortest Path (Unweighted)
def shortest_path_unweighted(graph, start, end):
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([(start, [start])])
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None


# Exercise 4: Dijkstra's Algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, weight in graph.get(node, []):
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances


# Exercise 5: Detect Cycle (Undirected)
def has_cycle_undirected(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False


# Exercise 6: Detect Cycle (Directed)
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
    
    color = {node: WHITE for node in all_nodes}
    
    def dfs(node):
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True
        color[node] = BLACK
        return False
    
    for node in all_nodes:
        if color[node] == WHITE and dfs(node):
            return True
    return False


# Exercise 7: Topological Sort
def topological_sort(graph):
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
    
    in_degree = {node: 0 for node in all_nodes}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    queue = deque([n for n in all_nodes if in_degree[n] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == len(all_nodes) else None


# Exercise 8: Connected Components
def count_connected_components(graph):
    visited = set()
    count = 0
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
    
    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1
    
    return count


# Exercise 9: Is Bipartite
def is_bipartite(graph):
    color = {}
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    for node in graph:
        if node not in color:
            if not bfs(node):
                return False
    return True


# Exercise 10: Find All Paths
def find_all_paths(graph, start, end):
    def dfs(node, path):
        if node == end:
            return [path]
        
        paths = []
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                paths.extend(dfs(neighbor, path + [neighbor]))
        return paths
    
    return dfs(start, [start])
'''
    print(solutions)


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--solutions":
        _show_solutions()
    else:
        print("=" * 60)
        print("GRAPH ALGORITHMS - EXERCISES")
        print("=" * 60)
        print("\nImplement each function and run this file to test.")
        print("Use 'python exercises.py --solutions' to see solutions.\n")
        
        try:
            test_bfs()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ bfs: {e}")
        
        try:
            test_dfs()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ dfs: {e}")
        
        try:
            test_shortest_path_unweighted()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ shortest_path_unweighted: {e}")
        
        try:
            test_dijkstra()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ dijkstra: {e}")
        
        try:
            test_has_cycle_undirected()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ has_cycle_undirected: {e}")
        
        try:
            test_has_cycle_directed()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ has_cycle_directed: {e}")
        
        try:
            test_topological_sort()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ topological_sort: {e}")
        
        try:
            test_count_connected_components()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ count_connected_components: {e}")
        
        try:
            test_is_bipartite()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ is_bipartite: {e}")
        
        try:
            test_find_all_paths()
        except (AssertionError, TypeError, AttributeError) as e:
            print(f"✗ find_all_paths: {e}")
        
        print("\n" + "=" * 60)
        print("Testing complete!")
        print("=" * 60)
