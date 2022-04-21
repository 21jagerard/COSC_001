def func1(list1, list2):
   if len(list1) == len(list2):
       list1 = list2

mylist1 = [10, 40, 30, 20, 50]
mylist2 = [1, 4, 3, 2, 5]
func1(mylist1, mylist2)
print(mylist1)
