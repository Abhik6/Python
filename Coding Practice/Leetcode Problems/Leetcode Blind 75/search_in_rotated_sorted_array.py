# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1
 
# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        print(f"Left : {l}")
        print(f"Right : {r}")
        while l<=r:
            mid = (l+r)//2
            print(f"Mid : {mid}")
            # print(nums[mid])
            # print(nums[l])
            if nums[mid] == target:
                return mid
            
            # Left Sorted Portion
            if nums[mid] >= nums[l]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right Sorted Portion
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1 
                else:
                    r = mid - 1
                     
            print(f"Left : {l}")
            print(f'Right : {r}')

        return -1
    
# nums = [4,5,6,7,0,1,2]
# target = 0
# nums = [4,5,6,7,0,1,2]
# target = 3
# nums = [1] 
# target = 0
# nums = [3,1]
# target = 1
nums = [5,1,3]
target = 5
sol = Solution()
result = sol.search(nums, target)
print(result)
