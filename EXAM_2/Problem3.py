# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/14/21
# Purpose: Exam 2, Problem 3 -- Define a function same_remainders that takes a list of positive
# integers glist and a positive integer k as parameters. Your function should return a list of
# lists where each inner list contains numbers that give the same remainder when divided by k.
# The order of inner lists or the order in which numbers appear in the inner lists does not matter.
# For example:
# 1. if glist = [11, 5, 4, 9, 2, 7] and k = 3, then your function should return [[9], [4, 7], [5, 11, 2]].
# 2. if glist = [8, 4, 24, 12] and k = 4, then your function should return [[8, 12, 4, 24]].
# 3. if glist = [ ] and k is any positive integer, then your function should return [ ].
# 4. if glist = [7, 3, 18, 11, 8] and k = 6, then your function should return [[18], [7], [8], [3], [11]].

# Purpose: this function takes a list of positive integers, glist, and a positive integer k, and returns the
# biggest remainder of integers in glist mod k
# Parameters: a list of positive integers, glist, and positive integer k
# Return: the biggest remainder of integers in glist mod k
def biggest_remainder(glist, k):
    remainder = 0
    for x in glist:
        if x % k > remainder:
            remainder = x % k
    return remainder

# Purpose: this function takes a list of positive integers glist and a positive integer k and returns a list of
# lists where each inner list contains numbers that give the same remainder when divided by k
# Parameters: a list of positive integers, glist, and positive integer k
# Return: a list of lists where each inner list contains numbers from glist that give the same remainder mod k
def same_remainders(glist, k):
    rem = biggest_remainder(glist, k)
    new_glol = []
    for i in range(rem + 1):
        list_i = []
        for x in glist:
            if x % k == i:
                list_i.append(x)
        if list_i != []:
            new_glol.append(list_i)
    return new_glol


print(same_remainders([11, 5, 4, 9, 2, 7], 3))  # return [[9], [4, 7], [5, 11, 2]]
print(same_remainders([8, 4, 24, 12], 4))  # return [[8, 12, 4, 24]]
print(same_remainders([ ], 2))  # return [ ]
print(same_remainders([7, 3, 18, 11, 8], 6))  # return [[18], [7], [8], [3], [11]]
