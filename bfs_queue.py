"""
BFS (Breadth-First Search) & Queue

BFS explores all nodes at the current depth before moving to next level.
Uses a queue (FIFO) to process nodes level by level. Common applications:
- Level-order tree traversal
- Shortest path in unweighted graphs
- Web crawling
- Social network connections
- Game state exploration

Time Complexity: O(V + E) for graphs, O(n) for trees
Space Complexity: O(w) where w is maximum width of tree/graph
"""

from collections import deque

def bfs_tree_level_order(root):
    """
    Binary Tree Level Order Traversal (LeetCode 102)
    Return nodes level by level from top to bottom.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

def bfs_shortest_path_binary_matrix(grid):
    """
    Shortest Path in Binary Matrix (LeetCode 1091)
    Find shortest path from top-left to bottom-right in binary matrix.
    """
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    n = len(grid)
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    grid[0][0] = 1  # Mark as visited
    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                  (0, 1), (1, -1), (1, 0), (1, 1)]
    
    while queue:
        row, col, distance = queue.popleft()
        
        if row == n - 1 and col == n - 1:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 0 <= new_col < n and 
                grid[new_row][new_col] == 0):
                grid[new_row][new_col] = 1  # Mark as visited
                queue.append((new_row, new_col, distance + 1))
    
    return -1

def bfs_number_of_islands(grid):
    """
    Number of Islands (LeetCode 200)
    Count number of islands (connected 1s) in 2D grid.
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # Mark as visited
        
        while queue:
            row, col = queue.popleft()
            
            # Check all 4 directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    grid[new_row][new_col] == '1'):
                    grid[new_row][new_col] = '0'
                    queue.append((new_row, new_col))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                bfs(r, c)
                islands += 1
    
    return islands

def bfs_rotting_oranges(grid):
    """
    Rotting Oranges (LeetCode 994)
    Find time for all fresh oranges to rot, or -1 if impossible.
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    # Find all rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    
    if fresh == 0:
        return 0
    
    time = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue and fresh > 0:
        time += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            row, col = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    grid[new_row][new_col] == 1):
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col))
                    fresh -= 1
    
    return time if fresh == 0 else -1

def bfs_word_ladder(begin_word, end_word, word_list):
    """
    Word Ladder (LeetCode 127)
    Find shortest transformation sequence from begin to end word.
    """
    if end_word not in word_list:
        return 0
    
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])
    visited = {begin_word}
    
    while queue:
        word, level = queue.popleft()
        
        if word == end_word:
            return level
        
        # Try changing each character
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, level + 1))
    
    return 0

if __name__ == "__main__":
    # Test Shortest Path in Binary Matrix
    print("=== Shortest Path in Binary Matrix ===")
    grid1 = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    print(f"Shortest path length: {bfs_shortest_path_binary_matrix(grid1)}")
    
    # Test Number of Islands
    print("\n=== Number of Islands ===")
    grid2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    print(f"Number of islands: {bfs_number_of_islands(grid2)}")
    
    # Test Rotting Oranges
    print("\n=== Rotting Oranges ===")
    grid3 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    print(f"Time to rot all oranges: {bfs_rotting_oranges(grid3)}")
    
    # Test Word Ladder
    print("\n=== Word Ladder ===")
    begin = "hit"
    end = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(f"Transformation length: {bfs_word_ladder(begin, end, word_list)}") 