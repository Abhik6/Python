def count_down(n, lst = []):
    """
    Function to return a list of integers from n to 1 using recursion.
    
    Parameters:
    n (int): The positive integer representing the starting point of the range.
    
    Returns:
    list: A list of integers from n to 1.
    """
    # Your code here
    if n<=0:
        return lst
    
    lst.append(n)
    print(lst)
    
    count_down(n-1, lst)
    
    return lst
        
print(count_down(5))