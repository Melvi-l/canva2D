from typing import List

from Vertex import Vertex 
from Segment import Segment

let = lambda a, b: a.x * b.y - a.y * b.x
def extremEdge(vertexList: List[Vertex]) -> List[Segment]:
    hull = []
    for i in range(len(vertexList)):
        for j in range(i+1, len(vertexList)):
            addExtremEdgeToHull(hull, vertexList, i, j)
    stitchHull(hull)


def addExtremEdgeToHull(hull, vertexList, i, j):
    if isExtremEdge(vertexList, i, j):
        hull.append(Segment(vertexList[i], vertexList[j]))
    
def isExtremEdge(vertexList, i, j):
    for k in range(len(vertexList)):
        # if k == i or k == j:
        #     break
        a, b, c = vertexList[i], vertexList[j], vertexList[k]
        v = Vertex(b.x-a.x, b.y-a.y)
        w = Vertex(c.x-a.x, c.y-a.y)
        val = let(v,w)
        if val < 0:
            return False
    return True
    
def stitchHull(hull)
