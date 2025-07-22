"""
Stack Problems - LeetCode 75 + Top Interview 150 + Top 100 Liked
Essential patterns for technical interviews.
"""

def valid_parentheses(s):
    """LC 20 - Stack for parentheses matching"""
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0

def min_stack():
    """LC 155 - Stack with min tracking"""
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []
        
        def push(self, val):
            self.stack.append(val)
            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)
        
        def pop(self):
            if self.stack.pop() == self.min_stack[-1]:
                self.min_stack.pop()
        
        def top(self):
            return self.stack[-1]
        
        def getMin(self):
            return self.min_stack[-1]
    
    return MinStack()

def implement_stack_using_queues():
    """LC 225 - Stack using queues"""
    from collections import deque
    
    class MyStack:
        def __init__(self):
            self.queue = deque()
        
        def push(self, x):
            self.queue.append(x)
            # Rotate to make the new element at the front
            for _ in range(len(self.queue) - 1):
                self.queue.append(self.queue.popleft())
        
        def pop(self):
            return self.queue.popleft()
        
        def top(self):
            return self.queue[0]
        
        def empty(self):
            return len(self.queue) == 0
    
    return MyStack()

def implement_queue_using_stacks():
    """LC 232 - Queue using stacks"""
    class MyQueue:
        def __init__(self):
            self.input_stack = []
            self.output_stack = []
        
        def push(self, x):
            self.input_stack.append(x)
        
        def pop(self):
            self._move_to_output()
            return self.output_stack.pop()
        
        def peek(self):
            self._move_to_output()
            return self.output_stack[-1]
        
        def empty(self):
            return len(self.input_stack) == 0 and len(self.output_stack) == 0
        
        def _move_to_output(self):
            if not self.output_stack:
                while self.input_stack:
                    self.output_stack.append(self.input_stack.pop())
    
    return MyQueue()

def evaluate_reverse_polish_notation(tokens):
    """LC 150 - Stack for postfix evaluation"""
    stack = []
    
    for token in tokens:
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    
    return stack[0]

def generate_parentheses(n):
    """LC 22 - Backtracking with stack validation"""
    def backtrack(open_count, close_count, current):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(open_count + 1, close_count, current + '(')
        
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ')')
    
    result = []
    backtrack(0, 0, "")
    return result

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

def car_fleet(target, position, speed):
    """LC 853 - Stack for car fleets"""
    cars = sorted(zip(position, speed), reverse=True)
    stack = []
    
    for pos, spd in cars:
        time = (target - pos) / spd
        
        if not stack or time > stack[-1]:
            stack.append(time)
    
    return len(stack)

def largest_rectangle_in_histogram(heights):
    """LC 84 - Monotonic stack"""
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel
    
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    return max_area

def next_greater_element_i(nums1, nums2):
    """LC 496 - Monotonic stack with hash map"""
    stack = []
    next_greater = {}
    
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    return [next_greater.get(num, -1) for num in nums1]

def asteroid_collision(asteroids):
    """LC 735 - Stack for asteroid collisions"""
    stack = []
    
    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            if abs(asteroid) > stack[-1]:
                stack.pop()
            elif abs(asteroid) == stack[-1]:
                stack.pop()
                break
            else:
                break
        else:
            stack.append(asteroid)
    
    return stack

def simplify_path(path):
    """LC 71 - Stack for path simplification"""
    stack = []
    
    for part in path.split('/'):
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    
    return '/' + '/'.join(stack)

def decode_string(s):
    """LC 394 - Stack for nested decoding"""
    stack = []
    current_num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char
    
    return current_str

def basic_calculator_ii(s):
    """LC 227 - Stack for expression evaluation"""
    stack = []
    num = 0
    sign = '+'
    
    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        
        if (not char.isdigit() and char != ' ') or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            
            sign = char
            num = 0
    
    return sum(stack)

def basic_calculator(s):
    """LC 224 - Stack for basic calculator"""
    stack = []
    num = 0
    sign = 1
    result = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            result *= stack.pop()
            result += stack.pop()
            num = 0
    
    return result + sign * num

def remove_k_digits(num, k):
    """LC 402 - Monotonic stack for digit removal"""
    stack = []
    
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # Remove remaining k digits from end
    while k > 0 and stack:
        stack.pop()
        k -= 1
    
    # Remove leading zeros
    result = ''.join(stack).lstrip('0')
    return result if result else '0'

def validate_stack_sequences(pushed, popped):
    """LC 946 - Simulate stack operations"""
    stack = []
    pop_index = 0
    
    for num in pushed:
        stack.append(num)
        while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1
    
    return pop_index == len(popped)

def longest_valid_parentheses(s):
    """LC 32 - Stack with index tracking"""
    stack = [-1]
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length

def trapping_rain_water_stack(height):
    """LC 42 - Stack-based solution"""
    stack = []
    water = 0
    
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = height[stack.pop()]
            if not stack:
                break
            width = i - stack[-1] - 1
            bounded_height = min(height[stack[-1]], h) - bottom
            water += width * bounded_height
        stack.append(i)
    
    return water

def maximal_rectangle(matrix):
    """LC 85 - Stack for histogram in each row"""
    if not matrix:
        return 0
    
    def largest_rectangle_area(heights):
        stack = []
        max_area = 0
        heights.append(0)
        
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        return max_area
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0
    
    for row in matrix:
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == '1' else 0
        max_area = max(max_area, largest_rectangle_area(heights))
    
    return max_area

def remove_duplicate_letters(s):
    """LC 316 - Stack with frequency tracking"""
    from collections import Counter
    
    count = Counter(s)
    stack = []
    seen = set()
    
    for char in s:
        count[char] -= 1
        
        if char in seen:
            continue
        
        while stack and char < stack[-1] and count[stack[-1]] > 0:
            seen.remove(stack.pop())
        
        stack.append(char)
        seen.add(char)
    
    return ''.join(stack)

def score_of_parentheses(s):
    """LC 856 - Stack for nested scoring"""
    stack = [0]
    
    for char in s:
        if char == '(':
            stack.append(0)
        else:
            score = stack.pop()
            stack[-1] += max(2 * score, 1)
    
    return stack[0]

def minimum_add_to_make_parentheses_valid(s):
    """LC 921 - Count unmatched parentheses"""
    left_needed = 0
    right_needed = 0
    
    for char in s:
        if char == '(':
            right_needed += 1
        else:
            if right_needed > 0:
                right_needed -= 1
            else:
                left_needed += 1
    
    return left_needed + right_needed

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

def next_greater_element_ii(nums):
    """LC 503 - Monotonic stack for circular array"""
    n = len(nums)
    result = [-1] * n
    stack = []
    
    # Process twice to handle circular nature
    for i in range(2 * n):
        while stack and nums[stack[-1] % n] < nums[i % n]:
            result[stack.pop() % n] = nums[i % n]
        stack.append(i)
    
    return result

def baseball_game(ops):
    """LC 682 - Stack for baseball game"""
    stack = []
    
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))
    
    return sum(stack)

def backspace_string_compare(s, t):
    """LC 844 - Stack for backspace processing"""
    def build_string(s):
        stack = []
        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
    return build_string(s) == build_string(t)

def remove_all_adjacent_duplicates_in_string(s):
    """LC 1047 - Stack for adjacent duplicates"""
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)

def remove_all_adjacent_duplicates_in_string_ii(s, k):
    """LC 1209 - Stack with count tracking"""
    stack = []  # (char, count)
    
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1] = (char, stack[-1][1] + 1)
        else:
            stack.append((char, 1))
        
        if stack[-1][1] == k:
            stack.pop()
    
    return ''.join(char * count for char, count in stack)

def make_the_string_great(s):
    """LC 1544 - Stack for case-sensitive duplicates"""
    stack = []
    
    for char in s:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)

def minimum_number_of_swaps_to_make_the_string_balanced(s):
    """LC 1963 - Count mismatched brackets"""
    stack = []
    
    for char in s:
        if char == '[':
            stack.append(char)
        else:  # char == ']'
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)
    
    # Count unmatched brackets
    unmatched = len(stack) // 2
    return (unmatched + 1) // 2

def check_if_word_is_valid_after_substitutions(s):
    """LC 1003 - Stack for abc validation"""
    stack = []
    
    for char in s:
        stack.append(char)
        if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
            stack.pop()
            stack.pop()
            stack.pop()
    
    return len(stack) == 0

def validate_stack_sequences_ii(pushed, popped):
    """LC 946 - Alternative approach"""
    i = 0
    stack = []
    
    for num in pushed:
        stack.append(num)
        while stack and i < len(popped) and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    
    return i == len(popped)

# Test cases
if __name__ == "__main__":
    # Test valid_parentheses
    print(valid_parentheses("()[]{}"))  # True
    
    # Test decode_string
    print(decode_string("3[a]2[bc]"))  # "aaabcbc"
    
    # Test largest_rectangle_in_histogram
    print(largest_rectangle_in_histogram([2,1,5,6,2,3]))  # 10
    
    # Test remove_duplicate_letters
    print(remove_duplicate_letters("bcabc"))  # "abc"
    
    # Test next_greater_element_ii
    print(next_greater_element_ii([1,2,1]))  # [2,-1,2] 