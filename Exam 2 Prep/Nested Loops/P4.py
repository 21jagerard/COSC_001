# Define a function that takes a list of lists as a parameter such that each inner list is a list of integers.
# The function should return a list containing all integers that occur only in one of the inner lists. For example:
# If the given list is [[10, 20, 30, 12], [10, 40, 30], [40, -10,  60], [20, 40]]
# then the function should return [12, -10,  60]
# If the given list is [[10, 20, 12, 30], [10, 40, 30, 60], [40, -10, 12, 60], [-10, 20, 40]]
# then the function should return []
# You can assume that all numbers within any inner list are unique.
# But the same number can appear in multiple inner lists.

def big_list(glol):
    new_list = []
    for i in glol:
        for j in i:
            new_list.append(j)

    return new_list

def unique_nums(glol):
    long_list = big_list(glol)
    unique_list = []
    for i in range(len(long_list)):
        unique = True
        for j in range(len(long_list)):
            if (i != j) and long_list[i] == long_list[j]:
                unique = False
        if unique:
            unique_list.append(long_list[i])

    print(unique_list)

unique_nums([[10, 20, 30, 12], [10, 40, 30], [40, -10,  60], [20, 40]])
unique_nums([[10, 20, 12, 30], [10, 40, 30, 60], [40, -10, 12, 60], [-10, 20, 40]])
