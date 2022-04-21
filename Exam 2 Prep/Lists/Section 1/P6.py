# Define a function that takes a list of integers glist and an integer n as parameters and returns a new list
# that contains the numbers in glist that are greater than n.

def func(glist, n):
    new_list = []
    for i in glist:
        if i > n:
            new_list.append(i)
    return new_list

print(func([1, 4, 5, 20, 2, 12, 81], 4))