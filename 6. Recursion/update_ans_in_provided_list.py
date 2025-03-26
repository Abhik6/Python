def update_indices_in_provided_list(arr, element, index, ans_lst):
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
        return ans_lst
    
    if arr[index] == element:
        ans_lst.append(index)

    return update_indices_in_provided_list(arr, element, index+1, ans_lst)

def update_indices_in_provided_list_reverse(arr, element, index, ans_lst):
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
        return
    
    update_indices_in_provided_list_reverse(arr, element, index+1, ans_lst)

    if arr[index] == element:
        ans_lst.append(index)

    return ans_lst

ans_lst = []

print(update_indices_in_provided_list([2,3,4,5,2,3,4], 2, 0, ans_lst))
ans_lst = []
print(update_indices_in_provided_list([2,3,4,5,2,3,4], 4, 0, ans_lst))
ans_lst = []
print(update_indices_in_provided_list([2,3,4,5,2,3,4], 3, 0, ans_lst))
ans_lst = []
print(update_indices_in_provided_list([2,3,4,5,2,3,4], 8, 0, ans_lst))

ans_lst = []
print(update_indices_in_provided_list_reverse([2,3,4,5,2,3,4], 2, 0, ans_lst))
ans_lst = []
print(update_indices_in_provided_list_reverse([2,3,4,5,2,3,4], 4, 0, ans_lst))
ans_lst = []
print(update_indices_in_provided_list_reverse([2,3,4,5,2,3,4], 3, 0, ans_lst))
ans_lst = []
print(update_indices_in_provided_list_reverse([2,3,4,5,2,3,4], 8, 0, ans_lst))
