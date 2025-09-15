# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
 
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1
 
# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0

        if len(height) == 0:
            return max_area

        l, r = 0, 1
        for l in range(len(height)):
            for r in range(l+1,len(height)):
                if height[l] >= height[r]:
                    area = (r-l)*height[r]  
                else:
                    area = (r-l)*height[l]
                    # l = r
                max_area = max(area, max_area)
                # r+=1
            
        return max_area
    
    def maxArea2(self, height: List[int]) -> int:

        max_area = 0

        if len(height) == 0:
            return max_area

        l, r = 0, len(height) - 1
        while l < r:
            area = (r-l) * min(height[l], height[r])
            max_area = max(area, max_area)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
     
        return max_area
    


# height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
height = [1,2,1]
sol = Solution()
result = sol.maxArea(height)
print(result)
result2 = sol.maxArea2(height)
print(result2)






        