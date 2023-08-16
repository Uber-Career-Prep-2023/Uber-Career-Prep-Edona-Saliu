'''
Time spent: 35 mins
Approach: DP, Tabulation
Time Complexity: O(n^2)
Space Complexity: O(n^2)
'''

def largestSquareOf1s(matrix):

    dimension = [[0]*len(matrix) for _ in range(len(matrix))]

    max_dimension = 0

    for i in range(len(matrix)):
        dimension[i][0] = matrix[i][0]
        dimension[0][i] = matrix[0][i]
        if dimension[i][0] == 1 or dimension[0][i] == 1:
            max_dimension = 1

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            if matrix[i][j] == 1:
                dimension[i][j] = min(dimension[i-1][j-1], dimension[i][j-1], dimension[i-1][j]) + 1
                max_size = max(max_dimension, dimension[i][j])

    return max_dimension

# Test case 1
matrix1 = [[0, 1, 1, 0, 1],
           [1, 1, 0, 1, 0],
           [0, 1, 1, 1, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1]]
print(largestSquareOf1s(matrix1))

# Test case 2
matrix2 = [[0, 1, 0, 0, 1],
           [1, 1, 1, 1, 0],
           [0, 1, 1, 1, 0],
           [1, 1, 1, 1, 0],
           [0, 0, 0, 0, 0]]
print(largestSquareOf1s(matrix2))

# Test case 3
matrix3 = [[1, 0, 1, 0, 1],
           [0, 1, 0, 1, 0],
           [1, 0, 1, 0, 1],
           [0, 1, 0, 1, 0],
           [1, 0, 1, 0, 1]]
print(largestSquareOf1s(matrix3))
