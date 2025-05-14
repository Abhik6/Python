# Duplicate Number

# Asked in Companies:
# Morgan Stanley
# HSBC Bank
# Microsoft

# Description:
# You are given an integer array nums. Write a function that returns True if any value appears at least twice in the array and False if every element is distinct.
# Your task is to implement the solution using a hashmap (Python dictionary).

# Input Parameters:
# nums (List[int]): A list of integers.

# Output:
# bool: True if any value appears at least twice in the array, otherwise False.

# Example:

# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: True
 
# Input: nums = [1, 2, 3, 4]
# Output: False
 
# Input: nums = [1, 2, 3, 1]
# Output: True

def contains_duplicate(nums):
    """
    Function to check if the array contains any duplicate elements.
    :param nums: List[int] -> The input list of integers
    :return: bool -> True if duplicates exist, False otherwise
    """
    # TODO: Implement this function using a hashmap
    num_map = {}

    for index, elem in enumerate(nums):
        if elem in num_map:
            return True

        num_map[elem] = index

    return False 
