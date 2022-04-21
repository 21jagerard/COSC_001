# Author: Anna Mikhailova
# Date: 10/20/21
# Purpose: Demo function calls

def funcA(n):
    if n > 10:
        print("funcA:", n)
        return n
    else:
        x = funcB(n + 2)
        return x

def funcB(n):
    if n > 10:
        print("funcB:", n)
        return n
    else:
        x = funcB(n + 1)
        return x

def funcC(n):
    if n > 10:
        print("funcC:", n)
        return n
    else:
        x = funcC(n+3)
        return x

print(funcA(5))