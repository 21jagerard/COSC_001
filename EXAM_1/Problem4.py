# Author: Anna Mikhailova
# Date: 09/30/21
# Purpose: In this question define a function print_fibs_decreasing that takes a positive integer n as
# parameter and prints all the numbers in Fibonacci series that are between 1 and n in
# decreasing order. n is included and your function should print it, if it is a Fibonacci sequence
# number. You are not allowed to use Python syntax that has not been discussed in class.

# Purpose: this function prints all fibonacci numbers less than or equal to the given parameter in decreasing order
# Parameters: This function takes a positive integer n
def print_fibs_decreasing(n):
    f1 = 0
    f2 = 1
    new = 0
    fib_count = 0
    while f2 <= n:
        new = f1 + f2
        f1 = f2
        f2 = new
        fib_count += 1
    while fib_count > 0:
        new = f2 - f1
        print(f1)
        f2 = f1
        f1 = new
        fib_count -= 1

num = int(input("Enter a positive integer:"))
print_fibs_decreasing(num)