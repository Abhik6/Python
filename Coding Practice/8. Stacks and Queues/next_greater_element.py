
def next_greater_element(lst, n):

    return_lst = []

    for index in range(n):

        elem = lst[index]
        max = -1

        for index1 in range(index+1, n):
            if lst[index1]>elem:
                max = lst[index1]
                break
        
        return_lst.append(max)
    
    return return_lst

def next_greater_element_soln(a, n):
    # Create a result array initialized with -1
    result = [-1] * n
    
    # Stack to store indexes of elements
    stack = []
 
    # Traverse the array from left to right
    for i in range(n):
        # For current element a[i], pop elements from the stack
        # while stack is not empty and the current element is greater than
        # element at index stored at the top of the stack
        while stack and a[stack[-1]] < a[i]:
            # Update the result for the index popped from the stack
            index = stack.pop()
            result[index] = a[i]
 
        # Push the current index onto the stack
        stack.append(i)
 
    return result

lst = [4, 5, 2, 25]
# lst = [4,3,2,5,10]
n = 4

next_greater_num = next_greater_element(lst, n)
print(next_greater_num)

        