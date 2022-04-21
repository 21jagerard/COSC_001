# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/11/21
# Purpose: Demo sorting

# Purpose: Find the index of the minimum value in the list between i and the end of the list
def find_min_indx(glist, i):
    min_i = i
    indx = i

    while indx < len(glist):
        if glist[indx] < glist[min_i]:
            min_i = indx
        indx += 1

    return min_i

print(find_min_indx([5, -7, 8, -2, 3,], 2))

# Purpose: Define a function tbat sorts a given list of integers in increasing order using selection sort
# Parameter: a list of integers
# Return: none

def selection_sort(glist):
    for i in range(0, len(glist)):
        mi = find_min_indx(glist, i)

        temp = glist[mi]
        glist[mi] = glist[i]
        glist[i] = temp

mlist = [8, -4, 8, -9, -4, 4, 5, 23, 18, 6]
# selection_sort(mlist)
# print(mlist)

mlist.sort(reverse = False)
nlist = sorted(mlist, reverse = True)
print(nlist, mlist)