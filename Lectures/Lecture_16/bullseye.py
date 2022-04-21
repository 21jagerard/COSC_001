from Lectures.Lecture_15.circle import Circle
from random import randint

class Bullseye:
    def __init__(self, x, y, size):
        self.size = size
        n = randint(3, 7)
        self.clist = []

        for i in range(n):
            if i % 3 == 0:
                c = Circle(x, y, (i + 1)*size, 1, 0, 0)
            elif i % 3 == 1:
                c = Circle(x, y, (i + 1) * size, 0, 1, 0)
            else:
                c = Circle(x, y, (i + 1) * size, 0, 0, 1)
            self.clist.append(c)

    def update(self):
        vx = 1
        vy = 1

        for c in self.clist:
            c.update(vx, vy)

    def draw(self):
        for i in range(len(self.clist) - 1, -1, -1):
            self.clist[i].draw()
