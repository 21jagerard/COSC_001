# Purpose: runtime of lists

def func1(n):  # O(n)
    rlist = []
    for i in range(n):
        rlist.append(i)

    return rlist

print(func1(4))

def func2(n):  # O(n^2)
    rlist = []
    i = n-1
    while i >= 0:
        rlist.insert(0, i)
        i -= 1

    return rlist

print(func2(4))

def func3(glist, val):  # O(n^2), n is len(glist)
    i = 0
    while i < len(glist):
        if glist[i] == val:
            del glist[i]
        i += 1

def func4(glist, val):  # O(n), n is len(glist)
    i = 0
    while i < len(glist):
        if glist[i] == val:
            return i
        i += 1

    return None

def func5(n):  # O(log(n))
    i = n
    while i > 1:
        i //= 2

def func6(n):  # O(n
    if n == 0:
        return

    print(n)
    func6(n-1)

def func7(n):  # O(log(n))
    if n < 1:
        return n
    print(n)
    func7(n//2)

def func8(glist):  # O(n^2), n = len(glist)
    if len(glist) == 0:
        return
    print(glist[0])
    slist = glist[1:]
    func8(slist)

def func9(glist, i=0):  # O(n), n = len(glist)
    if len(glist) == 1:
        return
    print(glist[i])
    func9(glist, i+1)
