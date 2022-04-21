#Dylan Witzke
#06/03/2022

from test import *

#def load graph
def load_graph(in_file):
    file = open(in_file, "r")

    vdict = {}

    for line in file:
        if len(line.split(";")) == 3:
            line = line.strip()
            line_info = line.split(";")

            xy_info = line_info[2].split(",")

            vname = line_info[0].strip()

            vertex = Vertex(vname, xy_info[0].strip(), xy_info[1].strip(), [])
            vdict[vertex.name] = vertex

    file.close()

    file = open(in_file, "r")

    for line in file:
        if len(line.split(";")) == 3:
            line = line.strip()
            line_info = line.split(";")

            vlist = line_info[1].split(",")

            vname = line_info[0].strip()

            for avert in vlist:
                vdict[vname].alist.append(vdict[avert.strip()])

    file.close()

    return vdict
