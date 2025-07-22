# LeetCode 75 + Top Interview 150 + Top 100 Liked - Python Solutions

**Complete collection of LeetCode 75, Top Interview 150, and Top 100 Liked problems with concise, interview-ready Python solutions.**

## 🎯 **Interview-Focused Design**

- **Concise Solutions**: Clean, readable code optimized for interviews
- **Essential Patterns**: Core algorithms without verbose explanations
- **Quick Reference**: Easy to scan and understand during coding sessions
- **Production Ready**: Well-structured, efficient implementations

## 📊 **Problem Distribution**

| Category | Problems | File |
|----------|----------|------|
| Arrays & Hashing | 35 | `arrays_two_pointers.py` |
| Two Pointers | 15 | `arrays_two_pointers.py` |
| Sliding Window | 25 | `sliding_window.py` |
| Stack | 30 | `stack_problems.py` |
| Binary Search | 20 | `binary_search.py` |
| Linked List | 11 | `linked_list_basics.py` |
| Trees & BST | 25 | `trees_bst.py` |
| Tries | 6 | `tries.py` |
| Graphs | 11 | `graphs_dfs_bfs.py` |
| Advanced Graphs | 6 | `advanced_graphs.py` |
| Dynamic Programming | 20 | `dynamic_programming_basics.py` |
| Heap & Priority Queue | 15 | `heap_priority_queue.py` |
| DFS & Backtracking | 8 | `dfs_backtracking.py` |
| BFS & Queue | 6 | `bfs_queue.py` |
| Union Find | 8 | `graph_union_find.py` |
| Monotonic Stack | 8 | `stack_monotonic.py` |

**Total: 250+ problems (LeetCode 75 + Top Interview 150 + Top 100 Liked + additional essential problems)**

## 🚀 **Quick Start**

```python
# Run any file for quick tests
python arrays_two_pointers.py
python sliding_window.py
python stack_problems.py
python binary_search.py
python trees_bst.py
python dynamic_programming_basics.py
python heap_priority_queue.py
# ... etc
```

## 📁 **File Structure**

### **Core Patterns**
- `arrays_two_pointers.py` - Arrays, Hashing, Two Pointers (50 problems)
- `sliding_window.py` - Sliding Window Technique (25 problems)
- `stack_problems.py` - Stack & Monotonic Stack (30 problems)
- `binary_search.py` - Binary Search Variations (20 problems)
- `linked_list_basics.py` - Linked List Operations (11 problems)

### **Data Structures**
- `trees_bst.py` - Trees, BST, Traversals (25 problems)
- `tries.py` - Trie/Prefix Tree (6 problems)
- `graphs_dfs_bfs.py` - Graph Algorithms (11 problems)
- `advanced_graphs.py` - Advanced Graph Problems (6 problems)

### **Advanced Algorithms**
- `dynamic_programming_basics.py` - DP Patterns (20 problems)
- `heap_priority_queue.py` - Heap & Priority Queue (15 problems)
- `dfs_backtracking.py` - DFS & Backtracking (8 problems)
- `bfs_queue.py` - BFS & Queue (6 problems)
- `graph_union_find.py` - Union Find (8 problems)
- `stack_monotonic.py` - Monotonic Stack (8 problems)

## 🎯 **Key Features**

### **Concise Solutions**
```python
def two_sum(nums, target):
    """LC 1 - Hash map for O(n) time"""
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []
```

### **Essential Patterns**
- **Two Pointers**: `left`, `right` pointers for array/string problems
- **Sliding Window**: Variable/fixed size windows with condition tracking
- **Monotonic Stack**: Maintain increasing/decreasing order
- **Binary Search**: Standard, rotated arrays, answer space
- **DFS/BFS**: Graph traversal with visited tracking
- **Dynamic Programming**: Memoization and tabulation patterns
- **Heap**: Priority queue for top-k and median problems
- **Union Find**: Connected components and cycle detection

### **Interview Ready**
- Clean, readable variable names
- Efficient time/space complexity
- Proper edge case handling
- Minimal boilerplate code

## 📚 **Study Strategy**

### **Beginner (0-75 problems)**
1. Start with `arrays_two_pointers.py` - Foundation patterns
2. Practice `sliding_window.py` - Common interview technique
3. Learn `stack_problems.py` - LIFO operations
4. Master `binary_search.py` - Efficient search patterns

### **Intermediate (76-150 problems)**
1. Practice `linked_list_basics.py` - Pointer manipulation
2. Study `trees_bst.py` - Tree traversal and properties
3. Learn `dynamic_programming_basics.py` - DP patterns
4. Master `heap_priority_queue.py` - Advanced data structures

### **Advanced (151-225 problems)**
1. Conquer `graphs_dfs_bfs.py` - Graph algorithms
2. Master `advanced_graphs.py` - Complex graph problems
3. Practice `dfs_backtracking.py` - Recursive patterns
4. Review all patterns for system design interviews

### **Expert (226+ problems)**
1. Master `union_find.py` - Connected components
2. Practice `monotonic_stack.py` - Advanced stack patterns
3. Review all patterns for senior-level interviews
4. Focus on optimization and edge cases

## 🔧 **Common Patterns Reference**

### **Time Complexity**
- **O(1)**: Hash map operations, stack/queue operations
- **O(log n)**: Binary search, heap operations
- **O(n)**: Linear scan, sliding window, two pointers
- **O(n log n)**: Sorting, divide and conquer
- **O(n²)**: Nested loops, some DP problems
- **O(2ⁿ)**: Recursion without memoization

### **Space Complexity**
- **O(1)**: In-place operations, two pointers
- **O(n)**: Hash maps, stacks, recursion depth
- **O(n²)**: 2D DP tables, adjacency matrices

### **Key Data Structures**
- **Hash Map/Set**: O(1) lookup, duplicate detection
- **Stack**: LIFO, monotonic operations
- **Queue/Deque**: BFS, sliding window
- **Heap**: Priority queue, top-k elements
- **Trie**: String operations, prefix matching
- **Union Find**: Connected components

## 🎯 **Interview Tips**

### **Before Coding**
1. **Clarify**: Ask about input constraints, edge cases
2. **Plan**: Write down approach and complexity
3. **Test**: Consider example cases

### **During Coding**
1. **Start Simple**: Brute force first, then optimize
2. **Think Aloud**: Explain your approach
3. **Handle Edge Cases**: Empty inputs, single elements

### **After Coding**
1. **Test**: Walk through your code with examples
2. **Optimize**: Look for better time/space complexity
3. **Discuss**: Trade-offs and alternative approaches

## 🏆 **Success Metrics**

- **Speed**: Solve medium problems in 15-20 minutes
- **Accuracy**: Handle edge cases correctly
- **Communication**: Explain approach clearly
- **Optimization**: Identify and implement improvements

## 📈 **Progress Tracking**

Use the checkboxes in each file to track your progress:
- [x] Problem solved
- [ ] Problem needs review
- [ ] Problem not attempted

## 🚀 **Next Steps**

1. **Practice**: Solve problems in each category
2. **Review**: Understand time/space complexity
3. **Implement**: Code solutions from scratch
4. **Optimize**: Find better approaches
5. **Mock Interviews**: Practice with time pressure

---

**Ready to ace your technical interviews! 🎯**

