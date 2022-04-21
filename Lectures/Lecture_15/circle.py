# Author: Anna Mikhailova
# Date: 10/15/21
# Purpose: Class file of circle class

from cs1lib import *

class Circle:
    def __init__(self, gx, gy, radius, r, g, b):
        self.x = gx
        self.y = gy
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b

    def copy(self):
        c = Circle(self.x, self.y, self.radius, self. r, self.g, self.b)
        return c

    def update(self, vx, vy):
        self.x += vx
        self.y += vy

    def draw(self):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x, self.y, self.radius)
    #
    # def __str__(self):
    #     # return "CS1"
    #     return str(self.x) + " " + str(self.y)


