# Climbing Stairs
# Asked in Companies:

# Infosys
# Accenture
# Morgan Stanley

# Description:
# You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 step or 2 steps. In how many distinct ways can you climb to the top?

# Input Parameters:
# n (int): The total number of steps required to reach the top (1 ≤ n ≤ 45).

# Output:
# Return the number of distinct ways to reach the top (int).

# Example:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
 
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbStairs(n):
    """
    Function to calculate the number of distinct ways to climb 'n' steps.
    
    :param n: int -> Total number of steps
    :return: int -> Number of distinct ways to climb to the top
    """
    
    if n == 1:
        return 1
    
    dp = [0]*(n)
    dp[n-1] = 1
    dp[n-2] = 2

    for i in range(n-3, -1, -1):
        one_step_paths = dp[i+1]
        two_step_paths = dp[i+2]

        dp[i] = one_step_paths + two_step_paths

    return dp[0]

n = 1
result= climbStairs(n)
print(result)
# print(dp)
