# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/4/21
# Purpose: checkpoint for Lab 1
# You will start by putting up a graphics window with just the paddles. Each paddle is a rectangular block,
# 80 pixels high and 20 pixels wide, initially in the upper-left and lower-right corners of a 400 x 400 window.
#
# You may choose whatever colors you like.
#
# The paddles may move up and down as follows:
#
# If the user presses the a key, then the left paddle moves up.
# If the user presses the z key, then the left paddle moves down.
# If the user presses the k key, then the right paddle moves up.
# If the user presses the m key, then the right paddle moves down.
# But no paddle may move outside the window. When the left paddle hits the top window boundary,
# pressing a has no effect, and when it hits the bottom window boundary, pressing z has no effect.
# Likewise, when the right paddle hits the top window boundary, pressing k has no effect,
# and when it hits the bottom window boundary, pressing m has no effect.
#
# Make sure to define constants for things that never change:
#
# The height and width of the window.
# The height and width of the paddles.
# The four keys of interest.
# The amount that a paddle moves when it moves.
# Remember that paddles move only vertically, and they may never move off the window.

from cs1lib import *

# ----------------------------------------------------------------------------------------------------------------------
# Paddles functions
# ----------------------------------------------------------------------------------------------------------------------

def l_paddle(x, y, w, h):
    set_fill_color(0.5, 0.8, 0.2)
    disable_stroke()
    draw_rectangle(x, y, w, h)

def r_paddle(x, y, w, h):
    set_fill_color(0.5, 0.8, 0.2)
    disable_stroke()
    draw_rectangle(x, y, w, h)

# ----------------------------------------------------------------------------------------------------------------------
# Paddle movement functions
# ----------------------------------------------------------------------------------------------------------------------

def l_paddle_move(m):
    global lx, ly
    ly += m
    l_paddle(lx, ly, L_PADDLE_WIDTH, L_PADDLE_HEIGHT)

def r_paddle_move(m):
    global rx, ry
    ry -= m
    r_paddle(rx-R_PADDLE_WIDTH, ry-R_PADDLE_HEIGHT, R_PADDLE_WIDTH, R_PADDLE_HEIGHT)

def key(val):
    global akey, zkey, kkey, mkey
    if val == "a":
        akey = True
    if val == "z":
        zkey = True
    if val == "k":
        kkey = True
    if val == "m":
        mkey = True

def release(val):
    global akey, zkey, kkey, mkey
    if val == "a":
        akey = False
    if val == "z":
        zkey = False
    if val == "k":
        kkey = False
    if val == "m":
        mkey = False

# ----------------------------------------------------------------------------------------------------------------------
# Main function
# ----------------------------------------------------------------------------------------------------------------------

def my_draw():
    # clears screen and sets background colour to dark blue
    set_clear_color(0.1, 0.1, 0.2)
    clear()

    # l_paddle(lx, ly, lx + L_PADDLE_WIDTH, ly + L_PADDLE_HEIGHT)
    # r_paddle(rx - R_PADDLE_WIDTH, ry - R_PADDLE_HEIGHT, rx, ry)

    l_paddle_move(0)
    r_paddle_move(0)

    if akey and ly > 0:
        l_paddle_move(-10)
    if zkey and ly < HEIGHT - L_PADDLE_HEIGHT:
        l_paddle_move(10)
    if kkey and ry > R_PADDLE_HEIGHT:
        r_paddle_move(10)
    if mkey and ry < HEIGHT:
        r_paddle_move(-10)

# ----------------------------------------------------------------------------------------------------------------------
# Variables
# ----------------------------------------------------------------------------------------------------------------------

WIDTH = 800
HEIGHT = 800

lx = 0
ly = 0

rx = 800
ry = 800

L_PADDLE_HEIGHT = 140
L_PADDLE_WIDTH = 60

R_PADDLE_HEIGHT = 140
R_PADDLE_WIDTH = 60

akey = False
zkey = False
kkey = False
mkey = False


start_graphics(my_draw, framerate=200, width=WIDTH, height=lyHEIGHT, key_press=key, key_release=release)


