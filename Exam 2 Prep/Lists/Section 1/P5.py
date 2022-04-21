# Define a function that takes a list of integers glist as parameter and prints the numbers at even index.
# For example if glist = [1, 4, 5, 20, 2, 12, 81]  then your program should print:
# 1, 5, 2, 81

def func(glist):
    for i in range(len(glist)):
        if i % 2 == 0:
            print(glist[i])

func([1, 4, 5, 20, 2, 12, 81])