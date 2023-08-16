'''
Time spent: 40 mins
Data Structure and Algorithm: minHeap and maxHeap.
Technique: Maintain two heaps
Time Complexity: O(log n)
Space Complexity: O(n)
'''

import heapq

class RunningMedian:
    def __init__(self):
        self.maxh = []  # stores the smaller half
        self.minh = []  # stores the larger half

    def addNumber(self, n):
        if len(self.maxh) == 0 or num < -self.maxh[0]:
            heapq.heappush(self.maxh, -n)  # push into maxh
        else:
            heapq.heappush(self.minh, n)  # push into minh

        if len(self.maxh) > len(self.minh) + 1:
            move = -heapq.heappop(self.maxh)
            heapq.heappush(self.minh, move)
        elif len(self.maxh) < len(self.minh):
            move = heapq.heappop(self.minh)
            heapq.heappush(self.maxh, -move)

    def findMedian(self):
        if len(self.maxh) == len(self.minh):
            return (-self.maxh[0] + self.minh[0]) / 2.0
        else:
            return -self.maxh[0] 

runningMedian = RunningMedian()
numbers = [9, 3, 7, 2, 8, 5]
for num in numbers:
    runningMedian.addNumber(num)
    print(runningMedian.findMedian())

runningMedian = RunningMedian()
numbers = [5, 15, 10, 20, 25]
for num in numbers:
    runningMedian.addNumber(num)
    print(runningMedian.findMedian())
