"""
Heap & Priority Queue - LeetCode 75
Essential patterns for technical interviews.
"""

import heapq
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_kth_largest(nums, k):
    """LC 215 - Find kth largest element using min heap"""
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def top_k_frequent_elements(nums, k):
    """LC 347 - Find k most frequent elements"""
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
    """LC 23 - Merge k sorted linked lists"""
    if not lists:
        return None
    
    # Create min heap with (value, list_index, node_index)
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, 0))
    
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

def find_median_from_data_stream():
    """LC 295 - Design data structure to find median of stream"""
    class MedianFinder:
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
            
            # Ensure max heap has at most one more element
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
    
    return MedianFinder()

def k_closest_points_to_origin(points, k):
    """LC 973 - Find k closest points to origin"""
    # Use max heap to keep k closest points
    heap = []
    
    for point in points:
        distance = point[0]**2 + point[1]**2
        heapq.heappush(heap, (-distance, point))
        
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [point for _, point in heap]

def last_stone_weight(stones):
    """LC 1046 - Last remaining stone weight"""
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
    """LC 767 - Reorganize string so no adjacent characters are same"""
    # Count character frequencies
    counter = Counter(s)
    
    # Use max heap to get most frequent characters first
    heap = [(-freq, char) for char, freq in counter.items()]
    heapq.heapify(heap)
    
    result = []
    prev_char = None
    
    while heap:
        freq, char = heapq.heappop(heap)
        
        if prev_char == char:
            if not heap:
                return ""  # Cannot reorganize
            freq2, char2 = heapq.heappop(heap)
            result.append(char2)
            prev_char = char2
            
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, char2))
            heapq.heappush(heap, (freq, char))
        else:
            result.append(char)
            prev_char = char
            
            if freq + 1 < 0:
                heapq.heappush(heap, (freq + 1, char))
    
    return ''.join(result)

def task_scheduler(tasks, n):
    """LC 621 - Minimum intervals to complete all tasks"""
    # Count task frequencies
    counter = Counter(tasks)
    
    # Use max heap to get most frequent tasks first
    heap = [-freq for freq in counter.values()]
    heapq.heapify(heap)
    
    time = 0
    queue = []  # (freq, available_time)
    
    while heap or queue:
        time += 1
        
        if heap:
            freq = heapq.heappop(heap)
            if freq + 1 < 0:
                queue.append((freq + 1, time + n))
        
        if queue and queue[0][1] <= time:
            heapq.heappush(heap, queue.pop(0)[0])
    
    return time

def minimum_cost_to_connect_sticks(sticks):
    """LC 1167 - Minimum cost to connect all sticks"""
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
    """LC 378 - Find kth smallest element in sorted matrix"""
    rows, cols = len(matrix), len(matrix[0])
    
    # Use min heap with (value, row, col)
    heap = [(matrix[0][0], 0, 0)]
    visited = set()
    
    for _ in range(k):
        val, row, col = heapq.heappop(heap)
        
        if row + 1 < rows and (row + 1, col) not in visited:
            heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
            visited.add((row + 1, col))
        
        if col + 1 < cols and (row, col + 1) not in visited:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            visited.add((row, col + 1))
    
    return val

def find_k_pairs_with_smallest_sums(nums1, nums2, k):
    """LC 373 - Find k pairs with smallest sums"""
    if not nums1 or not nums2:
        return []
    
    # Use min heap with (sum, i, j)
    heap = [(nums1[0] + nums2[0], 0, 0)]
    visited = set()
    result = []
    
    while heap and len(result) < k:
        total, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])
        
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            visited.add((i + 1, j))
        
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            visited.add((i, j + 1))
    
    return result

def sliding_window_median(nums, k):
    """LC 480 - Find median for each sliding window"""
    def add_num(num):
        heapq.heappush(max_heap, -num)
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    def remove_num(num):
        if num <= -max_heap[0]:
            max_heap.remove(-num)
            heapq.heapify(max_heap)
        else:
            min_heap.remove(num)
            heapq.heapify(min_heap)
        
        # Rebalance
        if len(max_heap) < len(min_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    def get_median():
        if len(max_heap) > len(min_heap):
            return -max_heap[0]
        return (-max_heap[0] + min_heap[0]) / 2
    
    max_heap = []
    min_heap = []
    result = []
    
    for i in range(len(nums)):
        add_num(nums[i])
        
        if i >= k - 1:
            result.append(get_median())
            remove_num(nums[i - k + 1])
    
    return result

def network_delay_time(times, n, k):
    """LC 743 - Dijkstra's algorithm with heap"""
    from collections import defaultdict
    
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Dijkstra's algorithm
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0
    
    heap = [(0, k)]
    visited = set()
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            if dist + weight < distances[neighbor]:
                distances[neighbor] = dist + weight
                heapq.heappush(heap, (distances[neighbor], neighbor))
    
    max_distance = max(distances.values())
    return max_distance if max_distance != float('inf') else -1

def cheapest_flights_within_k_stops(n, flights, src, dst, k):
    """LC 787 - Modified Dijkstra with stops constraint"""
    from collections import defaultdict
    
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))
    
    # (cost, stops, city)
    heap = [(0, 0, src)]
    visited = set()
    
    while heap:
        cost, stops, city = heapq.heappop(heap)
        
        if city == dst:
            return cost
        
        if (city, stops) in visited or stops > k:
            continue
        visited.add((city, stops))
        
        for neighbor, price in graph[city]:
            heapq.heappush(heap, (cost + price, stops + 1, neighbor))
    
    return -1

# Test cases
if __name__ == "__main__":
    # Test find_kth_largest
    print(find_kth_largest([3,2,1,5,6,4], 2))  # 5
    
    # Test top_k_frequent_elements
    print(top_k_frequent_elements([1,1,1,2,2,3], 2))  # [1, 2]
    
    # Test find_median_from_data_stream
    median_finder = find_median_from_data_stream()
    median_finder.addNum(1)
    median_finder.addNum(2)
    print(median_finder.findMedian())  # 1.5 