# Unique Paths II
# Description:
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.


# Parameters:
# grid (List[List[int]]): An m x n grid where grid[i][j] is either 0 (open space) or 1 (obstacle).


# Return Values:
# int: The number of possible unique paths from the top-left corner to the bottom-right corner avoiding obstacles.


# Example:

# Input: grid = [[0,0,0],[0,1,0],[0,0,0]] 
# Output: 2 
# Explanation: There are 2 unique paths from the top-left to the bottom-right corner.
 
# Input: grid = [[0,1,0],[0,0,0],[0,0,0]] 
# Output: 3
# Explanation: There are 3 unique path from the top-left to the bottom-right corner.


def uniquePathsWithObstacles(grid):

    m = len(grid)
    n = len(grid[0])
    if m==n==1 and grid[m-1][n-1]!= 1:
        return 1
    if m==1:
        if any(grid[0]):
            return 0
        else:
            return 1
    if n==1:
        if any([grid[i][0] for i in range(m)]):
            return 0
        else:
            return 1
    if grid[m-1][n-1]== 1 or grid[0][0]== 1:
        return 0
    
    dp = grid[:]
    dp = [[float('inf') if dp[i][j]==1 else dp[i][j] for j in range(n) ] for i in range(m)]
    print(dp)

    for elem in range(m-1):
        if grid[elem][n-1] == 1:
            continue
        elem_list = [dp[i][n-1] for i in range(elem+1, m-1)]
        if any(elem_list):
            dp[elem][n-1] = 0
        else:
            dp[elem][n-1] = 1
    
    for elem in range(n-1):
        if grid[m-1][elem] == 1:
            continue
        elem_list = [dp[m-1][j] for j in range(elem+1, n-1)]
        if any(elem_list):
            dp[m-1][elem] = 0
        else:
            dp[m-1][elem] = 1

    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            if dp[i][j]!= float('inf'):
                path_1_count = dp[i+1][j] if dp[i+1][j] != float('inf') else 0
                path_2_count = dp[i][j+1] if dp[i][j+1] != float('inf') else 0
                dp[i][j] = path_1_count + path_2_count

        
    return dp[0][0], dp
                

# grid = [[0,0,0],[0,1,0],[0,0,0]]
# grid = [[0,1,0],[0,0,0],[0,0,0]] 
grid = [[0,1],[0,0]]
# grid = [[0,0],[0,1]]
# grid = [[1]]
# grid = [[0]]
# grid = [[1,0],[0,0]]
# grid = [[0],[0]]
# grid = [[0],[1]]
# grid = [[1,0]]
# grid = [[0,1]]
# m= len(grid) 
# n = len(grid[0])
# print(m,n)
# print(grid[:][n-1])
print(uniquePathsWithObstacles(grid))