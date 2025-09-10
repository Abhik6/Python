# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 
# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

from typing import List
from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_list = list(nums)
        answers = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums_list)):
                if i!=j:
                    product*=nums_list[j]
            answers.append(product)
        
        return answers
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        answers = [1 for num in nums]

        for i in range(len(nums)):
            answers[i] = prefix
            prefix*=nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            answers[j]*=postfix
            postfix*=nums[j]
        
        return answers



        
        return answers
    
nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
sol = Solution()
result1 = sol.productExceptSelf(nums)
result2 = sol.productExceptSelf2(nums)
print(result1)
print(result2)


            