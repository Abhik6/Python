# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

# Constraints:

# 1 <= n <= 231 - 1
 

# Follow up: If this function is called many times, how would you optimize it?

from typing import List

class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0
        while n > 0:
            rem = n%2
            if rem == 1:
                count+=1
            n = n//2
        return count
    
    def hammingWeight2(self, n: int) -> int:
        count = 0
        while n:
            count+= n%2
            n = n >> 1
        return count
    
    def hammingWeight3(self, n: int) -> int:
        count = 0
        while n:
            n= n & (n-1)
            # print(n)
            count+=1
        
        return count


# n = 11
n = 128
# n = 2147483645
sol = Solution()
result = sol.hammingWeight(n)
print(result)
result2 = sol.hammingWeight2(n)
print(result2)
result3 = sol.hammingWeight3(n)
print(result3)
