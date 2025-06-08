def count_to_n(n):
    """
    Function to return a list of integers from 1 to n using recursion.
    
    Parameters:
    n (int): The positive integer representing the upper limit of the range.
    
    Returns:
    list: A list of integers from 1 to n.
    """
    # Your code here
    if n<=0:
        return list() # Base case
    
    lst = count_to_n(n-1)
    lst.append(n) 
    print(lst)
    return lst
        
print(count_to_n(5)) 
