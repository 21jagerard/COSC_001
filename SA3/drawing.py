# Author: Anna Mikhailova
# Date: 09/22/21
# Course: COSC_001
# Purpose: Short Assignment 3, write some code that creates 8 shapes, 2 lines, your name.
# Your code should include and use at least three functions that set colours
# You should write and use one function that sets the background.
# You also need a function that makes the entire drawing

from cs1lib import *

# ----------------------------------------------------------------------------------------------------------------------
# COLOUR FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

# Purpose: Setting background colour to light blue
# Parameters: none
def background_blue():
    set_clear_color(0.6, 0.8, 0.9)
    clear()

# Purpose: sets fill colour to white
# Parameters: none
def colour_white():
    set_fill_color(1, 1, 1)

# Purpose: sets fill colour to black
# Parameters: none
def colour_black():
    set_fill_color(0, 0, 0)

# Purpose: sets fill colour to red
# Parameters: none
def colour_red():
    set_fill_color(1, 0, 0)

# Purpose: outline the shape in black
# Parameters: none
def outline_black():
    enable_stroke()
    set_stroke_color(0, 0, 0)

# ----------------------------------------------------------------------------------------------------------------------
# SHAPE FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

# Purpose: draw a snowball
# Parameters: x, y coordinates, and r which is the size
def snow_ball(x, y, r):
    colour_white()
    disable_stroke()
    draw_circle(x, y, r)

# Purpose: drawing a little black dot to use for the eyes and mouth
# Parameters: x and y coordinates
def draw_face(x, y, r):
    colour_black()
    disable_stroke()
    draw_circle(x, y, r)

# Purpose: drawing a carrot nose
# Parameters: none
def draw_nose():
    outline_black()
    set_fill_color(1, .6, 0)
    draw_triangle(195, 92, 195, 100, 230, 96)

# Purpose: drawing a scarf
# Parameters: none
def draw_scarf():
    outline_black()
    colour_red()
    draw_polygon([[165, 130], [157, 140], [243, 140], [235, 130]])

    draw_circle(220, 135, 7)
    draw_polygon([[218, 142], [222, 142], [230, 192], [210, 192]])

# Purpose: drawing the snowman's hands
# Parameters: none
def draw_hands():
    outline_black()
    set_stroke_width(3)
    # left hand
    draw_line(135, 190, 85, 180)
    draw_line(85, 180, 80, 160)
    draw_line(85, 180, 80, 200)
    draw_line(85, 180, 65, 180)

    # right hand
    draw_line(265, 190, 315, 180)
    draw_line(315, 180, 320, 160)
    draw_line(315, 180, 320, 200)
    draw_line(315, 180, 335, 180)

# Purpose: signing my name
# Parameters: none
def sign_name():
    colour_black()
    enable_stroke()
    draw_text("Anna Mikhailova", 280, 390)

# Purpose: drawing a hat
# Parameters: none
def draw_hat():
    colour_black()
    draw_polygon([[165, 60], [235, 60], [238, 62], [162, 62]])
    draw_polygon([[180, 20], [220, 20], [223, 60], [177, 60]])

# ----------------------------------------------------------------------------------------------------------------------
# MAIN CODE
# ----------------------------------------------------------------------------------------------------------------------

# Purpose: Drawing a snowman!
# Parameters: none!
def my_draw():
    background_blue()

    # drawing body of snowman
    snow_ball(200, 300, 85)
    snow_ball(200, 190, 65)
    snow_ball(200, 100, 45)

    # drawing smile of snowman
    draw_face(221, 111, 2)
    draw_face(214, 113, 2)
    draw_face(207, 114, 2)
    draw_face(200, 115, 2)
    draw_face(193, 114, 2)
    draw_face(186, 113, 2)
    draw_face(179, 111, 2)

    # drawing eyes of snowman
    draw_face(215, 82, 5)
    draw_face(185, 82, 5)

    # drawing nose of snowman
    draw_nose()

    # drawing buttons of snowman
    draw_face(200, 160, 6)
    draw_face(200, 190, 6)
    draw_face(200, 220, 6)

    # drawing scarf
    draw_scarf()

    # drawing hands
    draw_hands()

    # drawing hat
    draw_hat()

    # signing my name
    sign_name()

start_graphics(my_draw)
