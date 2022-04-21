# Author: Anna Mikhailova
# Date: 09/27/21
# Purpose: Practice Assignment 2
# Define a function that takes positive integers m and n, and returns the product

def func(m, n):
    return m*n

a1 = float(input("Enter a number:"))
a2 = float(input("Enter another number:"))
x = func(a1, a2)
print("The product of", a1, "and", a2, "is", x)