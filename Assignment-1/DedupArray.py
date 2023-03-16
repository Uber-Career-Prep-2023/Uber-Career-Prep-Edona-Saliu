"""
Time spent: 15 mins

Time complexity: O(n)

Space complexity: O(1)

Algorithm: 
- keep a counter for the number of unique values found
- When we see a unique value, move it to the position of the counter
- Go from the last point in the counter and replace the rest of the arr with -1

Edge cases: 
- Empty arr??
- arr not sorted?
"""
def DedupArray(arr):
    l = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[l] = arr[i]
            l += 1

    for i in range(l, len(arr)):
        arr[i] = -1

    return arr

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(DedupArray(arr))

# spent 10 mins
# def two_sum(arr, k):
#     nums = {}
#     count = 0
#     for num in arr:
#         nums[num] = nums.get(num, 0) + 1

#     for num in arr:
#         target = k - num
#         if target in nums:
#             if num == target:
#                 count += nums[num] - 1
#             else:
#                 count += nums[target]
#     return count//2

