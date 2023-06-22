"""
Question 11: VacationDestinations
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly from each other with corresponding travel times in hours, return the number of destinations within k hours of the origin. Assume that having a stopover in a city adds an hour of travel time.

"""

"""
Time complexity: O(V+E)
Space complexity: O(V+E)
Time spent: 25 mins
"""

from collections import deque

def vac_dest(src, k, edges):
    graph = {}
    for x, y, dist in edges:
        graph[x] = graph.get(x, [])
        graph[x].append((y, dist))
        graph[y] = graph.get(y, [])
        graph[y].append((x, dist))

    # for key in graph:
    #     print(f"{key}: {graph[key]}")

    q = deque([(src, k+1)])
    seen = set()
    num_dest = 0
    while q:
        node, dist_left = q.popleft()
        dist_left -= 1

        seen.add(node)

        for kid, dist in graph[node]:
            if (kid not in seen and
                dist_left >= dist):
                num_dest += 1
                q.append((kid, dist_left-dist))

    return num_dest

edges = [("Boston", "New York", 4), ("New York", "Philadelphia", 2),
         ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1),
         ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

vac_dest("New York", 8, edges)