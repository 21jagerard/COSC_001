# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/12/21
# Purpose: Short Assignment 5 -- String Art

from cs1lib import *

WIDTH = 800
HEIGHT = 800

# Purpose: draw string art
# Parameters:
# a_1x, a_1y are the coordinates for the top of stick A
# a_2x, a_2y are the coordinates for the bottom of stick A
# b_1x, b_1y are the coordinates for the top of stick B
# b_2x, b_2y are the coordinates for the bottom of stick B
# num_strings is the number of strings
def string_art(a_1x, a_1y, a_2x, a_2y, b_1x, b_1y, b_2x, b_2y, num_strings):
    # sets background colour to black
    set_clear_color(0, 0, 0)
    clear()

    # draw the two sticks
    set_stroke_width(3)
    set_stroke_color(1, 0, 0)
    draw_line(a_1x, a_1y, a_2x, a_2y)
    draw_line(b_1x, b_1y, b_2x, b_2y)

    # draw strings between the two sticks
    f = float(1 / (num_strings - 1))  # fraction by which to increase for each string
    tack = 1  # starting at the first tack

    # first tack is at the top of stick 1
    a_tackx = a_1x
    a_tacky = a_1y

    # first tack is at the bottom of stick 2
    b_tackx = b_2x
    b_tacky = b_2y

    # initial blue and green values for the strings
    c_b = 1
    c_g = 0
    while tack <= num_strings:
        # set string colour
        c_b -= f  # making each string progressively less blue
        c_g += f  # making each string progressively more green
        set_stroke_color(0, c_g, c_b)  # changing colour of each string
        set_stroke_width(1)

        # draw string
        draw_line(a_tackx, a_tacky, b_tackx, b_tacky)

        # update A tack
        a_tackx += (f * (a_2x - a_1x))
        a_tacky += (f * (a_2y - a_1y))

        # update B tack
        b_tackx -= (f * (b_2x - b_1x))
        b_tacky -= (f * (b_2y - b_1y))

        # update tack count
        tack += 1

# Purpose: parameterless main function that calls the 9-parameter string_art function
# Parameters: none
def main():
    string_art(50, 100, 100, 400, 700, 360, 400, 700, 50)

start_graphics(main, width=WIDTH, height=HEIGHT)
