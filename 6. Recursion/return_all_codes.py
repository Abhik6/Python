
def get_char(value: int) -> str:
    if value<=0 or value>26:
        return ""
    return chr(96+value)

def return_all_codes_helper(s: str, index: int) -> list:

    # Base Case
    if s == '' or len(s) == index:
        return ['']

    # Recursion call
    single_digit = int(s[index])
    single_digit_recursion_codes = return_all_codes_helper(s, index+1)

    # My Work
    single_char = get_char(single_digit)
    codes = []
    for code in single_digit_recursion_codes:
        codes.append(single_char + code)

    if len(s)>1 and index+1<len(s):
        double_digit = int(s[index:index+2])
        if double_digit in range(10,27):
            # Recursion call
            double_digit_recursion_codes = return_all_codes_helper(s, index+2)
            # My Work
            double_char = get_char(double_digit)
            for code in double_digit_recursion_codes:
                codes.append(double_char + code)

    return codes


def return_all_codes(s: str) -> list:
    
    return return_all_codes_helper(s, 0)


print(return_all_codes('1123'))
print(return_all_codes('6723'))