# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Define a function print_evens that takes a positive integer n
# as parameter and prints all the even numbers between 0 and n, including n if it is an even number.

def print_evens(n):
    i = 0
    if n % 2 == 0:
        while i <= n:
            print(i)
            i += 2
    else:
        while i < n:
            print(i)
            i += 2

num = int(input("Enter an integer:"))
print_evens(num)