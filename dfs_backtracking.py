"""
DFS (Depth-First Search) & Backtracking

DFS explores as far as possible along each branch before backtracking.
Backtracking is a systematic way to iterate through all possible configurations
of a search space. Common applications:
- Tree/graph traversal
- Permutations and combinations
- Path finding
- Constraint satisfaction problems

Time Complexity: Varies by problem, often exponential for backtracking
Space Complexity: O(depth) for recursion stack
"""

def dfs_tree_traversal(root):
    """
    DFS Tree Traversal (Inorder, Preorder, Postorder)
    """
    def inorder(node, result):
        if node:
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)
    
    def preorder(node, result):
        if node:
            result.append(node.val)
            preorder(node.left, result)
            preorder(node.right, result)
    
    def postorder(node, result):
        if node:
            postorder(node.left, result)
            postorder(node.right, result)
            result.append(node.val)
    
    inorder_result = []
    preorder_result = []
    postorder_result = []
    
    inorder(root, inorder_result)
    preorder(root, preorder_result)
    postorder(root, postorder_result)
    
    return inorder_result, preorder_result, postorder_result

def generate_permutations(nums):
    """
    Permutations (LeetCode 46)
    Generate all possible permutations of distinct integers.
    """
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # backtrack
    
    result = []
    backtrack(0)
    return result

def generate_combinations(n, k):
    """
    Combinations (LeetCode 77)
    Generate all possible combinations of k numbers from 1 to n.
    """
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()  # backtrack
    
    result = []
    backtrack(1, [])
    return result

def n_queens(n):
    """
    N-Queens (LeetCode 51)
    Place n queens on n×n chessboard so no two queens threaten each other.
    """
    def is_safe(row, col, queens):
        for r, c in queens:
            if r == row or c == col or abs(r - row) == abs(c - col):
                return False
        return True
    
    def backtrack(row, queens):
        if row == n:
            result.append(queens[:])
            return
        
        for col in range(n):
            if is_safe(row, col, queens):
                queens.append((row, col))
                backtrack(row + 1, queens)
                queens.pop()  # backtrack
    
    result = []
    backtrack(0, [])
    return result

def word_search(board, word):
    """
    Word Search (LeetCode 79)
    Check if word exists in 2D board by connecting adjacent letters.
    """
    def dfs(row, col, word_index):
        if word_index == len(word):
            return True
        
        if (row < 0 or row >= len(board) or 
            col < 0 or col >= len(board[0]) or 
            board[row][col] != word[word_index]):
            return False
        
        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Try all 4 directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            if dfs(row + dr, col + dc, word_index + 1):
                return True
        
        # Backtrack
        board[row][col] = temp
        return False
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(row, col, 0):
                return True
    
    return False

if __name__ == "__main__":
    # Test Permutations
    print("=== Permutations ===")
    nums1 = [1, 2, 3]
    perms = generate_permutations(nums1)
    print(f"Permutations of {nums1}:")
    for perm in perms:
        print(perm)
    
    # Test Combinations
    print("\n=== Combinations ===")
    n, k = 4, 2
    combs = generate_combinations(n, k)
    print(f"Combinations of {k} numbers from 1 to {n}:")
    for comb in combs:
        print(comb)
    
    # Test N-Queens (small example)
    print("\n=== N-Queens ===")
    n_queens_result = n_queens(4)
    print(f"Number of solutions for 4-queens: {len(n_queens_result)}")
    print("First solution positions:", n_queens_result[0] if n_queens_result else [])
    
    # Test Word Search
    print("\n=== Word Search ===")
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    words = ["ABCCED", "SEE", "ABCB"]
    for word in words:
        result = word_search(board, word)
        print(f"Word '{word}' found: {result}") 