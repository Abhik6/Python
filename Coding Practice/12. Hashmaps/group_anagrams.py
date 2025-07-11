# Group Anagrams
# Asked in Companies:

# Intuit
# Expedia Group
# BNY
# Infosys

# Description
# You are given an array of strings strs. Your task is to group the anagrams together and return the result. An anagram is a word formed by rearranging the letters of another, using all the original letters exactly once.

# Input:
# strs: A list of strings.

# Output:
# Return a list of lists, where each list contains strings that are anagrams of each other. The order of the output and the order of the strings within each group does not matter.

# Example:

# Input:
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
 
# Output:
# [
#   ["eat", "tea", "ate"],
#   ["tan", "nat"],
#   ["bat"]
# ]
 
 
# Input:
# strs = [""]
 
# Output:
# [
#   [""]
# ]
 
 
# Input:
# strs = ["a"]
 
# Output:
# [
#   ["a"]
# ]

def group_anagrams(strs):
    # Core logic for the learner to implement
    anagram_map = {}

    for word in strs:
        sorted_word = sorted(word)
        sorted_word = ''.join(sorted_word)
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]
    result = []    
    for values in anagram_map.values():
        result.append(values)
    
    return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))


