# Author: Anna Mikhailova
# Date: 11/11/21
# Course: COSC_001
# Purpose: Exam 4 Problem 3; Define a recursive function that takes a list of positive integers glist
# as a parameter and returns a new list that contains all the numbers in glist that appear at
# odd indices. The order of numbers in the returned list does not matter.

def func(glist, new_list=[]):
    if len(glist) <= 1:
        return []
    elif len(new_list) <= len(glist):
        new_list.append(glist[1])
        func(glist[2:], new_list)
    return new_list
