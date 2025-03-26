def partition(arr, start, end):

    pivot = arr[end]
    pivot_index = start
    i = start

    while i<=end-1:
        if arr[i]<pivot:
            pivot_index+=1
        i+=1

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    i = start
    j = end

    while i<pivot_index and j>=pivot_index:
        if arr[i]<pivot:
            i+=1
        elif arr[j]>=pivot:
            j-=1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1

    return pivot_index


def quick_sort_helper(arr, start, end):

    if start>=end:
        return
    # mid = start + (end-start)//2
    pivot_index = partition(arr, start, end)

    quick_sort_helper(arr, start, pivot_index - 1)
    quick_sort_helper(arr, pivot_index + 1, end)

    return

def quick_sort(arr):
    """
    Function to perform quick sort on a list of integers using recursion.
    
    Parameters:
    arr (list of int): The list to be sorted.
    
    Returns:
    list of int: The sorted list.
    """
    # Your code here

    quick_sort_helper(arr, 0, len(arr) -1)
    return arr


# lst = [2,5,3,10,11,9,14,4]
# lst = [5, 2, 9, 1, 5, 6]
lst = [3, 0, 2, 5, -1, 4, 1]
partition(lst, 0, 6)
print(lst)

quick_sort(lst)
print(lst)