"""
Time spent: 10 mins

Time complexity: O(n)

Space complexity: O(n)

Algorithm: 
- for each number in arr, find the number that it needs to be added to to sum to k
- check how many of that number exist in the hash map of counts
- increment the counter by that value
- increment (or instantiate) the count of that specific number in the hash map
- return the count after looping through all nums in arr

Edge cases: 
- Empty arr??
- arr not sorted?
"""
def TwoSum(arr, k):
    nums = {}
    count = 0
    for num in arr:
        target = k - num
        if target in nums:
            count += nums[target]
        nums[num] = nums.get(num, 0) + 1
    return count

arr, k = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 4
print(TwoSum(arr, k))