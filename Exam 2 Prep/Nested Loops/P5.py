# Define a function that takes a list of positive integers (greater than 0) as a parameter and returns a list of lists.
# Your function should group the numbers based on the number of digits they have.
# Each inner list in the returned list represents one such group. Also, in the returned list the inner lists
# should be sorted in order of length of the numbers they contain. You are not allowed to sort the given list.
# For example:
# If the given list is [9, 67, 200, 456, 20023, 3, 10, 999] then it should return
# [[9, 3], [67, 10], [200, 456, 999], [20023]]
# If the given list is [] then it should return []

def longest_int(glist):
    longest = glist[0]
    for i in glist:
        if len(str(i)) > len(str(longest)):
            longest = i
    return longest

def sort_int(glist):
    limit = longest_int(glist)
    new_list = []
    for i in range(len(str(limit)) + 1):
        list_i = []
        for j in glist:
            if len(str(j)) == i:
                list_i.append(j)
        if list_i != []:
            new_list.append(list_i)
    print(new_list)

sort_int([9, 67, 200, 456, 20023, 3, 10, 999])