"""
Question 1: Build an Adjacency List/Set Representation of a Graph
Given an array of pairs of values representing edges in an unweighted graph, create the equivalent adjacency list/set representation (a map from element to a list or set of elements). Pairs represent directed edges: (A, B) means there is an edge from A to B. If the pair (B, A) is also provided then there is an undirected edge between A and B. For simplicity, you may assume that each node of the graph stores an integer rather than a generic data type and that the elements are distinct. Implement a basic DFS and BFS searching for a target value and a topological sort (using either DFS or Kahn’s algorithm).

"""

"""
Time complexity: O(N)
Space complexity: O(N)
Time spent: 5 mins
"""
def to_adj_list(lst_edges):
    graph = {}
    for x, y in lst_edges:
        graph[x] = graph.get(x, [])
        graph[x].append(y)
        graph[y] = graph.get(y, [])
    return graph

"""
Time complexity: O(V+E)
Space complexity: O(V)
Time spent: 6 mins
"""

from collections import deque

#bredth first search
def bfs(target, graph):
    nodes = graph.keys()
    seen = set()
    for node in nodes:
        if node in seen:
            continue

        q = deque([node])
        while q:
            node = q.popleft()
            seen.add(node)

            if node == target:
                return True

            for kid in graph[node]:
                if kid not in seen:
                    q.append(kid)
    return False

#depth first search
def dfs(target, graph):
    nodes = graph.keys()
    seen = set()
    for node in nodes:
        if node in seen:
            continue

        stack = [node]
        while stack:
            node = stack.pop()
            seen.add(node)

            if node == target:
                return True

            for kid in graph[node]:
                if kid not in seen:
                    stack.append(kid)
    return False

lst_edges = [(1, 2), (2, 3), (1, 3), (3, 2), (5, 0)]
bfs(0, to_adj_list(lst_edges))
