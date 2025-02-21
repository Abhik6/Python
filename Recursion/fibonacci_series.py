def fibonacci(n):
    """
    Function to calculate the nth Fibonacci number using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the Fibonacci number is to be calculated.
    
    Returns:
    int: The nth Fibonacci number.
    """
    # Your code here
    if n==0:
        return 0 # Base case 1
    elif n==1:
        return 1 # Base case 2
    
    last = fibonacci(n-1)
    second_last = fibonacci(n-2)
    ans = last + second_last
    
    return ans
    
print(fibonacci(3))
