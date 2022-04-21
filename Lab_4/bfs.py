# Author: Anna Mikhailova
# Date: 11/15/21
# Course: COSC_001
# Purpose: Lab 4; breadth-first search algorithm with back chaining

from Lab_4.vertex import Vertex
from collections import deque

# Parameters: take as parameters references to the start and goal vertices
# Return: a path of vertices connecting start and end vertices
def bfs(start, goal):
    frontier = deque()
    bkp_d = {}  # back pointer dictionary key is vertex and value is vertex from which it was reached

    frontier.append(start)
    bkp_d[start] = None

    while len(frontier) > 0:
        v = frontier.popleft()
        for u in v.adj_list:
            if u not in bkp_d:  # only adding into the frontier deque and bkp_d if the vertex has not been visited
                frontier.append(u)
                bkp_d[u] = v
        if goal in bkp_d:
            break

    path = []
    x = goal

    # setting new backpointers
    while x != None:
        path.append(x)
        if x in bkp_d:
            x = bkp_d[x]

    return path


