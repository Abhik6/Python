def sum_of_natural_numbers(n):
    """
    Function to calculate the sum of the first n natural numbers using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the sum is to be calculated.
    
    Returns:
    int: The sum of the first n natural numbers.
    """
    # Your code here
    
    if n == 1:
        return 1 # base case
    elif n == 0:
        return 0
    shortAns = sum_of_natural_numbers(n-1)
    ans = n + shortAns

    return ans
    
