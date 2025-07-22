"""
Arrays & Hashing + Two Pointers - NeetCode 75
Essential patterns for technical interviews.
"""

def contains_duplicate(nums):
    """LC 217 - Use set for O(n) time"""
    return len(nums) != len(set(nums))

def valid_anagram(s, t):
    """LC 242 - Compare character counts"""
    return sorted(s) == sorted(t)

def two_sum(nums, target):
    """LC 1 - Hash map for O(n) time"""
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

def group_anagrams(strs):
    """LC 49 - Group by sorted string"""
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        groups.setdefault(key, []).append(s)
    return list(groups.values())

def top_k_frequent(nums, k):
    """LC 347 - Counter + heap"""
    from collections import Counter
    return [num for num, _ in Counter(nums).most_common(k)]

def product_except_self(nums):
    """LC 238 - Prefix and suffix products"""
    n = len(nums)
    result = [1] * n
    
    # Prefix products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Suffix products
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

def valid_sudoku(board):
    """LC 36 - Check rows, cols, boxes"""
    seen = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                row = f"row{i}{board[i][j]}"
                col = f"col{j}{board[i][j]}"
                box = f"box{i//3}{j//3}{board[i][j]}"
                if row in seen or col in seen or box in seen:
                    return False
                seen.update([row, col, box])
    return True

def longest_consecutive(nums):
    """LC 128 - Check sequence starts"""
    num_set = set(nums)
    max_len = 0
    
    for num in num_set:
        if num - 1 not in num_set:  # Start of sequence
            curr_len = 1
            while num + curr_len in num_set:
                curr_len += 1
            max_len = max(max_len, curr_len)
    
    return max_len

def three_sum(nums):
    """LC 15 - Sort + two pointers"""
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

def container_with_most_water(height):
    """LC 11 - Two pointers from ends"""
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

def trapping_rain_water(height):
    """LC 42 - Two pointers with max tracking"""
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water

def valid_palindrome(s):
    """LC 125 - Two pointers with alphanumeric check"""
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

# ============================================================================
# ADDITIONAL PATTERNS
# ============================================================================

def two_sum_sorted(numbers, target):
    """LC 167 - Two pointers on sorted array"""
    left, right = 0, len(numbers) - 1
    
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
    
    return []

def is_subsequence(s, t):
    """LC 392 - Two pointers for subsequence"""
    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    return i == len(s)

def move_zeroes(nums):
    """LC 283 - Two pointers for in-place"""
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Quick tests for key problems
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("Valid Anagram:", valid_anagram("anagram", "nagaram"))
    print("Three Sum:", three_sum([-1, 0, 1, 2, -1, -4]))
    print("Container Water:", container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print("Trapping Water:", trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) 