"""
Question 8: AlternatingPath
Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length of the shortest path from the origin to the destination in which the edges traversed alternate in color. Return -1 if no such path exists.

"""

"""
Time complexity: O(V+E)
Space complexity: O(V+E)
Time spent: 21 mins
"""

from collections import deque

def alt_path(edges, src, dest):
    graph = {}
    for x, y, color in edges:
        graph[x] = graph.get(x, [])
        graph[x].append((y, color))
        graph[y] = graph.get(y, [])

    for key in graph:
        print(f"{key}: {graph[key]}")

    q = deque([(src, None, 0)])
    seen = set()
    while q:
        node, prev_color, path_len = q.popleft()

        seen.add((node, prev_color))
        if node == dest:
            return path_len

        for kid, color in graph[node]:
            if ((kid, color) not in seen and
                color != prev_color):
                q.append((kid, color, path_len+1))
    return -1

edges = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"),
         ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"),
         ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]

print(alt_path(edges, "E", "D"))
print(alt_path(edges, "A", "E"))