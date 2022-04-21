# Author: Anna Mikhailova
# Date: 11/11/21
# Course: COSC_001
# Purpose: Exam 4 Problem 1:

# 1
def func1(n):  # O(n)
    count = 0
    i = 0
    while i < n:
        count = count + 2
        i = i + 1
    print(count)

# 2
def func2(n):  # O(n)
    count = 1
    for i in range(n):
        count = count * 2

# 3
def func3(n):  # O(log(n))
    count = 1
    i = 1
    while i < n:
        i = i * 2
        count = count + 1

# 4
def func4(n):  # O(n * log(n))
    for j in range(n):
        i = n
        while i > 1:
            i = i // 3

# 5
def func5(n):  # O(n^2)
    count = 1
    for i in range(n):
        for j in range(n):
            count = count + 1
    print(count)

# 6
def func6(n):  # O(n)
    count = 1
    for i in range(n):
        count = count + 1
    for j in range(n):
        count = count + 1

# 7
def func7(n):  # O(n^2)
    res = []
    for i in range(n):
        res.insert(0, i)
    return res

# 8
def func8(n):  # O(n)
    res = []
    for i in range(n):
        res.append(i)
    return res

# 9
def func9(n):  # O(n)
    if n <= 1:
        return
    n = n - 2
    print(n)
    func9(n)

# 10
def func10(glist):  # O(n^2), where n = len(glist)
    if len(glist) == 0:
        return 1
    return glist[0] * func10(glist[1:])