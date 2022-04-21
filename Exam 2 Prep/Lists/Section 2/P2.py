# Define a function that takes a list of integers glist that is sorted (in increasing order)
# and an integer n as parameters and inserts n into glist in such a way that glist remains sorted.

def func(glist, n):
    for i in range(len(glist)):
        if glist[i] <= n <= glist[i + 1]:
            glist.insert(i+1, n)
            break
        # i += 1
    print(glist)

func([1, 2, 3, 4, 7, 8], 5)