# Author: Anna Mikhailova
# Date: 10/13/21
# Purpose: Classes // objects demo --> ideas and objects of the ideas

from random import randint
from cs1lib import *

class Ball:
    def __init__(self, gx, gy):
        self.x = gx
        self.y = gy
        self.vx = randint(-2, 3)
        self.vy = randint(-3, 2)

        # print("self:", self)

    def update_ball(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, r, g, b):
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, R)

    def __str__(self):
        # return "CS1"
        return str(self.x) + " " + str(self.y)


