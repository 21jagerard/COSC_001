# Author: Anna Mikhailova
# Course: COSC_001
# Date: 10/7/21
# Purpose: Lab 1

from cs1lib import *

# ----------------------------------------------------------------------------------------------------------------------
# Key press functions
# ----------------------------------------------------------------------------------------------------------------------

def key(val):
    global qkey, play, space
    if val == "q":
        qkey = True
    if val == " ":
        space = True
    if val == "r":
        play = True

def release(val):
    pass

# ----------------------------------------------------------------------------------------------------------------------
# Ball functions
# ----------------------------------------------------------------------------------------------------------------------

def ball(x, y):
    set_fill_color(1, 0.7, 0.2)
    disable_stroke()
    draw_circle(x, y, BSIZE)

def rwall(ball_x):
    global rwall_x
    if ball_x >= RIGHT_WALL - BSIZE:
        rwall_x = True

def lwall(ball_x):
    global lwall_x
    if ball_x <= BSIZE:
        lwall_x = True

def twall(ball_y):
    global twall_x
    if ball_y <= BSIZE:
        twall_x = True

def bwall(ball_y):
    global bwall_x
    if ball_y >= BOTTOM_WALL - BSIZE:
        bwall_x = True

def ball_move():
    global bx, by
    ball(bx, by)

# ----------------------------------------------------------------------------------------------------------------------
# Game functions
# ----------------------------------------------------------------------------------------------------------------------

def welcome():
    global start_up
    # clears screen and sets background colour to dark blue
    set_clear_color(0.1, 0.1, 0.2)
    clear()

    # Prompts user to enter the game
    enable_stroke()
    set_stroke_color(1, 1, 1)
    draw_text("WELCOME TO THE GAME!   PRESS -r- TO START,   PRESS -q- TO QUIT", WIDTH // 6, HEIGHT // 2)
    start_up = False

def game_reset():
    clear()
    # prompts user to re-start the game
    enable_stroke()
    set_stroke_color(1, 1, 1)
    draw_text("YOU HAVE CHOSEN TO PAUSE THE GAME.   PRESS -r- TO RE-START,   PRESS -q- TO QUIT", WIDTH // 7, HEIGHT // 2)

def game_over():
    global play, bx, by

    enable_stroke()
    set_stroke_color(1, 1, 1)
    draw_text("GAME OVER.   PRESS -r- TO RESET,   PRESS -q- to QUIT", WIDTH // 4, HEIGHT // 2)

# ----------------------------------------------------------------------------------------------------------------------
# Main function
# ----------------------------------------------------------------------------------------------------------------------

def my_game():
    global play, bx, by, vx, vy, twall_x, bwall_x

    if start_up:
        welcome()

    if rwall_x or lwall_x:  # game over if the ball hits a side wall
        play = False
        game_over()

    if play:
        # clears screen and sets background colour to dark blue
        set_clear_color(0.1, 0.1, 0.2)
        clear()

        ball_move()

        if not rwall_x and not lwall_x:
            rwall(bx)
            lwall(bx)
            twall(by)
            bwall(by)
            if twall_x or bwall_x:
                vy = -vy
                twall_x = False
                bwall_x = False
            bx += vx
            by += vy

    if space:
        game_reset()
    if qkey:
        cs1_quit()

# ----------------------------------------------------------------------------------------------------------------------
# Variables
# ----------------------------------------------------------------------------------------------------------------------

WIDTH = 800
HEIGHT = 800
LEFT_WALL = 0
RIGHT_WALL = WIDTH
TOP_WALL = 0
BOTTOM_WALL = HEIGHT

# Ball size and placement
BX = WIDTH // 2
BY = HEIGHT // 2
bx = BX
by = BY
BSIZE = 15

# Ball movements
vx = 1  # x velocity of the ball
vy = 1  # y velocity of the ball

# Keyboard booleans
qkey = False
space = False

# Game booleans
start_up = True
play = False
rwall_x = False  # boolean for if the right wall has been hit
lwall_x = False  # boolean for if the left wall has been hit
twall_x = False  # boolean for if the top wall has been hit
bwall_x = False  # boolean for if the bottom wall has been hit

start_graphics(my_game, framerate=200, width = WIDTH, height = HEIGHT, key_press=key, key_release=release)


