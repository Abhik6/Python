def permutations_helper(s, index):

    # Base Case
    if s == '' or len(s) == index:
        return ['']
    
    # Permutation Call
    permutaions_lst = permutations_helper(s, index+1)

    # My Work
    current_char = s[index]
    final_lst = []
    for permutation in permutaions_lst:
        for position in range(len(permutation)+1):
            final_lst.append(permutation[0:position] + current_char + permutation[position:])

    return final_lst


def permutations(s):
    """
    Function to generate all permutations of a string using recursion.
    
    Parameters:
    s (str): The string to generate permutations from.
    
    Returns:
    list of str: A list containing all permutations of the string.
    """
    # Your code here

    return permutations_helper(s, 0)


print(permutations('abc'))
print(permutations(''))