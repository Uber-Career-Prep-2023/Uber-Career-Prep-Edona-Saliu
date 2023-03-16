"""
Time spent: 10 mins

Time complexity: O(n)

Space complexity: O(1)

Algorithm: 
- Find the sum of the first k numbers
- Keep track of the max average seen using a variable
- loop over the remaining numbers in the arr
- add each to the curr sum and remove the number at the other end of the window
- re-evaluate the max average
- return the max average

Edge cases: 
- What if k is negative?
- What if k is 0?
- What if k > len(arr)?
- What if arr is empty?
"""
def MaxMeanSubArray(arr, k):
    window_sum = sum(arr[:k])
    max_avg = window_sum/k
    for i in range(len(arr)-k):
        window_sum += arr[i+k] - arr[i]
        avg = window_sum/k
        max_avg = max(max_avg, avg)
    return max_avg

arr, k = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5
# print(MaxMeanSubArray(arr, k))