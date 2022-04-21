# Author: Anna Mikhailova
# Date: 10/6/21
# Purpose: nested while loops

# i = 0
# while i < 5:
#     j = 0
#     while j < 3:
#         print(i, j)
#         j += 1
#     i += 1

def func(slist):
    i = 0
    while i < len(slist):
        cj = 0
        count_1 = 0
        in_s = slist[i]
        while j < len(in_s):
            if in_s[j] == "a":
                count_a += 1
            j += 1
        print(in_s, count_a)
        i += 1

func(["amelira", "vasanta", "daniel", "Samuel", "alejo"])