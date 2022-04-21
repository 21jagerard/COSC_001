# Author: Anna Mikhailova
# Date: 10/6/21
# Purpose: range function

mlist = [6, 6, 23, 8, 3, 91]

for i in range(0, len(mlist)):  # [0, 1, 2, 3, 4, 5]
    print(mlist[i], i)

for i in range(len(mlist)-1, 0, -1): 
    print(mlist[i], i)
