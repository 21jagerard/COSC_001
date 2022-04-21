# Author: Anna Mikhailova
# Date: 09/27/21
# Purpose: Practice Assignment 2
# Define a function that takes positive integers m and n, and returns the larger number

def larger_int(m, n):
    if m > n:
        return m
    else:
        return n

a1 = int(input("Enter an integer:"))
a2 = int(input("Enter another integer:"))

x = larger_int(a1, a2)
print("The larger number is", x)