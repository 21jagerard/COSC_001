# Define a function that takes two integers m and n as parameters and returns a list of all integers
# between m and n in the list (including both m and n if they are in the list). You may assume m <= n.

def func(m, n):
    glist = []
    i = m
    while i <= n:
        glist.append(i)
        i += 1
    print(glist)

func(5, 12)