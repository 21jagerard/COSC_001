# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/4/21
# Purpose: Recitation 3, Problem 1
# Use tools cs1lib to draw a red circle of radius = 20 on the center of the graphics window
# if "l" is pressed, moves ball left until released
# if "r" is pressed, moves ball right until released
# if both pressed, ball does not move

from cs1lib import *

def key(val):
    global left, right
    if val == "l":
        left = True
    if val == "r":
        right = True

def release(val):
    global left, right
    if val == "l":
        left = False
    if val == "r":
        right = False

def circle(x, y):
    set_fill_color(1, 0, 0)
    draw_circle(x, y, 20)

def my_draw():
    global bx, by
    set_clear_color(1, 1, 1)
    clear()

    circle(bx // 2, by // 2)

    if left:
        bx -= 10
    if right:
        bx += 10

WIDTH = 800
HEIGHT = 800
bx = WIDTH
by = HEIGHT

left = False
right = False

start_graphics(my_draw, width=WIDTH, height=HEIGHT, key_press=key, key_release=release)