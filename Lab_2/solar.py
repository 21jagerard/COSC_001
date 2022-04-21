# Author: Anna Mikhailova
# Date: 10/24/21
# Purpose: driver file for the body and system classes (solar system, in this case)

from Lab_2.body import Body
from Lab_2.system import System
from cs1lib import *

# General Parameters
WIDTH = 800  # pixels
HEIGHT = 800  # pixels

TIME_SCALE = 3.0e6  # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAME_RATE = 30  # frames per second
TIME_STEP = 1.0 / FRAME_RATE  # time between drawing each frame

def main():
    set_clear_color(0, 0, 0)  # black background

    clear()

    # Draw the system in its current state.
    solar.draw(WIDTH / 2, HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar.update(TIME_STEP * TIME_SCALE)

# Body(mass, x, y, vx, vy, rad, rgb)
sun = Body(1.98892e30, 0, 0, 0, 0, 25, 1, 1, 0)  # yellow sun
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 1, 0.4, 1)  # pink mercury
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 8, 0.8, 0.5, 0)  # orange venus
earth = Body(5.9736e24, -149.6e9, 0, 0, 29790, 10, 0, 0, 1)  # blue earth
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 5.5, 1, 0, 0)  # red mars
solar = System([sun, mercury, venus, earth, mars])

start_graphics(main, height=HEIGHT, width=WIDTH, framerate=FRAME_RATE)