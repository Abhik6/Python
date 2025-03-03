def binary_search_helper(arr, target, start, end):

    # Base Case
    if start>end:
        return False

    mid = start + (end - start)//2

    if arr[mid] == target:
        return True

    if target > arr[mid]:
        return binary_search_helper(arr, target, mid+1, end)  

    return binary_search_helper(arr, target, start, mid-1)  

def binary_search(arr, target):

    return binary_search_helper(arr, target, 0, len(arr)-1)


print(binary_search([2,3,4,5,6,2], 3))
print(binary_search([2,3,4,5,6,2], 5))
print(binary_search([2,3,4,5,6,2], 6))
print(binary_search([2,3,4,5,6,2], 10))