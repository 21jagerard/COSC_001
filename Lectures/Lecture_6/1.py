# Author: Anna Mikhailova
# Date: 09/24/21
# Purpose: global vs local vs parameters

# def func1(n):
#     x = 10
#     print(n, x)
#
# def func2(m):
#     x = 200
#     print(m, x)
#
# func1(4)
# func2(7)
# func1(11)

x = 1000

def func1(n):
    # global x  # --> global variables are bad in general, try to avoid them
    x = 10
    print(n, x)

func1(4)
print(x)
