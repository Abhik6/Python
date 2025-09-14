# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
 
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in res:
                        res.append(sorted([nums[i], nums[j], nums[k]]))
        
        return res
    
    # def threeSum2(self, nums: List[int]) -> List[List[int]]:

    #     res = []
    #     hashset = set(nums)

    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if -(nums[i] + nums[j]) in hashset \
    #             and sorted([nums[i], nums[j], -(nums[i]+nums[j])]) \
    #             not in res and (nums[i] != -(nums[i] + nums[j]) and nums[j] != -(nums[i] + nums[j])):
    #                 res.append(sorted([nums[i], nums[j], -(nums[i]+nums[j])]))
        
    #     return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:

        res = []
        sorted_nums = sorted(nums)
        print(sorted_nums)

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            l, r = i+1, len(sorted_nums)-1
            while l < r:
                print(f"Left : {l}")
                print(f"Right : {r}")
                sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                print(f"Sum : {sum}")
                print()
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    res.append([sorted_nums[i],sorted_nums[l],sorted_nums[r]])
                    l+=1
                    while sorted_nums[l] == sorted_nums[l-1] and l < r:
                        l+=1
        
        return res

    def threeSum3(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        print(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                print(f"Left : {l}")
                print(f"Right : {r}")
                sum = nums[i] + nums[l] + nums[r]
                print(f"Sum : {sum}")
                print()
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        
        return res

# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
nums = [0,0,0]
sol = Solution()
result1 = sol.threeSum(nums)
print(result1)
result2 = sol.threeSum2(nums)
print(result2)
result3 = sol.threeSum3(nums)
print(result3)




