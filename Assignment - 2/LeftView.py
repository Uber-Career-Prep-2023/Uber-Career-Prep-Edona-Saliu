
"""
Intuition:
- We want to traverse the binary tree in a way that we can keep track of the leftmost element of each level
- We can use BFS to traverse the tree level by level and keep track of the first element at each level
Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(n) where n is the maximum number of nodes in a level of the tree

Time: ~ 30 min
"""

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def LeftView(root):
    if not root:
        return []

    q = deque([root])
    res = []

    while q:
        level_size = len(q)

        for i in range(level_size):
            node = q.popleft()

            if i == 0:
                res.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return res
