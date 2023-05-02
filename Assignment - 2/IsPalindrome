"""
My general intution was to traverse the doubly linked list from the beginning and store each node's value in an array
Traverse the doubly linked list from the end and store each node's value in another array
Compare the two arrays. If they are identical, then the doubly linked list is a palindrome; otherwise, it is not

time complexity of O(n)
space complexity of O(n)

edge cases i would ask the interviewer:
 - do we check for empty linked list
 - only one element
 - even/odd/duplicate numbers
- diffrent data types

Time: 20 min

"""
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def isPalindrome(head):
    #Traverse the doubly linked list from the beginning and store each node's value in an array.
    forward = []
    node = head
    while node is not None:
        forward.append(node.val)
        node = node.next

    #Traverse the doubly linked list from the end and store each node's value in another array.
    backward = []
    node = head
    while node.next is not None:
        node = node.next
    while node is not None:
        backward.append(node.val)
        node = node.prev

    # Compare the two arrays.
    return forward == backward
