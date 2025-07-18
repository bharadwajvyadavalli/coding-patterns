"""
Dynamic Programming Basics

Dynamic Programming is a method for solving complex problems by breaking them
down into simpler subproblems. Key concepts:
- Optimal substructure: optimal solution contains optimal sub-solutions
- Overlapping subproblems: same subproblems solved multiple times
- Memoization: store results of subproblems to avoid recomputation
- Tabulation: build solution bottom-up using table

Common patterns:
- 1D DP: Fibonacci, climbing stairs, house robber
- 2D DP: Longest common subsequence, edit distance
- Knapsack problems
- Matrix chain multiplication
"""

def fibonacci_dp(n):
    """
    Fibonacci Number (LeetCode 509)
    Calculate nth Fibonacci number using DP.
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def climbing_stairs(n):
    """
    Climbing Stairs (LeetCode 70)
    Find number of ways to climb n stairs (1 or 2 steps at a time).
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def house_robber(nums):
    """
    House Robber (LeetCode 198)
    Find maximum money that can be robbed without alerting adjacent houses.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]

def longest_common_subsequence(text1, text2):
    """
    Longest Common Subsequence (LeetCode 1143)
    Find length of longest common subsequence between two strings.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def coin_change(coins, amount):
    """
    Coin Change (LeetCode 322)
    Find minimum number of coins needed to make up amount.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def edit_distance(word1, word2):
    """
    Edit Distance (LeetCode 72)
    Find minimum operations to convert word1 to word2.
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    
    return dp[m][n]

def unique_paths(m, n):
    """
    Unique Paths (LeetCode 62)
    Find number of unique paths from top-left to bottom-right in m×n grid.
    """
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]

def longest_increasing_subsequence(nums):
    """
    Longest Increasing Subsequence (LeetCode 300)
    Find length of longest strictly increasing subsequence.
    """
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def partition_equal_subset_sum(nums):
    """
    Partition Equal Subset Sum (LeetCode 416)
    Check if array can be partitioned into two subsets with equal sum.
    """
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

if __name__ == "__main__":
    # Test Fibonacci
    print("=== Fibonacci ===")
    for n in [0, 1, 5, 10]:
        result = fibonacci_dp(n)
        print(f"F({n}) = {result}")
    
    # Test Climbing Stairs
    print("\n=== Climbing Stairs ===")
    for n in [1, 2, 3, 4, 5]:
        result = climbing_stairs(n)
        print(f"Ways to climb {n} stairs: {result}")
    
    # Test House Robber
    print("\n=== House Robber ===")
    test_cases = [[1, 2, 3, 1], [2, 7, 9, 3, 1], [1, 2, 3, 4, 5]]
    for nums in test_cases:
        result = house_robber(nums)
        print(f"Houses: {nums} -> Max money: {result}")
    
    # Test Longest Common Subsequence
    print("\n=== Longest Common Subsequence ===")
    test_cases = [("abcde", "ace"), ("abc", "def"), ("abcba", "abcbcba")]
    for text1, text2 in test_cases:
        result = longest_common_subsequence(text1, text2)
        print(f"'{text1}' and '{text2}' -> LCS length: {result}")
    
    # Test Coin Change
    print("\n=== Coin Change ===")
    test_cases = [([1, 2, 5], 11), ([2], 3), ([1], 0)]
    for coins, amount in test_cases:
        result = coin_change(coins, amount)
        print(f"Coins: {coins}, Amount: {amount} -> Min coins: {result}")
    
    # Test Edit Distance
    print("\n=== Edit Distance ===")
    test_cases = [("horse", "ros"), ("intention", "execution")]
    for word1, word2 in test_cases:
        result = edit_distance(word1, word2)
        print(f"'{word1}' to '{word2}' -> Min operations: {result}")
    
    # Test Unique Paths
    print("\n=== Unique Paths ===")
    test_cases = [(3, 7), (3, 2), (7, 3)]
    for m, n in test_cases:
        result = unique_paths(m, n)
        print(f"{m}×{n} grid -> Unique paths: {result}")
    
    # Test Longest Increasing Subsequence
    print("\n=== Longest Increasing Subsequence ===")
    test_cases = [[10, 9, 2, 5, 3, 7, 101, 18], [0, 1, 0, 3, 2, 3]]
    for nums in test_cases:
        result = longest_increasing_subsequence(nums)
        print(f"Array: {nums} -> LIS length: {result}")
    
    # Test Partition Equal Subset Sum
    print("\n=== Partition Equal Subset Sum ===")
    test_cases = [[1, 5, 11, 5], [1, 2, 3, 5], [1, 2, 5]]
    for nums in test_cases:
        result = partition_equal_subset_sum(nums)
        print(f"Array: {nums} -> Can partition: {result}") 