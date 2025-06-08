def remove_char(str,ch):

    if len(str) == 0:
        return ''
    
    small_ans = remove_char(str[1:], ch)

    if str[0] != ch:
        return str[0] + small_ans
    
    return small_ans

    
print(remove_char('Welcome Homezzzz', 'z'))