from typing import List

from Vertex import Vertex 
from Segment import Segment
from Polygon import Polygon

let = lambda a, b: a.x * b.y - a.y * b.x
def sign(a: float): 
    if a<0:
        return -1
    return 1

def extremEdge(vertexList: List[Vertex]) -> Polygon:
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
    
def stitchHull(hull: List[Segment]) -> Polygon:
    print(hull[0])
    polygon = Polygon([hull.pop(0)])
    count = 0
    while len(hull) != 0 and count < 1000:
        # polygon.segmentList.append(hull.pop(0))
        for i in range(len(hull)):
            if hull[i].a == polygon.segmentList[-1].b:
                polygon.segmentList.append(hull.pop(i))
                break
            if hull[i].b == polygon.segmentList[-1].b:
                polygon.segmentList.append(hull.pop(i).reverse())
                break
        count += 1
    return polygon

def jarvisMarch(vertexList: List[Vertex]) -> Polygon:
    lastVertex = findLowest()
    direction = Segment(lastVertex, Vertex(lastVertex.x + 1, lastVertex.y))
    hull = []
    while lastVertex == hull[0]:
        hull.append(lastVertex)
        newVertex = findMinAngle(vertexList, direction)
        direction = Segment(lastVertex, newVertex)
        lastVertex = newVertex
    return listToPolygon(hull)

def findLowest(vertexList: List[Vertex]) -> Vertex:
    lowestVertex = Vertex(0,0)
    for vertex in vertexList:
        if vertex.y > lowestVertex.y:
            lowestVertex = vertex
    return lowestVertex

def findMinAngle(vertexList: List[Vertex]) -> Vertex:
    return vertexList[0]

def listToPolygon(hull: List (Vertex)) -> Polygon:
    polygon = Polygon([])
    for i in range(len(hull)-1):
        polygon.segmentList.append(Segment(hull[i], hull[i+1]))
    return polygon
