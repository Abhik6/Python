# House Robbers
# Asked in Companies:

# Dell
# Quickr
# Amazon
# Ola


# Description:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. The only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and it will automatically contact the police if two adjacent houses are broken into on the same night.
# Given an integer array nums representing the amount of money at each house, return the maximum amount of money you can rob tonight without alerting the police.


# Input Parameters:
# nums (List[int]): An array representing the amount of money in each house.

# Output:
# Return an integer representing the maximum amount of money you can rob without triggering the alarm.

# Example:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total money robbed = 1 + 3 = 4.
 
 
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9), and rob house 5 (money = 1).
#              Total money robbed = 2 + 9 + 1 = 12.


def rob(nums):
    """
    Function to return the maximum amount of money that can be robbed without triggering the alarm.
                
    :param nums: List[int] -> List of money stashed in each house
    :return: int -> Maximum money robbed
    """
                                
    # even_sum = 0
    # odd_sum = 0

    # for i in range(len(nums)):
    #     if i%2==0:
    #         even_sum+=nums[i]
    #     else:
    #         odd_sum+=nums[i]

    n = len(nums)
    if n==1:
        return nums[0], nums[0]
    dp = [0]*n
    dp[n-1] = nums[n-1]
    dp[n-2] = nums[n-2]

    for i in range(n-3, -1, -1):
        amount = 0
        for j in range(i+2, n):
            amount = max(amount, dp[j])
        dp[i] = nums[i] + amount

    
    return max(dp[0], dp[1]), dp
        

    # return max(even_sum, odd_sum)
nums = [1]                                                   
# nums = [1,2,3,1]
# nums = [2,7,9,3,1]
result, dp = rob(nums)
print(result)
print(dp)