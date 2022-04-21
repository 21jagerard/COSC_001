# Author: Anna Mikhailova
# Date: 10/22/21
# Purpose: returning a value in recursion

# def func(n):
#     if n <= 0:
#         return n
#
#     x = func(n - 1)
#     return x + n
#
# func(4)

def func(n):
    if n == 1:
        return n

    x = func(n - 1)
    return x * n

print(func(4))