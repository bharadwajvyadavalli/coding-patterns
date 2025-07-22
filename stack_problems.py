"""
Stack - NeetCode 75
Essential patterns for technical interviews.
"""

def valid_parentheses(s):
    """LC 20 - Stack with bracket matching"""
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0

class MinStack:
    """LC 155 - Stack with min tracking"""
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

def eval_rpn(tokens):
    """LC 150 - Stack for postfix evaluation"""
    stack = []
    ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
           '*': lambda x, y: x * y, '/': lambda x, y: int(x / y)}
    
    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
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
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        stack.append(i)
    
    return result

def car_fleet(target, position, speed):
    """LC 853 - Stack with time calculation"""
    cars = sorted(zip(position, speed), reverse=True)
    stack = []
    
    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
    
    return len(stack)

def largest_rectangle_area(heights):
    """LC 84 - Monotonic stack with area calculation"""
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel
    
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, h * w)
        stack.append(i)
    
    return max_area

# ============================================================================
# ADDITIONAL PATTERNS
# ============================================================================

def next_greater_element(nums1, nums2):
    """LC 496 - Monotonic stack with hash map"""
    stack = []
    next_greater = {}
    
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    return [next_greater.get(num, -1) for num in nums1]

def asteroid_collision(asteroids):
    """LC 735 - Stack simulation"""
    stack = []
    
    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            if stack[-1] < -asteroid:
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                stack.pop()
            break
        else:
            stack.append(asteroid)
    
    return stack

def simplify_path(path):
    """LC 71 - Stack for path processing"""
    stack = []
    
    for part in path.split('/'):
        if part == '..':
            if stack:
                stack.pop()
        elif part and part != '.':
            stack.append(part)
    
    return '/' + '/'.join(stack)

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Quick tests for key problems
    print("Valid Parentheses:", valid_parentheses("()[]{}"))
    
    # MinStack test
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print("MinStack min:", min_stack.getMin())
    
    print("RPN Evaluation:", eval_rpn(["2","1","+","3","*"]))
    print("Generate Parentheses:", generate_parentheses(3))
    print("Daily Temperatures:", daily_temperatures([73,74,75,71,69,72,76,73]))
    print("Car Fleet:", car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))
    print("Largest Rectangle:", largest_rectangle_area([2,1,5,6,2,3])) 