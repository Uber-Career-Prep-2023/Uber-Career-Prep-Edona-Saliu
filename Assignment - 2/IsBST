class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(log(n)), where n is the number of nodes in the tree
def isBST(root):
    def is_bst_helper(node, min_value, max_value):
        if node is None:
            return True
        
        if node.value < min_value or node.value > max_value:
            return False
        
        # Check the left subtree and right subtree recursively
        return is_bst_helper(node.left, min_value, node.value - 1) and \
               is_bst_helper(node.right, node.value + 1, max_value)

    return is_bst_helper(root, float("-inf"), float("inf"))


# Adding a traversal method to show the values of nodes on the tree for testing
def traverse_tree(root):
    def traverse_helper(node, result):
        if node is None:
            return
        traverse_helper(node.left, result)
        result.append(node.value)
        traverse_helper(node.right, result)

    tree_list = []
    traverse_helper(root, tree_list)
    return tree_list

