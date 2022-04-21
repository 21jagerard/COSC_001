# Purpose: graph

from Lectures.Lecture_26.vertex import Vertex

va = Vertex(20, "A", ["E", "B"])
vb = Vertex(21, "B", ["A", "C", "D", "E"])
vc - Vertex(19, "C", ["D", "B"])
vd = Vertex(22, "D", ["E", "B", "C"])
ve - Vertex(25, "E", ["A", "B", "D"])

# va.adj_list.append("E")
# va.adj_list.append("B")
# vb.adj_list.append("A")
# ve.adj_list.append("A")

# vertex_list = [va, vb, vc, vd, ve]
vertex_d = {}
vertex_d["A"] = va
vertex_d["B"] = vb
vertex_d["C"] = vc
vertex_d["D"] = vd
vertex_d["E"] = ve