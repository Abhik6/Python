def valid_parenthesis(str):

    stack = []

    if str == '':
        return True

    for char in str:
        if not stack:
            if char in ("(","{","["):
                stack.append(char)
            else:
                return False
        else:
            if char == ")":
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == "}":
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif char == "]":
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        print(stack)
    if stack:
        return False
    else:
        return True

    

# str = '(){}[]'
# str = '{[()]}'
# str = '[]{()}'
# str = '[{])'
# str = '{({'
str = '}[{()}]'

print(valid_parenthesis(str))