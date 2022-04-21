# Author: Anna Mikhailova
# Date: 10/4/21
# Purpose: Demo: going through all elements in a list

# Purpose: sum of all elements of a list of integers
# Parameter: A list of integers


def sum_list(glist):
    i = 0
    sum = 0

    while i < len(glist):
        sum += glist[i]
        i += 1
    return sum

print(sum_list([4, 6, 2, -7, 8]))

# Purpose: find the max element in a list of integers using while loop
# Parameter: A list of integers

def find_max(glist):
    curr_max = glist[0]
    i = 1
    while i < len(glist):
        if curr_max < glist[i]:
            curr_max = glist[i]
        i+=1
    return curr_max

mlist = [4, 6, 20, -7, 8]
print(find_max(mlist))

# Purpose: find the index of the max element in a list of integers using while loop
# Parameter: a list of integers

def find_max_i(glist):
    curr_max_i = 0
    i = 1
    while i < len(glist):
        if glist[curr_max_i] < glist[i]:
            curr_max_i = i
        i += 1

    return curr_max_i

mlist = [4, 6, 20, -7, 8]
print(find_max_i(mlist))

# Purpose: find the max element in a list of integers using for loop
# Parameter: A list of integers

def find_max(glist):
    curr_max = glist[0]

    for x in glist:
        if curr_max < x:
            curr_max = x

    return curr_max

mlist = [4, 6, 20, -7, 8]
print(find_max(mlist))

# Purpose: find the index of the max element in a list of integers using for loop
# Parameter: a list of integers

def find_max_i_for(glist):
    curr_max_i = 0

    for i in range(0, len(glist)):
        if glist[curr_max_i] < glist[i]:
            curr_max_i = i
    return curr_max_i
mlist = [4, 6, 20, -7, 80]
print(find_max_i_for(mlist))
