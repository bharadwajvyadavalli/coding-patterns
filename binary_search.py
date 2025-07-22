"""
Binary Search - NeetCode 75
Essential patterns for technical interviews.
"""

def binary_search(nums, target):
    """LC 704 - Standard binary search"""
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

def search_rotated_sorted_array(nums, target):
    """LC 33 - Binary search in rotated array"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
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

def search_matrix(matrix, target):
    """LC 74 - Binary search in 2D matrix"""
    if not matrix:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        row, col = mid // n, mid % n
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def min_eating_speed(piles, h):
    """LC 875 - Binary search on answer"""
    left, right = 1, max(piles)
    
    while left < right:
        mid = left + (right - left) // 2
        hours = sum((pile + mid - 1) // mid for pile in piles)
        
        if hours <= h:
            right = mid
        else:
            left = mid + 1
    
    return left

def find_min_rotated_sorted_array(nums):
    """LC 153 - Find minimum in rotated array"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]

class TimeMap:
    """LC 981 - Binary search with timestamps"""
    def __init__(self):
        self.store = {}
    
    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
    
    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        
        values = self.store[key]
        left, right = 0, len(values) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return values[right][1] if right >= 0 else ""

def find_median_sorted_arrays(nums1, nums2):
    """LC 4 - Binary search on partition"""
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition_x = left + (right - left) // 2
        partition_y = (m + n + 1) // 2 - partition_x
        
        max_left_x = nums1[partition_x - 1] if partition_x > 0 else float('-inf')
        min_right_x = nums1[partition_x] if partition_x < m else float('inf')
        max_left_y = nums2[partition_y - 1] if partition_y > 0 else float('-inf')
        min_right_y = nums2[partition_y] if partition_y < n else float('inf')
        
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (m + n) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            right = partition_x - 1
        else:
            left = partition_x + 1
    
    return 0

# ============================================================================
# ADDITIONAL PATTERNS
# ============================================================================

def sqrt(x):
    """LC 69 - Binary search for square root"""
    if x < 2:
        return x
    
    left, right = 2, x // 2
    
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

def capacity_to_ship_packages(weights, days):
    """LC 1011 - Binary search on capacity"""
    left, right = max(weights), sum(weights)
    
    while left < right:
        mid = left + (right - left) // 2
        days_needed = 1
        current_weight = 0
        
        for weight in weights:
            if current_weight + weight > mid:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight
        
        if days_needed <= days:
            right = mid
        else:
            left = mid + 1
    
    return left

def search_range(nums, target):
    """LC 34 - Binary search for range"""
    def find_first():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def find_last():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    return [find_first(), find_last()]

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Quick tests for key problems
    print("Binary Search:", binary_search([-1,0,3,5,9,12], 9))
    print("Search Rotated:", search_rotated_sorted_array([4,5,6,7,0,1,2], 0))
    print("Search Matrix:", search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print("Min Eating Speed:", min_eating_speed([3,6,7,11], 8))
    print("Find Min Rotated:", find_min_rotated_sorted_array([3,4,5,1,2]))
    print("Sqrt:", sqrt(8)) 