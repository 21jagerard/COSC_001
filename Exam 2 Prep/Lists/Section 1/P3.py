def func(list1, list2):
    if len(list1) == len(list2):
        return list2

mylist1 = [10, 40, 30, 20, 50]
mylist2 = [1, 4, 3, 2, 5]
mylist1 = func(mylist1, mylist2)
print(mylist1)