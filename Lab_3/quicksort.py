# Author: Anna Mikhailova
# Date: 11/2/21
# Course: COSC_001
# Purpose: Lab 3; sorting functions

# Purpose: sorts the sublist of the_list from indices p to r -- the_list[p:r+1]
# Parameters: a list the_list, start and end indices -- p, r --, and a compare function
# Return: returns the index where the pivot was placed -- in this case, index i + 1
def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    i = p - 1
    j = p
    while j < r:
        if compare_func(the_list[j], pivot):
            i += 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
        j += 1
    the_list[i + 1], the_list[r] = the_list[r], the_list[i + 1]
    return i + 1

# which sorts the sublist the_list[p : r+1], whose first item is in the_list[p] and whose last item is in the_list[r]
# Purpose: recursively sorts the given list via partitioning sublists of the_list
# Parameters: a list the_list, start and end indices -- p, r, -- and a compare function
# Return: returns the sorted list
def quicksort(the_list, p, r, compare_func):
    if len(the_list[p:r]) < 2:  # base case -- a sublist with fewer than two items is already sorted
        return the_list
    if p < r:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q - 1, compare_func)
        quicksort(the_list, q, r, compare_func)

# Purpose: calls the quicksort function on a list
# Parameters: a list -- the_list -- and a compare function
# Return: None
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)
