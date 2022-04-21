# Purpose: Given a list if positive integers return a list of the squares of the numbers in given list

def square_list(glist, i=0):
    if len(glist) == i:
        return []

    rlist = square_list(glist, i+1)
    rlist.insert(0, glist[i]**2)

    return rlist

print(square_list([2, 5, 3, 6]))