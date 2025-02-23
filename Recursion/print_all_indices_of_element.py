def find_indices_helper(arr, element, index, lst):
    if len(arr) == index:
        return lst
    
    if arr[index] == element:
        lst.append(index)

    return find_indices_helper(arr, element, index+1, lst)

def find_indices(arr, element):
    """
    Function to find all indices of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    list of int: A list containing all indices of the element in the array.
    """
    # Your code here

    return find_indices_helper(arr, element, 0, [])

print(find_indices([2,3,4,5,2,3,4], 2))
print(find_indices([2,3,4,5,2,3,4], 4))
print(find_indices([2,3,4,5,2,3,4], 3))
print(find_indices([2,3,4,5,2,3,4], 8))
