"""
Sliding Window - NeetCode 75
Essential patterns for technical interviews.
"""

def longest_substring_no_repeat(s):
    """LC 3 - Sliding window with set"""
    seen = set()
    left = max_len = 0
    
    for right, char in enumerate(s):
        while char in seen:
            seen.remove(s[left])
            left += 1
        seen.add(char)
        max_len = max(max_len, right - left + 1)
    
    return max_len

def character_replacement(s, k):
    """LC 424 - Sliding window with char count"""
    count = {}
    left = max_freq = max_len = 0
    
    for right, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
        max_freq = max(max_freq, count[char])
        
        if right - left + 1 - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

def check_inclusion(s1, s2):
    """LC 567 - Sliding window with char count"""
    if len(s1) > len(s2):
        return False
    
    count1 = [0] * 26
    count2 = [0] * 26
    
    for char in s1:
        count1[ord(char) - ord('a')] += 1
    
    for i in range(len(s2)):
        count2[ord(s2[i]) - ord('a')] += 1
        
        if i >= len(s1):
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        
        if count1 == count2:
            return True
    
    return False

def min_window(s, t):
    """LC 76 - Sliding window with char count"""
    if not t or not s:
        return ""
    
    count_t = {}
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    required = len(count_t)
    formed = 0
    window_count = {}
    
    left = 0
    min_len = float('inf')
    result = ""
    
    for right, char in enumerate(s):
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in count_t and window_count[char] == count_t[char]:
            formed += 1
        
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            
            window_count[s[left]] -= 1
            if s[left] in count_t and window_count[s[left]] < count_t[s[left]]:
                formed -= 1
            left += 1
    
    return result

def max_sliding_window(nums, k):
    """LC 239 - Monotonic deque"""
    from collections import deque
    
    dq = deque()
    result = []
    
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        if dq[0] == i - k:
            dq.popleft()
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

def find_anagrams(s, p):
    """LC 438 - Sliding window with char count"""
    if len(p) > len(s):
        return []
    
    count_p = [0] * 26
    count_s = [0] * 26
    
    for char in p:
        count_p[ord(char) - ord('a')] += 1
    
    result = []
    for i in range(len(s)):
        count_s[ord(s[i]) - ord('a')] += 1
        
        if i >= len(p):
            count_s[ord(s[i - len(p)]) - ord('a')] -= 1
        
        if count_s == count_p:
            result.append(i - len(p) + 1)
    
    return result

# ============================================================================
# ADDITIONAL PATTERNS
# ============================================================================

def max_sum_subarray_fixed(nums, k):
    """Fixed size sliding window"""
    if len(nums) < k:
        return 0
    
    curr_sum = sum(nums[:k])
    max_sum = curr_sum
    
    for i in range(k, len(nums)):
        curr_sum = curr_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

def min_subarray_sum(nums, target):
    """Variable size sliding window"""
    left = curr_sum = 0
    min_len = float('inf')
    
    for right, num in enumerate(nums):
        curr_sum += num
        
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

def max_consecutive_ones_iii(nums, k):
    """Flip k zeros to get max consecutive ones"""
    left = zeros = max_len = 0
    
    for right, num in enumerate(nums):
        if num == 0:
            zeros += 1
        
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Quick tests for key problems
    print("Longest Substring:", longest_substring_no_repeat("abcabcbb"))
    print("Character Replacement:", character_replacement("AABABBA", 1))
    print("Check Inclusion:", check_inclusion("ab", "eidbaooo"))
    print("Min Window:", min_window("ADOBECODEBANC", "ABC"))
    print("Max Sliding Window:", max_sliding_window([1,3,-1,-3,5,3,6,7], 3)) 