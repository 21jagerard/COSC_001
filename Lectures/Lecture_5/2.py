# Author: Anna Mikhailova
# Date: 09/22/21
# Purpose: count function demo

# x = "Test"
# y = "No. 1"
# z = x + y
# print(z)

def count_up(n):
    count = 0

    while count <= n:
        print(count)
        count += 1


x = int(input("Enter a number:"))
count_up(x)

# can call as many times as you want
