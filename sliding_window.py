"""
Sliding Window Technique

Sliding window is a technique where we maintain a subset of elements (window)
and slide it through the array/string to solve problems efficiently.
Common patterns:
- Fixed size window (find max/min in each window)
- Variable size window (find smallest/largest subarray with condition)
- Two pointers expanding/contracting window

Time Complexity: Usually O(n) - each element visited at most twice
Space Complexity: Usually O(1) or O(k) where k is window size
"""

def max_sum_subarray_fixed(nums, k):
    """
    Maximum Sum Subarray of Size K (Fixed Window)
    Find maximum sum of subarray with exactly k elements.
    """
    if len(nums) < k:
        return 0
    
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide window and update max
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

def min_subarray_sum(nums, target):
    """
    Minimum Size Subarray Sum (LeetCode 209)
    Find smallest subarray with sum >= target.
    """
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # Shrink window while sum >= target
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

def longest_substring_no_repeat(s):
    """
    Longest Substring Without Repeating Characters (LeetCode 3)
    Find length of longest substring without repeating characters.
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character already in window, shrink from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

def max_consecutive_ones_iii(nums, k):
    """
    Max Consecutive Ones III (LeetCode 1004)
    Find longest sequence of 1s after flipping at most k 0s.
    """
    left = 0
    zeros_count = 0
    max_length = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros_count += 1
        
        # Shrink window if too many zeros
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

if __name__ == "__main__":
    # Test Fixed Size Window
    print("=== Fixed Size Window ===")
    nums1 = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k1 = 4
    print(f"Array: {nums1}, Window size: {k1}")
    print(f"Max sum: {max_sum_subarray_fixed(nums1, k1)}")  # 24
    
    # Test Variable Size Window - Min Subarray Sum
    print("\n=== Variable Size Window - Min Subarray Sum ===")
    nums2 = [2, 3, 1, 2, 4, 3]
    target2 = 7
    print(f"Array: {nums2}, Target: {target2}")
    print(f"Min length: {min_subarray_sum(nums2, target2)}")  # 2
    
    # Test Longest Substring No Repeat
    print("\n=== Longest Substring No Repeat ===")
    test_strings = ["abcabcbb", "bbbbb", "pwwkew"]
    for s in test_strings:
        result = longest_substring_no_repeat(s)
        print(f"'{s}' -> {result}")
    
    # Test Max Consecutive Ones III
    print("\n=== Max Consecutive Ones III ===")
    nums3 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k3 = 2
    print(f"Array: {nums3}, K: {k3}")
    print(f"Max consecutive ones: {max_consecutive_ones_iii(nums3, k3)}")  # 6 