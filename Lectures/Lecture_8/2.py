# Author: Anna Mikhailova
# Date: 09/29/21
# Purpose: animations

from cs1lib import *

WIDTH = 800
HEIGHT = 800

sx = WIDTH // 2
sy = HEIGHT // 2
SSIZE = 50

bx = WIDTH // 2
by = HEIGHT // 2
BSIZE = 100


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
    draw_circle(x, y - 0.5*size, 0.5*size)

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
    draw_eye(x - 0.3*size, y - 0.3*size, 0.2*size)
    draw_eye(x + 0.3*size, y - 0.3*size, 0.2*size)

    # drawing mouth
    set_stroke_color(1, 0, 0)
    set_stroke_width(2)
    draw_line(x - 0.3*size, y + 0.3*size, x + 0.3*size, y + 0.3*size)

def my_draw():
    # set the background
    set_clear_color(1, 1, 1)
    clear()

    # Draw the little fellow
    smiley_draw(sx, sy, SSIZE, 1, 1, 0)

    # Draw the big fellow
    smiley_draw(bx, by, BSIZE, 0.5, 1, 1)

def my_mpress(mx, my):
    # print("In mouse press:", mx, my)
    global sx, sy, bx, by  # DO NOT FORGET THIS STEP
    sx = bx
    sy = by
    bx = mx
    by = my

def my_mrelease(mx, my):
    print("In mouse release:", mx, my)

def my_mmove(mx, my):
    print("In mouse move", mx, my)

start_graphics(my_draw, width = WIDTH, height = HEIGHT, mouse_press = my_mpress, mouse_release = my_mrelease, mouse_move = my_mmove)