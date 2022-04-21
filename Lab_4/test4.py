from test import *
from test3 import *
from test2 import *

W = 1012
H = 811

mpressed = False
mx = 0
my = 0
nx = 0
ny = 0

vdict = load_graph("dartmouth_graph.txt")
img = load_image("dartmouth_map.png")


def draw_map():
    for vert in vdict:
        vdict[vert].draw_vert(0, 0, 1)
        vdict[vert].draw_all_edges(0, 0, 1)

def press(x, y):
    global mpressed, mx, my
    mx = x
    my = y
    mpressed = True

def release(x, y):
    global mpressed
    mpressed = False

def move(x, y):
    global nx, ny
    nx = x
    ny = y

def main():
    draw_image(img, 0, 0)
    draw_map()

    for svert in vdict:
        if vdict[svert].in_square(mx, my):
            start = vdict[svert]
            start.draw_vert(1, 0, 0)
            if not vdict[svert].in_square(nx, ny):
                for gvert in vdict:
                    if vdict[gvert].in_square(nx, ny):
                        goal = vdict[gvert]
                        if start != None and goal != None:
                            vlist = bfs(start, goal)
                            cvert = goal
                            for vert in vlist:
                                vert.draw_edge(cvert, 1, 0, 0)
                                vert.draw_vert(1, 0, 0)
                                cvert = vert


start_graphics(main, height=H, width=W, mouse_press=press, mouse_move=move, mouse_release=release)

