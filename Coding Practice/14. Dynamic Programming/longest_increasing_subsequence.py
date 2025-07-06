# Longest Increasing Subsequence
# Asked in Companies:

# Sharechat
# Acko
# Facebook

# Description:
# You are given an integer array nums. Your task is to return the length of the longest strictly increasing subsequence in the array. A subsequence is a sequence that can be derived by deleting some or no elements from the array without changing the order of the remaining elements.


# Input Parameters:
# nums (List[int]): A list of integers.

# Output:
# Return an integer representing the length of the longest strictly increasing subsequence.


# Example:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 
# Input: nums = [0,1,0,3,2,3]
# Output: 4

def longest_increasing_subsequence(arr):

    n = len(arr)
    lis = [1]*n

    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                lis[i] = max(lis[i], lis[j]+1)
    
    result = max(lis)

    return result

# nums = [10,9,2,5,3,7,101,18]
# nums = [7,7,7,7,7,7,7]
nums = [0,1,0,3,2,3]
print(longest_increasing_subsequence(nums))

    
