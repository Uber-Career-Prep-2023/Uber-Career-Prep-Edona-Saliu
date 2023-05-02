"""
Intuition: -> 
  temporary node to store the node that needs to be moved to the front, and connects it to the original head of the list to make it the new head

time complexity: O(n) 
space complexity: O(1)

Time: 40 min
"""



class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

def MoveNthLastToFront(head_node, n):
    # Counting the number of nodes in the linked list
    count = 0
    current_node = head_node
    
    while current_node is not None:
        count += 1
        current_node = current_node.next_node
    
    # Finding the position of the node to move to the front
    position = count - n
    
    # Traverse the linked list to the position and get the node
    temp_head = head_node
    temp_count = 0
    temp_node = None
    
    while temp_head is not None:
        temp_count += 1
        
        if temp_count == position:
            temp_node = temp_head.next_node
            temp_head.next_node = temp_head.next_node.next_node
            break
            
        temp_head = temp_head.next_node
    
    # Moving the node to the front
    if temp_node is not None:
        temp_node.next_node = head_node
        head_node = temp_node
        
    return head_node

def print_linked_list(head_node):
    if head_node is None:
        print("Empty")
        return
        
    itr = head_node
    linked_list_str = ''
    while itr:
        linked_list_str += str(itr.val) + '-->'
        itr = itr.next_node
    linked_list_str += "none"

    print(linked_list_str)
