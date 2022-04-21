# Author: Anna Mikhailova
# Date: 09/27/21
# Purpose: Practice Assignment 1
# Draw a Bull's-eye with a blue outer circle, green middle circle,
# and red inner circle. Use a separate function for each circle

from cs1lib import *

def blue_circ():
    set_fill_color(0, 0, 1)
    draw_circle(200, 200, 120)

def green_circ():
    set_fill_color(0, 1, 0)
    draw_circle(200, 200, 80)

def red_circ():
    set_fill_color(1, 0, 0)
    draw_circle(200, 200, 40)

def my_draw():

    blue_circ()
    green_circ()
    red_circ()

start_graphics(my_draw)

