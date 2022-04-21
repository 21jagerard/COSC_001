# Author: Anna Mikhailova
# Date: 10/20/21
# Purpose: Simulation of a physical ball bouncing

from cs1lib import *

FRAME_RATE = 500
TIME_SCALE = 3
TIME_STEP = TIME_SCALE * 1/FRAME_RATE

PIXEL_PER_METER = 20  # scale
RADIUS = 1  # meters

H = 400
W = 400

x = 0  # meters
y = 10  # meters

v_x = 3  # meters per second
v_y = 0  # meters per second
G = -9.8  # meters per second^2

def update_ball():
    global x, y, v_y
    x += v_x * TIME_STEP
    y += v_y * TIME_STEP

    if y <= 0:
        v_y = - v_y
    else:
        v_y += G * TIME_STEP

def draw_ball():
    pixel_x = x * PIXEL_PER_METER
    pixel_y = H - y * PIXEL_PER_METER
    pixel_r = RADIUS * PIXEL_PER_METER

    set_fill_color(1, 1, 0)
    draw_circle(pixel_x, pixel_y, pixel_r)

def main_draw():
    set_clear_color(1, 1, 1)
    clear()

    draw_ball()
    update_ball()

start_graphics(main_draw, height=H, width=W, framerate=FRAME_RATE)