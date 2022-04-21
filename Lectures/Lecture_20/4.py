# Author: Anna Mikhailova
# Date: 10/27/21
# Purpose: recursively computing fibonacci and why it's a bad idea

def binary_search(glist):
    start = 0
    end = len(glist) - 1

    while start <= end:
        mid = (start + end) // 2

        if glist[mid] < val:
            start = mid + 1
        elif glist[mid] > val:
            end = mid - 1
        else:
            return mid
    return

