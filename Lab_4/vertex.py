# Author: Anna Mikhailova
# Date: 11/12/21
# Course: COSC_001
# Purpose: Lab 4; class file for vertex class
from cs1lib import *
EDGE_WIDTH = 4
VERTEX_RAD = 6

class Vertex:
    def __init__(self, vname, xpos, ypos, vlist):
        self.name = vname
        self.x = int(xpos)
        self.y = int(ypos)
        self.adj_list = vlist

    def __str__(self):
        adj_string = ""
        for a_vert in self.adj_list:
            if adj_string != "":
                adj_string += ", " + a_vert.name
            else:
                adj_string += a_vert.name
        return self.name + "; Location: " + self.x + ", " + self.y + "; Adjacent vertices: " + adj_string

    def draw_vert(self, r, g, b):
        set_fill_color(r, g, b)
        disable_stroke()
        draw_circle(self.x, self.y, VERTEX_RAD)

    def draw_edge(self, vert, r, g, b):
        set_stroke_color(r, g, b)
        enable_stroke()
        set_stroke_width(EDGE_WIDTH)
        draw_line(self.x, self.y, vert.x, vert.y)

    def draw_adj_edges(self, r, g, b):
        for a_vert in self.adj_list:
            self.draw_edge(a_vert, r, g, b)

    def in_vert_square(self, x, y):
        if (self.x-VERTEX_RAD <= x <= self.x+VERTEX_RAD) and (self.y-VERTEX_RAD <= y <= self.y+VERTEX_RAD):
            return True
        else:
            return False
