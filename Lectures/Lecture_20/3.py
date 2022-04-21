# Author: Anna Mikhailova
# Date: 10/27/21
# Purpose: recursively computing fibonacci and why it's a bad idea

def fib(n):
    if n == 1 or n == 2:
        return 1

    n2 = fib(n - 2)
    n1 = fib(n - 1)

    return n2 + n1

print(fib(7))