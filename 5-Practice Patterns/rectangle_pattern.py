# Rectangle Pattern

# Problem Description:
# You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).

# Input:
# Two integers n and m, where 1 <= n, m <= 100.

# Output:
# A list of strings where each string represents a row of the rectangle pattern.

# Example:

# Input: n = 4, m = 5
# Output: ['*****', '*****', '*****', '*****']
 
# Input: n = 3, m = 2
# Output: ['**', '**', '**']

def generate_rectangle(n,m):
    lst = []
    for i in range(n):
        str = ''
        for j in range(m):
            str+='*'
        lst.append(str)
    return lst

pattern = generate_rectangle(4,5)
print(pattern)