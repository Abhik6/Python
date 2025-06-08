# Greatest Number Product
# Asked in Companies:
# Linkedin
# Amazon

# Description:
# You are given an array ARR of integers. Your task is to find the greatest number in the array such that this number is also equal to the product of two different elements from the same array.

# Input Parameters:
# ARR (List[int]): A list of integers.

# Output:
# An integer which is the greatest number that is also the product of two different elements in the array. If no such number exists, return -1.

# Example:

# Input: ARR = [1, 2, 3, 6, 12]
# Output: 12
# Explanation: The number 12 is present in the array and it is the product of 2 and 6.
 
# Input: ARR = [4, 2, 3, 8]
# Output: 8
# Explanation: The number 8 is present in the array and it is the product of 2 and 4.


def greatest_product_equal_to_element(arr):
    """
    Function to find the greatest number in the array that is equal to the product of two different elements.
    
    :param arr: List[int] -> The input list of integers
    :return: int -> The greatest number in the array that is equal to the product of two different elements
    """
    # TODO: Implement the logic using a hashmap approach
    num_map = {}
    for index, elem in enumerate(arr):
        num_map[elem] = index
    
    max_product = -1
    for i in range(len(arr)):
        elem = arr[i]
        for j in range(i+1, len(arr)):
            product = elem*arr[j]
            if product in num_map:
                max_product = max(max_product, product)
    
    return max_product


ARR = [1, 2, 3, 6, 12]
print(greatest_product_equal_to_element(ARR))

ARR = [4, 2, 3, 8]
print(greatest_product_equal_to_element(ARR))

