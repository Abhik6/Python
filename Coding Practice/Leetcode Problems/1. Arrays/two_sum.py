# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup_dict = {nums[i]: i for i in range(len(nums))}
        
        for idx in range(len(nums)):
            diff = target - nums[idx]
            match_idx = lookup_dict.get(diff)
            if match_idx is not None and match_idx != idx:
                return [idx, match_idx]

# nums = [2,7,11,15]
# target = 9
# nums = [3,2,4] 
# target = 6
nums = [3,3]
target = 6
sol = Solution()
result = sol.twoSum(nums,target)
print(result)