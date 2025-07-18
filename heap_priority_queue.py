"""
Heap & Priority Queue

Heap is a specialized tree-based data structure that satisfies the heap property.
Priority Queue is an abstract data type that operates similar to a regular queue
but each element has a priority. Common applications:
- Top K elements
- Merge K sorted lists
- Find median from data stream
- Dijkstra's algorithm
- Huffman coding

Time Complexity: O(log n) for insert/delete, O(1) for peek
Space Complexity: O(n) for storing elements
"""

import heapq
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_kth_largest(nums, k):
    """
    Kth Largest Element in an Array (LeetCode 215)
    Find kth largest element using min heap.
    """
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def top_k_frequent_elements(nums, k):
    """
    Top K Frequent Elements (LeetCode 347)
    Find k most frequent elements.
    """
    # Count frequencies
    counter = Counter(nums)
    
    # Use min heap to keep top k frequent
    heap = []
    for num, freq in counter.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Extract elements (reverse order)
    result = []
    while heap:
        result.append(heapq.heappop(heap)[1])
    
    return result[::-1]

def merge_k_sorted_lists(lists):
    """
    Merge k Sorted Lists (LeetCode 23)
    Merge k sorted linked lists into one sorted list.
    """
    if not lists:
        return None
    
    # Create min heap with (value, list_index, node_index)
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, list_idx, node_idx = heapq.heappop(heap)
        
        # Create new node
        current.next = ListNode(val)
        current = current.next
        
        # Add next element from same list if available
        if node_idx + 1 < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][node_idx + 1], list_idx, node_idx + 1))
    
    return dummy.next

class MedianFinder:
    """
    Find Median from Data Stream (LeetCode 295)
    Design data structure to find median of stream of numbers.
    """
    def __init__(self):
        self.max_heap = []  # Left half (max heap)
        self.min_heap = []  # Right half (min heap)
    
    def addNum(self, num):
        # Add to max heap first
        heapq.heappush(self.max_heap, -num)
        
        # Balance heaps
        if (self.max_heap and self.min_heap and 
            -self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # Ensure size balance
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2

def k_closest_points_to_origin(points, k):
    """
    K Closest Points to Origin (LeetCode 973)
    Find k closest points to origin using max heap.
    """
    heap = []
    
    for point in points:
        distance = point[0]**2 + point[1]**2
        heapq.heappush(heap, (-distance, point))
        
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [point for _, point in heap]

def last_stone_weight(stones):
    """
    Last Stone Weight (LeetCode 1046)
    Smash heaviest stones and return weight of last remaining stone.
    """
    # Convert to max heap (negate values)
    heap = [-stone for stone in stones]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        stone1 = -heapq.heappop(heap)
        stone2 = -heapq.heappop(heap)
        
        if stone1 != stone2:
            heapq.heappush(heap, -(stone1 - stone2))
    
    return -heap[0] if heap else 0

def reorganize_string(s):
    """
    Reorganize String (LeetCode 767)
    Reorganize string so no adjacent characters are same.
    """
    # Count character frequencies
    counter = Counter(s)
    
    # Use max heap to get most frequent characters first
    heap = [(-freq, char) for char, freq in counter.items()]
    heapq.heapify(heap)
    
    result = []
    prev_char = None
    
    while heap:
        freq, char = heapq.heappop(heap)
        
        # If same as previous, try next character
        if char == prev_char:
            if not heap:
                return ""
            freq2, char2 = heapq.heappop(heap)
            result.append(char2)
            prev_char = char2
            
            # Put back first character if still has frequency
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, char2))
            heapq.heappush(heap, (freq, char))
        else:
            result.append(char)
            prev_char = char
            
            # Put back if still has frequency
            if freq + 1 < 0:
                heapq.heappush(heap, (freq + 1, char))
    
    return ''.join(result)

def minimum_cost_to_connect_sticks(sticks):
    """
    Minimum Cost to Connect Sticks (LeetCode 1167)
    Connect sticks with minimum cost (cost = sum of lengths).
    """
    if len(sticks) <= 1:
        return 0
    
    heapq.heapify(sticks)
    total_cost = 0
    
    while len(sticks) > 1:
        stick1 = heapq.heappop(sticks)
        stick2 = heapq.heappop(sticks)
        
        cost = stick1 + stick2
        total_cost += cost
        
        heapq.heappush(sticks, cost)
    
    return total_cost

def kth_smallest_element_in_sorted_matrix(matrix, k):
    """
    Kth Smallest Element in a Sorted Matrix (LeetCode 378)
    Find kth smallest element in matrix where rows and columns are sorted.
    """
    rows, cols = len(matrix), len(matrix[0])
    heap = [(matrix[0][0], 0, 0)]
    visited = set()
    
    for _ in range(k - 1):
        val, row, col = heapq.heappop(heap)
        
        # Add right neighbor
        if col + 1 < cols and (row, col + 1) not in visited:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            visited.add((row, col + 1))
        
        # Add bottom neighbor
        if row + 1 < rows and (row + 1, col) not in visited:
            heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
            visited.add((row + 1, col))
    
    return heapq.heappop(heap)[0]

if __name__ == "__main__":
    # Test Find Kth Largest
    print("=== Find Kth Largest ===")
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    result = find_kth_largest(nums1, k1)
    print(f"Array: {nums1}, K: {k1}")
    print(f"Kth largest: {result}")
    
    # Test Top K Frequent Elements
    print("\n=== Top K Frequent Elements ===")
    nums2 = [1, 1, 1, 2, 2, 3]
    k2 = 2
    result = top_k_frequent_elements(nums2, k2)
    print(f"Array: {nums2}, K: {k2}")
    print(f"Top K frequent: {result}")
    
    # Test K Closest Points
    print("\n=== K Closest Points to Origin ===")
    points = [[1, 3], [-2, 2], [2, -2]]
    k3 = 2
    result = k_closest_points_to_origin(points, k3)
    print(f"Points: {points}, K: {k3}")
    print(f"K closest: {result}")
    
    # Test Last Stone Weight
    print("\n=== Last Stone Weight ===")
    stones = [2, 7, 4, 1, 8, 1]
    result = last_stone_weight(stones)
    print(f"Stones: {stones}")
    print(f"Last stone weight: {result}")
    
    # Test Median Finder
    print("\n=== Median Finder ===")
    median_finder = MedianFinder()
    test_nums = [1, 2, 3, 4, 5]
    for num in test_nums:
        median_finder.addNum(num)
        print(f"Added {num}, Median: {median_finder.findMedian()}")
    
    # Test Reorganize String
    print("\n=== Reorganize String ===")
    test_strings = ["aab", "aaab", "aaabc"]
    for s in test_strings:
        result = reorganize_string(s)
        print(f"'{s}' -> '{result}'")
    
    # Test Minimum Cost to Connect Sticks
    print("\n=== Minimum Cost to Connect Sticks ===")
    sticks = [2, 4, 3]
    result = minimum_cost_to_connect_sticks(sticks)
    print(f"Sticks: {sticks}")
    print(f"Minimum cost: {result}")
    
    # Test Kth Smallest in Sorted Matrix
    print("\n=== Kth Smallest in Sorted Matrix ===")
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k4 = 8
    result = kth_smallest_element_in_sorted_matrix(matrix, k4)
    print(f"Matrix: {matrix}")
    print(f"K: {k4}, Kth smallest: {result}") 