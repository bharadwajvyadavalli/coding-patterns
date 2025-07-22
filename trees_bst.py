"""
Trees & BST - LeetCode 75 + Top Interview 150
Essential patterns for technical interviews.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root):
    """LC 226 - Swap left and right children"""
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return root

def maximum_depth_of_binary_tree(root):
    """LC 104 - Recursive DFS"""
    if not root:
        return 0
    return 1 + max(maximum_depth_of_binary_tree(root.left), 
                   maximum_depth_of_binary_tree(root.right))

def diameter_of_binary_tree(root):
    """LC 543 - Track diameter during height calculation"""
    def dfs(node):
        if not node:
            return 0
        
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        
        diameter[0] = max(diameter[0], left_height + right_height)
        return 1 + max(left_height, right_height)
    
    diameter = [0]
    dfs(root)
    return diameter[0]

def balanced_binary_tree(root):
    """LC 110 - Check height difference"""
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return check_height(root) != -1

def binary_tree_right_side_view(root):
    """LC 199 - BFS, take last node at each level"""
    if not root:
        return []
    
    from collections import deque
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            
            if i == level_size - 1:  # Last node in level
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

def count_good_nodes_in_binary_tree(root):
    """LC 1448 - Track path maximum"""
    def dfs(node, max_val):
        if not node:
            return 0
        
        count = 1 if node.val >= max_val else 0
        new_max = max(max_val, node.val)
        
        count += dfs(node.left, new_max)
        count += dfs(node.right, new_max)
        
        return count
    
    return dfs(root, float('-inf'))

def validate_binary_search_tree(root):
    """LC 98 - Inorder traversal should be sorted"""
    def inorder(node):
        if not node:
            return True
        
        if not inorder(node.left):
            return False
        
        if self.prev is not None and node.val <= self.prev:
            return False
        
        self.prev = node.val
        return inorder(node.right)
    
    self.prev = None
    return inorder(root)

def kth_smallest_element_in_bst(root, k):
    """LC 230 - Inorder traversal"""
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        inorder(node.right)
    
    self.count = 0
    self.result = None
    inorder(root)
    return self.result

def construct_binary_tree_from_preorder_and_inorder_traversal(preorder, inorder):
    """LC 105 - Use inorder to find left/right subtrees"""
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    inorder_index = inorder.index(root_val)
    
    root.left = construct_binary_tree_from_preorder_and_inorder_traversal(
        preorder[1:1 + inorder_index], inorder[:inorder_index])
    root.right = construct_binary_tree_from_preorder_and_inorder_traversal(
        preorder[1 + inorder_index:], inorder[inorder_index + 1:])
    
    return root

def binary_tree_maximum_path_sum(root):
    """LC 124 - Track max path through each node"""
    def dfs(node):
        if not node:
            return 0
        
        left_sum = max(0, dfs(node.left))
        right_sum = max(0, dfs(node.right))
        
        self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)
        return node.val + max(left_sum, right_sum)
    
    self.max_sum = float('-inf')
    dfs(root)
    return self.max_sum

def serialize_deserialize_binary_tree():
    """LC 297 - Preorder with null markers"""
    def serialize(root):
        if not root:
            return "null"
        return str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)
    
    def deserialize(data):
        def build_tree(values):
            if not values or values[0] == "null":
                values.pop(0)
                return None
            
            root = TreeNode(int(values.pop(0)))
            root.left = build_tree(values)
            root.right = build_tree(values)
            return root
        
        return build_tree(data.split(","))
    
    return serialize, deserialize

def binary_tree_level_order_traversal(root):
    """LC 102 - BFS with level tracking"""
    if not root:
        return []
    
    from collections import deque
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

def binary_tree_preorder_traversal(root):
    """LC 144 - Root, left, right"""
    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    result = []
    dfs(root)
    return result

def binary_tree_postorder_traversal(root):
    """LC 145 - Left, right, root"""
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    
    result = []
    dfs(root)
    return result

def binary_tree_inorder_traversal(root):
    """LC 94 - Left, root, right"""
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    result = []
    dfs(root)
    return result

def lowest_common_ancestor_of_a_binary_search_tree(root, p, q):
    """LC 235 - Find LCA in BST"""
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor_of_a_binary_search_tree(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor_of_a_binary_search_tree(root.right, p, q)
    else:
        return root

def path_sum(root, target_sum):
    """LC 112 - Check if path exists to leaf"""
    if not root:
        return False
    
    if not root.left and not root.right:
        return target_sum == root.val
    
    return (path_sum(root.left, target_sum - root.val) or 
            path_sum(root.right, target_sum - root.val))

def same_tree(p, q):
    """LC 100 - Compare trees recursively"""
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)

def subtree_of_another_tree(root, sub_root):
    """LC 572 - Check if subRoot is subtree of root"""
    if not sub_root:
        return True
    if not root:
        return False
    
    if same_tree(root, sub_root):
        return True
    
    return (subtree_of_another_tree(root.left, sub_root) or 
            subtree_of_another_tree(root.right, sub_root))

def lowest_common_ancestor_of_a_binary_tree(root, p, q):
    """LC 236 - Find LCA in binary tree"""
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor_of_a_binary_tree(root.left, p, q)
    right = lowest_common_ancestor_of_a_binary_tree(root.right, p, q)
    
    if left and right:
        return root
    return left or right

def binary_tree_level_order_traversal_ii(root):
    """LC 107 - Level order from bottom to top"""
    if not root:
        return []
    
    from collections import deque
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.insert(0, current_level)
    
    return result

def sum_root_to_leaf_numbers(root):
    """LC 129 - DFS with path sum"""
    def dfs(node, current_sum):
        if not node:
            return 0
        
        current_sum = current_sum * 10 + node.val
        
        if not node.left and not node.right:
            return current_sum
        
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)
    
    return dfs(root, 0)

def count_complete_tree_nodes(root):
    """LC 222 - Binary search on complete tree"""
    def get_height(node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    if not root:
        return 0
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    
    if left_height == right_height:
        return (1 << left_height) + count_complete_tree_nodes(root.right)
    else:
        return (1 << right_height) + count_complete_tree_nodes(root.left)

def construct_binary_tree_from_inorder_and_postorder_traversal(inorder, postorder):
    """LC 106 - Build tree from inorder and postorder"""
    if not inorder or not postorder:
        return None
    
    root_val = postorder[-1]
    root = TreeNode(root_val)
    
    inorder_index = inorder.index(root_val)
    
    root.left = construct_binary_tree_from_inorder_and_postorder_traversal(
        inorder[:inorder_index], postorder[:inorder_index])
    root.right = construct_binary_tree_from_inorder_and_postorder_traversal(
        inorder[inorder_index + 1:], postorder[inorder_index:-1])
    
    return root

def flatten_binary_tree_to_linked_list(root):
    """LC 114 - Flatten tree to right-skewed tree"""
    def flatten_helper(node):
        if not node:
            return None
        
        # Flatten left subtree
        left_tail = flatten_helper(node.left)
        
        # Flatten right subtree
        right_tail = flatten_helper(node.right)
        
        # If left subtree exists, insert it between root and right subtree
        if node.left:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        
        # Return the rightmost node
        return right_tail if right_tail else (left_tail if left_tail else node)
    
    flatten_helper(root)

def recover_binary_search_tree(root):
    """LC 99 - Find swapped nodes in BST"""
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        
        if self.prev and self.prev.val > node.val:
            if not self.first:
                self.first = self.prev
            self.second = node
        
        self.prev = node
        inorder(node.right)
    
    self.prev = None
    self.first = None
    self.second = None
    
    inorder(root)
    
    # Swap the values
    if self.first and self.second:
        self.first.val, self.second.val = self.second.val, self.first.val

def binary_tree_zigzag_level_order_traversal(root):
    """LC 103 - Zigzag level order traversal"""
    if not root:
        return []
    
    from collections import deque
    queue = deque([root])
    result = []
    level = 0
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if level % 2 == 1:
            current_level.reverse()
        
        result.append(current_level)
        level += 1
    
    return result

def path_sum_ii(root, target_sum):
    """LC 113 - Find all paths with target sum"""
    def dfs(node, current_sum, path):
        if not node:
            return
        
        current_sum += node.val
        path.append(node.val)
        
        if not node.left and not node.right and current_sum == target_sum:
            result.append(path[:])
        
        dfs(node.left, current_sum, path)
        dfs(node.right, current_sum, path)
        
        path.pop()
    
    result = []
    dfs(root, 0, [])
    return result

def binary_tree_paths(root):
    """LC 257 - Find all root-to-leaf paths"""
    def dfs(node, path):
        if not node:
            return
        
        path.append(str(node.val))
        
        if not node.left and not node.right:
            result.append("->".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        
        path.pop()
    
    result = []
    dfs(root, [])
    return result

# Test cases
if __name__ == "__main__":
    # Test same_tree
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    print(same_tree(p, q))  # True
    
    # Test maximum_depth_of_binary_tree
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(maximum_depth_of_binary_tree(root))  # 3
    
    # Test binary_tree_right_side_view
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    print(binary_tree_right_side_view(root))  # [1, 3, 4] 