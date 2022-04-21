# Purpose: define a function that builds a list recursively

def func(n):
    if n == 0:
        return []

    rlist = func(n-1)
    rlist.append(n)
    return rlist


func(4)