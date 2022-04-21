# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/14/21
# Purpose: Exam 2, Problem 2 -- Define a function string_slicing that takes a string gstr, and two
# non-negative integers m and n as parameters. Your function should return a new string with
# the characters in gstr from index m to n (including m but not n) in the order they appear in
# gstr. In other words, the string returned by your function will be equal to gstr[m:n]. Assume
# m <= n; m <= len(gstr)-1; and n <= len(gstr).
# In this question you not allowed to use:
# ● the built-in list/string slicing in Python
# ● while loops
# For example:
# 1. if gstr = “testing”, m = 1 and n = 5, then your function should return “esti”.
# 2. if gstr = “dartmouth”, m = 0 and n = 4, then your function should return “dart”.
# 3. if gstr = “testing”, m = 2 and n = 7, then your function should return “sting”.
# 4. if gstr = “dartmouth”, m = 3 and n = 3, then your function should return “” (when you
# print an empty string you will only see a blank line in the output window).

# Purpose: this function takes a string, gstr, and slices it at the specified indices
# Parameters: a string, and two non-negative integers, m and n, that are the cutoff indices;
# we assume that m <= n, m <= len(gstr)-1, and n <= len(gstr)
# Return: a new string with the characters in gstr from index m to n (including m but not n)
def string_slicing(gstr, m, n):
    new_string = ""
    for x in range(m, n):
        new_string += gstr[x]
    return new_string

print(string_slicing("testing", 1, 5))
print(string_slicing("dartmouth", 0, 4))
print(string_slicing("testing", 2, 7))
print(string_slicing("dartmouth", 3, 3))