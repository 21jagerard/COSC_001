# Author: Anna Mikhailova
# Date: 09/24/21
# Purpose: demo cs1lib by drawing rolling eyes smiley

from cs1lib import *

# Purpose: drawing an eye
# Parameters: x, y -- location and size
def draw_eye(x, y, size):
    # Outer circle
    set_fill_color(1, 1, 1)
    set_stroke_color(0, 0, 0)
    draw_circle(x, y, size)

    # Inner circle
    set_fill_color(0, 0, 0)
    draw_circle(x, y - 0.5*size, 0.5*size)

# Purpose: drawing a smiley face!
# Parameters: no parameters
def smiley_draw():
    # setting background colour to white
    set_clear_color(1, 1, 1)
    clear()

    # drawing face
    set_fill_color(1, 1, 0)
    # disable_stroke()
    enable_stroke()
    set_stroke_color(0, 0, 0)
    draw_circle(200, 200, 100)

    # drawing eyes
    draw_eye(160, 170, 25)
    draw_eye(240, 170, 25)

    # drawing mouth
    set_stroke_color(1, 0, 0)
    set_stroke_width(2)
    draw_line(170, 240, 230, 240)

start_graphics(smiley_draw, width = 800, height = 800)