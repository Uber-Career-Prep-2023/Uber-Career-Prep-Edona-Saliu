"""
Time: 40 min
"""

class Node:
    def __init__(self, val:int, right = None, left = None) -> None:
        self.val:int = val
        self.right = right
        self.left = left
        
class BST:

    "tc: O(n) and sc: O(1)"
    def min_node(self, root):
        min_val = [root.val]
        def helper(root):
            if root.left:
                min_val[0] = min(root.left.val, min_val[0])
                helper(root.left)
            if root.right:
                min_val[0] = min(root.right.val, min_val[0])
                helper(root.right)
        return min_val[0]
    "tc: O(n) and sc: O(1)"
    def max_node(self, root):
        max_val = [root.val]
        def helper(root):
            if root.left:
                max_val[0] = max(root.left.val, max_val[0])
                helper(root.left)
            if root.right:
                max_val[0] = max(root.right.val, max_val[0])
                helper(root.right)
        return max_val[0]
    "tc: O(n) and sc: O(1)"
    def contains(self, val, root):
        def helper(root, val):
            if not root:
                return False
            if root.val == val:
                return True
            return helper(root.left, val) or helper(root.right, val)
        return helper(root, val)

    "tc: O(n) and sc: O(n)"
    def insert(self, val):
        if not self.contains(val):
            self.root = self.insert_helper(self.root, val)
    
    def insert_helper(self, node, val): 
        if not node:
            return Node(val)
        elif val < node.val:
            node.left = self.insert_helper(node.left, val)
        else:
            node.right = self.insert_helper(node.right, val)
        return node

    "tc: O(n) and sc: O(n)"
    def delete(self, val):
        if self.contains(val):
            self.delete_helper(self.root, val)
    
    def delete_helper(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self.delete_helper(node.left, val)
        elif val > node.val:
            node.right = self.delete_helper(node.right, val)
        else:
            if node.right is None and node.left is None:
                node = None
            elif node.left is None: 
                node = node.right
            
            elif node.right is None:    
                node = node.left

            else:
                replace = self.min_node(node.right)
                node.right = self.delete_helper(node.right, replace)
                node.val = replace
        return node