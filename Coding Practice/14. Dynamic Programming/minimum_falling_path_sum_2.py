# Minimum Falling Path Sum II

# Asked in companies:
# Apple
# Codenation
# Google
# Arcesium


# Description:
# Given an n×nn \times nn×n integer matrix grid, return the minimum sum of a falling path with non-zero shifts. A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.


# Parameters:
# grid (List[List[int]]): A 2D list where each inner list represents a row of the matrix.

# Return Values:
# int: The minimum sum of a falling path with non-zero shifts.


# Example:

# Input: grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
# Output: 13 
# Explanation: The minimum falling path sum with non-zero shifts is 1 → 5 → 7 with a total sum of 13.
 
# Input: grid = [[5, 1, 3], [2, 4, 6], [7, 8, 9]] 
# Output: 11
# Explanation: The minimum falling path sum with non-zero shifts is 1 → 4 → 9 with a total sum of 15.

def minFallingPathSum(grid):

    n = len(grid)
    if n == 1:
        return grid[0][0]
    dp = grid[:]

    for i in range(n-2, -1, -1):
        for j in range(n-1, -1, -1):
            # sum = float('inf')
            # if (j+1)<=(n-1):
            #     sum = min(sum, grid[i+1][j+1])
            # if (j-1)>=0:
            #     sum = min(sum, grid[i+1][j-1])
            # print(grid[i+1][0:j]+grid[i+1][j+1:n])
            sum = min(grid[i+1][0:j]+grid[i+1][j+1:n])
            
            dp[i][j] = sum + grid[i][j]

    return min(dp[0]), dp


# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
# grid = [[5, 1, 3], [2, 4, 6], [7, 8, 9]] 
grid = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
result, dp = minFallingPathSum(grid)
print(result)
print(dp)
# Expected: -192

