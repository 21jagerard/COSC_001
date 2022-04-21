from Lectures.Lecture_16.bullseye import Bullseye
from cs1lib import *

H = 400
W = 400

b = Bullseye(200, 200, 20)


def main_draw():
    set_clear_color(1, 1, 1)
    clear()

    b.update()
    b.draw()


start_graphics(main_draw, width=W, height=H)
