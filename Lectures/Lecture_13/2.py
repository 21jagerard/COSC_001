# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/11/21
# Purpose: Categorizing string in given list by length

# Purpose: Define a function that takes a list of strings as parameter and returns a list of lists, where inner lists
# contain strings in given list. Each inner list contains strings of same length and the inner lists with shorter
# strings come before the inner lists with longer strings in the returned list of lists

# Parameter: A non-empty list of non-empty strings

def find_max_len(glist):
    max_l = len(glist[0])

    for s in glist:
        if len(s) > max_l:
            max_l = len(s)

    return max_l

# Parameter: A list of non-empty strings
# Return: A list of lists, where each inner list contains strings in given list

def by_len(glist):
    rlist = []
    if len(glist) == 0:
        return rlist

    maxl = find_max_len(glist)

    for i in range(0, maxl):
        rlist.append([])

    for s in glist:
        indx = len(s) - 1
        rlist[indx].append(s)

    for i in range(len(rlist) - 1, -1, -1):
        if rlist[i] == []:
            del rlist[i]

    return rlist

print(by_len(["max", "x", "min", "exam", "testing", "dartmouth", "a", "test"]))

