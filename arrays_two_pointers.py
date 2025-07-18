"""
Arrays & Two Pointers Technique

Two pointers is a technique where we use two pointers to traverse an array
from different positions or directions. Common patterns:
- One pointer at start, one at end (palindrome, sorted array problems)
- Both pointers at start (sliding window, remove duplicates)
- Fast and slow pointers (cycle detection, find middle)

Time Complexity: Usually O(n) - we traverse the array once
Space Complexity: Usually O(1) - we only use a few extra variables
"""

def two_sum_sorted(nums, target):
    """
    Two Sum II - Input Array Is Sorted (LeetCode 167)
    Given a sorted array, find two numbers that add up to target.
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

def remove_duplicates_sorted(nums):
    """
    Remove Duplicates from Sorted Array (LeetCode 26)
    Remove duplicates in-place, return new length.
    """
    if not nums:
        return 0
    
    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    
    return write_index

def valid_palindrome(s):
    """
    Valid Palindrome (LeetCode 125)
    Check if string is palindrome, ignoring non-alphanumeric chars.
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == "__main__":
    # Test Two Sum Sorted
    print("=== Two Sum Sorted ===")
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Array: {nums1}, Target: {target1}")
    print(f"Result: {two_sum_sorted(nums1, target1)}")  # [1, 2]
    
    # Test Remove Duplicates
    print("\n=== Remove Duplicates ===")
    nums2 = [1, 1, 2, 2, 3, 4, 4, 5]
    print(f"Original: {nums2}")
    new_length = remove_duplicates_sorted(nums2)
    print(f"New length: {new_length}")
    print(f"Modified array: {nums2[:new_length]}")
    
    # Test Valid Palindrome
    print("\n=== Valid Palindrome ===")
    test_strings = ["A man, a plan, a canal: Panama", "race a car", "Was it a car or a cat I saw?"]
    for s in test_strings:
        result = valid_palindrome(s)
        print(f"'{s}' -> {result}") 