# Define a function that takes two lists glist1 and glist2 as parameters and returns True
# if they are the reverse of each other, otherwise returns False.
# For simplicity you can assume that the given lists contain only integers.

def func(glist1, glist2):
    for i in range(len(glist1)):
        if glist1[i] != glist2[len(glist2) - (i+1)]:
            return False
        i += 1
    return True

print(func([1, 2, 3], [4, 2, 1]))