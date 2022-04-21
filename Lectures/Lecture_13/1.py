# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/11/21
# Purpose: Categorizing negatives and positives

# Purpose: Define a function that takes a list of non-zero integers as parameters an returns a list
# containing two inner lists. the first inner list contains all negative numbers in the given list
# and the second inner list contains all positive numbers in the given list

# Parameter: A list of non-zero integers
# Return: a list of lists where each inner list has integers in given list
def neg_pos(glist):
    rlist = [[], []]

    for x in glist:
        if x < 0:
            rlist[0].append(x)
        else:
            rlist[1].append(x)

    return rlist

print(neg_pos([1, 4, -8, 9, 45, -3, -6, 45]))