# Author: Anna Mikhailova
# Date: 10/1/21
# Purpose: lists

mlist = [10, 4, 7, 12, 45, 40]
# indices 0  1  2  3   4   5....
print(mlist)

print(len(mlist))

print(mlist[3])

mlist[2] = 100

print(mlist)
print(mlist[len(mlist)-1])
print(mlist[-1])

# Adding to a list
mlist.append(3)
print(mlist)

# Adding at a specific index
mlist.insert(1, 12)
print(mlist)

# Delete from a list
mlist.remove(12)
print(mlist)

# Delete a specific index
del mlist[0]
print(mlist)