# 1. Define a recursive function that takes a list of integers as parameter and returns True if the list is sorted in
# increasing order otherwise it returns False.
def func1(glist):
    if glist[0] > glist[1]:
        return False
    else:
        func1(glist[1:])
    return True

# 2. Define a recursive function that takes two strings s1 and s2 as parameters and checks if s2 is a prefix of s1.
# For example: s2 = “test” and s = “testing” then s1 is a prefix of s2.
def func2(s1, s2):
    if s2[0] != s1[0]:
        return False
    else:
        func2(s1[1:], s2[1:])
    return True

# 3. Define a recursive function that takes two strings s1 and s2 as parameters and checks if s2 is a substring of s1.
def func3(s1, s2):
    if s2[0] not in s1:
        return False
    else:
        func2(s1, s2[1:])
    return True

# 4. Write a recursive function that takes two non-negative integers n and k as parameters and prints the first k
# even numbers greater than n.
def func4(n, k):
    if k <= 0:
        return
    else:
        print(n + 1)
        func4(n + 1, k - 1)

# 5. Write a recursive function that takes two non-negative integers n and k as parameters and returns a list
# containing first k even numbers greater than n.
def func5(n, k):
    if k <= 0:
        return
    else:
        if (n + 1) % 2 == 1:
            func5(n+1, k)
        else:
            print(n + 1)
            func5(n + 1, k - 1)

# 6. Write a recursive function that takes a list of integers glist that is sorted in increasing order and an integer
# key as a parameter. The function should insert the key into glist such that glist remains sorted.
def func6(glist, key):
    if key <= glist[0]:
        glist.insert(0, key)
        return glist
    else:
        func6(glist[1:], key)

# 7. Write a recursive function find_min that takes a list of integers as a parameter and returns the minimum element
# in the list.'
def func7(glist, i=0):
    # for i in glist:
    #     if glist[0] < glist[i]:
    #         return glist[0]
    #     else:
    #         func7(glist[1:])
    if i == len(glist) - 1:
        return glist[-1]

    m = func7(glist, i + 1)
    if m < glist[i]:
        return m
    else:
        return glist[i]

# 8. Write a recursive function find_min_index that takes a list of integers as a parameter and returns that index of
# the minimum element in the list.
def func8(glist, i=0):
    if i == len(glist) - 1:
        return i

    m = func8(glist, i + 1)
    if glist[m] < glist[i]:
        return m
    else:
        return glist[i]

# 9. Define a recursive function that takes two positive integers n and k as parameters and does the following:
# prints first k even numbers between 1 and n if there are at least k even numbers between 1 and n
# otherwise it prints all the even numbers between 1 and n.
def func9(n, k):
    if n == 1:
        return 0

    x = func9(n - 1, k)
    if x == k:
        return x
    else:
        if n % 2 == 0:
            print(n)
            return x + 1
        else:
            return x
