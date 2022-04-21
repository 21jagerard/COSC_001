# Define a function that takes a list of lists glol as parameter.  You may assume that each inner list inside glol
# is a list of integers. For example: [[1, 2], [10, 20], [30, 10], [-4, -5]].
# Your function returns True if at least one list inside glol is sorted in increasing order and at least
# one list is sorted in decreasing order, else it returns False.

def is_increasing(glist):
    for i in range(len(glist) - 1):
        if glist[i] > glist[i + 1]:
            return False
    return True

def is_decreasing(glist):
    for i in range(len(glist) - 1):
        if glist[i] < glist[i + 1]:
            return False
    return True

def func(glol):
    inc = False
    dec = False
    for i in glol:
        if is_increasing(i):
            inc = True
        if is_decreasing(i):
            dec = True
    return inc and dec

alol = [[10, 20], [10, 40, 30], [1, 8, 5], [100, 20, 3]]
alol1 = [[20, 10], [10, 40, 30], [1, 8, 5], [100, 20, 3]]
alol2 = [[10, 20, 1], [10, 40, 30], [1, 18, 50, 0], [100, 200, 3]]

print(func(alol))
print(func(alol1))
print(func(alol2))