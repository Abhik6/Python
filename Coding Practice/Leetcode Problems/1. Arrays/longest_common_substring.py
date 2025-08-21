# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
 
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common_prefix = ""
        if len(strs) == 0:
            return common_prefix

        first_elem = strs[0]
        is_matching = True
        for idx in range(len(first_elem)):
            current_char = first_elem[idx]
            for elem in strs[1:]:
                if idx > len(elem) - 1:
                    return common_prefix
                if current_char != elem[idx]:
                    is_matching = False
                    return common_prefix
            if is_matching:
                common_prefix +=current_char

        return common_prefix

    def longestCommonPrefix_alt(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""
        
        prefix = strs[0]

        for idx in range(1, len(strs)):
            curr_elem = strs[idx]
            while curr_elem.find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]
                if prefix == "":
                    return ""

        return prefix 


strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
sol = Solution()
result = sol.longestCommonPrefix(strs)
print(result)

result = sol.longestCommonPrefix_alt(strs)
print(result)

        