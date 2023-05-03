"""
Time complexity:
__init__ in Node class: O(1)
__init__ in LinkedList class: O(1)
insertAtFront: O(1)
insertAtBack: O(n)
insertAfter: O(n)
deleteFront: O(1)
deleteBack: O(n)
deleteNode: O(n)
length: O(n)
reverseIterative: O(n)
helper (used in reverseRecursive): O(n)
reverseRecursive: O(n)

Space complexity: O(n)

Time: 45 min
"""

class Node:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtFront(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        return self.head
        
        
    def insertAtBack(self, val):
        node = Node(val)
        
        if self.head is None:
            self.head = node
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
    
    def insertAfter(self, val, loc):
        node = Node(val)
        temp = self.head
        
        while temp != loc:
            temp = temp.next
        
        if temp == loc:
            if loc.next:
                node.next = loc.next
            temp.next = node
            
    def deleteFront(self):
        temp = self.head
        if temp:
            self.head = temp.next
            
        return self.head
    def deleteBack(self):
        if self.head:
            prev = None
            curr = self.head
            while curr.next:
                prev = curr
                curr = curr.next 
            prev.next = None
        
    def deleteNode(self, loc):
        if self.head:
            temp = self.head
            while temp.next and temp.next != loc:
                temp = temp.next

            if temp.next == loc:
                after = temp.next.next
                temp.next = after

            return self.head
    
    def length(self):
        counter = 0
        temp = self.head
        while temp:
            counter +=1
            temp = temp.next
        return counter
    
    def reverseIterative(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def helper(self, temp):
        if not temp or not temp.next:
            return temp
        
        head = self.helper(temp.next)
        temp.next.next = temp
        temp.next = None
        return head
    
    def reverseRecursive(self):
        self.head = self.helper(self.head)