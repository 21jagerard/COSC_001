# Author: Anna Mikhailova
# Date: 10/22/21
# Purpose: iterating over a list/string recursively

def sum_list(glist):
    if len(glist) == 0:
        return 0

    small_list = glist[1:]
    x = sum_list(small_list)

    return x + glist[0]

print(sum_list([10, 2, 4, 7]))