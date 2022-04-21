# Author: Anna Mikhailova
# Date: 10/13/21
# Purpose: Demo driver file


from Lectures.Lecture_14.ball import Ball
from cs1lib import *


b1 = Ball(200, 300)
b2 = Ball(100, 200)

# # b1.update_ball()
# # b2.update_ball()
# print(b1)
# s = str(b1) + str(b2)
# print(s)

def maindraw():
    b1.draw(1, 0, 0)
    b2.draw(0, 1, 0)

start_graphics(maindraw)