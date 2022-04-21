# Author: Anna Mikhailova
# Date: 11/11/21
# Course: COSC_001
# Purpose: Exam 4 Problem 2;  Define a recursive function that takes two positive integers n and p
# as parameters and prints all the multiples of p between 1 and n in increasing order. A
# number x is a multiple of p if x % p == 0

def func(n, p, i=1):
    if i <= n:
        if i % p == 0:
            print(i)
        func(n, p, i+1)

