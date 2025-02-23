def find_last_index(arr, element, accum=-1, index=-1):
    """
    Function to find the last index of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    int: The last index of the element in the array, or -1 if not found.
    """
    # Your code here

    if len(arr) == 0:
        return index
    
    accum += 1 
    if arr[0] == element:
        index = accum
    return find_last_index(arr[1:], element, accum, index)




print(find_last_index([3,2,5,2,8,2,1], 2))
print(find_last_index([3,2,5,2,8,2,1], 3))
print(find_last_index([3,2,5,2,8,2,1], 10))
print(find_last_index([3,2,5,2,8,2,1], 1))

