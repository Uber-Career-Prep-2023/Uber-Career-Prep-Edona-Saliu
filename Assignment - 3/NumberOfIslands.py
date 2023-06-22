"""
Question 4: NumberOfIslands
Given a binary matrix in which 1s represent land and 0s represent water. Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).

"""
"""
Time complexity: O(N)
Space complexity: O(N)
Time spent: 12 mins
"""

from collections import deque

def gen_kids(graph, x, y):
    n_r, n_c = len(graph), len(graph[0])
    all = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    kids = []
    for x1, y1 in all:
        if (0 <= x1 < n_r and
            0 <= y1 < n_c and
            graph[x1][y1] == 1):
            kids.append((x1, y1))
    return kids

def num_islands(graph):
    count = 0
    n_r, n_c = len(graph), len(graph[0])
    seen = set()
    for x in range(n_r):
        for y in range(n_c):
            if (x, y) in seen or graph[x][y] == 0:
                continue
            count += 1
            q = deque([(x, y)])
            while q:
                node = q.popleft()

                seen.add(node)

                for kid in gen_kids(graph, node[0], node[1]):
                    if kid not in seen:
                        q.append(kid)
    return count

matrix = [[1, 0, 1, 1, 1],
          [1, 1, 0, 1, 1],
          [0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0]]

ans = num_islands(matrix)
ans