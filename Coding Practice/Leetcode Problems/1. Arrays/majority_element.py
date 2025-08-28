# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 
# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums_freq = {}
        for elem in nums:
            if elem in nums_freq:
                nums_freq[elem]= nums_freq.get(elem,0)+1
            else:
                nums_freq[elem]= 1

        print(nums_freq)
        max_count = 0
        major_elem = None
        for elem, count in nums_freq.items():
            if max_count < count:
                max_count = count
                major_elem = elem
        
        return major_elem

# nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
sol = Solution()
result = sol.majorityElement(nums)
print(result)

        