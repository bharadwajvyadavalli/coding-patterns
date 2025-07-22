"""
Dynamic Programming Basics - LeetCode 75
Essential patterns for technical interviews.
"""

def fibonacci_dp(n):
    """LC 509 - Calculate nth Fibonacci number using DP"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def climbing_stairs(n):
    """LC 70 - Find number of ways to climb n stairs"""
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def house_robber(nums):
    """LC 198 - Find maximum money that can be robbed"""
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

def house_robber_ii(nums):
    """LC 213 - House robber with circular arrangement"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Rob first house to second-to-last, or second house to last
    return max(house_robber(nums[:-1]), house_robber(nums[1:]))

def longest_common_subsequence(text1, text2):
    """LC 1143 - Find length of longest common subsequence"""
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
    """LC 322 - Find minimum number of coins needed"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_ii(amount, coins):
    """LC 518 - Find number of combinations to make amount"""
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]

def unique_paths(m, n):
    """LC 62 - Find number of unique paths from top-left to bottom-right"""
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]

def unique_paths_ii(obstacle_grid):
    """LC 63 - Unique paths with obstacles"""
    if not obstacle_grid or obstacle_grid[0][0] == 1:
        return 0
    
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if obstacle_grid[i][j] == 1:
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    
    return dp[m - 1][n - 1]

def longest_increasing_subsequence(nums):
    """LC 300 - Find length of longest increasing subsequence"""
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def partition_equal_subset_sum(nums):
    """LC 416 - Check if array can be partitioned into two equal subsets"""
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

def word_break(s, word_dict):
    """LC 139 - Check if string can be segmented into dictionary words"""
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]

def word_break_ii(s, word_dict):
    """LC 140 - Return all possible word break combinations"""
    word_set = set(word_dict)
    
    def backtrack(start):
        if start == len(s):
            return [""]
        
        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                for sentence in backtrack(end):
                    if sentence:
                        result.append(word + " " + sentence)
                    else:
                        result.append(word)
        
        return result
    
    return backtrack(0)

def combination_sum_iv(nums, target):
    """LC 377 - Find number of combinations that add up to target"""
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    
    return dp[target]

def decode_ways(s):
    """LC 91 - Number of ways to decode a string"""
    if not s or s[0] == '0':
        return 0
    
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, len(s) + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[len(s)]

def palindromic_substrings(s):
    """LC 647 - Count number of palindromic substrings"""
    def count_palindromes(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    total = 0
    for i in range(len(s)):
        total += count_palindromes(i, i)  # Odd length
        total += count_palindromes(i, i + 1)  # Even length
    
    return total

def longest_palindromic_substring(s):
    """LC 5 - Find longest palindromic substring"""
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        palindrome = expand_around_center(i, i)
        if len(palindrome) > len(longest):
            longest = palindrome
        
        # Even length palindromes
        palindrome = expand_around_center(i, i + 1)
        if len(palindrome) > len(longest):
            longest = palindrome
    
    return longest

def edit_distance(word1, word2):
    """LC 72 - Minimum number of operations to convert word1 to word2"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

def burst_balloons(nums):
    """LC 312 - Maximum coins from bursting balloons"""
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], 
                                    nums[left] * nums[i] * nums[right] + 
                                    dp[left][i] + dp[i][right])
    
    return dp[0][n - 1]

def perfect_squares(n):
    """LC 279 - Minimum number of perfect squares that sum to n"""
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    
    return dp[n]

# Test cases
if __name__ == "__main__":
    # Test house_robber
    print(house_robber([1,2,3,1]))  # 4
    
    # Test word_break
    print(word_break("leetcode", ["leet", "code"]))  # True
    
    # Test longest_increasing_subsequence
    print(longest_increasing_subsequence([10,9,2,5,3,7,101,18]))  # 4 