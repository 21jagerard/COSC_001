# Author: Anna Mikhailova
# Date: 10/6/21
# Purpose: for loop vs. while loop (End condition + re-computation)

# def func(n):
#     i = 0
#     while i < n:
#         print(i)
#         i += 1
#
#     print("End of while loop", i)
#
# func(4)
#
# def func_for(n):
#     for i in range(0, n):
#         print(i)
#
#     print("End of for loop", i)
#
# func_for(4)

# ----------------------------------------------------------------------------------------------------------------------
# Recomputation
# ----------------------------------------------------------------------------------------------------------------------
#
# i = 0
# while i < 10:
#     print(i)
#     if i == 4:
#         i = 6
#     i += 1
#
# for i in range(0, 10):
#     print(i, end = " ")
#     if i == 4:
#         i = 6
#     print(i)

# ----------------------------------------------------------------------------------------------------------------------
# Deleting from a list
# ----------------------------------------------------------------------------------------------------------------------

mlist = [18, 4, 6, 8, 8, 9]
i = 0
# while i < len(mlist):
#     if mlist[i] == 8:
#         del mlist[i]
#     else:
#         i += 1
# print(mlist)
#
# for i in range(0, len(mlist)):
#     if mlist[i] == 8:
#         del mlist[i]
#
# print(mlist)

for i in range(len(mlist)-1, -1, -1):
    if mlist[i] == 8:
        del mlist[i]

print(mlist)
