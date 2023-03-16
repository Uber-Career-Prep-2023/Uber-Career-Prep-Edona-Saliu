"""
Time spent: 20 mins

Time complexity: O(n)

Space complexity: O(n)

Algorithm: 
- Keep track of the sum of each prefix in an array
- If I encounter a prefix with the same sum as another previous prefix
then I have found a subarray with a sum of zero
- I initialize the dictionary of prefixes with a 0 sum prefix since [] is also a prefix

Edge cases: 
- 
"""
def ZeroSumSubArrays(nums):
    prefix_sums = {0: 1}
    curr_sum = 0
    count = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum in prefix_sums:
            count += prefix_sums[curr_sum]
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

    return count

nums = [4, 5, 2, -1, -3, -3, 4, 6, -7]
# print(ZeroSumSubArrays(nums))