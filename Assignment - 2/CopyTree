"""
# Time: 25 minutes
# Space Complexity: O(n)
# Time Complexity: O(n)

"""

from BinarySearchTree import Node 
from BinarySearchTree import BinarySearchTree
import pdb


def copyTree(bst):
    # create a new BinarySearchTree instance to store the copied tree
    copied_tree = BinarySearchTree()

    # define a recursive helper function to traverse the original tree and copy its nodes
    def traverse_and_copy(node: Node):
        if node:
            # insert the current node's value into the copied tree
            copied_tree.insert(node.val)
            # recursively traverse the left and right subtrees and copy their nodes
            traverse_and_copy(node.left)
            traverse_and_copy(node.right)

    # start the traversal from the root of the original tree
    traverse_and_copy(bst.root)

    # return the copied tree
    return copied_tree


if __name__ == "__main__":
    # define a recursive function to check if two BinarySearchTree nodes are equal
    def is_equal(bst_node, bst_node_copy):
        if (bst_node and bst_node_copy == None) or (bst_node_copy and bst_node == None):
            # one node is None while the other is not, so they are not equal
            return False
        elif bst_node == None and bst_node_copy == None:
            # both nodes are None, so they are equal
            return True
        else:
            # compare the values of the two nodes and their child nodes
            print("bst_node: ", bst_node.val)
            print("bst_node_copy: ", bst_node_copy.val)
            print("deepcopy: ", (bst_node is bst_node_copy), "\n")
            equal_copy = (bst_node.val == bst_node_copy.val) and (bst_node is not bst_node_copy)
            if equal_copy:
                # recursively check the child nodes of both nodes
                return is_equal(bst_node.left, bst_node_copy.left) and is_equal(bst_node.right, bst_node_copy.right)
            else:
                # the two nodes have different values, so they are not equal
                return False
            
   