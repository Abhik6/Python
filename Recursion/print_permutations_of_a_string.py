def print_permutations_helper(s, index, taken_over):
    # Base Case
    if s == '' or len(s) == index:
        print(taken_over)
        return
    
    current_char = s[index]

    for i in range(len(taken_over)+1):
        print_permutations_helper(s, index+1, taken_over[0:i] + current_char + taken_over[i:])

def print_permutations(s):
    """
    Function to generate all permutations of a string using recursion.
    
    Parameters:
    s (str): The string to generate permutations from.
    
    Returns:
    list of str: A list containing all permutations of the string.
    """
    # Your code here

    print_permutations_helper(s, 0, '')

    return
print_permutations('abc')