# Author: Anna Mikhailova
# Date: 10/22/21
# Purpose: Demo a recursive function

# def func(n):
#     if n <= 0:
#         return
#
#     func(n - 1)
#     print("test")
#
# func(4)

# def func(a, b):
#     return a + b
#
# print(func(10, 20))

def func(n):
    if n <= 0:
        return
    print(n)
    func(n - 1)

func(4)