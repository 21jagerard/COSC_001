# Author: Anna Mikhailova
# Date: 10/15/21
# Purpose: class file of Bullseye class

from Lectures.Lecture_15.circle import Circle
from random import randint

class Bullseye:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

        self.c1 = Circle(x, y, size, 1, 0, 0)
        self.c2 = Circle(x, y, 2*size, 0, 1, 0)
        self.c3 = Circle(x, y, 3*size, 0, 0, 1)

    def update(self):
        vx = randint(-5, 5)
        vy = randint(-5, 5)

        self.c1.update(vx, vy)
        self.c2.update(vx, vy)
        self.c3.update(vx, vy)

    def draw(self):
        self.c3.draw()
        self.c2.draw()
        self.c1.draw()
