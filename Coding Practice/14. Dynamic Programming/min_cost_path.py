"""
You have a cost matrix called cost[][], and you need to find the minimum cost 
to reach a specific position (M, N) starting from the top-left corner (0, 0).

Each cell in the matrix has a cost that you need to add up to get the total cost 
for the path you take. You can only move down, to the right, or diagonally 
down-right from any cell. 

Keep in mind that all costs are positive integers.
"""

def min_cost_path_recursion(cost_matrix, M, N, func):

    func[M][N]+=1 

    if M == 0 and N == 0:
        return cost_matrix[M][N]
    
    if M < 0 or N < 0:
        return float('inf')
    
    cost_top = min_cost_path_recursion(cost_matrix, M-1, N, func)

    cost_left = min_cost_path_recursion(cost_matrix, M, N-1, func)

    cost_diagonal = min_cost_path_recursion(cost_matrix, M-1, N-1, func)

    min_cost = cost_matrix[M][N] + min(cost_top, cost_left, cost_diagonal)

    return min_cost


def min_cost_path_memoization(cost_matrix, M, N, memo, func):

    
    if M == 0 and N == 0:
        memo[M][N] = cost_matrix[M][N]
        return cost_matrix[M][N]
    
    func[M][N]+=1
    
    if M < 0 or N < 0:
        return float('inf')
    
    if memo[M][N-1] != 0:
        cost_left = memo[M][N-1]
    else:
        cost_left = min_cost_path_memoization(cost_matrix, M, N-1, memo, func)

    if memo[M-1][N-1] != 0:
        cost_diagonal = memo[M-1][N-1]
    else:
        cost_diagonal = min_cost_path_memoization(cost_matrix, M-1, N-1, memo, func)
    
    if memo[M-1][N] != 0:
        cost_top = memo[M-1][N]
    else:
        cost_top = min_cost_path_memoization(cost_matrix, M-1, N, memo, func)
    
    min_cost = cost_matrix[M][N] + min(cost_top, cost_left, cost_diagonal)
    memo[M][N] = min_cost

    return min_cost

    
def min_cost_path_tabulation(cost_matrix, M, N):

    dp = [[0 for _ in range(len(cost_matrix))] for _ in range(len(cost_matrix))]

    dp[0][0] = cost_matrix[0][0]

    for row in range(1, len(cost_matrix)):
        dp[row][0] = dp[row-1][0] + cost_matrix[row][0]

    for column in range(1, len(cost_matrix)):
        dp[0][column] = dp[0][column-1] + cost_matrix[0][column]

    for row in range(1, len(cost_matrix)):
        for col in range(1, len(cost_matrix)):
            cost_left = dp[row][col-1]
            cost_diag = dp[row-1][col-1]
            cost_top = dp[row-1][col]
            
            dp[row][col] = cost_matrix[row][col] + min(cost_left, cost_diag, cost_top)
    
    return dp[M][N], dp


cost_matrix = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]
M, N = 2, 2
func = [[0 for _ in range(len(cost_matrix))] for _ in range(len(cost_matrix))]
print(func)
print(f"Minimum cost to reach ({M}, {N}) using Recursion: {min_cost_path_recursion(cost_matrix, M, N,func)}")
print(func)

print()

func = [[0 for _ in range(len(cost_matrix))] for _ in range(len(cost_matrix))]
memo = [[0 for _ in range(len(cost_matrix))] for _ in range(len(cost_matrix))]
print("func:",func)
print("memo:",memo)
print(f"Minimum cost to reach ({M}, {N}) using Memoization: {min_cost_path_memoization(cost_matrix, M, N, memo, func)}")
print("func:",func)
print("memo:",memo)

print()

min_cost, dp = min_cost_path_tabulation(cost_matrix, M, N)
print(f"Minimum cost to reach ({M}, {N}) using Tabulation: {min_cost}")
print(dp)
