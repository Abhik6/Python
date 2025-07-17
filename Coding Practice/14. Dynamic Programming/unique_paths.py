# Unique Paths

# Asked in companies:
# Uber
# Adobe
# SAP Labs
# Amazon

# Description:
# There is a robot on an m x n grid. The robot starts at the top-left corner (i.e., grid[0][0]) and aims to reach the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Parameters:
# m (int): Number of rows in the grid.
# n (int): Number of columns in the grid.

# Return Values:
# int: The number of possible unique paths from the top-left corner to the bottom-right corner.


# Example:

# Input: m = 3, n = 7 
# Output: 28 
# Explanation: There are 28 unique paths from the top-left to the bottom-right corner.
 
 
# Input: m = 3, n = 2 
# Output: 3 
# Explanation: There are 3 unique paths from the top-left to the bottom-right corner.


def uniquePaths(m, n):

    dp = [[1]*n for _ in range(m)]
    # print(dp)

    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]

    return dp[0][0], dp

# m = 3 
# n = 7 
m=3
n=2
result, dp = uniquePaths(m,n)
print(result)
print(dp)