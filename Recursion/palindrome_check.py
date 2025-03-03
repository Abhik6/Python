def is_palindrome_helper(s, start, end):

    if start>=end:
        return True
    
    if s[start] != s[end]:
        return False
    
    return is_palindrome_helper(s, start+1, end-1)

def is_palindrome(s):
    """
    Function to check if a string is a palindrome using recursion.
    
    Parameters:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    return is_palindrome_helper(s, 0, len(s)-1)

print(is_palindrome('nitin'))
print(is_palindrome('malayalam'))
print(is_palindrome('abcde'))