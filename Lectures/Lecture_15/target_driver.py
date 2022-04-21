# Author: Anna Mikhailova
# Date: 10/15/21
# Purpose: driver file for bulls eye

from cs1lib import *
from Lectures.Lecture_15.bulls_eye import Bullseye
from random import randint

H = 1000
W = 1000
N = 100

blist = []
for i in range(N):
    x = randint(0, 1000)
    y = randint(0, 1000)
    size = randint(10, 30)
    b = Bullseye(x, y, size)
    blist.append(b)

def main():
    set_clear_color(1, 1, 1)
    clear()

    for b in blist:
        b.update()
        b.draw()

start_graphics(main, width = W, height = H)




