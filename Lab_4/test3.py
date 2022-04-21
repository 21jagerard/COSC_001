
from collections import deque

def bfs(start, goal):
    var = deque()
    var.append(start)

    visit = {}
    visit[start] = None

    while len(var) > 0:
        cvert = var.popleft()

        for nvert in cvert.alist:
            if nvert not in visit:
                var.append(nvert)
                visit[nvert] = cvert

        if goal in visit:
            break

    path = []
    x = goal

    while x != None:
        path.append(x)
        if x in visit:
            x = visit[x]

    return path



