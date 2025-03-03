def subsequences_helper(s,index):
    # Base Case
    if len(s) == index:
        return ['']
    
    my_char = s[index]

    # Recursion Call
    subsequence_lst =  subsequences_helper(s, index+1)

    # My Work
    my_subsequnces = []
    for subsequence in subsequence_lst:
        my_subsequnces.append(my_char + subsequence)

    subsequence_lst.extend(my_subsequnces)
    return subsequence_lst


def subsequences(s):
    """
    Function to generate all subsequences of a string using recursion.
    
    Parameters:
    s (str): The string to generate subsequences from.
    
    Returns:
    list of str: A list containing all subsequences of the string.
    """
    # Your code here
    if s == '':
        return []
    return subsequences_helper(s,0)

print(subsequences('abc'))
print(subsequences(''))

    
    
    