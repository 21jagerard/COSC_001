#Author: Vasanta
#Date: 11/08/2021
#Purpose: Demo dictionaries

#Purpose: Print how many times each value appears in the list
#Restriction: The runtime of the function must be O(n+m), where m is the length
#of glist.
#Assumption: glist only has values between 0 and n (including n)

# def func(glist, n):
#     count_list = [0]*(n+1)
#     print(count_list)
#
#     for val in glist:
#         count_list[val] = count_list[val] + 1
#
#     for i in range(len(count_list)):
#         print(i, count_list[i])
#
# mlist = [10, 5, 3, 8, 2, 0, 6, 2, 8, 9, 10, 3, 5, 8, 9, 5]
# func(mlist, 10)

#Dictionaries have key-value pairs, key is like index in a list
#and value is like the element in the list
#Key and value can be of any type
d = {} #O(1)
d["cs1"] = 5 #O(1)
d["cs10"] = 3
d["cs50"] = 4
d["cs57"] = 1
d["cs30"] = 2

print(d) #O(n), n is length of d
print(d["cs10"]) #O(1)
print(len(d)) #O(1)
#print(d["cs70"]) #error
del d["cs10"] #O(1)
print(d)

#The loop below is O(n), n is len(d)
for key in d: #This look will go over all the keys in the dictionary d
    #print(key, d[key])
    if d[key] == 4:
        print(key)


#O(1), checking is a key in there in the dictionary
if "cs50" in d:
    print(d["cs50"])



