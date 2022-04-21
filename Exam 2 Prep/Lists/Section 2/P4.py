# Define a function that takes a list of strings slist as parameter and checks if at least
# one of the strings is a palindrome. It should return True or False.
# [Hint: You can use the function is_palindrome that takes a string as parameter
# and return True or False discussed in class.]

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True

def func(slist):
    for i in slist:
        if is_palindrome(i):
            return True

print(func(["homework", "alphabet"]))