# Minimum cost to climb stairs
# Asked in Companies:

# Oyo
# Squadstack
# Byjus


# Description:
# You are given an integer array cost where cost[i] is the cost of the i-th step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor.


# Input Parameters:
# cost (List[int]): An array of integers where cost[i] represents the cost of the i-th step. (2 ≤ len(cost) ≤ 1000)

# Output:
# Return the minimum cost to reach the top of the floor (int).


# Example:

# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
 
 
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: You will start at index 0.
# - Climb one step to index 2, pay 1.
# - Climb two steps to index 4, pay 1.
# - Climb two steps to index 6, pay 1.
# - Climb one step to index 7, pay 1.
# - Climb two steps to index 9, pay 1.
# - Climb one step to reach the top.

def minCostClimbingStairs(cost):
    """
    Function to calculate the minimum cost to reach the top of the staircase.
                
    :param cost: List[int] -> The cost associated with each step
    :return: int -> Minimum cost to reach the top
    """
    n = len(cost)
    dp = [0]*(n)

    dp[n-1] = cost[n-1] 

    for i in range(n-2, -1, -1):
        if (i+2)<=(n-1):
            two_step_cost = dp[i+2]
        else:
            two_step_cost = 0

        one_step_cost = dp[i+1]

        dp[i] = cost[i] + min(two_step_cost, one_step_cost)

    result = min(dp[0], dp[1])

    return result, dp

                                                                                                            

# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
cost = [10,15,20]
result, dp = minCostClimbingStairs(cost)
print(result)
print(dp)
