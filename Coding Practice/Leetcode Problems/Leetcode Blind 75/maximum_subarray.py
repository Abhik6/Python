# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        sum = 0

        for elem in nums:
            sum+=elem

            if sum > max_sum:
                max_sum = sum
            
            if sum < 0:
                sum = 0

        return max_sum
    
    def maxSubArray2(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for elem in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum+=elem

            max_sum = max(curr_sum, max_sum)
            
        return max_sum
    
nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [5,4,-1,7,8]
sol = Solution()
result1 = sol.maxSubArray(nums)
print(result1)
result2 = sol.maxSubArray2(nums)
print(result2)

    