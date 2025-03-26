def linear_search(arr, target, index):
    """
    Function to perform linear search on an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    target (int): The element to search for.
    
    Returns:
    bool: True if target is found, False otherwise.
    """
    # Your code here

    if len(arr) == index:
        return False
    
    if arr[index] == target:
        return True
    
    return linear_search(arr, target, index+1)

print(linear_search([2,3,4,5,6,2], 3, 0))
print(linear_search([2,3,4,5,6,2], 5, 0))
print(linear_search([2,3,4,5,6,2], 6, 0))
print(linear_search([2,3,4,5,6,2], 10, 0))
    
