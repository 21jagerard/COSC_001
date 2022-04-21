# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/14/21
# Purpose: Exam 2, Problem 5 -- Define a function longest_equal_halves that takes a string gstr as a parameter.
# It should return the longest non-empty substring of gstr that has two equal halves. Here are few things to note:
# 1. A substring of a string gstr is anything that can be created using build-in slicing in Python gstr[m:n]
# where m <= n, 0 <= m <= len(gstr), and 0 <= n <= len(gstr).
# 2. A string has two equal halves when the string is even length and its first half is equal to the second half.
# For example:
# 1. if gstr = “xyztesttestabab”, then your function should return “testtest”.
# 2. if gstr = “xyzxyz”, then your function should return “xyzxyz”.
# 3. if gstr = “xyzabcd”, then your function should return “” (an empty string).
# 4. if gstr = “”, then your function should return “” (when you print an empty string you will
# only see a blank line in the output window).
# 5. if gstr = “xyxyabab”, then your function may return “xyxy” or “abab”.

# Purpose: this function takes a string, gstr, as a parameter and returns the longest non-empty substring of gstr
# that has two equal halves
# Parameter: a string, gstr
# Return: longest non-empty substring of gstr that has two equal halves
def longest_equal_halves(gstr):
    longest_double = ""
    for m in range(len(gstr)):
        for n in range(m, len(gstr)):
            current_double = gstr[m : n] + gstr[m : n]
            if current_double in gstr:
                if len(current_double) > len(longest_double):
                    longest_double = current_double
    return longest_double


print(longest_equal_halves("xyztesttestabab"))  # return "testtest"
print(longest_equal_halves("xyzxyz"))  # return "xyzxyz"
print(longest_equal_halves("xyzabcd"))  # return ""
print(longest_equal_halves(""))  # return ""
print(longest_equal_halves("xyxyabab"))  # return xyxy or abab
