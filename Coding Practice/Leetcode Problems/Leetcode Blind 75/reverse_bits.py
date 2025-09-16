# Reverse bits of a given 32 bits signed integer.

# Example 1:
# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

# Example 2:
# Input: n = 2147483644
# Output: 1073741822
# Explanation:
# Integer	Binary
# 2147483644	01111111111111111111111111111100
# 1073741822	00111111111111111111111111111110

# Constraints:
# 0 <= n <= 231 - 2
# n is even.

# Follow up: If this function is called many times, how would you optimize it?

from typing import List 

class Solution:
    def reverseBits(self, n: int) -> int:
        bin = []
        while n:
            bin.append(n%2)
            n=n//2
        print(bin)
        res = 0
        idx = 0
        if len(bin)<32:
            idx+=(32-len(bin))
        for i in range(len(bin)-1,-1,-1):
            # print(i)
            res+=bin[i]*(2**idx)
            idx+=1

        return res

    def reverseBits2(self, n: int) -> int:
        bin = []
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            bin.append(bit)
            res = res | (bit << (32-i))
        print(bin)
        return res


n = 43261596
sol = Solution()
result = sol.reverseBits(n)
print(result) 
result2 = sol.reverseBits2(n)
print(result2) 


