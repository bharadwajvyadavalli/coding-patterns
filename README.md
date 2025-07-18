# LeetCode Boilerplate Code

A comprehensive collection of Python boilerplate code for fundamental LeetCode concepts and techniques. Each file contains clear examples and implementations of common algorithms and data structures.

## 📁 File Structure

```
leetcode-problems/
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

## 📊 Common DSA Problems & Complexity Reference

| Problem Category/Technique | Common Problems | Optimal Time Complexity | Optimal Space Complexity |
|---|---|---|---|
| **Arrays & Two Pointers** | Two Sum (sorted array) | O(n) | O(1) |
| | Remove Duplicates from Sorted Array | O(n) | O(1) |
| | Valid Palindrome | O(n) | O(1) |
| **Sliding Window** | Max Sum Subarray of Fixed Size | O(n) | O(1) |
| | Longest Substring Without Repeating Characters | O(n) | O(k) or O(1) (for fixed alphabet size) |
| | Minimum Window Substring | O(N+M) where N is text length, M is pattern length | O(K) where K is alphabet size |
| **Binary Search** | Standard Binary Search | O(log n) | O(1) |
| | Find First/Last Occurrence | O(log n) | O(1) |
| | Search in Rotated Sorted Array | O(log n) | O(1) |
| **DFS & Backtracking** | Permutations | O(N!) | O(N) (for recursion stack) |
| | Combinations | O(N! / (K! * (N-K)!)) | O(K) (for current combination) |
| | N-Queens | O(N!) | O(N) (for board and recursion stack) |
| | Word Search | O(Rows * Cols * 3^L) where L is word length | O(L) (for recursion stack) |
| **BFS & Queue** | Level Order Tree Traversal | O(N) | O(W) (max width of tree) |
| | Shortest Path in Unweighted Graph | O(V + E) | O(V) |
| | Number of Islands | O(Rows * Cols) | O(Rows * Cols) (for queue/visited set) |
| **Linked List Basics** | Reverse Linked List | O(n) | O(1) |
| | Detect Cycle (Floyd's) | O(n) | O(1) |
| | Merge Two Sorted Lists | O(m+n) | O(1) |
| **Stack & Monotonic Stack** | Valid Parentheses | O(n) | O(n) |
| | Next Greater Element | O(n) | O(n) |
| | Largest Rectangle in Histogram | O(n) | O(n) |
| **Dynamic Programming** | Fibonacci Sequence | O(n) (iterative) | O(1) (iterative) |
| | Climbing Stairs | O(n) | O(1) |
| | Longest Common Subsequence | O(m*n) | O(m*n) or O(min(m,n)) |
| | Coin Change | O(amount * number_of_coins) | O(amount) |
| **Graph & Union-Find** | Union-Find Operations | O(α(n)) (amortized inverse Ackermann function) | O(n) |
| | Number of Connected Components | O(V + E) | O(V) |
| | Kruskal's Algorithm (MST) | O(E log E) or O(E log V) | O(V + E) |
| **Heap & Priority Queue** | Kth Largest Element | O(N log K) | O(K) |
| | Top K Frequent Elements | O(N log K) | O(K) |
| | Merge K Sorted Lists | O(N log K) where N is total elements, K is number of lists | O(K) |

**Notes:**
- `n` = array/string length, `N` = total elements, `K` = parameter value
- `V` = vertices, `E` = edges, `W` = tree width, `L` = word length
- `α(n)` = inverse Ackermann function (very slow growing)
- This table provides general complexity guidelines for common interview problems

## 🚀 Quick Start

Each file can be run independently to see examples in action:

```bash
python arrays_two_pointers.py
python sliding_window.py
python binary_search.py
# ... etc
```

## 📚 Concepts Covered

### 1. **Arrays & Two Pointers** (`arrays_two_pointers.py`)
- Two Sum II (sorted array)
- Remove duplicates from sorted array
- Valid palindrome
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### 2. **Sliding Window** (`sliding_window.py`)
- Fixed size window (max sum subarray)
- Variable size window (min subarray sum)
- Longest substring without repeating characters
- Max consecutive ones III
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) or O(k)

### 3. **Binary Search** (`binary_search.py`)
- Standard binary search
- First/last occurrence
- Insert position
- Square root calculation
- Rotated array search
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

### 4. **DFS & Backtracking** (`dfs_backtracking.py`)
- Tree traversal (inorder, preorder, postorder)
- Permutations and combinations
- N-Queens problem
- Word search
- **Time Complexity**: Varies (often exponential)
- **Space Complexity**: O(depth)

### 5. **BFS & Queue** (`bfs_queue.py`)
- Level-order tree traversal
- Shortest path in binary matrix
- Number of islands
- Rotting oranges
- Word ladder
- **Time Complexity**: O(V + E) for graphs
- **Space Complexity**: O(w) where w is max width

### 6. **Linked List Basics** (`linked_list_basics.py`)
- Reverse linked list
- Cycle detection (Floyd's algorithm)
- Find middle node
- Merge sorted lists
- Add two numbers
- Palindrome check
- **Time Complexity**: O(n) for traversal
- **Space Complexity**: O(1)

### 7. **Stack & Monotonic Stack** (`stack_monotonic.py`)
- Valid parentheses
- Next greater element
- Daily temperatures
- Largest rectangle in histogram
- Evaluate RPN
- Min stack implementation
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

### 8. **Dynamic Programming** (`dynamic_programming_basics.py`)
- Fibonacci sequence
- Climbing stairs
- House robber
- Longest common subsequence
- Coin change
- Edit distance
- **Time Complexity**: Varies by problem
- **Space Complexity**: O(n) or O(n²)

### 9. **Graph & Union-Find** (`graph_union_find.py`)
- Union-Find data structure
- Number of provinces
- Redundant connection
- Graph valid tree
- Accounts merge
- Minimum spanning tree (Kruskal's)
- **Time Complexity**: O(α(n)) for union-find
- **Space Complexity**: O(n)

### 10. **Heap & Priority Queue** (`heap_priority_queue.py`)
- Kth largest element
- Top K frequent elements
- Merge K sorted lists
- Median finder
- K closest points
- Last stone weight
- **Time Complexity**: O(log n) for insert/delete
- **Space Complexity**: O(n)

## 🎯 Usage Examples

### Running Individual Files
```bash
# Test two pointers technique
python arrays_two_pointers.py

# Test sliding window
python sliding_window.py

# Test binary search
python binary_search.py
```

### Using Functions in Your Code
```python
from arrays_two_pointers import two_sum_sorted, remove_duplicates_sorted

# Use the functions
nums = [2, 7, 11, 15]
result = two_sum_sorted(nums, 9)  # [1, 2]
```

## 🔧 Key Features

- **Clean, readable code** with clear comments
- **Comprehensive examples** for each technique
- **Test cases** included in each file
- **Time and space complexity** documented
- **LeetCode problem references** for context
- **Modular design** for easy integration

## 📖 Learning Path

1. Start with **Arrays & Two Pointers** for basic array manipulation
2. Move to **Sliding Window** for subarray problems
3. Learn **Binary Search** for efficient searching
4. Explore **DFS & Backtracking** for recursive problems
5. Study **BFS & Queue** for level-wise traversal
6. Master **Linked List** operations
7. Understand **Stack** applications
8. Dive into **Dynamic Programming** patterns
9. Learn **Graph & Union-Find** for connectivity problems
10. Finish with **Heap & Priority Queue** for optimization

## 🤝 Contributing

Feel free to add more examples, improve existing code, or add new techniques. Each file should:
- Include clear docstrings
- Have working examples
- Include test cases
- Document time/space complexity

## 📝 Notes

- All code is written in Python 3
- Uses standard library only (no external dependencies)
- Functions are designed to be easily adaptable for LeetCode problems
- Test cases demonstrate typical usage patterns

## 🎓 Resources

- [LeetCode](https://leetcode.com/) - Practice problems
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - Algorithm tutorials
- [CLRS](https://en.wikipedia.org/wiki/Introduction_to_Algorithms) - Algorithm textbook

---

Happy coding! 🚀