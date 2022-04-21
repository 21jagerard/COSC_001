# Author: Anna Mikhailova
# Date: 10/27/21
# Purpose: recursive compute the sum of last k even numbers between 1 and n

def print_las_k(n, k):
    if n == 1 or k == 0:
        return

    if n % 2 == 0:
        print(n)
        print_las_k(n-1, k-1)
    else:
        print_las_k(n-1, k)
