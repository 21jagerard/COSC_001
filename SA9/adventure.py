# Author: Anna Mikhailova
# Date: 11/11/21
# Course: COSC_001
# Purpose: Short Assignment 9; driver file
from SA9.vertex import Vertex

def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)

        # YOU WRITE THIS PART
        # create a graph vertex here and add it to the dictionary
            story_vertex = Vertex(vertex_name, text, adjacent_vertices)
            vertex_dict[story_vertex.name] = [story_vertex.data, story_vertex.adj_list]

    file.close()

    return vertex_dict

story_dict = load_story("story.txt")

in_story = True
def choose_you_own_adventure(vdict):
    global in_story, ch
    new_vert = "START"
    in_story = True
    while in_story:
        print(vdict[new_vert][0])
        if len(vdict[new_vert][1]) == 0:
            in_story = not in_story
        else:
            ch = ord(input("Enter your choice:")) - ord("a")
            new_vert = vdict[new_vert][1][ch]

choose_you_own_adventure(story_dict)