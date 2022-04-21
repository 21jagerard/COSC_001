# Author: Anna Mikhailova
# Date: 10/4/21
# Purpose: creating a new list

# Purpose: create a list with all integers between m na dn, including m and n
# ParameterP: two positive integers m and n, assume m < n

def create_mn_list(m, n):
    i = m
    rlist = []

    while i <= n:
        # rlist.append(i)
        rlist += [i]
        i += 1

    return rlist

print(create_mn_list(3, 7))

def create_string(n):
    i = 0
    rstr = ""
    while i < n:
        rstr += "a"
        i += 1
        print(rstr)
