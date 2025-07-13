# Minimum Falling Path Sum
# Asked in companies:

# Google
# Uber
# Zomato
# TRC


# Description:
# Given an n×nn \times nn×n array of integers matrix, return the minimum sum of any falling path through the matrix. A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


# Parameters:
# matrix (List[List[int]]): A 2D list where each inner list represents a row of the matrix.

# Return Values:
# int: The minimum sum of any falling path through the matrix.


# Example:

# Input: matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]] 
# Output: 13 
# Explanation: The minimum path sum is 2 → 1 → 4 → 6 with a total sum of 13.
 
# Input: matrix = [[-19, 57], [-40, -5]] 
# Output: -59 
# Explanation: The minimum path sum is -19 → -40 → -5 with a total sum of -59.


def minFallingPathSum(matrix):

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    
    dp = matrix.copy()

    for i in range(n-2,-1,-1):
        for j in range(n-1, -1, -1):
            # print(i)
            # print(j)
            sum = matrix[i+1][j]
            if (j+1)<=(n-1):
                sum = min(sum, matrix[i+1][j+1])
            if (j-1)>=0:
                sum = min(sum, matrix[i+1][j-1])
            dp[i][j] = sum + matrix[i][j]
    
    return min(dp[0]), dp

# matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]] 
matrix = [[-19, 57], [-40, -5]] 
result, dp = minFallingPathSum(matrix)

print(result)
print(dp)