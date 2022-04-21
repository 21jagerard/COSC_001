# Crowd class file
from random import randint
from Recitation_6.face import Face

class Crowd:
    def __init__(self, n):
        self.face_list = []
        for i in range(n):
            x_i = randint(0, 400)
            y_i = randint(0, 400)
            face_i = Face(x_i, y_i, 20)
            self.face_list.append(face_i)

    def look_at(self, lx, ly):
        for face in self.face_list:
            face.lookat(lx, ly)

    def draw(self):
        for face in self.face_list:
            face.draw()
