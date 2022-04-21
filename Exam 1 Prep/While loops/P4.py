# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Define a function product_even that takes a positive integer n
# as parameter and prints the product of all even numbers between 1 and n (including n).

def product_even(n):
    i = 2
    prod = 1
    if n % 2 == 0:
        while i <= n:
            prod *= i
            i += 2
    else:
        while i < n:
            prod *= i
            i += 2
    print(prod)
num = int(input("Enter an integer:"))
product_even(num)