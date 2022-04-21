# Author: Anna Mikhailova
# Date: 11/11/21
# Course: COSC_001
# Purpose: Short Assignment 9; class file for vertex class

class Vertex:
    def __init__(self, vname, vdata, vlist):
        self.name = vname
        self.data = vdata
        self.adj_list = vlist