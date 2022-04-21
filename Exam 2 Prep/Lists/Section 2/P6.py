#  Define a function that takes two lists gl1 and gl2 of integers as parameters. Assume the following:
# a. Each list has unique numbers. (Note: A number can occur in both lists)
# b. Both lists are sorted in increasing order
#
# Your function should return a list that is sorted in increasing order and contains the numbers in both the lists.
# But if a number appears in both the lists then it should appear only once in the result list.
# For example:
# If gl1 = [10, 20, 30, 40] and gl2 = [11, 20, 44, 56, 60] then the result list will be [10, 11, 20, 30, 40, 44, 56, 60]
# If gl1 = [ ] and gl2 = [11, 20, 44] then the result list will be [11, 20, 44]

def func(gl1, gl2):
    new_list = []
    for i in gl1:
        if i not in gl2:
            new_list.append(i)
        for j in gl2:
            if j not in new_list:
                new_list.append(j)
    new_list = sorted(new_list, reverse=False)
    print(new_list)

func([10, 20, 30, 40], [11, 20, 44, 56, 60])
