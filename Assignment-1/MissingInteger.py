"""
Time spent: 25 mins

Time complexity: O(logn)

Space complexity: O(1)

Algorithm: 
- Binary search
- I chose which half to search based on whether the difference between the index of the 
start and end of the half is less than the difference of the numbers at that index
- If for both halves the differences are equal (for the positions and values), then
the missing value must be the average of the end value of the left half and start value
of the right

Edge cases: 
- More than one missing number?
- If the missing number is at the start or end
- No missing number?
"""
def MissingInteger(arr, n):
    if arr[-1] != n:
        return n
    if arr[0] != 1:
        return 1

    f, l = 0, n-2
    while f < l:
        m = (f + l)//2
        if arr[m] - arr[f] > m-f:
            l = m
        elif arr[l] - arr[m+1] > l-(m+1):
            f = m+1
        else:
            return (arr[m] + arr[m+1])//2
    return -1

arr, n = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12], 12
# print(MissingInteger(arr, n))
