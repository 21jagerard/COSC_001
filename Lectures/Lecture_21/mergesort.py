# Author: Anna Mikhailova
# Date: 10/29/21
# Purpose: mergesort

# def merge(glist1, glist2):
#     i = 0
#     j = 0
#     res = []
#
#     while i < len(glist1) and j < len(glist2):  # both lists have numbers remainings
#         if glist1[i] < glist2[j]:
#             res.append(glist1[i])
#             i += 1
#         else:
#             res.append(glist2[j])
#             j += 1
#
#     while j < len(glist2):  # numbers remaining in glist2 but glist 1 is done
#         res.append(glist2[j])
#         j += 1
#
#     while i < len(glist1):  # numbers remaining in glist1  but glist 2 is done
#         res.append(glist1[i])
#         i += 1
#
#     return res
#
# print(merge([1, 2, 3, 9], [5, 7, 8]))


def merge(glist, p, q, r):
    glist1 = glist[p:q+1]
    glist2 = glist[q+1:r+1]

    i = 0
    j = 0
    k = p

    while i < len(glist1) and j < len(glist2):
        if glist1[i] < glist2[j]:
            glist[k] = glist1[i]
            i += 1
            k += 1
        else:  # glist1[i] >= glist2[j]
            glist[k] = glist2[j]
            j += 1
            k += 1

    while j < len(glist2):
        glist[k] = glist2[j]
        j += 1
        k += 1

    while i < len(glist1):
        glist[k] = glist1[i]
        i += 1
        k += 1

def mergesort(glist, p=0, r=None):
    if r == None:
        r = len(glist) - 1

    if p >= r:
        return

    mid = (p + r) // 2

    mergesort(glist, p, mid)
    mergesort(glist, mid+1, r)

    merge(glist, p, mid, r)

mlist = [1, 5, 2, 19, 34, -2, 8, 4, 6, 9, 10, 11]

# Quicksort partition: [9, -5, 10, 11, 23, 71, 24, 13]
mergesort(mlist)
print(mlist)
