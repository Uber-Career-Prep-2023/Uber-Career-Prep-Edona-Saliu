class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def insert_at_front(self, val):
        new_node = Node(val)
        new_node.prev = None
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else: 
            self.tail = new_node
        self.head = new_node

    def insert_at_back(self, val):
        new_node = Node(val)
        new_node.next = None
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_after(self, loc, val):
        if not loc:
            return
        if self.tail == loc:
            return self.insert_at_back(loc,val)
        new_node = Node(val)
        new_node.next = loc.next
        loc.next = new_node
        new_node.next.prev = new_node
        new_node.prev = loc

    def delete_front(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        ptr = self.head.next
        self.head.next = None
        ptr.prev = None
        self.head = ptr

    def delete_back(self):
        if not self.head:
            return
        ptr = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        ptr.prev = None

    def delete_node(self, loc):
        if not self.head:
            return
        if self.head == loc:
            self.head = self.head.next
            self.head.prev.next = None
            self.head.prev = None
            return
        previous = loc.prev
        post = loc.next
        previous.next = post
        post.prev = previous
        loc.next = None
        loc.prev = None

    def length(self):
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def display(self):
        ptr = self.head
        s = ""
        while ptr:
            s += str(ptr.data) + " "
            ptr = ptr.next
        return(s[:-1])
