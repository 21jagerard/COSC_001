# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Define a function product_odd that takes two positive integers m and n
# as parameters and prints the product of all odd numbers between m and n. You may assume m < n and m is odd.

def product_odd(m, n):
    prod = 1
    if m % 2 == 0:
        count = m + 1
        while count < n:
            prod *= count
            count += 2
    else:
        count = m + 2
        while count < n:
            prod *= count
            count += 2
    print(prod)

num1 = int(input("Enter a lower bound:"))
num2 = int(input("Enter an upper bound:"))
product_odd(num1, num2)
