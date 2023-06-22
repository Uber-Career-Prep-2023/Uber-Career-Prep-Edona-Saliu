"""
Question 5: FirstKBinaryNumbers
Given a number, k, return an array of the first k binary numbers, represented as strings.

"""

"""
Time complexity: O(N)
Space complexity: O(N)
Time spent: 6 min
"""

from collections import deque

def first_k_bin(n):
    if n == 0:
        return []

    ans = ["0"]
    q = deque(["1"])
    for i in range(n-1):
        node = q.popleft()
        ans.append(node)

        q.append(node + "0")
        q.append(node + "1")
    return ans

lst = first_k_bin(7)
lst