"""
Arrays & Two Pointers - LeetCode 75 + Top Interview 150 + Top 100 Liked
Essential patterns for technical interviews.
"""

def two_sum(nums, target):
    """LC 1 - Hash map for O(n) time"""
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

def contains_duplicate(nums):
    """LC 217 - Hash set for O(n) time"""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def valid_anagram(s, t):
    """LC 242 - Count character frequencies"""
    if len(s) != len(t):
        return False
    
    from collections import Counter
    return Counter(s) == Counter(t)

def group_anagrams(strs):
    """LC 49 - Group by sorted string"""
    from collections import defaultdict
    
    groups = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())

def top_k_frequent_elements(nums, k):
    """LC 347 - Counter + heap"""
    from collections import Counter
    import heapq
    
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

def product_of_array_except_self(nums):
    """LC 238 - Prefix and suffix products"""
    n = len(nums)
    result = [1] * n
    
    # Left to right
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Right to left
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

def valid_sudoku(board):
    """LC 36 - Check rows, columns, and boxes"""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                continue
            
            num = board[i][j]
            box_idx = (i // 3) * 3 + j // 3
            
            if (num in rows[i] or num in cols[j] or num in boxes[box_idx]):
                return False
            
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_idx].add(num)
    
    return True

def encode_and_decode_strings():
    """LC 271 - Length + delimiter"""
    class Codec:
        def encode(self, strs):
            return ''.join(f"{len(s)}#{s}" for s in strs)
        
        def decode(self, s):
            result = []
            i = 0
            while i < len(s):
                j = s.find('#', i)
                length = int(s[i:j])
                result.append(s[j+1:j+1+length])
                i = j + 1 + length
            return result
    
    return Codec()

def longest_consecutive_sequence(nums):
    """LC 128 - Hash set with streak counting"""
    num_set = set(nums)
    max_streak = 0
    
    for num in num_set:
        if num - 1 not in num_set:  # Start of streak
            current_streak = 1
            while num + current_streak in num_set:
                current_streak += 1
            max_streak = max(max_streak, current_streak)
    
    return max_streak

def find_all_numbers_disappeared_in_an_array(nums):
    """LC 448 - Mark numbers as negative"""
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    
    return [i + 1 for i, num in enumerate(nums) if num > 0]

def find_the_duplicate_number(nums):
    """LC 287 - Floyd's cycle detection"""
    slow = fast = nums[0]
    
    # Find intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

def subarray_sum_equals_k(nums, k):
    """LC 560 - Prefix sum with hash map"""
    from collections import defaultdict
    
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]
        prefix_sum[current_sum] += 1
    
    return count

def shortest_unsorted_continuous_subarray(nums):
    """LC 581 - Find unsorted boundaries"""
    n = len(nums)
    start = end = 0
    
    # Find start of unsorted
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            start = i - 1
            break
    
    # Find end of unsorted
    for i in range(n-2, -1, -1):
        if nums[i] > nums[i+1]:
            end = i + 1
            break
    
    if start == end == 0:
        return 0
    
    # Find min and max in unsorted range
    min_val = min(nums[start:end+1])
    max_val = max(nums[start:end+1])
    
    # Expand boundaries
    while start > 0 and nums[start-1] > min_val:
        start -= 1
    while end < n-1 and nums[end+1] < max_val:
        end += 1
    
    return end - start + 1

def container_with_most_water(height):
    """LC 11 - Two pointers from ends"""
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

def trapping_rain_water(height):
    """LC 42 - Two pointers with max tracking"""
    if not height:
        return 0
    
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
    """LC 125 - Two pointers with character filtering"""
    import re
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

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
            
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result

def four_sum(nums, target):
    """LC 18 - Two nested loops + two pointers"""
    nums.sort()
    result = []
    
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            
            left, right = j + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
    
    return result

def move_zeroes(nums):
    """LC 283 - Two pointers for in-place swap"""
    non_zero = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero], nums[i] = nums[i], nums[non_zero]
            non_zero += 1

def remove_duplicates_sorted(nums):
    """LC 26 - Two pointers for in-place removal"""
    if not nums:
        return 0
    
    unique = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[unique]:
            unique += 1
            nums[unique] = nums[i]
    
    return unique + 1

def remove_duplicates_sorted_ii(nums):
    """LC 80 - Allow at most 2 duplicates"""
    if len(nums) <= 2:
        return len(nums)
    
    unique = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[unique-2]:
            nums[unique] = nums[i]
            unique += 1
    
    return unique

def rotate_array(nums, k):
    """LC 189 - Reverse in three steps"""
    k %= len(nums)
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)

def best_time_buy_sell_stock(prices):
    """LC 121 - Track min price and max profit"""
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

def best_time_buy_sell_stock_ii(prices):
    """LC 122 - Sum all positive differences"""
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

def jump_game(nums):
    """LC 55 - Track maximum reachable position"""
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:
            return True
    
    return True

def jump_game_ii(nums):
    """LC 45 - BFS with level tracking"""
    if len(nums) <= 1:
        return 0
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            if current_end >= len(nums) - 1:
                break
    
    return jumps

def h_index(citations):
    """LC 274 - Sort and find h-index"""
    citations.sort(reverse=True)
    
    for i, citation in enumerate(citations):
        if citation <= i:
            return i
    
    return len(citations)

def insert_delete_getrandom():
    """LC 380 - Hash map + list for O(1) operations"""
    import random
    
    class RandomizedSet:
        def __init__(self):
            self.nums = []
            self.val_to_index = {}
        
        def insert(self, val):
            if val in self.val_to_index:
                return False
            self.val_to_index[val] = len(self.nums)
            self.nums.append(val)
            return True
        
        def remove(self, val):
            if val not in self.val_to_index:
                return False
            
            index = self.val_to_index[val]
            last_val = self.nums[-1]
            
            self.nums[index] = last_val
            self.val_to_index[last_val] = index
            
            self.nums.pop()
            del self.val_to_index[val]
            return True
        
        def getRandom(self):
            return random.choice(self.nums)
    
    return RandomizedSet()

def merge_sorted_array(nums1, m, nums2, n):
    """LC 88 - Merge from end to avoid overwriting"""
    p1, p2, p = m - 1, n - 1, m + n - 1
    
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

def majority_element(nums):
    """LC 169 - Boyer-Moore voting algorithm"""
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate

def majority_element_ii(nums):
    """LC 229 - Boyer-Moore for two candidates"""
    if not nums:
        return []
    
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0
    
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    # Verify candidates
    result = []
    for candidate in [candidate1, candidate2]:
        if nums.count(candidate) > len(nums) // 3:
            result.append(candidate)
    
    return result

def gas_station(gas, cost):
    """LC 134 - Track total and current balance"""
    if sum(gas) < sum(cost):
        return -1
    
    total = 0
    current = 0
    start = 0
    
    for i in range(len(gas)):
        current += gas[i] - cost[i]
        total += gas[i] - cost[i]
        
        if current < 0:
            current = 0
            start = i + 1
    
    return start if total >= 0 else -1

def candy(ratings):
    """LC 135 - Two passes: left to right and right to left"""
    n = len(ratings)
    candies = [1] * n
    
    # Left to right
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    
    # Right to left
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    
    return sum(candies)

def roman_to_integer(s):
    """LC 13 - Process from right to left"""
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    
    for char in reversed(s):
        curr = roman[char]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    
    return result

def integer_to_roman(num):
    """LC 12 - Greedy with predefined values"""
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = []
    for value, symbol in values:
        while num >= value:
            result.append(symbol)
            num -= value
    
    return ''.join(result)

def length_of_last_word(s):
    """LC 58 - Process from end"""
    i = len(s) - 1
    
    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1
    
    # Count characters
    length = 0
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    
    return length

def longest_common_prefix(strs):
    """LC 14 - Compare characters at same position"""
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for string in strs[1:]:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    
    return strs[0]

def reverse_words_in_string(s):
    """LC 151 - Split, reverse, join"""
    return ' '.join(s.split()[::-1])

def zigzag_conversion(s, num_rows):
    """LC 6 - Track direction and row"""
    if num_rows == 1:
        return s
    
    rows = [''] * num_rows
    current_row = 0
    direction = 1
    
    for char in s:
        rows[current_row] += char
        
        if current_row == 0:
            direction = 1
        elif current_row == num_rows - 1:
            direction = -1
        
        current_row += direction
    
    return ''.join(rows)

def daily_temperatures(temperatures):
    """LC 739 - Monotonic stack"""
    stack = []
    result = [0] * len(temperatures)
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result

def partition_labels(s):
    """LC 763 - Track last occurrence of each character"""
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    result = []
    start = end = 0
    
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        
        if i == end:
            result.append(end - start + 1)
            start = end + 1
    
    return result

def k_closest_points_to_origin(points, k):
    """LC 973 - Sort by distance"""
    def distance(point):
        return point[0]**2 + point[1]**2
    
    points.sort(key=distance)
    return points[:k]

def robot_bounded_in_circle(instructions):
    """LC 1041 - Check if robot returns to origin or changes direction"""
    x = y = 0
    dx, dy = 0, 1  # Start facing north
    
    for instruction in instructions:
        if instruction == 'G':
            x += dx
            y += dy
        elif instruction == 'L':
            dx, dy = -dy, dx
        elif instruction == 'R':
            dx, dy = dy, -dx
    
    # Robot is bounded if it returns to origin OR doesn't face north
    return (x == 0 and y == 0) or (dx != 0 or dy != 1)

def minimum_remove_to_make_valid_parentheses(s):
    """LC 1249 - Track indices of parentheses"""
    stack = []
    to_remove = set()
    
    # Mark invalid closing parentheses
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    
    # Mark unmatched opening parentheses
    to_remove.update(stack)
    
    # Build result
    return ''.join(char for i, char in enumerate(s) if i not in to_remove)

# Test cases
if __name__ == "__main__":
    # Test group_anagrams
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    
    # Test longest_consecutive_sequence
    print(longest_consecutive_sequence([100,4,200,1,3,2]))  # 4
    
    # Test product_of_array_except_self
    print(product_of_array_except_self([1,2,3,4]))  # [24,12,8,6]
    
    # Test three_sum
    print(three_sum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
    
    # Test daily_temperatures
    print(daily_temperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0] 