def minimum_steps_to_one(n, func_call={}):

    if n in func_call:
        func_call[n]+=1
    else:
        func_call[n] = 1
    
    if n <= 1:
        return 0, func_call
    
    div_3 = float('inf')
    div_2 = float('inf')
    if n%3==0:
        div_3, func_call = minimum_steps_to_one(n//3, func_call)

    if n%2==0:
        div_2, func_call = minimum_steps_to_one(n//2, func_call)
    
    sub_1, func_call = minimum_steps_to_one(n-1)

    steps = 1 + min(div_3, div_2, sub_1)

    return steps, func_call

def minimum_steps_to_one_memoization(n, memo={}, func_call={}):

    if n in func_call:
        func_call[n]+=1
    else:
        func_call[n] = 1
    
    if n <= 1:
        return 0, memo, func_call
    
    div_3 = float('inf')
    div_2 = float('inf')
    if n%3==0:
        if n//3 in memo:
            div_3 = memo[n//3]
        else:
            div_3, memo, func_call = minimum_steps_to_one_memoization(n//3, memo, func_call)

    if n%2==0:
        if n//2 in memo:
            div_2 = memo[n//2]
        else:
            div_2, memo, func_call = minimum_steps_to_one_memoization(n//2, memo, func_call)
    
    if (n-1) in memo:
        sub_1 = memo[n-1]
    else:
        sub_1, memo, func_call = minimum_steps_to_one_memoization(n-1, memo, func_call)

    steps = 1 + min(div_3, div_2, sub_1)
    memo[n] = steps

    return steps, memo, func_call

def minimum_steps_to_one_tabulation(n):

    dp = {i:0 for i in range(1,n+1)}
    dp[2] = 1
    dp[3] = 1

    for i in range(4,n+1):
        steps = float('inf')
        if i%3==0:
            steps=dp[i//3]
        if i%2==0:
            steps = min(steps, dp[i//2])
        steps = 1 + min(steps, dp[i-1])

        dp[i] = steps
        
    return dp[n], dp

func_calls = {}
print(minimum_steps_to_one(10, func_calls))
print(minimum_steps_to_one_memoization(10, {}, func_calls))
print(minimum_steps_to_one_tabulation(10))
    
