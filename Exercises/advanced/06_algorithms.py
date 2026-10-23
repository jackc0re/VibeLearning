"""
Advanced Exercise 6: Advanced Algorithms
========================================
Dijkstra with a heap, A* on a grid, 0/1 knapsack dynamic
programming, Rabin-Karp string matching, and run-length encoding.
"""

print("=" * 50)
print("EXERCISE 6: Advanced Algorithms")
print("=" * 50)


# =============================================================================
# EXERCISE 6.1: Dijkstra's Shortest Path
# =============================================================================
print("\n--- Exercise 6.1: Dijkstra's Shortest Path ---")
"""
Weighted graph, non-negative weights, adjacency dict.

Write dijkstra(graph, start) using heapq that returns
(distances, previous): shortest distance from start to every node
and each node's predecessor on its best path.

Also write reconstruct_path(previous, start, target) that walks
the previous links backwards to build the path.
"""

import heapq


# Your code below:
GRAPH = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1, "E": 3},
    "E": {"D": 3},
}


def dijkstra(graph, start):
    """Return (distances, previous) for shortest paths from start."""
    pass


# Test (uncomment after implementing)
# distances, previous = dijkstra(GRAPH, "A")
# print(distances["E"])  # 7


# =============================================================================
# EXERCISE 6.2: A* Pathfinding on a Grid
# =============================================================================
print("\n--- Exercise 6.2: A* Pathfinding on a Grid ---")
"""
Find the shortest path from S to G on GRID below, where '#' is a
wall. A* = Dijkstra plus a heuristic: use the Manhattan distance
to the goal and store (f, g, cell) entries in the heap, where
g is the cost so far and f = g + heuristic.
"""


# Your code below:
GRID = [
    "S....",
    ".###.",
    ".#...",
    ".#.#.",
    "...#G",
]


def astar(grid, start, goal):
    """Return the shortest path as a list of (row, col), or None."""
    pass


# Test (uncomment after implementing)
# path = astar(GRID, (0, 0), (4, 4))
# print(len(path) - 1)  # steps taken


# =============================================================================
# EXERCISE 6.3: Dynamic Programming (0/1 Knapsack)
# =============================================================================
print("\n--- Exercise 6.3: Dynamic Programming (0/1 Knapsack) ---")
"""
Each item can be taken once. Write knapsack(items, capacity):
- items is a list of (name, weight, value)
- Build a bottom-up dp table: dp[i][w] = best value using the
  first i items with capacity w
- Return (best_value, chosen_names) by walking the table backwards
"""


# Your code below:
ITEMS = [
    ("tent", 2, 3),
    ("sleeping_bag", 1, 2),
    ("stove", 1, 2),
    ("food", 3, 4),
]


def knapsack(items, capacity):
    """Return (best value, list of chosen item names)."""
    pass


# Test (uncomment after implementing)
# print(knapsack(ITEMS, 4))  # (7, ['tent', 'sleeping_bag', 'stove'])


# =============================================================================
# EXERCISE 6.4: String Matching (Rabin-Karp)
# =============================================================================
print("\n--- Exercise 6.4: String Matching (Rabin-Karp) ---")
"""
Find every start index of pattern in text.

- naive_search: compare the pattern at every position, O(n * m)
- rabin_karp: slide a rolling hash over the text (remove the left
  character, add the right one); when the hash matches, confirm
  with a direct slice comparison before reporting a match
Both return a sorted list of start indices.
"""


# Your code below:
TEXT = "the quick brown fox jumps over the lazy dog the end"
PATTERN = "the"


def naive_search(pattern, text):
    """Check the pattern at every position: O(n * m)."""
    pass


def rabin_karp(pattern, text):
    """Rolling-hash search with verification on hash hits."""
    pass


# Test (uncomment after implementing)
# print(rabin_karp(PATTERN, TEXT))


# =============================================================================
# EXERCISE 6.5: Compression (Run-Length Encoding)
# =============================================================================
print("\n--- Exercise 6.5: Compression (Run-Length Encoding) ---")
"""
Write the classic RLE pair:

- run_length_encode("aaabccdddd") -> "a3b1c2d4"
- run_length_decode("a3b1c2d4") -> "aaabccdddd"
- Both must handle the empty string; counts may be multi-digit
"""


# Your code below:
def run_length_encode(text):
    """Replace each run of equal characters with char + count."""
    pass


def run_length_decode(encoded):
    """Expand char + count pairs back into the original text."""
    pass


# Test (uncomment after implementing)
# print(run_length_encode("aaabccdddd"))


# =============================================================================
# SOLUTIONS
# =============================================================================

print("\n" + "=" * 50)
print("SOLUTIONS")
print("=" * 50)

# SOLUTION 6.1
print("\n--- Solution 6.1 ---")


def dijkstra(graph, start):
    """Return (distances, previous) for shortest paths from start."""
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    visited = set()
    while heap:
        dist, node = heapq.heappop(heap)
        if node in visited:
            continue  # stale heap entry; the real one was processed
        visited.add(node)
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))
    return distances, previous


def reconstruct_path(previous, start, target):
    """Walk previous links backwards from target to start."""
    if previous.get(target) is None and target != start:
        return None  # unreachable
    path = [target]
    while path[-1] != start:
        path.append(previous[path[-1]])
    return path[::-1]


distances, previous = dijkstra(GRAPH, "A")
print(f"Distances from A: {distances}")
route = reconstruct_path(previous, "A", "E")
print(f"Path A -> E: {' -> '.join(route)} (cost {distances['E']})")
expected = {"A": 0, "B": 1, "C": 3, "D": 4, "E": 7}
print("PASS" if distances == expected and route == ["A", "B", "C", "D", "E"] else "FAIL")

# SOLUTION 6.2
print("\n--- Solution 6.2 ---")


def astar(grid, start, goal):
    """Return the shortest path as a list of (row, col), or None."""
    rows, cols = len(grid), len(grid[0])

    def heuristic(cell):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

    open_heap = [(heuristic(start), 0, start)]
    g_score = {start: 0}
    came_from = {}

    while open_heap:
        _, cost, current = heapq.heappop(open_heap)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]
        for d_row, d_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbor = (current[0] + d_row, current[1] + d_col)
            r, c = neighbor
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == "#":
                continue
            new_cost = cost + 1
            if new_cost < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(open_heap, (new_cost + heuristic(neighbor), new_cost, neighbor))
    return None


path = astar(GRID, (0, 0), (4, 4))
print(f"Path: {path}")
print(f"Steps: {len(path) - 1}")

path_cells = set(path)
print("Map with the path marked '*':")
for r, row in enumerate(GRID):
    rendered = "".join(
        "*" if (r, c) in path_cells and char == "." else char
        for c, char in enumerate(row)
    )
    print(f"  {rendered}")
print("PASS" if len(path) - 1 == 8 else "FAIL")

# SOLUTION 6.3
print("\n--- Solution 6.3 ---")


def knapsack(items, capacity):
    """Return (best value, list of chosen item names)."""
    count = len(items)
    dp = [[0] * (capacity + 1) for _ in range(count + 1)]
    for i in range(1, count + 1):
        _, weight, value = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

    chosen = []
    w = capacity
    for i in range(count, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, weight, _ = items[i - 1]
            chosen.append(name)
            w -= weight
    chosen.reverse()
    return dp[count][capacity], chosen


best_value, chosen = knapsack(ITEMS, 4)
print(f"Best value for capacity 4: {best_value}")
print(f"Chosen items: {chosen}")
print("PASS" if best_value == 7 and chosen == ["tent", "sleeping_bag", "stove"] else "FAIL")

# SOLUTION 6.4
print("\n--- Solution 6.4 ---")


def naive_search(pattern, text):
    """Check the pattern at every position: O(n * m)."""
    matches = []
    for start in range(len(text) - len(pattern) + 1):
        if text[start : start + len(pattern)] == pattern:
            matches.append(start)
    return matches


def rabin_karp(pattern, text):
    """Rolling-hash search with verification on hash hits."""
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []
    base, mod = 256, 1_000_000_007
    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        window_hash = (window_hash * base + ord(text[i])) % mod
    top_power = pow(base, m - 1, mod)

    matches = []
    for start in range(n - m + 1):
        if window_hash == pattern_hash and text[start : start + m] == pattern:
            matches.append(start)
        if start < n - m:
            window_hash = (
                (window_hash - ord(text[start]) * top_power) * base + ord(text[start + m])
            ) % mod
    return matches


naive_hits = naive_search(PATTERN, TEXT)
rolling_hits = rabin_karp(PATTERN, TEXT)
print(f"naive_search: {naive_hits}")
print(f"rabin_karp  : {rolling_hits}")
print("PASS" if naive_hits == rolling_hits else "FAIL")

# SOLUTION 6.5
print("\n--- Solution 6.5 ---")


def run_length_encode(text):
    """Replace each run of equal characters with char + count."""
    if not text:
        return ""
    parts = []
    current = text[0]
    count = 1
    for char in text[1:]:
        if char == current:
            count += 1
        else:
            parts.append(f"{current}{count}")
            current = char
            count = 1
    parts.append(f"{current}{count}")
    return "".join(parts)


def run_length_decode(encoded):
    """Expand char + count pairs back into the original text."""
    parts = []
    i = 0
    while i < len(encoded):
        char = encoded[i]
        i += 1
        digits = ""
        while i < len(encoded) and encoded[i].isdigit():
            digits += encoded[i]
            i += 1
        parts.append(char * int(digits))
    return "".join(parts)


sample = "aaabccdddd"
encoded = run_length_encode(sample)
decoded = run_length_decode(encoded)
print(f"encode({sample!r}) = {encoded!r}")
print(f"decode({encoded!r}) = {decoded!r}")
print(f"encode('') = {run_length_encode('')!r}, decode('') = {run_length_decode('')!r}")
print("Roundtrip PASS" if decoded == sample and encoded == "a3b1c2d4" else "Roundtrip FAIL")

print("\n" + "=" * 50)
print("Great job! Move on to 07_data_processing.py")
print("=" * 50)
