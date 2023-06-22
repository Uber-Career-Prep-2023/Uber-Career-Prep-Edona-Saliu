"""
Question 2: Build a Heap
Write a min heap class according to the following API using an array as the underlying data structure. (A max heap has the same implementation; you simply need to flip the direction of the comparators.) For simplicity, you can assume that the heap holds integers rather than generic comparables.
"""

from math import floor

class MinHeap:
    def __init__(self):
        self.heap_list = []  # Initialize an empty list to store the heap elements

    def top(self):
        if len(self.heap_list) > 0:
            return self.heap_list[0]  # Return the minimum element at the top of the heap

    # Time Complexity: O(log(n)) (n = size of heap already)
    # Space Complexity: N/A or O(1) (input size can't change)
    def insert(self, value):
        self.heap_list.append(value)  # Insert the value at the rightmost bottom position of the heap
        i = len(self.heap_list) - 1

        # Bubble up the inserted value until its parent is smaller than it
        parent_i = floor((i - 1) / 2)
        while parent_i >= 0 and self.heap_list[parent_i] > self.heap_list[i]:
            self.heap_list[i] = self.heap_list[parent_i]  # Swap parent and child
            self.heap_list[parent_i] = value
            i = parent_i
            parent_i = floor((i - 1) / 2)

    # Time Complexity: O(log(n)) (n = size of heap already)
    # Space Complexity: N/A or O(1) (input size can't change)
    def delete(self):
        # Move the last element to the head
        self.heap_list[0] = self.heap_list[-1]
        del self.heap_list[-1]

        # Swap the head element with its smallest child
        i = 0
        child_left, child_right = i * 2 + 1, i * 2 + 2

        while child_left < len(self.heap_list) and child_right < len(self.heap_list):
            temp = self.heap_list[i]
            if self.heap_list[child_left] < self.heap_list[child_right]:
                self.heap_list[i] = self.heap_list[child_left]
                self.heap_list[child_left] = temp
                i = child_left
            else:
                self.heap_list[i] = self.heap_list[child_right]
                self.heap_list[child_right] = temp
                i = child_right

            child_left, child_right = i * 2 + 1, i * 2 + 2  # Update child indices

        # Handle the case where you must delete with one child out of range
        if child_left >= len(self.heap_list) and child_right < len(self.heap_list) and self.heap_list[
            child_right] < self.heap_list[i]:
            temp = self.heap_list[child_right]
            self.heap_list[child_right] = self.heap_list[i]
            self.heap_list[i] = temp
        if child_right >= len(self.heap_list) and child_left < len(self.heap_list) and self.heap_list[
            child_left] < self.heap_list[i]:
            temp = self.heap_list[child_left]
            self.heap_list[child_left] = self.heap_list[i]
            self.heap_list[i] = temp

    def return_list(self):  # for testing
        return self.heap_list