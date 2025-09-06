# 1. Write a Python Program to print Prime Numbers between 2 numbers

def print_prime_nums(num1, num2):

    for num in range(num1,num2+1):
        is_prime = True 
        for i in range(2, num):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

# print_prime_nums(100, 200)

# 2. Write a sorting function without using the list.sort function

def sort_list(lst):

    sorted_lst = []
    while lst:
        minimum = lst[0]
        for i in range(1,len(lst)):
            if minimum > lst[i]:
                minimum = lst[i]
        
        sorted_lst.append(minimum)
        lst.remove(minimum)
    
    return sorted_lst

# lst = [8,10,67,2,5,23]
# result = sort_list(lst)
# print(result)


# 4. Write a Python program to print Fibonacci Series

def print_fibo_series(n):

    if n==1:
        return [0]
    dp = [None for i in range(n)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp

# print(print_fibo_series(9))

# 5. Write a Python program to print a list in reverse

def reverse_list(lst):
    print(lst[::-1])

# lst = [8,10,67,2,5,23]
# reverse_list(lst)

# 6. Write a Python program to check whether a string is a Palindrome or not 

def is_palindrome(s):

    i = 0
    j = len(s)-1

    while i<=j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    
    return True

# s = 'racecar'
# s = 'hello'
# result = is_palindrome(s)
# print(result)
    
# 7. Write a Python program to print set of duplicates in a list

def get_duplicates_in_list(lst):
    elem_count = {}
    dups = set()
    for elem in lst:
        if elem in elem_count:
            elem_count[elem]+=1
            dups.add(elem)
        else:
            elem_count[elem] = 1
    
    return list(dups)

# lst = [1,1,1,1,2,2,2,3,3,3,6,7,8,4,6]
# lst = [1,2,3,4]
# result = get_duplicates_in_list(lst)
# print(result)

# 8. Write a Python program to print number of words in a given sentence

def count_words(s):
    words = s.split(" ")
    print(words)
    return len(words)

# s = "A palindrome string is a sequence of characters that reads the same forward and backward. This means that if the string is reversed, it remains identical to the original string."
# s = ""
# result = count_words(s)
# print(result)

# 9. Given an array arr[] of n elements, write a Python function to search a given element x in arr[].

def search_elem(arr, elem):
    for element in arr:
        if element == elem:
            return element
    return None

# arr = [2,3,4,5,6,7,8,9]
# elem = 10
# print(search_elem(arr, elem))

# 10. Write a Python program to implement a Binary Search

def binary_search(arr, elem):

    sorted_array = sorted(arr)
    print(sorted_array)
    return binary_search_helper(sorted_array, elem)
    

def binary_search_helper(sorted_array, elem):
        if len(sorted_array)==0:
            return None
        if len(sorted_array)==1 and sorted_array[0]!=elem:
            return None

        start = 0
        end = len(sorted_array)
        mid = (end-start)//2
        print(f"\nSorted Array: {sorted_array}")
        print(f"Mid: {sorted_array[mid]}")

        if sorted_array[mid] == elem:
            return elem
        elif elem < sorted_array[mid]:
            return binary_search_helper(sorted_array[start:mid], elem)
        else:
            return binary_search_helper(sorted_array[mid:end], elem)
        
arr = [2,3,4,5,6,7,8,9,1]
elem = 6
print(binary_search(arr, elem))

         
