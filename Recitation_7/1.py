# # 1. Define a recursive function that takes a positive
# # integer as parameter and prints all the multiples of 5
# # between 1 and n
# # a) in increasing order
# # b) in decreasing order
#
# def func(n):
#     if n > 0:
#         if n % 5 == 0:
#             print(n)
#         func(n-1)
#
# func(15)
#
# def func1(n, i=1):
#     if i <= n:
#         if i % 5 == 0:
#             print(i)
#         func1(n, i+1)
#
# func1(15)

# 2. Define a recursive function that takes a list of
# positive integers as parameter and counts the number of
# 3 digit numbers in the given list.
# You can solve it using list slicing or by using
# an optional index parameter (as we did in class
# with most problems)

def func2(glist, i=0, num_3=0):
    if i <= len(glist) - 1:
        num_3 = func2(glist, i + 1, num_3)
        if len(str(glist[i])) == 3:
            num_3 += 1
    return num_3


print(func2([100, 20, 234, 1, 2, 345, 347]))


# 3. Define a recursive function that takes a list of
# positive integers as parameter and returns a list of
# all 3 digit numbers in the given list.
# You can solve it using list slicing or by using
# an optional index parameter (as we did in class
# with most problems)

def func3(glist, i=0, num_3_list=None):
    if num_3_list is None:
        num_3_list = []
    if i <= len(glist) - 1:
        num_3_list = func3(glist, i + 1, num_3_list)
        if len(str(glist[i])) == 3:
            num_3_list.append(glist[i])
    return num_3_list


print(func3([100, 20, 234, 1, 2, 345, 347]))
