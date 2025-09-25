# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

# "1" -> 'A'
# "2" -> 'B'
# ...
# "25" -> 'Y'
# "26" -> 'Z'

# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

# For example, "11106" can be decoded into:
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.

# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.
# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation:
# "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation:
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
# Input: s = "06"
# Output: 0
# Explanation:
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

# Constraints:
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

class Solution:

    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.numDecodings_helper(s, memo)

    def numDecodings_helper(self, s: str, memo: dict) -> int:

        print(f"String : {s}")

        if len(s) == 1 and s[0] != '0':
            return 1
        
        if len(s)==0 or s[0] == '0':
            return 0
        
        if s in memo:
            return memo[s]
        
        if len(s)>1:
            num_decodings = self.numDecodings(s[1:])
            # num_decodings+=1
            print(f"Single Number: {num_decodings}")
        
        if len(s)>=2:
            if int(s[0:2]) <= 26:
                if len(s)>2:
                    num_decodings+= self.numDecodings(s[2:])
                else:
                    num_decodings+=1
                print(f"Double Number: {num_decodings}")
        
        # num_decodings+=1
        print(f"Final Number : {num_decodings}")
        memo[s] = num_decodings
        
        return num_decodings

    def numDecodings2(self, s: str) -> int:
        
        dp = [0 for _ in range(len(s)+1)]
        dp[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if i + 1 <= len(s)-1 and int(s[i:i+2]) >= 1 and int(s[i:i+2]) <= 26:
                dp[i]+= dp[i+2]
        
        return dp[0]


s = "12"  
# s = "226"  
# s = "06"
sol = Solution()
result = sol.numDecodings(s)
print(result)
result2 = sol.numDecodings2(s)
print(result2)
# print(dp)
        





