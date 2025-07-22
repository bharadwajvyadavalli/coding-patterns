"""
Trees & BST - NeetCode 75
Essential patterns for technical interviews.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    """LC 226 - Swap left and right children"""
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root

def max_depth(root):
    """LC 104 - Recursive DFS"""
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

def diameter_of_binary_tree(root):
    """LC 543 - Track diameter during height calculation"""
    diameter = [0]
    
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        diameter[0] = max(diameter[0], left + right)
        return max(left, right) + 1
    
    height(root)
    return diameter[0]

def is_balanced(root):
    """LC 110 - Check height difference"""
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    
    return check(root) != -1

def right_side_view(root):
    """LC 199 - BFS, take last node at each level"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

def good_nodes(root):
    """LC 1448 - Track path maximum"""
    def dfs(node, path_max):
        if not node:
            return 0
        count = 1 if node.val >= path_max else 0
        new_max = max(path_max, node.val)
        return count + dfs(node.left, new_max) + dfs(node.right, new_max)
    
    return dfs(root, float('-inf'))

def is_valid_bst(root):
    """LC 98 - Inorder traversal should be sorted"""
    def inorder(node, prev):
        if not node:
            return True
        if not inorder(node.left, prev):
            return False
        if prev[0] is not None and node.val <= prev[0]:
            return False
        prev[0] = node.val
        return inorder(node.right, prev)
    
    return inorder(root, [None])

def kth_smallest(root, k):
    """LC 230 - Inorder traversal"""
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result[0] += 1
        if result[0] == k:
            result[1] = node.val
        inorder(node.right)
    
    result = [0, None]
    inorder(root)
    return result[1]

def build_tree(preorder, inorder):
    """LC 105 - Use inorder to find left/right subtrees"""
    def build(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end:
            return None
        
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        root_idx = inorder_map[root_val]
        left_size = root_idx - in_start
        
        root.left = build(pre_start + 1, pre_start + left_size, in_start, root_idx - 1)
        root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)
        return root
    
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    return build(0, len(preorder) - 1, 0, len(inorder) - 1)

def max_path_sum(root):
    """LC 124 - Track max path through each node"""
    def dfs(node):
        if not node:
            return 0
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        result[0] = max(result[0], left + right + node.val)
        return max(left, right) + node.val
    
    result = [float('-inf')]
    dfs(root)
    return result[0]

def serialize(root):
    """LC 297 - Preorder with null markers"""
    def preorder(node):
        if not node:
            return ['null']
        return [str(node.val)] + preorder(node.left) + preorder(node.right)
    
    return ','.join(preorder(root))

def deserialize(data):
    """LC 297 - Reconstruct from preorder"""
    def build(values):
        if values[0] == 'null':
            values.pop(0)
            return None
        root = TreeNode(int(values.pop(0)))
        root.left = build(values)
        root.right = build(values)
        return root
    
    return build(data.split(','))

def level_order(root):
    """LC 102 - BFS with level tracking"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level = []
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result

def preorder_traversal(root):
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

def postorder_traversal(root):
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

# ============================================================================
# ADDITIONAL PATTERNS
# ============================================================================

def inorder_traversal(root):
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

def lowest_common_ancestor(root, p, q):
    """LC 236 - Find LCA in BST"""
    if not root or root == p or root == q:
        return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left and right:
        return root
    return left or right

def path_sum(root, target_sum):
    """LC 112 - Check if path exists to leaf"""
    def dfs(node, current_sum):
        if not node:
            return False
        current_sum += node.val
        if not node.left and not node.right:
            return current_sum == target_sum
        return dfs(node.left, current_sum) or dfs(node.right, current_sum)
    
    return dfs(root, 0)

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Quick tests
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    print("Max Depth:", max_depth(root))
    print("Invert Tree:", invert_tree(root))
    print("Level Order:", level_order(root))
    print("Preorder:", preorder_traversal(root)) 