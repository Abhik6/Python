
words_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9': 'wxyz'}

def return_all_words_helper(s, index):
    if len(s) == index or s == '' or s == '1':
        return ['']
    
    # Recursion call
    words = return_all_words_helper(s, index+1)

    # My work
    current_num = s[index]
    current_word = words_dict.get(current_num)
    final_words = []

    for char in current_word:
        for word in words:
            final_words.append(char + word)
    
    return final_words


def return_all_words(s):

    return return_all_words_helper(s, 0)

print(return_all_words('23'))
print(return_all_words('1')) 
print(return_all_words('')) 