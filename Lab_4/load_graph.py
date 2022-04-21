# Author: Anna Mikhailova
# Date: 11/12/21
# Course: COSC_001
# Purpose: Lab 4;
from Lab_4.vertex import Vertex

# Parameters: file
# Purpose: create one Vertex object per line in the data file and add to a dictionary a reference to each
# Vertex object it creates
# Return: dictionary of Vertex objects
def load_graph(fname):
    dartmouth_graph_fp = open(fname, "r")

    vert_dict = {}
    for line in dartmouth_graph_fp:

        if len(line.split(";")) == 3:
            loc_info = line.strip()
            loc_info_list = loc_info.split(";")

            # creates a list of x and y coordinates for each vertex
            xy_cord = loc_info_list[2].split(",")

            # create a Vertex object for each line in the dictionary, with an empty adjacency list
            vertex = Vertex(loc_info_list[0].strip(), xy_cord[0].strip(), xy_cord[1].strip(), [])
            vert_dict[vertex.name] = vertex
    dartmouth_graph_fp.close()

    dartmouth_graph_fp = open(fname, "r")

    for line in dartmouth_graph_fp:
        # append the adjacent vertices (Vertex objects) to each Vertex object's adjacency list
        if len(line.split(";")) == 3:
            loc_info = line.strip()
            loc_info_list = loc_info.split(";")

            # get names of adjacent vertices
            a_list = loc_info_list[1].split(",")

            # get name of the vertex and append adjacent Vertex objects to the adjacency list
            vname = loc_info_list[0].strip()
            for a_vert in a_list:
                vert_dict[vname].adj_list.append(vert_dict[a_vert.strip()])

    dartmouth_graph_fp.close()
    return vert_dict

