"""
Question 9: MergeKSortedArrays
Given an array of k sorted arrays, merge the k arrays into a single sorted array.

"""

"""
Time complexity: O(n log k) -> n(total number of ele) and k(number of arrays)
Space complexity: O(k) ->storing k elements
"""

import heapq

def mergeKSortedArrays(k, arrays):
    heap = []  # Initialize an empty heap
    result = []  # To store the merged sorted array

    # Populate the heap with the first element of each array
    for i in range(k):
        if arrays[i]:
            heap.append((arrays[i][0], i, 0))

    heapq.heapify(heap)  # Convert the list into a heap

    # Merge the sorted arrays using the heap
    while heap:
        value, array_index, index = heapq.heappop(heap)  # Pop the minimum value from the heap
        result.append(value)  # Append the value to the result

        if index + 1 < len(arrays[array_index]):
            # If there are more elements in the same array, push the next element to the heap
            heapq.heappush(heap, (arrays[array_index][index + 1], array_index, index + 1))

    return result  # Return the merged sorted array


print(mergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))