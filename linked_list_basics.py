"""
Linked List Basics

Linked list is a linear data structure where elements are stored in nodes,
and each node points to the next node. Common operations:
- Traversal
- Insertion (beginning, end, middle)
- Deletion
- Reversal
- Cycle detection
- Finding middle element

Time Complexity: O(n) for traversal, O(1) for head operations
Space Complexity: O(1) for most operations
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse Linked List (LeetCode 206)
    Reverse a singly linked list iteratively.
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

def detect_cycle(head):
    """
    Linked List Cycle (LeetCode 141)
    Detect if linked list has a cycle using Floyd's algorithm.
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

def find_middle_node(head):
    """
    Middle of the Linked List (LeetCode 876)
    Find middle node using slow/fast pointer technique.
    """
    if not head or not head.next:
        return head
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge_two_sorted_lists(l1, l2):
    """
    Merge Two Sorted Lists (LeetCode 21)
    Merge two sorted linked lists into one sorted list.
    """
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 if l1 else l2
    
    return dummy.next

def remove_nth_from_end(head, n):
    """
    Remove Nth Node From End of List (LeetCode 19)
    Remove the nth node from the end of the list.
    """
    dummy = ListNode(0)
    dummy.next = head
    
    first = dummy
    second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node
    second.next = second.next.next
    
    return dummy.next

def add_two_numbers(l1, l2):
    """
    Add Two Numbers (LeetCode 2)
    Add two numbers represented by linked lists.
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        # Get values from lists
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        # Create new node
        current.next = ListNode(digit)
        current = current.next
        
        # Move to next nodes
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next

def is_palindrome_linked_list(head):
    """
    Palindrome Linked List (LeetCode 234)
    Check if linked list is palindrome using O(1) space.
    """
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    current = slow
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    # Compare first and second half
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True

def print_linked_list(head):
    """Helper function to print linked list"""
    current = head
    values = []
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values) + " -> None"

if __name__ == "__main__":
    # Create test linked lists
    def create_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    # Test Reverse Linked List
    print("=== Reverse Linked List ===")
    list1 = create_list([1, 2, 3, 4, 5])
    print(f"Original: {print_linked_list(list1)}")
    reversed_list = reverse_linked_list(list1)
    print(f"Reversed: {print_linked_list(reversed_list)}")
    
    # Test Find Middle Node
    print("\n=== Find Middle Node ===")
    list2 = create_list([1, 2, 3, 4, 5])
    middle = find_middle_node(list2)
    print(f"List: {print_linked_list(list2)}")
    print(f"Middle node value: {middle.val}")
    
    # Test Merge Two Sorted Lists
    print("\n=== Merge Two Sorted Lists ===")
    list3 = create_list([1, 3, 5])
    list4 = create_list([2, 4, 6])
    merged = merge_two_sorted_lists(list3, list4)
    print(f"List 1: {print_linked_list(create_list([1, 3, 5]))}")
    print(f"List 2: {print_linked_list(create_list([2, 4, 6]))}")
    print(f"Merged: {print_linked_list(merged)}")
    
    # Test Add Two Numbers
    print("\n=== Add Two Numbers ===")
    num1 = create_list([2, 4, 3])
    num2 = create_list([5, 6, 4])
    sum_list = add_two_numbers(num1, num2)
    print(f"Number 1: {print_linked_list(create_list([2, 4, 3]))}")
    print(f"Number 2: {print_linked_list(create_list([5, 6, 4]))}")
    print(f"Sum: {print_linked_list(sum_list)}")
    
    # Test Palindrome
    print("\n=== Palindrome Linked List ===")
    palindrome_list = create_list([1, 2, 2, 1])
    non_palindrome_list = create_list([1, 2, 3, 4])
    print(f"List: {print_linked_list(palindrome_list)}")
    print(f"Is palindrome: {is_palindrome_linked_list(palindrome_list)}")
    print(f"List: {print_linked_list(non_palindrome_list)}")
    print(f"Is palindrome: {is_palindrome_linked_list(non_palindrome_list)}") 