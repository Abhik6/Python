# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation:
# All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 
# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set(nums)
        if len(nums) == len(unique_nums):
            return False

        return True
    
    def containsDuplicate_alt(self, nums: List[int]) -> bool:
        nums_dict = {}
        for elem in nums:
            if nums_dict.get(elem,0)!=0:
                return True
            nums_dict[elem] = 1

        return False

nums = [1,2,3,1] 
# nums = [1,2,3,4]  
# nums = [1,1,1,3,3,4,3,2,4,2] 
sol = Solution()
result = sol.containsDuplicate(nums)
result1 = sol.containsDuplicate_alt(nums)
print(result)
print(result1)