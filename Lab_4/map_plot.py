# Author: Anna Mikhailova
# Date: 11/15/21
# Course: COSC_001
# Purpose: Lab 4; visualize the map

from cs1lib import *
from Lab_4.vertex import Vertex
from Lab_4.load_graph import load_graph
from Lab_4.bfs import bfs


WIDTH = 1012
HEIGHT = 811
mpressed = False
mx = 0
my = 0
new_x = 0
new_y = 0

img = load_image("dartmouth_map.png")
vertex_dict = load_graph("dartmouth_graph.txt")

# Purpose: draw all of the vertices and edges
# Parameters: none
def draw_map():
    for vertex in vertex_dict:
        vertex_dict[vertex].draw_vert(0, 0, 1)
        vertex_dict[vertex].draw_adj_edges(0, 0, 1)

# Purpose: tracking press of mouse
# Parameters: x and y -- coordinates for the x and y location of mouse, respectively
def press(x, y):
    global mpressed, mx, my
    mx = x
    my = y
    mpressed = True

# Purpose: tracking release of mouse
# Parameters: x and y -- coordinates for the x and y location of mouse, respectively
def release(x, y):
    global mpressed
    mpressed = False

# Purpose: tracking mouse movement
# Parameters: x and y -- coordinates for the x and y location of mouse, respectively
def move(x, y):
    global new_x, new_y
    new_x = x
    new_y = y

# Purpose: main draw function
# Parameters: none
def main():
    draw_image(img, 0, 0)  # draws campus map
    draw_map()  # draws graph

    for vertex1 in vertex_dict:
        if vertex_dict[vertex1].in_vert_square(mx, my):  # if a vertex is clicked on:
            start_vert = vertex_dict[vertex1]  # sets selected vertex to start_vert
            start_vert.draw_vert(1, 0, 0)  # colours selected vertex in red
            if not vertex_dict[vertex1].in_vert_square(new_x, new_y):  # if mouse moves away from clicked vertex
                for vertex2 in vertex_dict:
                    if vertex_dict[vertex2].in_vert_square(new_x, new_y):  # if mouse hovers over new vertex
                        goal_vert = vertex_dict[vertex2]  # sets selected vertex to goal_vert
                        if start_vert != None and goal_vert != None:  # if start and goal vertices selected
                            connected_vert_list = bfs(start_vert, goal_vert)  # conducts BFS on start and goal vertices
                            old_vert = goal_vert
                            for vert in connected_vert_list:  # draws the path from start vertex to goal vertex
                                vert.draw_edge(old_vert, 1, 0, 0)
                                vert.draw_vert(1, 0, 0)
                                old_vert = vert

start_graphics(main, width=WIDTH, height=HEIGHT, mouse_move=move, mouse_press=press, mouse_release=release)