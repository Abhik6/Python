# Count Even Odd
# Asked in Companies:

# Walmart
# Adobe
# Paypal

# Description:
# You are given an array ARR of integers of size N. Your task is to determine the following:
# The number of elements that occur an odd number of times in the array.
# The number of elements that occur an even number of times in the array.
# Your solution should make use of a hashmap (Python dictionary) to track the count of each element.

# Input Parameters:
# ARR (List[int]): A list of integers.
# N (int): The size of the array.

# Output:
# A tuple with two integers:
# The first integer is the count of elements that occur an odd number of times.
# The second integer is the count of elements that occur an even number of times.

# Example:

# Input: ARR = [1, 2, 3, 2, 3, 3]
# Output: (1, 2)
# Explanation: 
# - 1 occurs 1 time (odd), 2 occurs 2 times (even), 3 occurs 3 times (odd)
# - Number of elements occurring odd times = 2 (1, 3)
# - Number of elements occurring even times = 1 (2)
 
 
# Input: ARR = [5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7]
# Output: (1, 2)
# Explanation:
# - 5 occurs 6 times (even), 6 occurs 4 times (even), 7 occurs 1 time (odd)
# - Number of elements occurring odd times = 1 (7)
# - Number of elements occurring even times = 2 (5, 6)


def count_odd_even_occurrences(arr):
    """
    Function to count the number of elements that occur an odd number of times
    and the number of elements that occur an even number of times.
    
    :param ARR: List[int] -> The input list of integers
    :return: Tuple[int, int] -> A tuple containing two values:
             - The number of elements with odd occurrences
             - The number of elements with even occurrences
    """

    n = len(arr)
    count_freq = {}
    for i in range(n):
        count_freq[arr[i]] = count_freq.get(arr[i],0) + 1
        # if count_freq.get(arr[i]) is not None:
        #     count_freq[arr[i]] += 1
        # else:
        #     count_freq[arr[i]] = 1

    even = 0
    odd = 0
    for elem in count_freq.keys():
        if count_freq[elem] % 2 == 0:
            even+=1
        else:
            odd+=1
    
    return odd, even


