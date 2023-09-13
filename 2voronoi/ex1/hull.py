from typing import List
from Vertex import Vertex
from Segment import Segment


let = lambda a, b: a.x * b.y - a.y * b.x
def sign(a: float): 
    if a<0:
        return -1
    return 1

def extremEdge(vertexList: List[Vertex]) -> List[Vertex]:
    hull = []
    for i in range(len(vertexList)):
        for j in range(len(vertexList)):
            if i!=j:
                addExtremEdgeToHull(hull, vertexList, i, j)
    return stitchHull(hull)

def addExtremEdgeToHull(hull, vertexList, i, j):
    if isExtremEdge(vertexList, i, j):
        hull.append(Segment(vertexList[i], vertexList[j]))
    
def isExtremEdge(vertexList, i, j):
    lastSign = None
    for k in range(len(vertexList)):
        # if k == i or k == j:
        #     break
        a, b, c = vertexList[i], vertexList[j], vertexList[k]
        v = Vertex(b.x-a.x, b.y-a.y)
        w = Vertex(c.x-a.x, c.y-a.y)
        val = let(v,w)
        newSign = sign(val)
        if not(lastSign is None) and newSign != lastSign:
            return False
        lastSign = newSign
    return True
    
def stitchHull(hull: List[Segment]) -> List[Vertex]:
    segment = hull.pop(0)
    vertexList = [segment.a, segment.b]
    while len(hull) != 0:
        for i in range(len(hull)):
            if hull[i].a == vertexList[-1]:
                segment = hull.pop(i)
                vertexList.append(segment.b)
                break
            if hull[i].b == vertexList[-1]:
                segment = hull.pop(i)
                vertexList.append(segment.a)
                break
    return vertexList