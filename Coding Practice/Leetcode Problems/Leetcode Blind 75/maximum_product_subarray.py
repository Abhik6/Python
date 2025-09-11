# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Constraints:
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_product = nums[0]
        # curr_product = 1

        # for num in nums:
        #     curr_product*=num
        #     max_product = max(curr_product, max_product)

        #     if num == 0:
        #         curr_product = 1
        
        # return max_product

        res = max(nums)
        curr_max, curr_min = 1, 1
        i = 0

        for num in nums:
            tmp = curr_max * num
            curr_max = max((curr_max * num),(curr_min * num), num)
            curr_min = min(tmp,(curr_min * num), num)
            res = max(res, curr_max)
            print(f"Index : {i}")
            print(f"Current Max : {curr_max}")
            print(f"Current Min : {curr_min}")
            if num == 0:
                curr_max, curr_min = 1, 1
            
            i+=1
        
        return res

nums = [2,3,-2,4]  
# nums = [-2,0,-1]
# nums = [-3,-1,-1]
# nums = [3,-1,4]
sol = Solution()
result = sol.maxProduct(nums)
print(result)