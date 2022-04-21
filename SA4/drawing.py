# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/1/21
# Purpose: Short Assignment 4
#
# In this assignment, you will write a drawing program, a bit like MS Paint or Adobe Photoshop.
# Your program should open up a graphics window, and allow the user to use the mouse to draw on a simulated chalkboard.
# If the mouse button is released, the user should be able to move the mouse pointer around without drawing anything.
# If the mouse button is pressed down, the board is drawn on using the current chalk color.
#
# The board should be black. The color should initially be white. If the user presses the key 'r',
# then the current chalk color should change to red, and everything drawn after this should be red,
# until another color key is pressed. Use 'b' for blue, 'g' for green, and 'y' for yellow.
# You can add other colors if you like, but you do not need to.

from cs1lib import *

# ----------------------------------------------------------------------------------------------------------------------
# MOVEMENT FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

# Purpose: tracking press of mouse
# Parameters: mx and my -- coordinates for the x and y location of mouse, respectively
def press(mx, my):
    global mpressed
    mpressed = True

# Purpose: tracking release of mouse
# Parameters: mx and my -- coordinates for the x and y location of mouse, respectively
def release(mx, my):
    global mpressed
    mpressed = False

# Purpose: tracking mouse movement across graphics window
# Parameters: mx and my -- coordinates for the x and y location of mouse, respectively
def move(mx, my):
    global new_x, new_y, old_y, old_x
    new_y = my
    new_x = mx

# Purpose: switching colours depending on key pressed
# Parameters: an keyboard input element (a single character)
def key(val):
    if val == "r":
        set_stroke_color(1, 0, 0)
    if val == "b":
        set_stroke_color(0, 0, 1)
    if val == "g":
        set_stroke_color(0, 1, 0)
    if val == "y":
        set_stroke_color(1, 1, 0)
    if val == "w":
        set_stroke_color(1, 1, 1)
    if val == "c":
        clear()

# ----------------------------------------------------------------------------------------------------------------------
# MAIN FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

# Purpose: draws a line wherever used wants to
# Parameters: none
def pic_draw():
    global old_x, old_y, new_x, new_y
    enable_stroke()
    set_stroke_width(2)

    draw_line(old_x, old_y, new_x, new_y)
    old_x = new_x
    old_y = new_y
# Parameters: none
def my_draw():
    # clears screen and sets background colour to black
    global first_clear, old_y, old_x
    if first_clear:
        set_clear_color(0, 0, 0)
        clear()
        set_stroke_color(1, 1, 1)
        first_clear = False

    # calls the draw functions once the mouse is pressed
    if mpressed:
        pic_draw()
    elif not mpressed:
        old_x = mouse_x()
        old_y = mouse_y()

WIDTH = 1600
HEIGHT = 1600

old_x = 400
old_y = 400
new_x = 400
new_y = 400

mpressed = False
first_clear = True

start_graphics(my_draw, width=WIDTH, height=HEIGHT, key_press=key, mouse_press=press, mouse_release=release,
               mouse_move=move)

