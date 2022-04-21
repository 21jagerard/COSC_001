# Author: Vasanta
# Date: 11/10/2021
# Purpose: Graph
from Lectures.Lecture_27.vertex import Vertex

vertex_d = {}

# First pass through the information file
va = Vertex(21, "A", [])
vertex_d["A"] = va

vb = Vertex(24, "B", [])
vertex_d["B"] = vb

vc = Vertex(25, "C", [])
vertex_d["C"] = vc

vd = Vertex(19, "D", [])
vertex_d["D"] = vd

ve = Vertex(22, "E", [])
vertex_d["E"] = ve

# Second pass through the information file

# "B" and "E" are adjacent to "A"
va.adj_list.append(vb)
va.adj_list.append(ve)
