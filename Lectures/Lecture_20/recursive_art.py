from cs1lib import *

def rec_art(x, y, size, n=0):
    if size < 10:
        return

    set_fill_color(n*0.2, 1, 1)

    draw_rectangle(x, y, size, size)
    new_size = size//2

    rec_art(x, y, new_size, n + 1)
    rec_art(x, y + new_size, new_size, n + 1)
    rec_art(x + new_size, y + new_size, new_size, n + 1)


def my_draw():
    set_clear_color(1, 1, 1)
    clear()

    rec_art(0, 0, 800)

start_graphics(my_draw, width=800, height=800)


