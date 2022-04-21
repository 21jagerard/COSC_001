# Author: Anna Mikhailova
# Date: 09/22/21
# Purpose: demo import statements

# from math import sqrt
# print(sqrt(4))

# import cs1lib == from cs1lib import *

from cs1lib import *


def my_draw():  # this function should NOT take any parameters
    print("Test")


start_graphics(my_draw)
# needs to be called in the main part of your code;
# when you run it, creates a graphics window and calls function 40x / sec
