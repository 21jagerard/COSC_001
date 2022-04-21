# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Demo return statement

def func(n, m):
    return n + m

x = func(func(100, 200), func(10, 20))
print(x)