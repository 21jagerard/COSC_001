# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Define a function check_number_evens that takes two positive integers n and k as parameters.
# Your function prints “at least k evens” if there are at least k even numbers between 1 and n,
# or prints “less than k evens” if there are less than k even numbers between 1 and n.

def check_number_evens(n, k):
    count = 0
    i = 0
    while count <= k:
        i += 2
        count += 1
    if count < n:
        print("At least", k, "evens.")
    else:
        print("Less than", k, "evens.")

check_number_evens(20, 4)

