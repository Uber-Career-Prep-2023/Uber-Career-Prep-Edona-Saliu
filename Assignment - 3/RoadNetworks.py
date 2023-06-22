"""
Question 6: RoadNetworks
In some states, it is not possible to drive between any two towns because they are not connected to the same road network. Given a list of towns and a list of pairs representing roads between towns, return the number of road networks. (For example, a state in which all towns are connected by roads has 1 road network, and a state in which none of the towns are connected by roads has 0 road networks.)

"""

"""
Time complexity: O(V+E)
Space complexity: O(V+E)
Time spent: 27 mins
"""

from collections import deque

def road_networks(cities, roads):
    graph = {}
    for city in cities:
        graph[city] = []

    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    # for key in graph:
    #     print(f"{key}: {graph[key]}")

    city_clumps = 0
    seen = set()
    for city in cities:
        if city in seen or not graph[city]:
            continue
        city_clumps += 1
        q = deque([city])
        while q:
            node = q.popleft()

            seen.add(node)

            for kid in graph[node]:
                if kid not in seen:
                    q.append(kid)
    return city_clumps

cities = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay",
          "Fairbanks", "McCarthy", "Copper Center", "Healy", "Anchorage"]

roads = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"),
("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"),
("Healy", "Anchorage")]

road_networks(cities, roads)