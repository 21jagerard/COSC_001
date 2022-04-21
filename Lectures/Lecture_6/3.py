# Author: Anna Mikhailova
# Date: 09/24/21
# Purpose: locations where you can define functions and call functions

def func1(n):
    print("func1:", n)
    func2(36)

def func2(n):
    print("func2:", n)

func1(10)

# def func1(n):
#     print("func1:", n)
#     func2(36)
#
# func1(10)
#
# def func2(n):
#     print("func2:", n)