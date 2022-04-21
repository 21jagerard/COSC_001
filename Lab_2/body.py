# Author: Anna Mikhailova
# Date: 10/21/21
# Purpose: class file for Body class; The Body class represents an individual body, such as the Earth,
# the moon, the Sun, or any other planet

from cs1lib import *

class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.p_rad = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):
        self.x += self.vx * timestep  # updates x position
        self.y += self.vy * timestep  # updates y position

    def update_velocity(self, ax, ay, timestep):
        self.vx += ax * timestep  # updates x velocity
        self.vy += ay * timestep  # updates y velocity

    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x * pixels_per_meter + cx, cy - self.y * pixels_per_meter, self.p_rad)  # draws body