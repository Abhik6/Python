def count_digits(n):
    """
    Function to find the number of digits in a number using recursion.
    
    Parameters:
    n (int): The positive integer whose digits are to be counted.
    
    Returns:
    int: The number of digits in the integer.
    """
    # Your code here
    
    if n < 10:
        return 1 # Base case
    next_num = n//10
        
    small_ans = count_digits(next_num)
    ans = 1 + small_ans
    
    return ans
    
print(count_digits(12345))