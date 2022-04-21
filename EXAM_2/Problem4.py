# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/14/21
# Purpose: Exam 2, Problem 4 -- Define a function no_common_chars that takes a list of strings
# slist and a string gstr as parameters. Your function should return a new list of strings
# (without modifying slist) that do not have any characters that are in gstr. The returned list
# can only contain strings in slist.
# The order of strings in the returned list does not matter. You are not allowed to use sort
# (built-in or your own) for this problem.
# For example:
# 1. if slist = [“pan”, “must”, “check”, “final”, “good”] and gstr = “pea”, then your function should return
# [“must”, “good”] as “must” and “good” are the only words in slist that do not have the characters “p”, “e” or “a”.
# 2. if slist = [“peterpan”, “must”, “check”, “final”, “good”, “eagle”] and gstr = “”, then your
# function should return [“peterpan”, “must”, “check”, “final”, “good”, “eagle”] as there are no letters in gstr.
# 3. if slist = [ ] and gstr = “peel”, then your function should return [ ] as there are no strings in slist.
# 4. if slist = [“test”, “happen”, “common”, “keep”] and gstr = “xyzx”, then your function should return
# [“test”, “happen”, “common”, “keep”] as all strings is slist do not have the characters “x”, “y” and “z”.

# Purpose: this function takes a list of strings, slist, and a string, gstr, as parameters and returns a new list of
# strings that have no characters in common with gstr
# Parameters: a list of strings, slist, and a string, gstr
# Return: a list of strings in slist that do not have any characters that are in gstr
def no_common_chars(slist, gstr):
    new_list = slist
    same_chars_list = []
    for x in new_list:
        for i in x:
            if i in gstr:
                same_chars_list.append(x)
                break
    for y in same_chars_list:
        new_list.remove(y)
    return new_list

print(no_common_chars(["pan", "must", "check", "final", "good"], "pea"))  # [“must”, “good”]
print(no_common_chars(["peterpan", "must", "check", "final", "good", "eagle"], ""))
# [“peterpan”, “must”, “check”, “final”, “good”, “eagle”
print(no_common_chars([ ], "peel"))  # [ ]
print(no_common_chars(["test", "happen", "common", "keep"], "xyzx"))  # [“test”, “happen”, “common”, “keep”]

