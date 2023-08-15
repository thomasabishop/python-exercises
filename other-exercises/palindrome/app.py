'''
Determine if word is a palindrome
'''


def is_palindrome(inp):
    inp_list = list(inp)
    inp_list_len = len(inp_list)
    for i in range(inp_list_len):
        if inp_list[i] != inp_list[inp_list_len - 1 - i]:
            return False
    return True


def main():
    palindrome_one = "soros"
    palindrome_two = "torot"
    not_palindrome = "chair"

    print(is_palindrome(palindrome_one))
    print(is_palindrome(palindrome_two))
    print(is_palindrome(not_palindrome))


if __name__ == '__main__':
    main()
