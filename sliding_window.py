"""
Sliding Window - LeetCode 75 + Top Interview 150 + Top 100 Liked
Essential patterns for technical interviews.
"""

def longest_substring_without_repeating(s):
    """LC 3 - Sliding window with character tracking"""
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

def longest_repeating_character_replacement(s, k):
    """LC 424 - Sliding window with frequency count"""
    from collections import Counter
    
    count = Counter()
    left = 0
    max_freq = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])
        
        if right - left + 1 - max_freq > k:
            count[s[left]] -= 1
            left += 1
    
    return right - left + 1

def permutation_in_string(s1, s2):
    """LC 567 - Fixed-size sliding window"""
    if len(s1) > len(s2):
        return False
    
    from collections import Counter
    s1_count = Counter(s1)
    window_count = Counter()
    
    for i in range(len(s2)):
        window_count[s2[i]] += 1
        
        if i >= len(s1):
            window_count[s2[i - len(s1)]] -= 1
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
        
        if window_count == s1_count:
            return True
    
    return False

def minimum_window_substring(s, t):
    """LC 76 - Variable-size sliding window"""
    from collections import Counter
    
    if not t or not s:
        return ""
    
    t_count = Counter(t)
    required = len(t_count)
    formed = 0
    window_count = Counter()
    
    left = 0
    min_len = float('inf')
    min_start = 0
    
    for right in range(len(s)):
        char = s[right]
        window_count[char] += 1
        
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        while left <= right and formed == required:
            char = s[left]
            
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            
            left += 1
    
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""

def find_all_anagrams_in_string(s, p):
    """LC 438 - Fixed-size sliding window"""
    from collections import Counter
    
    if len(p) > len(s):
        return []
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    for i in range(len(s)):
        window_count[s[i]] += 1
        
        if i >= len(p):
            window_count[s[i - len(p)]] -= 1
            if window_count[s[i - len(p)]] == 0:
                del window_count[s[i - len(p)]]
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result

def sliding_window_maximum(nums, k):
    """LC 239 - Monotonic deque"""
    from collections import deque
    
    if not nums or k == 0:
        return []
    
    dq = deque()
    result = []
    
    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

def minimum_size_subarray_sum(nums, target):
    """LC 209 - Variable-size sliding window"""
    if not nums:
        return 0
    
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

def fruit_into_baskets(fruits):
    """LC 904 - Sliding window with two types"""
    from collections import Counter
    
    basket = Counter()
    left = 0
    max_fruits = 0
    
    for right in range(len(fruits)):
        basket[fruits[right]] += 1
        
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1
        
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits

def longest_substring_with_at_most_two_distinct(s):
    """LC 159 - Sliding window with two distinct characters"""
    from collections import Counter
    
    char_count = Counter()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char_count[s[right]] += 1
        
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

def longest_substring_with_at_most_k_distinct(s, k):
    """LC 340 - Sliding window with k distinct characters"""
    from collections import Counter
    
    char_count = Counter()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char_count[s[right]] += 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

def subarray_product_less_than_k(nums, k):
    """LC 713 - Sliding window with product"""
    if k <= 1:
        return 0
    
    left = 0
    product = 1
    count = 0
    
    for right in range(len(nums)):
        product *= nums[right]
        
        while product >= k:
            product //= nums[left]
            left += 1
        
        count += right - left + 1
    
    return count

def maximum_sum_subarray_size_k(nums, k):
    """LC 643 - Fixed-size sliding window"""
    if len(nums) < k:
        return 0
    
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def substring_with_concatenation_of_all_words(s, words):
    """LC 30 - Sliding window with word matching"""
    if not s or not words:
        return []
    
    from collections import Counter
    
    word_len = len(words[0])
    word_count = Counter(words)
    result = []
    
    for i in range(word_len):
        left = i
        current_count = Counter()
        word_used = 0
        
        for j in range(i, len(s) - word_len + 1, word_len):
            word = s[j:j + word_len]
            
            if word in word_count:
                current_count[word] += 1
                word_used += 1
                
                while current_count[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    current_count[left_word] -= 1
                    word_used -= 1
                    left += word_len
                
                if word_used == len(words):
                    result.append(left)
            else:
                current_count.clear()
                word_used = 0
                left = j + word_len
    
    return result

def longest_substring_with_at_least_k_repeating_characters(s, k):
    """LC 395 - Divide and conquer with sliding window"""
    if len(s) < k:
        return 0
    
    from collections import Counter
    count = Counter(s)
    
    # Find characters that appear less than k times
    for char, freq in count.items():
        if freq < k:
            return max(longest_substring_with_at_least_k_repeating_characters(substring, k) 
                      for substring in s.split(char))
    
    return len(s)

def minimum_window_subsequence(s, t):
    """LC 727 - Sliding window for subsequence"""
    def is_subsequence(s, t):
        i = 0
        for char in t:
            i = s.find(char, i)
            if i == -1:
                return False
            i += 1
        return True
    
    if not is_subsequence(s, t):
        return ""
    
    min_len = float('inf')
    min_start = 0
    
    for start in range(len(s)):
        if s[start] == t[0]:
            end = start
            t_idx = 0
            
            while end < len(s) and t_idx < len(t):
                if s[end] == t[t_idx]:
                    t_idx += 1
                end += 1
            
            if t_idx == len(t) and end - start < min_len:
                min_len = end - start
                min_start = start
    
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""

def maximum_points_you_can_obtain_from_cards(card_points, k):
    """LC 1423 - Sliding window on both ends"""
    n = len(card_points)
    if k >= n:
        return sum(card_points)
    
    # Take all from left
    left_sum = sum(card_points[:k])
    max_sum = left_sum
    
    # Gradually take from right, remove from left
    right_sum = 0
    for i in range(k):
        right_sum += card_points[n - 1 - i]
        left_sum -= card_points[k - 1 - i]
        max_sum = max(max_sum, left_sum + right_sum)
    
    return max_sum

def count_number_of_nice_subarrays(nums, k):
    """LC 1248 - Sliding window with odd count"""
    def at_most_k_odds(k):
        left = 0
        count = 0
        result = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                count += 1
            
            while count > k:
                if nums[left] % 2 == 1:
                    count -= 1
                left += 1
            
            result += right - left + 1
        
        return result
    
    return at_most_k_odds(k) - at_most_k_odds(k - 1)

def max_consecutive_ones_iii(nums, k):
    """LC 1004 - Sliding window with zero count"""
    left = 0
    zeros = 0
    max_length = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

def longest_subarray_of_ones_after_deleting_one_element(nums):
    """LC 1493 - Sliding window with at most one zero"""
    left = 0
    zeros = 0
    max_length = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        
        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        
        max_length = max(max_length, right - left)
    
    return max_length

def frequency_of_the_most_frequent_element(nums, k):
    """LC 1838 - Sliding window with operations"""
    nums.sort()
    left = 0
    current_sum = 0
    max_freq = 0
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # Check if we can make all elements in window equal to nums[right]
        while (right - left + 1) * nums[right] - current_sum > k:
            current_sum -= nums[left]
            left += 1
        
        max_freq = max(max_freq, right - left + 1)
    
    return max_freq

def maximize_the_confusion_of_an_exam(answer_key, k):
    """LC 2024 - Sliding window for both T and F"""
    def max_consecutive_char(c):
        left = 0
        changes = 0
        max_length = 0
        
        for right in range(len(answer_key)):
            if answer_key[right] != c:
                changes += 1
            
            while changes > k:
                if answer_key[left] != c:
                    changes -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    return max(max_consecutive_char('T'), max_consecutive_char('F'))

def k_radius_subarray_averages(nums, k):
    """LC 2090 - Fixed-size sliding window with average"""
    n = len(nums)
    result = [-1] * n
    
    if 2 * k + 1 > n:
        return result
    
    current_sum = sum(nums[:2 * k + 1])
    result[k] = current_sum // (2 * k + 1)
    
    for i in range(k + 1, n - k):
        current_sum = current_sum - nums[i - k - 1] + nums[i + k]
        result[i] = current_sum // (2 * k + 1)
    
    return result

def minimum_swaps_to_group_all_ones_together_ii(nums):
    """LC 2134 - Sliding window with circular array"""
    ones_count = sum(nums)
    if ones_count == 0:
        return 0
    
    # Create circular array
    circular = nums + nums
    
    # Count ones in first window
    window_ones = sum(circular[:ones_count])
    min_swaps = ones_count - window_ones
    
    # Slide window
    for i in range(ones_count, len(circular)):
        window_ones = window_ones - circular[i - ones_count] + circular[i]
        min_swaps = min(min_swaps, ones_count - window_ones)
    
    return min_swaps

def longest_turbulent_subarray(nums):
    """LC 978 - Sliding window with alternating pattern"""
    if len(nums) <= 1:
        return len(nums)
    
    max_length = 1
    current_length = 1
    prev_diff = 0
    
    for i in range(1, len(nums)):
        curr_diff = nums[i] - nums[i-1]
        
        if (prev_diff > 0 and curr_diff < 0) or (prev_diff < 0 and curr_diff > 0):
            current_length += 1
        else:
            current_length = 2 if curr_diff != 0 else 1
        
        max_length = max(max_length, current_length)
        prev_diff = curr_diff
    
    return max_length

def grumpy_bookstore_owner(customers, grumpy, minutes):
    """LC 1052 - Sliding window with grumpy mask"""
    n = len(customers)
    
    # Calculate base satisfaction
    base_satisfaction = sum(customers[i] for i in range(n) if not grumpy[i])
    
    # Calculate additional satisfaction from grumpy window
    max_additional = 0
    current_additional = 0
    
    for i in range(n):
        if grumpy[i]:
            current_additional += customers[i]
        
        if i >= minutes and grumpy[i - minutes]:
            current_additional -= customers[i - minutes]
        
        max_additional = max(max_additional, current_additional)
    
    return base_satisfaction + max_additional

# Test cases
if __name__ == "__main__":
    # Test longest_substring_without_repeating
    print(longest_substring_without_repeating("abcabcbb"))  # 3
    
    # Test minimum_window_substring
    print(minimum_window_substring("ADOBECODEBANC", "ABC"))  # "BANC"
    
    # Test find_all_anagrams_in_string
    print(find_all_anagrams_in_string("cbaebabacd", "abc"))  # [0, 6]
    
    # Test max_consecutive_ones_iii
    print(max_consecutive_ones_iii([1,1,1,0,0,0,1,1,1,1,0], 2))  # 6
    
    # Test frequency_of_the_most_frequent_element
    print(frequency_of_the_most_frequent_element([1,2,4], 5))  # 3 