"""
insertAtFront(head, val): O(1) time complexity, O(1) space complexity
insertAtBack(head, val): O(n) time complexity (where n is the length of the linked list), O(1) space complexity
insertAfter(head, val, loc): O(n) time complexity (where n is the length of the linked list), O(1) space complexity
deleteFront(head): O(1) time complexity, O(1) space complexity
deleteBack(head): O(n) time complexity (where n is the length of the linked list), O(1) space complexity
length(head): O(n) time complexity (where n is the length of the linked list), O(n) space complexity (due to the recursive call stack)
reverseIterative(head): O(n) time complexity (where n is the length of the linked list), O(1) space complexity
reverseRecursive(head): O(n) time complexity (where n is the length of the linked list), O(n) space complexity (due to the recursive call stack)

Time: 40 min
"""
class Node:
    def __init__(self, data, next_node = None, prev = None):
        self.data = data
        self.next = next_node 
        self.prev = prev

def insertAtFront(head, val):
    node = Node(val, next_node=head)
    node.next.prev = node
    return node

def insertAtBack(head, val):
    node = Node(val)
    
    prevNode = head
    while prevNode.next:
        prevNode = prevNode.next
    prevNode.next = node
    node.prev = prevNode

def insertAfter(head, val, loc):
    node = Node(val)

    prev = head
    while prev and (prev is loc) == False:
        prev = prev.next

    if prev:
        oldNext = prev.next
        prev.next = node 
        node.next = oldNext
        oldNext.prev = node

def deleteFront(head):
    head.next.prev = None
    return head.next

def deleteBack(head):
    prev = head
    curr = head.next
    while curr.next:
        prev = prev.next
        curr = curr.next
    
    prev.next = None

def length(head):
    if head:
        return 1 + length(head.next)
    else:
        return 0

def reverseIterative(head):
    prev = head
    curr = head.next
    prev.next = None 
    while prev2:
        save_next = curr.next
        curr.next = prev 
        prev.prev = curr    

        prev = curr
        curr = save_next
    return prev

def reverseRecursive(head):
    if (head == None) or (head.next == None):
        return head
    else:
        last = head.next
        reverseNode = reverseRecursive(head.next)
        
        # adjust pointers
        last.next = head
        head.prev = last
        head.next = None
        return reverseNode