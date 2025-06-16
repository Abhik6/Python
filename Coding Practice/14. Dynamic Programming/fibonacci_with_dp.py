def fibonacci_without_memoization(n, memo={}, count={}):
    if n<=1:
        return 1
    
    if count.get(n) is not None:
        count[n]+=1
    else:
        count[n] = 1
        
    elem_1 = fibonacci_without_memoization(n-1, memo, count)
    elem_2 = fibonacci_without_memoization(n-2, memo, count)

    result = elem_1 + elem_2

    return result

def fibonacci_with_memoization(n, memo={}, count={}):
    if n<=1:
        return 1
    
    if count.get(n) is not None:
        count[n]+=1
    else:
        count[n] = 1

    if memo.get(n-1) is not None:
        elem_1 = memo[n-1]  
    else:
        elem_1 = fibonacci_with_memoization(n-1, memo, count)
        memo[n-1] = elem_1
        
    if memo.get(n-2) is not None:
        elem_2 = memo[n-2]   
    else:
        elem_2 = fibonacci_with_memoization(n-2, memo, count)
        memo[n-2] = elem_2
        

    result = elem_1 + elem_2
    memo[n] = result
    print(memo)
    return result

def fibonacci_with_tabulation(n):

    dp = [-1]*(n+1)
    dp[0] = 1
    dp[1] = 1
    print(dp)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        print(dp)
    
    return dp[n]

count = {}
print(fibonacci_with_memoization(8, {}, count))
print(count)
# count = {}
# print(fibonacci_without_memoization(8, {}, count))
# print(count)
# print()
print(fibonacci_with_tabulation(8))