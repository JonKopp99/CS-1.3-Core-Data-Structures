#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase




def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    pass
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    text = text.lower()
    left = 0
    rigth = len(text) - 1
    while left != rigth and left < rigth:
        if text[left] not in string.ascii_lowercase:
            left += 1
            continue
        if text[rigth] not in string.ascii_lowercase:
            rigth -= 1
            continue
        if text[left] != text[rigth]:
            return False
        left += 1
        rigth -= 1

    return True
    

def is_palindrome_recursive(text, left=None, right=None):
    # implement the is_palindrome function recursively 
    pass
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    text = text.lower()
    if left == None:
        left = 0
    if right == None:
        right = len(text) - 1

    if left >= right:
        return True
        
    if text[left] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left + 1, right)
    elif text[right] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left, right - 1)
    elif text[left] == text[right]:
        return is_palindrome_recursive(text, left + 1, right - 1)

    return False
    


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
