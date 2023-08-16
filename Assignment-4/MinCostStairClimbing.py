'''
Time spent: 20 mins
Approach: Dynamic Programming
Time Complexity:  O(n)
Space Complexity: O(n)
'''

def minCostStairClimbing(costs):
    if len(costs) == 1 or len(costs) == 2:
        return min(costs)
    cache = [0] * len(costs)
    cache[0], cache[1] = costs[0], costs[1]
    for i in range(2, len(costs)):
        cache[i] = min(cache[i-1], cache[i-2]) + costs[i]
    return min(cache[-1], cache[-2])

# Test Cases
print(minCostStairClimbing([10, 15, 20]))  # Should output 15 (Climb steps 1, 3)
print(minCostStairClimbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # Should output 6 (Climb steps 1, 3, 5, 7, 10)
print(minCostStairClimbing([0, 1, 2, 2]))  # Should output 2 (Climb steps 1, 3)
print(minCostStairClimbing([0, 2, 2, 1]))  # Should output 2 (Climb steps 1, 3)
print(minCostStairClimbing([2, 1, 3, 4, 1, 2]))  # Should output 6 (Climb steps 1, 3, 5)
