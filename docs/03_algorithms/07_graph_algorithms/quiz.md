# 🧠 Graph Algorithms Quiz

Test your understanding of graph algorithms!

---

## Question 1

**What data structure does BFS use?**

- A) Stack
- B) Queue
- C) Heap
- D) Array

<details>
<summary>Show Answer</summary>

**B) Queue**

BFS uses a queue (FIFO) to explore nodes level by level. Nodes are added to the back and removed from the front, ensuring we visit all nodes at distance k before any node at distance k+1.

</details>

---

## Question 2

**What data structure does DFS use?**

- A) Queue
- B) Heap
- C) Stack (or recursion)
- D) Hash table

<details>
<summary>Show Answer</summary>

**C) Stack (or recursion)**

DFS uses a stack (LIFO) or the implicit call stack through recursion. This allows it to go as deep as possible before backtracking.

</details>

---

## Question 3

**What is the time complexity of BFS and DFS?**

- A) O(V)
- B) O(E)
- C) O(V + E)
- D) O(V × E)

<details>
<summary>Show Answer</summary>

**C) O(V + E)**

Both BFS and DFS visit each vertex once (O(V)) and examine each edge once (O(E)), giving O(V + E) total time complexity.

</details>

---

## Question 4

**Which algorithm finds the shortest path in an unweighted graph?**

- A) DFS
- B) BFS
- C) Dijkstra
- D) Bellman-Ford

<details>
<summary>Show Answer</summary>

**B) BFS**

BFS naturally finds the shortest path in unweighted graphs because it explores nodes level by level. The first time we reach a node, we've found the shortest path to it.

</details>

---

## Question 5

**Dijkstra's algorithm does NOT work correctly with:**

- A) Directed graphs
- B) Undirected graphs
- C) Negative edge weights
- D) Sparse graphs

<details>
<summary>Show Answer</summary>

**C) Negative edge weights**

Dijkstra's greedy approach assumes that once a node is visited, its shortest distance is final. Negative edges can violate this assumption. Use Bellman-Ford for graphs with negative edges.

</details>

---

## Question 6

**What is the time complexity of Dijkstra's algorithm with a min-heap?**

- A) O(V²)
- B) O(V + E)
- C) O((V + E) log V)
- D) O(V × E)

<details>
<summary>Show Answer</summary>

**C) O((V + E) log V)**

With a min-heap:
- Each vertex is extracted once: O(V log V)
- Each edge may cause a decrease-key: O(E log V)
- Total: O((V + E) log V)

</details>

---

## Question 7

**Which algorithm can detect negative cycles?**

- A) BFS
- B) Dijkstra
- C) Bellman-Ford
- D) Prim's

<details>
<summary>Show Answer</summary>

**C) Bellman-Ford**

Bellman-Ford runs V-1 relaxation passes. If any edge can still be relaxed after V-1 passes, a negative cycle exists. Dijkstra cannot detect negative cycles.

</details>

---

## Question 8

**What is the time complexity of Floyd-Warshall algorithm?**

- A) O(V²)
- B) O(V³)
- C) O(V × E)
- D) O(E log V)

<details>
<summary>Show Answer</summary>

**B) O(V³)**

Floyd-Warshall uses three nested loops over all vertices to compute all-pairs shortest paths, giving O(V³) time complexity.

</details>

---

## Question 9

**A topological sort is only possible for:**

- A) Undirected graphs
- B) Directed Acyclic Graphs (DAGs)
- C) Weighted graphs
- D) Connected graphs

<details>
<summary>Show Answer</summary>

**B) Directed Acyclic Graphs (DAGs)**

Topological sort orders vertices so that for every edge u→v, u comes before v. This is only possible if there are no cycles (otherwise, which comes first in a cycle?).

</details>

---

## Question 10

**In cycle detection for undirected graphs using DFS, a cycle is detected when:**

- A) We visit a node twice
- B) We find a back edge to a visited node that isn't the parent
- C) The stack overflows
- D) We can't find any more neighbors

<details>
<summary>Show Answer</summary>

**B) We find a back edge to a visited node that isn't the parent**

In undirected graphs, we track the parent to avoid false positives (A-B-A is not a cycle). A cycle exists when we find an edge to a visited node that isn't our immediate parent.

</details>

---

## Question 11

**What colors are used in the 3-color DFS cycle detection for directed graphs?**

- A) Red, Green, Blue
- B) White, Gray, Black
- C) Start, Middle, End
- D) Unvisited, Visited, Done

<details>
<summary>Show Answer</summary>

**B) White, Gray, Black**

- **White**: Not yet visited
- **Gray**: Currently being processed (in the current DFS path)
- **Black**: Completely processed

A cycle exists if we encounter a Gray node (back edge in current path).

</details>

---

## Question 12

**Prim's and Kruskal's algorithms are used for:**

- A) Shortest path
- B) Minimum Spanning Tree
- C) Topological sort
- D) Cycle detection

<details>
<summary>Show Answer</summary>

**B) Minimum Spanning Tree**

Both algorithms find a Minimum Spanning Tree (MST) - a subset of edges that connects all vertices with minimum total weight and no cycles.

</details>

---

## Question 13

**What data structure does Kruskal's algorithm use to detect cycles?**

- A) Stack
- B) Queue
- C) Union-Find (Disjoint Set)
- D) Hash table

<details>
<summary>Show Answer</summary>

**C) Union-Find (Disjoint Set)**

Kruskal's sorts edges by weight and adds them if they don't create a cycle. Union-Find efficiently checks if two vertices are already connected (same component).

</details>

---

## Question 14

**A graph is bipartite if and only if:**

- A) It has no cycles
- B) It has no odd-length cycles
- C) It is connected
- D) It has an even number of vertices

<details>
<summary>Show Answer</summary>

**B) It has no odd-length cycles**

A graph is bipartite (2-colorable) if and only if it contains no odd-length cycles. We can check this using BFS/DFS by trying to 2-color the graph.

</details>

---

## Question 15

**Which statement about BFS vs DFS is FALSE?**

- A) BFS uses more memory for wide graphs
- B) DFS uses more memory for deep graphs
- C) BFS always finds the shortest path
- D) DFS can be implemented recursively

<details>
<summary>Show Answer</summary>

**C) BFS always finds the shortest path**

BFS finds the shortest path only in **unweighted** graphs. For weighted graphs, you need Dijkstra's or Bellman-Ford. The other statements are true.

</details>

---

## 🏆 Score Guide

| Score | Rating |
|-------|--------|
| 13-15 | ⭐⭐⭐⭐⭐ Graph Master! |
| 10-12 | ⭐⭐⭐⭐ Great understanding! |
| 7-9 | ⭐⭐⭐ Good progress! |
| 4-6 | ⭐⭐ Review the concepts |
| 0-3 | ⭐ Start with the basics |

---

## 📚 Review Topics

If you struggled with certain questions, review these topics:

- **Questions 1-4**: BFS and DFS fundamentals
- **Questions 5-8**: Shortest path algorithms
- **Questions 9-11**: Topological sort and cycle detection
- **Questions 12-13**: Minimum Spanning Tree
- **Questions 14-15**: Graph properties and comparisons
