# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Define a function last_n_evens2 that takes two positive integers n and k as parameters.
# It should print the last k even numbers between 1 and n. You can make the following assumptions:
# There are at least k even numbers between 1 and n

def last_n_evens2(n, k):
    if n % 2 == 0:
        while k > 0:
            n -= 2
            print(n)
            k -= 1
    else:
        n -= 1
        while k > 0:
            print(n)
            n -= 2
            k -= 1

upp_lim = int(input("What do you want the upper limit to be?"))
num = int(input("How many of the last evens would you like to print?"))

last_n_evens2(upp_lim, num)
