# Triangle Array
# Asked in companies:

# Flipkart
# Ola
# Toluna


# Description:
# Given a triangle array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


# Parameters:
# triangle (List[List[int]]): A list of lists where each inner list represents a row in the triangle.

# Return Values:
# int: The minimum path sum from the top to the bottom of the triangle.


# Example:

# Input: triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]] 
# Output: 11 
# Explanation: The path with the minimum sum is 2 → 3 → 5 → 1, which sums to 11.
 
 
# Input: triangle = [[-10]] 
# Output: -10 
# Explanation: There is only one element in the triangle.

def minimumTotal(triangle):

    n = len(triangle)
    if n == 1:
        return triangle[0][0]

    dp = [[triangle[i][j] for j in range(0,i+1)] for i in range(n)]

    for i in range(n-2, -1, -1):
        for j in range(i, -1, -1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])

    return dp[0][0]



triangle = [[-10]] 
# triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]] 
print(minimumTotal(triangle))

