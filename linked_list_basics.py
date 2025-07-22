"""
Linked List - NeetCode 75
Essential patterns for technical interviews.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def has_cycle(head):
    """LC 141 - Floyd's cycle detection"""
    if not head or not head.next:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

def reorder_list(head):
    """LC 143 - Find middle, reverse second half, merge"""
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # Merge
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

def copy_random_list(head):
    """LC 138 - Hash map for random pointers"""
    if not head:
        return None
    
    # Create copy nodes
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next
    
    # Set next and random pointers
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next
    
    return old_to_new[head]

def find_duplicate(nums):
    """LC 287 - Floyd's cycle detection on array"""
    slow = fast = 0
    
    # Find meeting point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find start of cycle
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

class LRUCache:
    """LC 146 - Hash map + doubly linked list"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0, 0)  # dummy head
        self.tail = ListNode(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = ListNode(key, value)
        self.cache[key] = node
        self._add(node)
        
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
    
    def _add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

def merge_k_lists(lists):
    """LC 23 - Priority queue"""
    import heapq
    
    heap = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(heap, (head.val, i, head))
    
    dummy = curr = ListNode()
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

def reverse_k_group(head, k):
    """LC 25 - Reverse in groups"""
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length
    
    def reverse_group(start, end):
        prev, curr = None, start
        while curr != end:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
    length = get_length(head)
    dummy = ListNode(0, head)
    group_prev = dummy
    
    while length >= k:
        group_start = group_prev.next
        group_end = group_start
        
        for _ in range(k):
            group_end = group_end.next
        
        reversed_start = reverse_group(group_start, group_end)
        group_prev.next = reversed_start
        group_start.next = group_end
        group_prev = group_start
        length -= k
    
    return dummy.next

# ============================================================================
# ADDITIONAL HELPER FUNCTIONS
# ============================================================================

def find_middle_node(head):
    """Find middle node of linked list"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def is_palindrome_linked_list(head):
    """LC 234 - Find middle, reverse second half, compare"""
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # Compare
    first, second = head, prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True

def remove_nth_from_end(head, n):
    """LC 19 - Two pointers"""
    dummy = ListNode(0, head)
    first = second = dummy
    
    for _ in range(n + 1):
        first = first.next
    
    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next

def add_two_numbers(l1, l2):
    """LC 2 - Add with carry"""
    dummy = curr = ListNode()
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        
        curr.next = ListNode(total % 10)
        curr = curr.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Quick tests for key problems
    print("Has Cycle:", has_cycle(None))  # False
    
    # Create test list: 1->2->3->4->5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    print("Find Duplicate:", find_duplicate([1,3,4,2,2]))
    
    # LRU Cache test
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print("LRU Get 1:", lru.get(1))
    
    print("Reverse K Group:", reverse_k_group(head, 2)) 