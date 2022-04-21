# Author: Anna Mikhailova
# Date: 10/26/21
# Course: COSC_001
# Purpose: Short Assignment 8; Perform binary search for key on the sublist of the_list starting at index left and
# going up to and including index right. If key appears in the_list, return the index where it appears.
# Otherwise, return None. Requires the_list to be sorted.

from random import randint

# Parameters: a sorted list of integers, an integer value key, left and right are integers representing indices
# Purpose: Perform binary search for key on the sublist of the_list starting at index left and going up to and
# # including index right. If key appears in the_list, return the index where it appears. Otherwise, return None.
def binary_search(the_list, key, left=None, right=None):
    # If using the default parameters, then search the entire list.
    if left is None and right is None:
        left = 0
        right = len(the_list) - 1

    # Checks that sublist is non-empty
    if right >= left:
        midpoint = (left + right) // 2  # calculates midpoint
        if the_list[midpoint] == key:
            return midpoint
        elif the_list[midpoint] > key:  # else, if key is less than the value at the midpoint, run binary search on the
            # left sublist
            return binary_search(the_list, key, left, midpoint - 1)
        else:  # else, if key is greater than the value at the midpoint, run the binary search on the right sublist
            return binary_search(the_list, key, midpoint + 1, right)
    else:  # if sublist is empty
        return None

# Driver code for binary search.
n = int(input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1

# Binary search wants a sorted list.
the_list = sorted(the_list)
print("The list: " + str(the_list))

while True:
    key = input("What value to search for? ('?' to see the list, 'q' to quit): ")
    if key == "?":
        print("The list: " + str(the_list))
    elif key == "q":
        break
    else:
        key = int(key)
        index = binary_search(the_list, key)
        if index == None:
            print(str(key) + " not found")
        else:
            print(str(key) + " found at index " + str(index))

