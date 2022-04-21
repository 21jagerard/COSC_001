# Author: Anna Mikhailova
# Date: 09/27/21
# Purpose: Practice Assignment 2
# Define a function that returns the larger of the two products of positive integers

def func(a, b):
    return a*b

def larger_int(m, n):
    if m > n:
        return m
    else:
        return n

x = larger_int(func(125, 1234), func(234, 678))
print(x)



