# Pascals Triangle 2
# Asked in Companies:

# Maq Software
# Ola
# Google


# Description:
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it. The triangle starts with a single 1 at the top, and each row contains one more element than the previous row.


# Input Parameters:
# rowIndex (int): The 0-based index of the row in Pascal's triangle to return (0 ≤ rowIndex ≤ 33).

# Output:
# Return the Pascal's triangle row as a list of integers.


# Example:

# Input: rowIndex = 3
# Output: [1, 3, 3, 1]
 
# Input: rowIndex = 0
# Output: [1]
 
# Input: rowIndex = 1
# Output: [1, 1]


def getRow(rowIndex):
    """
    Function to return the rowIndex-th row of Pascal's triangle.
    
    :param rowIndex: int -> Index of the row to return
    :return: List[int] -> The rowIndex-th row of Pascal's triangle
    """
    
    dp = [[1 for j in range(i+1)] for i in range(rowIndex+1)]
    for i in range(2,rowIndex+1):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    return dp[rowIndex]

rowIndex = 1
print(getRow(rowIndex))


