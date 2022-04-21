from cs1lib import *


def pic_draw():
    global old_x, old_y, new_x, new_y
    enable_stroke()
    set_stroke_width(2)

    draw_line(old_x, old_y, new_x, new_y)
    old_x = new_x
    old_y = new_y

def my_draw():
    global first_clear, old_x, old_y
    if first_clear:
        set_clear_color(0, 0, 0)  # makes the initial background black
        clear()
        set_stroke_color(1, 1, 1)
        first_clear = False

    if mpressed:
        pic_draw()

    elif not mpressed:
        old_x = mouse_x()
        old_y = mouse_y()


# function that says to draw line from old point to new point and sets stroke width to 2

def press(mx, my):
    global mpressed
    mpressed = True

def release(mx, my):
    global mpressed
    mpressed = False


def move(mx, my):
    global new_x, new_y, old_y, old_x
    new_y = my
    new_x = mx


# press and release assign the boolean value True or False to draw, meaning that if mouse is released, the
# mydraw fucntion stops drawing, and if it is clicked, it draws

old_x = 400
old_y = 400
new_x = 400
new_y = 400
mpressed = False
first_clear = True

start_graphics(my_draw, mouse_press=press, mouse_release=release, mouse_move=move)