"""
Binary Search - LeetCode 75 + Top Interview 150
Essential patterns for technical interviews.
"""

def binary_search(nums, target):
    """LC 704 - Standard binary search"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def search_in_rotated_sorted_array(nums, target):
    """LC 33 - Binary search in rotated array"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
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

def search_a_2d_matrix(matrix, target):
    """LC 74 - Binary search in 2D matrix"""
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // cols, mid % cols
        value = matrix[row][col]
        
        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def koko_eating_bananas(piles, h):
    """LC 875 - Binary search on answer"""
    left, right = 1, max(piles)
    
    def can_eat_all(speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours <= h
    
    while left < right:
        mid = (left + right) // 2
        if can_eat_all(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

def find_minimum_in_rotated_sorted_array(nums):
    """LC 153 - Find minimum in rotated array"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]

def time_based_key_value_store():
    """LC 981 - Binary search with timestamps"""
    from collections import defaultdict
    
    class TimeMap:
        def __init__(self):
            self.store = defaultdict(list)
        
        def set(self, key, value, timestamp):
            self.store[key].append((timestamp, value))
        
        def get(self, key, timestamp):
            if key not in self.store:
                return ""
            
            values = self.store[key]
            left, right = 0, len(values) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if values[mid][0] <= timestamp:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return values[right][1] if right >= 0 else ""
    
    return TimeMap()

def median_of_two_sorted_arrays(nums1, nums2):
    """LC 4 - Binary search on partition"""
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition_x = (left + right) // 2
        partition_y = (m + n + 1) // 2 - partition_x
        
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        
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

def sqrt(x):
    """LC 69 - Binary search for square root"""
    if x <= 1:
        return x
    
    left, right = 1, x
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

def capacity_to_ship_packages_within_d_days(weights, days):
    """LC 1011 - Binary search on capacity"""
    left, right = max(weights), sum(weights)
    
    def can_ship(capacity):
        current_weight = 0
        days_needed = 1
        
        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight
        
        return days_needed <= days
    
    while left < right:
        mid = (left + right) // 2
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

def find_first_and_last_position_of_element_in_sorted_array(nums, target):
    """LC 34 - Binary search for range"""
    def find_first():
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
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
            mid = (left + right) // 2
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

def find_peak_element(nums):
    """LC 162 - Binary search for peak"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

def first_bad_version(n):
    """LC 278 - Binary search for first bad version"""
    def is_bad_version(version):
        # This is a mock function - LeetCode provides the actual implementation
        return version >= 4  # Example: version 4 and above are bad
    
    left, right = 1, n
    
    while left < right:
        mid = (left + right) // 2
        if is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

def search_in_rotated_sorted_array_ii(nums, target):
    """LC 81 - Binary search with duplicates"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        
        # Handle duplicates
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False

def find_minimum_in_rotated_sorted_array_ii(nums):
    """LC 154 - Find minimum with duplicates"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1  # Handle duplicates
    
    return nums[left]

def split_array_largest_sum(nums, m):
    """LC 410 - Binary search on answer"""
    left, right = max(nums), sum(nums)
    
    def can_split(max_sum):
        pieces = 1
        current_sum = 0
        
        for num in nums:
            if current_sum + num > max_sum:
                pieces += 1
                current_sum = num
            else:
                current_sum += num
        
        return pieces <= m
    
    while left < right:
        mid = (left + right) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

def search_insert_position(nums, target):
    """LC 35 - Binary search for insert position"""
    left, right = 0, len(nums)
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def find_smallest_letter_greater_than_target(letters, target):
    """LC 744 - Binary search for next letter"""
    left, right = 0, len(letters)
    
    while left < right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return letters[left % len(letters)]

def arrange_coins(n):
    """LC 441 - Binary search for complete rows"""
    left, right = 0, n
    
    while left <= right:
        mid = (left + right) // 2
        coins_needed = mid * (mid + 1) // 2
        
        if coins_needed <= n:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

def valid_perfect_square(num):
    """LC 367 - Check if number is perfect square"""
    if num < 2:
        return True
    
    left, right = 2, num // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def find_k_closest_elements(arr, k, x):
    """LC 658 - Binary search + two pointers"""
    left, right = 0, len(arr) - k
    
    while left < right:
        mid = (left + right) // 2
        
        # Compare distances
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    
    return arr[left:left + k]

def pow_x_n(x, n):
    """LC 50 - Binary search for power"""
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1 / x
    
    half = pow_x_n(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        if n > 0:
            return half * half * x
        else:
            return half * half / x

# Test cases
if __name__ == "__main__":
    # Test binary_search
    print(binary_search([-1,0,3,5,9,12], 9))  # 4
    
    # Test find_peak_element
    print(find_peak_element([1,2,3,1]))  # 2
    
    # Test first_bad_version
    print(first_bad_version(5))  # 4
    
    # Test search_insert_position
    print(search_insert_position([1,3,5,6], 5))  # 2 