"""
Time spent: 10 mins

Time complexity: O(nlogn)

Space complexity: O(n)

Algorithm: 
- sort intervals
- make a new list for merged intervals
- go through each intervals and check if the intervals overlaps with the previous one in res
- If it does, merge them
- If not, append the new interval

Edge cases: 
- Same exact interval in the list??
- Empty list of intervals
"""
def MergeIntervals(intervals):
    intervals = sorted(intervals)
    res = [intervals[0]]
    for s, e in intervals[1:]:
        if res[-1][0] <= s <= res[-1][1]:
            new_e = max(e, res[-1][1])
            res[-1] = (res[-1][0], new_e)
        else:
            res.append((s, e))
    return res

intervals = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
# print(MergeIntervals(intervals))