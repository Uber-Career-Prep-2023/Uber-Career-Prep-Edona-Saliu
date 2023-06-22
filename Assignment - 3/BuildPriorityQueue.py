"""
Question 3: Build a Priority Queue
A priority queue functions like a queue except that elements are removed in order of priority rather than insertion. This is typically implemented as a max heap that stores pairs of elements and numeric weights, with the weights used as the values in the heap. Implement a priority queue according to the following API using a heap as the underlying data structure. For simplicity, you can assume the priority queue stores string elements with integer priorities. Start by copy-pasting your heap implementation from question 2 and making modifications.

"""

"""
Time complexity: 
    top() operation: O(1) - Retrieving the top element from the priority queue is a constant-time operation.
    insert() operation: O(log n) - Inserting an element into the heap takes logarithmic time, where n is the number of elements in the heap.
    remove() operation: O(log n) - Removing the element with the highest priority from the heap also takes logarithmic time.

Space complexity:O(n)
Time: 35 mins
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to store the elements

    def top(self):
        return self.queue[0][1]  # Return the top element of the priority queue

    def insert(self, item, priority):
        heapq.heappush(self.queue, (priority, item))  # Insert the item with its priority into the heap

    def remove(self):
        heapq.heappop(self.queue)  # Remove the element with the highest priority

pq = PriorityQueue()

# Test Case 1: Insert elements with different priorities
pq.insert("Task 1", 3)
pq.insert("Task 2", 1)
pq.insert("Task 3", 2)

print("Top element:", pq.top())  # Expected output: "Task 2"

# Test Case 2: Insert elements with the same priority
pq.insert("Task 4", 2)
pq.insert("Task 5", 2)

print("Top element:", pq.top())  # Expected output: "Task 2"

# Test Case 3: Remove the top element
pq.remove()
print("Top element after removal:", pq.top())  # Expected output: "Task 3"