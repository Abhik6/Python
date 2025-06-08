def merge(arr, start, mid, end):
    i = start
    j = mid+1
    new_lst = []

    while i<=mid and j<=end:
        if arr[i]<arr[j]:
            new_lst.append(arr[i])
            i+=1
        elif arr[i]>arr[j]:
            new_lst.append(arr[j])
            j+=1
        elif arr[i]==arr[j]:
            new_lst.append(arr[i])
            new_lst.append(arr[j])
            i+=1
            j+=1

    while i<=mid:
        new_lst.append(arr[i])
        i+=1
    
    while j<=end:
        new_lst.append(arr[j])
        j+=1

    new_lst_index = 0
    sorted_list_index = start

    while sorted_list_index <=end:
        arr[sorted_list_index] = new_lst[new_lst_index]
        sorted_list_index+=1
        new_lst_index+=1
    
    return


def merge_sort_helper(arr, start, end):

    if start>=end:
        return
    
    mid = start + (end-start)//2

    merge_sort_helper(arr, start, mid)
    merge_sort_helper(arr, mid+1, end)

    merge(arr, start, mid, end)

    return
        

def merge_sort(arr):
    """
    Function to perform merge sort on a list of integers using recursion.
    
    Parameters:
    arr (list of int): The list to be sorted.
    
    Returns:
    list of int: The sorted list.
    """
    # Your code here

    merge_sort_helper(arr, 0, len(arr)-1)
    return arr

lst = [2,5,3,10,11,9,14,4]
merge(lst, 0, 1, 3)
print(lst)

merge_sort(lst)
print(lst)