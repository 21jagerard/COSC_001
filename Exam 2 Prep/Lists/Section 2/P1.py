# Define a function that takes a list of integers glist as input and returns a list containing
# those numbers in glist that are equal to the index at which they appear in glist. For example:
# If glist = [0, 13, 2, 33, 5, 67, 36, 7] then your function should return [0, 2, 7]
# If glist =[10, 20, 30, 40, 50] then your function should return [ ]

def func(glist):
    new_list = []
    for i in range(len(glist)):
        if i == glist[i]:
            new_list.append(glist[i])
    print(new_list)

func([0, 13, 2, 33, 5, 67, 36, 7])