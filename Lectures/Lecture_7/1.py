# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: Demo break and continue statements

def func(n):
    i = 5

    while i < n:
        i += 1
        if i == 8:
            # break --> stops loop at the last i that is smaller than 8
            continue  # --> skips over i that is equal to 8
        print(i)

    print("Out of while loop")

func(15)