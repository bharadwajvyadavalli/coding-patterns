"""
Binary Search Technique

Binary search is an efficient algorithm for finding elements in sorted arrays.
Key concepts:
- Works only on sorted arrays
- Reduces search space by half in each iteration
- Can find exact value, first occurrence, last occurrence, or insertion point
- Can be applied to answer "yes/no" questions (binary search on answer)

Time Complexity: O(log n) - halves search space each iteration
Space Complexity: O(1) - iterative, O(log n) - recursive
"""

def binary_search_exact(nums, target):
    """
    Standard Binary Search (LeetCode 704)
    Find exact target in sorted array, return index or -1.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_first_occurrence(nums, target):
    """
    Find First and Last Position (LeetCode 34)
    Find first occurrence of target in sorted array.
    """
    left, right = 0, len(nums) - 1
    first_pos = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            first_pos = mid
            right = mid - 1  # Continue searching left half
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return first_pos

def binary_search_insert_position(nums, target):
    """
    Search Insert Position (LeetCode 35)
    Find position where target should be inserted to maintain sorted order.
    """
    left, right = 0, len(nums)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def binary_search_sqrt(x):
    """
    Sqrt(x) (LeetCode 69)
    Find integer square root using binary search.
    """
    if x <= 1:
        return x
    
    left, right = 1, x
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Return floor of sqrt

def binary_search_rotated_array(nums, target):
    """
    Search in Rotated Sorted Array (LeetCode 33)
    Find target in array that was rotated at some pivot.
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

if __name__ == "__main__":
    # Test Standard Binary Search
    print("=== Standard Binary Search ===")
    nums1 = [1, 3, 5, 7, 9, 11, 13, 15]
    targets1 = [7, 10, 1, 15]
    for target in targets1:
        result = binary_search_exact(nums1, target)
        print(f"Target {target}: index {result}")
    
    # Test First Occurrence
    print("\n=== First Occurrence ===")
    nums2 = [1, 2, 2, 2, 3, 4, 4, 5]
    target2 = 2
    print(f"Array: {nums2}, Target: {target2}")
    print(f"First occurrence: {binary_search_first_occurrence(nums2, target2)}")
    
    # Test Insert Position
    print("\n=== Insert Position ===")
    nums3 = [1, 3, 5, 6]
    targets3 = [5, 2, 7, 0]
    for target in targets3:
        pos = binary_search_insert_position(nums3, target)
        print(f"Insert {target} at position {pos}")
    
    # Test Square Root
    print("\n=== Square Root ===")
    test_numbers = [4, 8, 16, 25]
    for num in test_numbers:
        sqrt_val = binary_search_sqrt(num)
        print(f"sqrt({num}) = {sqrt_val}")
    
    # Test Rotated Array Search
    print("\n=== Rotated Array Search ===")
    nums4 = [4, 5, 6, 7, 0, 1, 2]
    targets4 = [0, 3, 5]
    for target in targets4:
        result = binary_search_rotated_array(nums4, target)
        print(f"Target {target}: index {result}") 