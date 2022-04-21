# Author: Anna Mikhailova
# Date: 10/21/21
# Purpose: driver file for the body and system classes (earth-moon system, in this case)

# from Lab_2.body import Body
# from Lab_2.system import System

from test3 import Body
from test4 import System
from cs1lib import *

# General Parameters
WIDTH = 800  # pixels
HEIGHT = 800  # pixels

TIME_SCALE = 100000  # real seconds per simulation second
PIXELS_PER_METER = 3 / (10 ** 7)  # distance scale for the simulation

FRAME_RATE = 30  # frames per second
TIME_STEP = 1.0 / FRAME_RATE  # time between drawing each frame

def main():
    set_clear_color(0, 0, 0)  # black background

    clear()

    # Draw the system in its current state.
    earth_moon.draw(WIDTH / 2, HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    earth_moon.update(TIME_STEP * TIME_SCALE)


earth = Body(5.9736e24, 0, 0, 0, 0, 24, 0, 0, 1)  # blue earth
moon = Body(7.3477e22, 3.84403e8, 0, 0, 1022, 4, 1, 1, 1)  # white moon
earth_moon = System([earth, moon])

start_graphics(main, height=HEIGHT, width=WIDTH, framerate=FRAME_RATE)

