
"""
Technique: iterative tree traversal, specifically using a while loop to traverse the tree until either the target value is found or the traversal reaches a leaf node 

time complexity O(h)
space complexity O(1)
time : ~20 min

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def FloorInBST(root_node, target):
    current_node = root_node
    result = current_node.value
    while current_node is not None:
        if current_node.value == target:
            result = current_node.value
            return result
        elif current_node.value > target:
            result = current_node.value
            current_node = current_node.left_child
        else:
            current_node = current_node.right_child
    return result


