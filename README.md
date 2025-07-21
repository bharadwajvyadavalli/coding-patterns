# Coding Patterns
A comprehensive collection of Python boilerplate code for fundamental coding patterns and techniques. Each file contains clear examples and implementations of common algorithms and data structures used in competitive programming and technical interviews.

## 📁 File Structure
```
coding-patterns/
├── arrays_two_pointers.py      # Two pointers technique
├── sliding_window.py           # Sliding window technique  
├── binary_search.py            # Binary search variations
├── dfs_backtracking.py         # DFS and backtracking
├── bfs_queue.py                # BFS and queue operations
├── linked_list_basics.py       # Linked list operations
├── stack_monotonic.py          # Stack and monotonic stack
├── dynamic_programming_basics.py # Dynamic programming patterns
├── graph_union_find.py         # Graph and union-find
├── heap_priority_queue.py      # Heap and priority queue
└── README.md                   # This file
```

## 📊 Common DSA Concepts & Complexity Reference

| Technique | Key Concepts | Typical Time Complexity | Typical Space Complexity |
|---|---|---|---|
| **Two Pointers** | Linear scanning from both ends, meeting in middle, fast/slow pointers | O(n) | O(1) |
| **Sliding Window** | Fixed/variable window optimization, substring/subarray problems | O(n) | O(k) where k is window size or alphabet |
| **Binary Search** | Divide and conquer on sorted data, finding boundaries, search space reduction | O(log n) | O(1) iterative, O(log n) recursive |
| **Depth-First Search (DFS)** | Tree/graph traversal, backtracking, exploring all paths | O(V + E) for graphs, O(n) for trees | O(h) where h is max depth |
| **Backtracking** | Constraint satisfaction, generating permutations/combinations, pruning search space | O(b^d) where b is branching factor, d is depth | O(d) for recursion stack |
| **Breadth-First Search (BFS)** | Level-order traversal, shortest path in unweighted graphs, minimum steps | O(V + E) for graphs, O(n) for trees | O(w) where w is maximum width |
| **Dynamic Programming** | Optimal substructure, overlapping subproblems, memoization/tabulation | O(n*m) typical for 2D problems | O(n*m) for 2D table, O(n) optimized |
| **Greedy Algorithms** | Local optimal choices, activity selection, interval scheduling | O(n log n) with sorting | O(1) to O(n) |
| **Union-Find (Disjoint Set)** | Connected components, cycle detection, minimum spanning tree | O(α(n)) amortized per operation | O(n) for parent array |
| **Heap/Priority Queue** | Top-k problems, merge operations, scheduling | O(log n) insert/delete, O(1) peek | O(n) for heap storage |
| **Trie (Prefix Tree)** | String prefix matching, autocomplete, word games | O(m) where m is string length | O(ALPHABET_SIZE * N * M) worst case |
| **Segment Tree** | Range queries, range updates, lazy propagation | O(log n) query/update | O(n) for tree storage |
| **Binary Indexed Tree** | Prefix sum queries, range sum updates, frequency counting | O(log n) query/update | O(n) for tree storage |
| **Graph Algorithms** | Shortest path (Dijkstra, Floyd-Warshall), MST (Kruskal, Prim) | O(V log V + E) to O(V³) | O(V) to O(V²) |
| **String Algorithms** | Pattern matching (KMP, Rabin-Karp), longest common subsequence | O(n + m) to O(n*m) | O(m) for pattern, O(n*m) for DP |

