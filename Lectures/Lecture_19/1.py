def sum_list(glist):
    if len(glist) == 0:
        return 0

    slist = glist[1:]
    # print_list(slist)
    # print(glist[0])

    x = sum_list(slist)
    return x + glist[0]

print(sum_list([3, 6, 2, 5]))

def sum_list2(glist, i=0):
    # base case
    if len(glist) == i:
        return 0

    x = sum_list2(glist, i+1)
    return x + glist[i]

print(sum_list2([3, 6, 2, 5]))