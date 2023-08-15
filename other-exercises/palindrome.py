'''
Determine if word is a palindrome
'''

palindrome_one = "soros"
palindrome_two = "torot"
not_palindrome = "chair"


# look again at loop constructs
def is_palindrome(inp):
    inp_list = list(inp)
    inp_list_len = len(inp_list)
    for i in range(inp_list_len):
        if inp_list[i] != inp_list[inp_list_len - 1 - i]:
            return False
    return True


print(is_palindrome(not_palindrome))
