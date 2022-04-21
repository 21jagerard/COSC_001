# Author: Anna Mikhailova
# Date: 10/27/21
# Purpose: recursive is_palindrome

def is_palindrome(s, i=0, j=None):
    if j == None:
        j = len(s) - 1

    if i >= j:
        return None

    if s[i] != s[j]:
        return False

    res = is_palindrome(s, i + 1, j - 1)
    return res