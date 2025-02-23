def recursive_sum(arr):
    """
    Function to calculate the sum of an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    
    Returns:
    int: The sum of the array elements.
    """
    # Your code here
    
    if len(arr) == 0:
        return 0
    
    left_over_sum = recursive_sum(arr[1:])

    sum = arr[0] + left_over_sum

    return sum

def recursive_sum_tail(arr, sum=0):
    """
    Function to calculate the sum of an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    
    Returns:
    int: The sum of the array elements.
    """
    # Your code here
    
    if len(arr) == 0:
        return sum
    
    sum += arr[0]
    
    return recursive_sum_tail(arr[1:], sum)


print(recursive_sum([1,2,]))
print(recursive_sum_tail([1,2]))