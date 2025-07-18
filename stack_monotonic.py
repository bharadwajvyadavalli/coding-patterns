"""
Stack & Monotonic Stack

Stack is a LIFO (Last In, First Out) data structure.
Monotonic stack maintains elements in strictly increasing or decreasing order.
Common applications:
- Parentheses matching
- Next greater/smaller element
- Histogram problems
- Expression evaluation
- Undo operations

Time Complexity: O(n) for most operations
Space Complexity: O(n) for stack storage
"""

def valid_parentheses(s):
    """
    Valid Parentheses (LeetCode 20)
    Check if string has valid parentheses pairs.
    """
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return len(stack) == 0

def next_greater_element(nums):
    """
    Next Greater Element (LeetCode 496)
    Find next greater element for each element in array.
    """
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    
    return result

def daily_temperatures(temperatures):
    """
    Daily Temperatures (LeetCode 739)
    Find number of days to wait for warmer temperature.
    """
    stack = []
    result = [0] * len(temperatures)
    
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result

def largest_rectangle_histogram(heights):
    """
    Largest Rectangle in Histogram (LeetCode 84)
    Find largest rectangle area in histogram.
    """
    stack = []
    max_area = 0
    heights.append(0)  # Add sentinel
    
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

def evaluate_reverse_polish_notation(tokens):
    """
    Evaluate Reverse Polish Notation (LeetCode 150)
    Evaluate postfix expression.
    """
    stack = []
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: int(x / y)}
    
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            stack.append(operators[token](a, b))
        else:
            stack.append(int(token))
    
    return stack[0]

def min_stack():
    """
    Min Stack (LeetCode 155)
    Design stack that supports push, pop, top, and retrieving minimum element.
    """
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []
        
        def push(self, val):
            self.stack.append(val)
            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)
        
        def pop(self):
            if self.stack:
                if self.stack[-1] == self.min_stack[-1]:
                    self.min_stack.pop()
                return self.stack.pop()
        
        def top(self):
            return self.stack[-1] if self.stack else None
        
        def getMin(self):
            return self.min_stack[-1] if self.min_stack else None
    
    return MinStack()

def asteroid_collision(asteroids):
    """
    Asteroid Collision (LeetCode 735)
    Simulate asteroid collisions where larger asteroids destroy smaller ones.
    """
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

if __name__ == "__main__":
    # Test Valid Parentheses
    print("=== Valid Parentheses ===")
    test_strings = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for s in test_strings:
        result = valid_parentheses(s)
        print(f"'{s}' -> {result}")
    
    # Test Next Greater Element
    print("\n=== Next Greater Element ===")
    nums1 = [4, 1, 2, 3]
    result1 = next_greater_element(nums1)
    print(f"Array: {nums1}")
    print(f"Next greater: {result1}")
    
    # Test Daily Temperatures
    print("\n=== Daily Temperatures ===")
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    result2 = daily_temperatures(temps)
    print(f"Temperatures: {temps}")
    print(f"Days to wait: {result2}")
    
    # Test Largest Rectangle in Histogram
    print("\n=== Largest Rectangle in Histogram ===")
    heights = [2, 1, 5, 6, 2, 3]
    max_area = largest_rectangle_histogram(heights)
    print(f"Heights: {heights}")
    print(f"Max area: {max_area}")
    
    # Test Evaluate RPN
    print("\n=== Evaluate Reverse Polish Notation ===")
    tokens = ["2", "1", "+", "3", "*"]
    result3 = evaluate_reverse_polish_notation(tokens)
    print(f"Expression: {tokens}")
    print(f"Result: {result3}")
    
    # Test Min Stack
    print("\n=== Min Stack ===")
    min_stack_obj = min_stack()
    operations = [("push", 3), ("push", 1), ("push", 5), ("getMin", None), 
                  ("pop", None), ("top", None), ("getMin", None)]
    
    for op, val in operations:
        if op == "push":
            min_stack_obj.push(val)
            print(f"Pushed {val}")
        elif op == "pop":
            result = min_stack_obj.pop()
            print(f"Popped {result}")
        elif op == "top":
            result = min_stack_obj.top()
            print(f"Top: {result}")
        elif op == "getMin":
            result = min_stack_obj.getMin()
            print(f"Min: {result}")
    
    # Test Asteroid Collision
    print("\n=== Asteroid Collision ===")
    asteroids = [5, 10, -5]
    result4 = asteroid_collision(asteroids)
    print(f"Asteroids: {asteroids}")
    print(f"After collision: {result4}") 