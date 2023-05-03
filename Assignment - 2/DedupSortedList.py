"""
Time complexity: O(n)
Space complexity: O(1)
Time: 15 mins

I assumed the list is sorted so I did not add an additional data structure to keep track of the values seen before, because the linked list is sorted and we only need to check adjacent nodes for duplicate
"""
def DedupSortedList(head):
    curr = head
    
    while curr != None and curr.next != None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head
            