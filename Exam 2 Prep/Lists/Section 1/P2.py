def func2(list1, list2):
   i = 0
   if len(list1) == len(list2):
       while i < len(list2):
           list1[i] = list2[i]
           i = i + 1

mylist1 = [10, 40, 30, 20, 50]
mylist2 = [1, 4, 3, 2, 5]
func2(mylist1, mylist2)
print(mylist1)