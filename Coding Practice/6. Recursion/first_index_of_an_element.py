def find_first_index(arr, element):
    """
    Function to find the first index of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    int: The first index of the element in the array, or -1 if not found.
    """
    # Your code here

    if len(arr) == 0:
        return -1
    
    if arr[0] == element:
        return 0
    
    returned_index = find_first_index(arr[1:], element)

    if returned_index == -1:
        return returned_index
    else:
        return returned_index + 1
    
print(find_first_index([3,2,5,2,8,2,1], 2))
print(find_first_index([3,2,5,2,8,2,1], 3))
print(find_first_index([3,2,5,2,8,2,1], 10))
print(find_first_index([3,2,5,2,8,2,1], 1))

