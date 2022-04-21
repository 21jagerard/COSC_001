# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/11/21
# Purpose: Problem 1 -- Define a function that takes positive integer n and returns a list of all multiples of 3 or
# 5 between 1 and n (including n if it meets the conditions).

def mult_3_or_5(n):
    mult_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            mult_list.append(i)
    return mult_list

print(mult_3_or_5(12))
