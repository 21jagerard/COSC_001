# Define a function that takes a list of integers glist as parameter and prints the even numbers in glist.
# For example if glist = [1, 4, 5, 20, 2, 12, 81]  then your program should print:
# 4, 20, 2, 12

def func(glist):
    for i in glist:
        if i % 2 == 0:
            print(i)

func([1, 4, 5, 20, 2, 12, 81])
