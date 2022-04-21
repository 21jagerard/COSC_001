# Author: Anna Mikhailova
# Date: 10/1/21
# Purpose: animations

from cs1lib import *

WIDTH = 800
HEIGHT = 800

sx = WIDTH // 2
sy = HEIGHT // 2
SSIZE = 50

bx = WIDTH // 2
by = HEIGHT // 2
bsize = 100
mpressed = False
gpressed = False
spressed = False

# ----------------------------------------------------------------------------------------------------------------------
# SMILEY FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

# Purpose: drawing a rolling eye
# Parameters: x, y -- location and size
def draw_eye(x, y, size):
    # Outer circle
    set_fill_color(1, 1, 1)
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_stroke_width(1)
    draw_circle(x, y, size)

    # Inner circle
    set_fill_color(0, 0, 0)
    draw_circle(x, y - 0.5 * size, 0.5 * size)


# Purpose: drawing a smiley face!
# Parameters: position coordinates, size, colour values
def smiley_draw(x, y, size, r, g, b):
    # drawing face
    set_fill_color(r, g, b)
    # disable_stroke()
    enable_stroke()
    set_stroke_color(0, 0, 0)
    draw_circle(x, y, size)

    # drawing eyes
    draw_eye(x - 0.3 * size, y - 0.3 * size, 0.2 * size)
    draw_eye(x + 0.3 * size, y - 0.3 * size, 0.2 * size)

    # drawing mouth
    set_stroke_color(1, 0, 0)
    set_stroke_width(2)
    draw_line(x - 0.3 * size, y + 0.3 * size, x + 0.3 * size, y + 0.3 * size)

# ----------------------------------------------------------------------------------------------------------------------
# MAIN FUNCTION
# ----------------------------------------------------------------------------------------------------------------------

def my_draw():
    global bsize
    # set the background
    set_clear_color(1, 1, 1)
    clear()

    # Draw the big fellow
    smiley_draw(bx, by, bsize, 0.5, 1, 1)

    if gpressed == True and bsize < 300:
        bsize += 10

    if spressed == True and bsize > 10:
        bsize -= 10

# ----------------------------------------------------------------------------------------------------------------------
# MOVEMENT FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

def my_mpress(mx, my):
    global mpressed
    mpressed = True

def my_mrelease(mx, my):
    global mpressed
    mpressed = False

def my_mmove(mx, my):
    global bx, by

    if mpressed:
        # mpressed == True: -- mpressed is true, condition will be true //  mpressed is false, condition will  be false
        bx = mx
        by = my

def my_kpress(value):
    global gpressed, spressed

    if value == "g":  # and bsize < 300:
        gpressed = True
        # bsize += 10

    if value == "s":  # and bsize > 10:
        spressed = True
        # bsize -= 10

def my_krelease(value):
    global gpressed, spressed

    if value == "g":  # and bsize < 300:
        gpressed = False
        # bsize += 10

    if value == "s":  # and bsize > 10:
        spressed = False
        # bsize -= 10

start_graphics(my_draw, width=WIDTH, height=HEIGHT, mouse_press=my_mpress, mouse_release=my_mrelease,
               mouse_move=my_mmove, key_press=my_kpress, key_release=my_krelease)
