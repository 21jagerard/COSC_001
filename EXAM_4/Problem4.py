# Author: Anna Mikhailova
# Date: 11/11/21
# Course: COSC_001
# Purpose: Exam 4 Problem 4;  Define a recursive function that takes two strings s1 and s2 and a
# non-negative integer k as parameters and returns True if there are exactly k indices where
# characters in s1 match the characters in s2, otherwise it returns False.

def func(s1, s2, k, i=0, count=0):
    if i <= min(len(s1), len(s2)) - 1:
        if s1[i] == s2[i]:
            count += 1
        return func(s1, s2, k, i + 1, count)
    elif count != k:
        return False
    return True



