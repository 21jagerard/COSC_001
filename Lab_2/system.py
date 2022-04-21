# Author: Anna Mikhailova
# Date: 10/21/21
# Purpose: class file for system class; The System class has just one instance variable, which was
# a reference to a list. Each item in the list is a reference to a Body object.

from Lab_2.body import Body
from cs1lib import *
from math import sqrt

GRAVITY = 6.67384e-11

class System:
    def __init__(self, body_list):
        self.body_list = body_list

    def compute_acceleration(self, n):
        total_ax = 0
        total_ay = 0
        for i in range(len(self.body_list)):
            if i != n:
                dx = self.body_list[i].x - self.body_list[n].x  # computes x distance between bodies
                dy = self.body_list[i].y - self.body_list[n].y  # computes y distance between bodies
                r = sqrt((dx ** 2) + (dy ** 2))  # computes total distance between bodies
                a = (GRAVITY * self.body_list[i].mass) / (r ** 2)  # computes total acceleration
                total_ax += (a * dx) / r  # updates total x acceleration
                total_ay += (a * dy) / r  # updates total y acceleration
        return (total_ax, total_ay)

    def update(self, time_step):
        for i in range(len(self.body_list)):
            self.body_list[i].update_position(time_step)  # updates system body position

        for i in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(i)  # computes acceleration of the body
            self.body_list[i].update_velocity(ax, ay, time_step)  # updates system body velocity

    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)  # draws system body
