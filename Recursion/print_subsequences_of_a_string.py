def print_subsequences(s, taken_over, index):
    """
    Function to print all subsequences of a string using recursion.
    
    Parameters:
    s (str): The string to generate subsequences from.
    
    Returns: None
    """

    # Base Case
    if s == '' or len(s) == index:
        print(taken_over)
        return
    
    current_char = s[index]
    
    # Recursion Call
    print_subsequences(s, taken_over + current_char, index+1)
    print_subsequences(s, taken_over, index+1)

    return

print_subsequences('abc', '', 0)


