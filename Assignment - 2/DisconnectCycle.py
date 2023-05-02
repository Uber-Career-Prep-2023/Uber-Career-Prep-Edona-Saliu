'''
Intuition:
-  to use two pointers - a slow pointer and a fast pointer - to detect a cycle in the linked list
Time complexity: O(n) 
Space complexity: O(n) 

Time: 20min
Not sure if it is the best solution

Edge cases to consider:
 - is list empty or only one node
 - is the cycle starting at the head of the linked list

'''

def DisconnectCycle(head):
    visited = set()
    curr = head
    prev = None
    
    while curr:
        if curr in visited:
            prev.next = None
            break
        else:
            visited.add(curr)
            prev = curr
            curr = curr.next
    
    return head

