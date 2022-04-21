# Author: Anna Mikhailova
# Date: 10/4/21
# Purpose: strings are like lists

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

print(is_palindrome("homework"))