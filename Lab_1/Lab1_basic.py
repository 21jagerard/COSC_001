# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/7/21
# Purpose: Lab 1

from cs1lib import *

# ----------------------------------------------------------------------------------------------------------------------
# Variables
# ----------------------------------------------------------------------------------------------------------------------

# Game window
WIDTH = 800
HEIGHT = 800
LEFT_WALL = 0
RIGHT_WALL = WIDTH
TOP_WALL = 0
BOTTOM_WALL = HEIGHT

# Coordinates for the top left corner of left paddle
lx = 0
ly = 0

# Coordinates for bottom right corner of right paddle
rx = WIDTH
ry = HEIGHT

# Paddle parameters
PADDLE_HEIGHT = 140
PADDLE_WIDTH = 60

# Paddle movements
UP = -2
DOWN = 2

# Ball size and placement
BX = WIDTH // 2
BY = HEIGHT // 2
bx = BX
by = BY
BSIZE = 10

# Ball movements
VX = 2  # x velocity of the ball
VY = 2  # y velocity of the ball
vx = VX
vy = VY

# Keyboard state variables
akey = False  # "a" moves left paddle up
zkey = False  # "z" moves left paddle down
kkey = False  # "k" moves right paddle up
mkey = False  # "m" moves right paddle down
qkey = False  # "q" quits the game

# Game state variables
play = False  # boolean for if the game is in play (game in progress)
ball_moving = False  # boolean for if the ball is moving (ball moves)
pause = False  # boolean for if the game is paused
restart = False  # boolean for if the game is restarted
end = False

# ----------------------------------------------------------------------------------------------------------------------
# Paddles functions
# ----------------------------------------------------------------------------------------------------------------------

def l_paddle(x, y, w, h):
    set_fill_color(0.5, 0.8, 0.2)
    disable_stroke()
    draw_rectangle(x, y, w, h)

def r_paddle(x, y, w, h):
    set_fill_color(0.5, 0.8, 0.2)
    disable_stroke()
    draw_rectangle(x, y, w, h)

# ----------------------------------------------------------------------------------------------------------------------
# Paddle movement functions
# ----------------------------------------------------------------------------------------------------------------------

def l_paddle_move(m):
    global lx, ly
    ly += m
    l_paddle(lx, ly, PADDLE_WIDTH, PADDLE_HEIGHT)

def r_paddle_move(m):
    global rx, ry
    ry -= m
    r_paddle(rx-PADDLE_WIDTH, ry-PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

def key(val):
    global akey, zkey, kkey, mkey, qkey, pause, ball_moving
    if val == "a":
        akey = True
    if val == "z":
        zkey = True
    if val == "k":
        kkey = True
    if val == "m":
        mkey = True
    if val == "q":
        qkey = True
    if val == " ":
        pause = True
        ball_moving = True

def release(val):
    global akey, zkey, kkey, mkey, pause
    if val == "a":
        akey = False
    if val == "z":
        zkey = False
    if val == "k":
        kkey = False
    if val == "m":
        mkey = False
    if val == " ":
        pause = False

# ----------------------------------------------------------------------------------------------------------------------
# Ball functions
# ----------------------------------------------------------------------------------------------------------------------

def ball(x, y):
    set_fill_color(1, 0.7, 0.2)
    disable_stroke()
    draw_circle(x, y, BSIZE)

def rwall(ball_x):
    global play, vx, vy
    if ball_x >= RIGHT_WALL - BSIZE:
        vx = 0
        vy = 0
        enable_stroke()
        set_stroke_color(1, 1, 1)
        draw_text("GAME OVER.  PRESS -SPACE- TO RESTART OR -q- TO QUIT.", WIDTH // 4, HEIGHT // 2)

def lwall(ball_x):
    global play, vx, vy
    if ball_x <= BSIZE:
        vx = 0
        vy = 0
        enable_stroke()
        set_stroke_color(1, 1, 1)
        draw_text("GAME OVER.  PRESS -SPACE- TO RESTART OR -q- TO QUIT.", WIDTH // 4, HEIGHT // 2)

def twall(ball_y):
    global vy
    if ball_y <= BSIZE:
        vy = -vy

def bwall(ball_y):
    global vy
    if ball_y >= BOTTOM_WALL - BSIZE:
        vy = -vy

def ball_move():
    global bx, by, ball_moving
    if ball_moving:
        ball(bx, by)

# ----------------------------------------------------------------------------------------------------------------------
# Game functions
# ----------------------------------------------------------------------------------------------------------------------

def paddle_touch():
    global bx, by, rx, ry, vx
    if (bx + BSIZE) >= (rx - PADDLE_WIDTH) and ((ry >= by + BSIZE) and by - BSIZE >= ry - PADDLE_HEIGHT) or \
        (bx - BSIZE) <= (lx + PADDLE_WIDTH) and ((ly <= by - BSIZE) and (by + BSIZE <= ly + PADDLE_HEIGHT)):
        vx = -vx

def game_start():
    enable_stroke()
    set_stroke_color(1, 1, 1)
    draw_text("WELCOME TO PONG! PRESS -SPACE- TO START THE GAME.", WIDTH // 4, HEIGHT // 2)

def game_end():
    if qkey:
        cs1_quit()

# ----------------------------------------------------------------------------------------------------------------------
# Main function
# ----------------------------------------------------------------------------------------------------------------------

def my_game():
    global play, bx, by, vx, vy, pad_hit, rx, ry, lx, ly
    # clears screen and sets background colour to dark blue
    set_clear_color(0.1, 0.1, 0.2)
    clear()

    # Paddles aren't moving unless keys are pressed
    l_paddle_move(0)
    r_paddle_move(0)

    # moving paddles when keys are pressed
    if akey and ly > 0:  # moves left paddle up
        l_paddle_move(UP)
    if zkey and ly < HEIGHT - PADDLE_HEIGHT:  # moves left paddle down
        l_paddle_move(DOWN)
    if kkey and ry > PADDLE_HEIGHT:  # moves right paddle down
        r_paddle_move(DOWN)
    if mkey and ry < HEIGHT:  # moves right paddle up
        r_paddle_move(UP)

    rwall(bx)  # checks if ball hit right wall
    lwall(bx)  # checks if ball hit left wall
    twall(by)  # checks if ball hit top wall
    bwall(by)  # checks if ball hit bottom wall

    paddle_touch()  # checks if ball hit paddle

    bx += vx
    by += vy

    # to restart game:
    if pause:
        # game_reset()

        # resets the position of the ball
        bx = BX
        by = BY

        # resets the ball's velocity
        vx = VX
        vy = VY

        # resets the position of the paddles
        lx = 0
        ly = 0
        rx = WIDTH
        ry = HEIGHT
        play = True

    if play:
        ball_move()
    if not play:
        game_start()

    game_end()

start_graphics(my_game, framerate=200, width = WIDTH, height = HEIGHT, key_press=key, key_release=release)


