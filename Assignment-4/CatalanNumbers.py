'''
Time spent: 20 mins
Time Complexity: O(n^2)
Space Complexity: O(n)
'''

def catalanNumbers(n):
    catlan_number = [0 for _ in range(n+1)]
    catlan_number[0] = 1

    for i in range(1, n+1):
        for j in range(i):
            catlan_number[i] += catlan_number[j] * catlan_number[i-j-1]

    return catlan_number

print(catalanNumbers(1))  # Output: [1, 1]
print(catalanNumbers(5))  # Output: [1, 1, 2, 5, 14, 42]