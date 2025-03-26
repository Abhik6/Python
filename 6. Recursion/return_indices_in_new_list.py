def return_indices_in_new_list(arr, element, index):
    """
    Function to find all indices of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    list of int: A list containing all indices of the element in the array.
    """
    # Your code here

    if len(arr) == index:
        return []
    
    ans_lst = return_indices_in_new_list(arr, element, index+1)

    if arr[index] == element:
        ans_lst.insert(0,index)

    return ans_lst

def return_indices_in_new_list_reverse(arr, element, index):
    """
    Function to find all indices of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    list of int: A list containing all indices of the element in the array.
    """
    # Your code here

    if len(arr) == index:
        return []
    
    ans_lst = return_indices_in_new_list_reverse(arr, element, index+1)

    if arr[index] == element:
        ans_lst.append(index)

    return ans_lst


print(return_indices_in_new_list([2,3,4,5,2,3,4], 2, 0))
print(return_indices_in_new_list([2,3,4,5,2,3,4], 4, 0))
print(return_indices_in_new_list([2,3,4,5,2,3,4], 3, 0))
print(return_indices_in_new_list([2,3,4,5,2,3,4], 8, 0))

print(return_indices_in_new_list_reverse([2,3,4,5,2,3,4], 2, 0))
print(return_indices_in_new_list_reverse([2,3,4,5,2,3,4], 4, 0))
print(return_indices_in_new_list_reverse([2,3,4,5,2,3,4], 3, 0))
print(return_indices_in_new_list_reverse([2,3,4,5,2,3,4], 8, 0))